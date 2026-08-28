#!/usr/bin/env python3
"""Local web UI for pipeline/ingest.py: paste a link, watch progress, review
the extracted entry and its fit score, then accept or discard it.

Usage:
    python3 pipeline/webapp.py [--port 8765]

Loads ANTHROPIC_API_KEY from a .env file at the repo root on startup (same
file ingest.py's `source .env` uses), so it works no matter how the server
process itself was launched.

Stdlib only (http.server) -- no new dependency for a local single-user tool.
This never commits to git; accepting an entry only writes data.json and
regenerates AI4Science.md, same as ingest.py's non-dry-run path.
"""
import argparse
import json
import os
import queue
import subprocess
import sys
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_dotenv():
    """Parse `export KEY="value"` / `KEY=value` lines from .env, best-effort."""
    env_path = REPO_ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        line = line.removeprefix("export ").strip()
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


_load_dotenv()

import ingest  # noqa: E402 -- must follow _load_dotenv() so the SDK sees the key

JOBS: dict[str, dict] = {}
JOBS_LOCK = threading.Lock()

INDEX_HTML = """<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>AI4Science ingest</title>
<style>
  :root { color-scheme: light dark; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
         max-width: 760px; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }
  h1 { font-size: 1.3rem; }
  .row { display: flex; gap: 0.5rem; }
  input[type=text] { flex: 1; padding: 0.5rem; font-size: 1rem; }
  button { padding: 0.5rem 1rem; font-size: 1rem; cursor: pointer; }
  button:disabled { cursor: not-allowed; opacity: 0.5; }
  #log { margin-top: 1rem; font-family: ui-monospace, monospace; font-size: 0.85rem;
         color: #666; white-space: pre-wrap; min-height: 1.5rem; }
  #result { margin-top: 1.5rem; border: 1px solid #8883; border-radius: 8px; padding: 1rem; display: none; }
  .score { display: inline-block; padding: 0.15rem 0.6rem; border-radius: 999px; font-weight: 600; }
  .score.good { background: #1a7f371a; color: #1a7f37; }
  .score.warn { background: #9a67001a; color: #9a6700; }
  .score.bad { background: #cf222e1a; color: #cf222e; }
  .badge { display: inline-block; padding: 0.15rem 0.5rem; border-radius: 6px; background: #8883; font-size: 0.8rem; margin-left: 0.4rem; }
  .gate { margin-top: 0.75rem; padding: 0.75rem; border-radius: 6px; background: #9a67001a; color: #9a6700; }
  ul { padding-left: 1.2rem; }
  .actions { margin-top: 1rem; display: flex; gap: 0.5rem; }
  #discardBtn { background: transparent; }
  details summary { cursor: pointer; margin-top: 0.75rem; }
  pre { white-space: pre-wrap; font-size: 0.8rem; }
  #status { margin-top: 0.75rem; font-weight: 600; }
</style>
</head>
<body>
<h1>AI4Science catalogue ingest</h1>
<p>Paste a paper URL. Claude fetches it, extracts a catalogue entry, and scores how well it fits.</p>

<div class="row">
  <input id="url" type="text" placeholder="https://www.nature.com/articles/...">
  <button id="goBtn" onclick="startIngest()">Fetch &amp; analyze</button>
</div>

<div id="log"></div>
<div id="result"></div>
<div id="status"></div>

<script>
let currentJob = null;

function el(tag, attrs, children) {
  const e = document.createElement(tag);
  Object.entries(attrs || {}).forEach(([k, v]) => { if (k === "class") e.className = v; else if (k === "html") e.innerHTML = v; else e.setAttribute(k, v); });
  (children || []).forEach(c => e.appendChild(c));
  return e;
}

function scoreClass(score) {
  if (score >= 60) return "good";
  if (score >= 30) return "warn";
  return "bad";
}

async function startIngest() {
  const url = document.getElementById("url").value.trim();
  if (!url) return;
  document.getElementById("goBtn").disabled = true;
  document.getElementById("log").textContent = "Starting...";
  document.getElementById("result").style.display = "none";
  document.getElementById("status").textContent = "";

  const resp = await fetch("/api/ingest", {
    method: "POST", headers: {"Content-Type": "application/json"},
    body: JSON.stringify({url}),
  });
  const data = await resp.json();
  if (!resp.ok) {
    document.getElementById("log").textContent = "Error: " + (data.error || resp.statusText);
    document.getElementById("goBtn").disabled = false;
    return;
  }
  currentJob = data.job_id;
  const es = new EventSource("/api/events/" + currentJob);
  const log = document.getElementById("log");
  es.onmessage = (ev) => {
    const msg = JSON.parse(ev.data);
    if (msg.type === "progress") {
      log.textContent += "\\n" + msg.text;
    } else if (msg.type === "result") {
      es.close();
      document.getElementById("goBtn").disabled = false;
      renderResult(msg);
    } else if (msg.type === "error") {
      es.close();
      document.getElementById("goBtn").disabled = false;
      log.textContent += "\\n\\nFailed: " + msg.text;
    }
  };
}

function renderResult(msg) {
  const entry = msg.entry;
  const box = document.getElementById("result");
  box.style.display = "block";
  box.innerHTML = "";

  const header = el("div", {}, [
    el("span", {class: "score " + scoreClass(entry.fit_score), html: "fit " + entry.fit_score + "/100"}),
    el("span", {class: "badge", html: entry.source_access}),
    el("span", {class: "badge", html: entry.category}),
  ]);
  box.appendChild(header);
  box.appendChild(el("h3", {html: entry.model}));
  box.appendChild(el("p", {html: "<em>" + entry.headline + "</em>"}));
  box.appendChild(el("p", {html: entry.fit_rationale}));

  if (entry.key_results && entry.key_results.length) {
    const ul = el("ul", {});
    entry.key_results.forEach(r => ul.appendChild(el("li", {html: r})));
    box.appendChild(ul);
  }

  if (msg.gate_reasons && msg.gate_reasons.length) {
    const gate = el("div", {class: "gate"});
    gate.appendChild(el("strong", {html: "Flagged for review:"}));
    const ul = el("ul", {});
    msg.gate_reasons.forEach(r => ul.appendChild(el("li", {html: r})));
    gate.appendChild(ul);
    box.appendChild(gate);
  }

  const details = el("details", {}, [
    el("summary", {html: "Full extracted JSON"}),
    el("pre", {html: JSON.stringify(entry, null, 2)}),
  ]);
  box.appendChild(details);

  const actions = el("div", {class: "actions"});
  const addLabel = (msg.gate_reasons && msg.gate_reasons.length) ? "Add anyway" : "Add to repo";
  const addBtn = el("button", {id: "addBtn", html: addLabel});
  addBtn.onclick = () => commit(currentJob);
  const discardBtn = el("button", {id: "discardBtn", html: "Discard"});
  discardBtn.onclick = () => discard(currentJob);
  actions.appendChild(addBtn);
  actions.appendChild(discardBtn);
  box.appendChild(actions);
}

async function commit(jobId) {
  document.getElementById("addBtn").disabled = true;
  document.getElementById("discardBtn").disabled = true;
  const resp = await fetch("/api/commit", {
    method: "POST", headers: {"Content-Type": "application/json"},
    body: JSON.stringify({job_id: jobId}),
  });
  const data = await resp.json();
  const status = document.getElementById("status");
  if (resp.ok) {
    status.textContent = "Added to " + data.category + ". data.json + AI4Science.md updated on disk -- review the diff and commit yourself.";
  } else {
    status.textContent = "Failed to add: " + (data.error || resp.statusText);
    document.getElementById("addBtn").disabled = false;
    document.getElementById("discardBtn").disabled = false;
  }
}

async function discard(jobId) {
  await fetch("/api/discard", {
    method: "POST", headers: {"Content-Type": "application/json"},
    body: JSON.stringify({job_id: jobId}),
  });
  document.getElementById("status").textContent = "Discarded. Nothing was written.";
  document.getElementById("result").style.display = "none";
}
</script>
</body>
</html>
"""


def run_ingest_job(job_id: str, url: str, model: str):
    job = JOBS[job_id]

    def notify(text: str):
        job["queue"].put({"type": "progress", "text": text})

    try:
        entry = ingest.fetch_entry(url, model, on_progress=notify)
        gate_reasons = ingest.review_gate(entry, job["fit_threshold"])
        job["entry"] = entry
        job["gate_reasons"] = gate_reasons
        job["status"] = "done"
        job["queue"].put({"type": "result", "entry": entry, "gate_reasons": gate_reasons})
    except Exception as exc:  # noqa: BLE001 -- surface any failure to the UI
        job["status"] = "error"
        job["queue"].put({"type": "error", "text": str(exc)})


class Handler(BaseHTTPRequestHandler):
    def _json(self, status: int, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        return json.loads(self.rfile.read(length) or b"{}")

    def do_GET(self):
        if self.path == "/":
            body = INDEX_HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path.startswith("/api/events/"):
            self._sse(self.path.removeprefix("/api/events/"))
        else:
            self._json(404, {"error": "not found"})

    def _sse(self, job_id: str):
        with JOBS_LOCK:
            job = JOBS.get(job_id)
        if job is None:
            self._json(404, {"error": "unknown job"})
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        while True:
            try:
                msg = job["queue"].get(timeout=30)
            except queue.Empty:
                self.wfile.write(b": keepalive\n\n")
                self.wfile.flush()
                continue
            self.wfile.write(f"data: {json.dumps(msg)}\n\n".encode("utf-8"))
            self.wfile.flush()
            if msg["type"] in ("result", "error"):
                return

    def do_POST(self):
        if self.path == "/api/ingest":
            self._handle_ingest()
        elif self.path == "/api/commit":
            self._handle_commit()
        elif self.path == "/api/discard":
            self._handle_discard()
        else:
            self._json(404, {"error": "not found"})

    def _handle_ingest(self):
        body = self._read_json()
        url = (body.get("url") or "").strip()
        if not url:
            self._json(400, {"error": "url is required"})
            return
        data = ingest.load_data()
        if url in ingest.existing_urls(data):
            self._json(409, {"error": "already in the catalogue"})
            return

        job_id = uuid.uuid4().hex
        with JOBS_LOCK:
            JOBS[job_id] = {
                "queue": queue.Queue(),
                "status": "running",
                "entry": None,
                "gate_reasons": [],
                "fit_threshold": 60,
            }
        threading.Thread(target=run_ingest_job, args=(job_id, url, "claude-sonnet-5"), daemon=True).start()
        self._json(202, {"job_id": job_id})

    def _handle_commit(self):
        body = self._read_json()
        job_id = body.get("job_id")
        with JOBS_LOCK:
            job = JOBS.get(job_id)
        if job is None or job["status"] != "done":
            self._json(400, {"error": "job not ready"})
            return
        try:
            data = ingest.load_data()
            category = ingest.insert_entry(data, dict(job["entry"]))
            ingest.DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
            subprocess.run(
                [sys.executable, str(ingest.GENERATE_SCRIPT), str(ingest.DATA_PATH), str(ingest.MD_PATH)],
                check=True,
            )
        except Exception as exc:  # noqa: BLE001
            self._json(500, {"error": str(exc)})
            return
        with JOBS_LOCK:
            JOBS.pop(job_id, None)
        self._json(200, {"ok": True, "category": category})

    def _handle_discard(self):
        body = self._read_json()
        with JOBS_LOCK:
            JOBS.pop(body.get("job_id"), None)
        self._json(200, {"ok": True})

    def log_message(self, fmt, *args):  # quieter default logging
        sys.stderr.write(f"[webapp] {self.address_string()} {fmt % args}\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8765)))
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Serving on http://127.0.0.1:{args.port}", file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
