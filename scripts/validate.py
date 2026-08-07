#!/usr/bin/env python3
"""Validate the catalogue data.

    python scripts/validate.py            # schema + duplicate check (CI gate)
    python scripts/validate.py --report   # also print field coverage per domain
    python scripts/validate.py --links    # also check that every URL resolves

Errors block a merge. Warnings do not -- they are the "this entry could be
richer" backlog, which `--report` summarises.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.schema import (  # noqa: E402
    DATA_DIR,
    Issue,
    Vocab,
    entry_key,
    load_domain,
    load_domains,
    validate_entry,
)

# Fields we want filled everywhere; `--report` counts how far off we are.
COVERAGE_FIELDS = [
    "doi",
    "params",
    "backbone",
    "pretraining",
    "data",
    "tasks",
    "modalities",
    "performance",
    "notebooklm",
]


def describe(entry: dict, index: int) -> str:
    model = (entry.get("model") or {}).get("name") if isinstance(entry, dict) else None
    if model:
        return f"[{index}] {model}"
    title = str(entry.get("title", "?"))[:48] if isinstance(entry, dict) else "?"
    return f"[{index}] {title}"


def check_links(entries_by_domain: dict[str, list[dict]]) -> list[Issue]:
    import urllib.error
    import urllib.request

    issues: list[Issue] = []
    seen: dict[str, int | str] = {}
    for slug, entries in entries_by_domain.items():
        for i, entry in enumerate(entries):
            model = entry.get("model") or {}
            for label, url in (
                ("url", entry.get("url")),
                ("model.repo", model.get("repo")),
                ("model.weights", model.get("weights")),
                ("notebooklm", entry.get("notebooklm")),
            ):
                if not url:
                    continue
                if url in seen:
                    status = seen[url]
                else:
                    request = urllib.request.Request(
                        url,
                        method="HEAD",
                        headers={"User-Agent": "AwesomeBiomedicalAI-linkcheck"},
                    )
                    try:
                        with urllib.request.urlopen(request, timeout=20) as response:
                            status = response.status
                    except urllib.error.HTTPError as exc:
                        status = exc.code
                    except Exception as exc:  # noqa: BLE001 - network is best-effort
                        status = type(exc).__name__
                    seen[url] = status
                # Publishers routinely answer HEAD with 403 behind a bot wall; only
                # a hard 404/410 is worth failing a maintainer's PR over.
                if status in (404, 410):
                    issues.append(
                        Issue(
                            "error",
                            f"{slug} {describe(entry, i)}",
                            f"{label} is dead ({status}): {url}",
                        )
                    )
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", action="store_true", help="print field coverage")
    parser.add_argument("--links", action="store_true", help="check that URLs resolve")
    args = parser.parse_args()

    vocab = Vocab.load()
    domains = load_domains()

    issues: list[Issue] = []
    entries_by_domain: dict[str, list[dict]] = {}
    keys_seen: dict[str, str] = {}

    for domain in domains:
        slug = domain["slug"]
        if not (DATA_DIR / f"{slug}.yaml").exists():
            continue
        entries = load_domain(slug)
        entries_by_domain[slug] = entries

        for i, entry in enumerate(entries):
            where = f"{slug} {describe(entry, i)}"
            issues.extend(validate_entry(entry, where, vocab))

            if not isinstance(entry, dict):
                continue
            key = entry_key(entry)
            if key in keys_seen:
                issues.append(
                    Issue(
                        "error",
                        where,
                        f"duplicate of {keys_seen[key]} (same {key.split(':', 1)[0]})",
                    )
                )
            else:
                keys_seen[key] = where

    if args.links:
        issues.extend(check_links(entries_by_domain))

    errors = [i for i in issues if i.level == "error"]
    warnings = [i for i in issues if i.level == "warn"]
    total = sum(len(v) for v in entries_by_domain.values())

    if errors:
        print(f"{len(errors)} error(s):")
        for issue in errors:
            print(issue)
        print()

    if warnings and args.report:
        print(f"{len(warnings)} warning(s):")
        for issue in warnings:
            print(issue)
        print()

    if args.report:
        print("Field coverage")
        print(f"  {'domain':<20} {'n':>4}  " + "  ".join(f"{f[:8]:>8}" for f in COVERAGE_FIELDS))
        for slug, entries in entries_by_domain.items():
            filled = Counter()
            for entry in entries:
                for field_name in COVERAGE_FIELDS:
                    if entry.get(field_name) not in (None, "", [], {}):
                        filled[field_name] += 1
            cells = "  ".join(
                f"{filled[f]}/{len(entries):<6}"[:8].rjust(8) for f in COVERAGE_FIELDS
            )
            print(f"  {slug:<20} {len(entries):>4}  {cells}")
        print()

        needs_verify = defaultdict(list)
        for slug, entries in entries_by_domain.items():
            for entry in entries:
                if entry.get("verify"):
                    name = (entry.get("model") or {}).get("name", entry.get("title"))
                    needs_verify[slug].append(name)
        if needs_verify:
            print("Entries flagged for human verification")
            for slug, names in needs_verify.items():
                for name in names:
                    print(f"  {slug}: {name}")
            print()

    unmigrated = [
        d["slug"] for d in domains if not (DATA_DIR / f"{d['slug']}.yaml").exists()
    ]
    print(f"Validated {total} entries across {len(entries_by_domain)} structured domain(s).")
    if unmigrated:
        print(f"Still hand-maintained markdown: {', '.join(unmigrated)}")
    if warnings and not args.report:
        print(f"{len(warnings)} warning(s) -- run with --report to see them.")

    if errors:
        print("\nFAILED")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
