#!/usr/bin/env python3
"""Render a domain catalogue markdown page from its data.json.

Usage: generate.py <data.json> <output.md>
"""
import json
import re
import sys
from pathlib import Path


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def anchor_id(entry: dict) -> str:
    return f"model-{entry['id']}-{entry['date'].replace('-', '')}"


def authors_line(authors: list[dict]) -> str:
    parts = []
    for a in authors:
        parts.append(f"[{a['name']}]({a['url']})" if a.get("url") else a["name"])
    return " & ".join(parts)


def tags_and_text(field: dict | None) -> str:
    if not field:
        return "—"
    tags = field.get("tags") or []
    text = field.get("text") or ""
    tag_str = " ".join(f"`{t}`" for t in tags)
    if tag_str and text:
        return f"{tag_str}<br>{text}"
    return tag_str or text or "—"


def training_data_cell(field: dict | None) -> str:
    if not field:
        return "—"
    text = field.get("text") or ""
    stat = field.get("stat")
    if stat and text:
        return f"{text}<br>**{stat}**"
    return stat or text or "—"


def render_info_table(entry: dict) -> str:
    rows = []
    if entry.get("params"):
        rows.append(("Parameters", entry["params"]))
    if entry.get("backbone"):
        rows.append(("Backbone", entry["backbone"]))
    rows.append(("Pre-training", tags_and_text(entry.get("pretraining"))))
    rows.append(("Training data", training_data_cell(entry.get("training_data"))))
    rows.append(("Downstream tasks", tags_and_text(entry.get("downstream_tasks"))))
    if entry.get("modalities"):
        rows.append(("Modalities", ", ".join(f"`{m}`" for m in entry["modalities"])))
    if entry.get("code"):
        rows.append(("Code", f"[{entry['code'].split('//')[-1]}]({entry['code']})"))
    if entry.get("weights"):
        w = entry["weights"]
        link = f"[{w.split('//')[-1]}]({w})" if w.startswith("http") else w
        rows.append(("Weights", link))
    if entry.get("license"):
        rows.append(("License", entry["license"]))
    if entry.get("note"):
        rows.append(("Note", entry["note"]))

    lines = ["| | |", "| --- | --- |"]
    for label, value in rows:
        lines.append(f"| **{label}** | {value} |")
    return "\n".join(lines)


def render_entry_detail(entry: dict) -> str:
    aid = anchor_id(entry)
    summary = f"<b>{entry['model']}</b> — {entry['title']} <i>({entry['venue']} {entry['date']})</i>"
    doi_link = f" · [doi:{entry['doi']}](https://doi.org/{entry['doi']})" if entry.get("doi") else ""
    header = (
        f"**[{entry['title']}]({entry['url']})**\n\n"
        f"*{entry['venue']}* · {entry['date']} · {authors_line(entry['authors'])}{doi_link}"
    )
    body = [f'<a id="{aid}"></a>', "<details>", f"<summary>{summary}</summary>", "", header, "", render_info_table(entry)]

    results = entry.get("key_results") or []
    if results:
        body += ["", "**Key results**", ""]
        body += [f"- {r}" for r in results]

    body += ["", "</details>"]
    return "\n".join(body)


def render_category(cat: dict) -> str:
    header = ["| Date | Model | Venue | Model size | Open | Headline result |", "| --- | --- | --- | --- | --- | --- |"]
    rows = []
    for e in cat["entries"]:
        model_link = f"[{e['model']}](#{anchor_id(e)})"
        size = e.get("params") or "not stated"
        open_badge = "✓" if e.get("open") else "—"
        headline = e.get("headline") or "—"
        rows.append(f"| {e['date']} | {model_link} | {e['venue']} | {size} | {open_badge} | {headline} |")
    table = "\n".join(header + rows)

    details = "\n\n".join(render_entry_detail(e) for e in cat["entries"])
    return f"### {cat['title']}\n\n{table}\n\n{details}"


def render_tools(tools: list[dict]) -> str:
    header = ["| Name | Description | Links |", "| --- | --- | --- |"]
    rows = []
    for t in tools:
        links = []
        if t.get("code"):
            links.append(f"[code]({t['code']})")
        if t.get("homepage"):
            links.append(f"[homepage]({t['homepage']})")
        rows.append(f"| {t['name']} | {t['description']} | {' · '.join(links) or '—'} |")
    return "\n".join(header + rows)


def render_maintainer(m: dict) -> str:
    name = m["name"]
    if m.get("homepage"):
        line = f"[{name}]({m['homepage']})"
    else:
        line = f"@{name}"
    if m.get("github"):
        line += f" ([GitHub]({m['github']}))"
    return line


def render(data: dict) -> str:
    total = sum(len(c["entries"]) for c in data["categories"])
    parts = [
        "<!-- GENERATED FILE - DO NOT EDIT BY HAND -->",
        "<!-- Generated from pipeline/ai4science/data.json by pipeline/generate.py -->",
        "<!-- Edits made here are overwritten by the next run of the generator. -->",
        "",
        f"# {data['domain']}",
        "",
        data["scope"],
        "",
        f"**Maintainer:** {render_maintainer(data['maintainer'])}",
        "",
        f"**{total} entries** across {len(data['categories'])} categories · [Back to index](README.md)",
        "",
        "## Catalogue",
        "",
    ]
    for cat in data["categories"]:
        parts.append(render_category(cat))
        parts.append("")

    if data.get("tools"):
        parts += [
            "## Tools",
            "",
            "AI tools the team uses for research and literature work. Not papers/models — utilities.",
            "",
            render_tools(data["tools"]),
            "",
        ]

    parts.append("---")
    return "\n".join(parts) + "\n"


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    data_path, out_path = Path(sys.argv[1]), Path(sys.argv[2])
    data = json.loads(data_path.read_text())
    out_path.write_text(render(data))
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
