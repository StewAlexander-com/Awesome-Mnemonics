"""
Awesome Mnemonics CLI – pipeline and search from mnemonics-index.yaml.

Usage:
  mnemonic pipeline [name-or-id]   Show pipeline(s). No arg = list all.
  mnemonic search <term>           Mnemonics and pipelines matching term.

Output formats (--output): table (default), json, markdown.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from importlib import resources


def find_index() -> tuple[str, bool]:
    """Return (path_or_empty, from_pkg). from_pkg: load via importlib.resources."""
    # 1) Env override
    path = os.environ.get("AWESOME_MNEMONICS_INDEX")
    if path and os.path.isfile(path):
        return (path, False)
    # 2) Cwd
    cand = os.path.join(os.getcwd(), "mnemonics-index.yaml")
    if os.path.isfile(cand):
        return (cand, False)
    # 3) Bundled in package (avoids as_file temp-cleanup; read_text is safe)
    try:
        resources.read_text("mnemonic_cli", "data/mnemonics_index.yaml")
        return ("", True)
    except Exception:
        pass
    return ("", False)


def load_index(path: str, from_pkg: bool) -> dict:
    try:
        import yaml
    except ImportError:
        print("Requires PyYAML: pip install PyYAML", file=sys.stderr)
        sys.exit(1)
    if from_pkg:
        raw = resources.read_text("mnemonic_cli", "data/mnemonics_index.yaml")
        return yaml.safe_load(raw) or {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _fmt_table(fmt: str, *, json_out: dict | None = None, md: str | None = None) -> str:
    if fmt == "json":
        return json.dumps(json_out, indent=2)
    if fmt == "markdown":
        return md or ""
    return ""


def cmd_pipeline(data: dict, name_or_id: str | None, fmt: str) -> None:
    pipelines = data.get("pipelines") or []
    if not name_or_id:
        # list all
        rows = []
        for p in pipelines:
            steps = " → ".join(p.get("steps") or [])
            rows.append({"id": p.get("id", ""), "name": p.get("name", ""), "steps": steps})
        if fmt == "json":
            print(json.dumps({"pipelines": rows}, indent=2))
            return
        if fmt == "markdown":
            print("| id | name | steps |")
            print("|----|------|-------|")
            for r in rows:
                print(f"| {r['id']} | {r['name']} | {r['steps']} |")
            return
        for r in rows:
            print(f"  {r['id']}: {r['name']}  [{r['steps']}]")
        return

    q = (name_or_id or "").lower()
    for p in pipelines:
        pid = (p.get("id") or "").lower()
        pname = (p.get("name") or "").lower()
        if q in pid or q in pname:
            steps = p.get("steps") or []
            obj = {
                "name": p.get("name", p.get("id", "")),
                "id": p.get("id", ""),
                "steps": steps,
                "when": p.get("when"),
                "time": p.get("time"),
                "tags": p.get("tags", []),
            }
            if fmt == "json":
                print(json.dumps(obj, indent=2))
                return
            if fmt == "markdown":
                print(f"## {obj['name']}\n")
                print(f"- **Steps:** {' → '.join(steps)}")
                if obj.get("when"):
                    print(f"- **When:** {obj['when']}")
                if obj.get("time"):
                    print(f"- **Time:** {obj['time']}")
                if obj.get("tags"):
                    print(f"- **Tags:** {', '.join(obj['tags'])}")
                return
            print("Pipeline:", obj["name"])
            print("  Steps:", " → ".join(steps))
            if p.get("when"):
                print("  When:", p["when"])
            if p.get("time"):
                print("  Time:", p["time"])
            return

    print("No pipeline matching:", name_or_id, file=sys.stderr)
    sys.exit(1)


def cmd_search(data: dict, term: str, fmt: str) -> None:
    if not term:
        print("Usage: mnemonic search <term>", file=sys.stderr)
        sys.exit(1)
    q = term.lower()
    mnemonics = data.get("mnemonics") or []
    pipelines = data.get("pipelines") or []

    hits_m: list[dict] = []
    for m in mnemonics:
        mid = (m.get("id") or "").lower()
        tags = " ".join(m.get("tags") or []).lower()
        if q in mid or q in tags:
            hits_m.append({"id": m.get("id", ""), "tags": m.get("tags", [])})

    hits_p: list[dict] = []
    for p in pipelines:
        pid = (p.get("id") or "").lower()
        pname = (p.get("name") or "").lower()
        tags = " ".join(p.get("tags") or []).lower()
        if q in pid or q in pname or q in tags:
            steps = " → ".join(p.get("steps") or [])
            hits_p.append({
                "id": p.get("id", ""),
                "name": p.get("name", ""),
                "steps": steps,
                "tags": p.get("tags", []),
            })

    if fmt == "json":
        print(json.dumps({"mnemonics": hits_m, "pipelines": hits_p}, indent=2))
        return

    if fmt == "markdown":
        print("### Mnemonics\n")
        if hits_m:
            print("| id | tags |")
            print("|----|------|")
            for h in hits_m:
                print(f"| {h['id']} | {', '.join(h['tags'])} |")
        else:
            print("*None*")
        print("\n### Pipelines\n")
        if hits_p:
            print("| id | name | steps |")
            print("|----|------|-------|")
            for h in hits_p:
                print(f"| {h['id']} | {h['name']} | {h['steps']} |")
        else:
            print("*None*")
        return

    # table (default)
    print("Mnemonics:")
    if hits_m:
        for h in hits_m:
            print(f"  {h['id']:<12}  tags: {h['tags']}")
    else:
        print("  (none)")
    print("Pipelines:")
    if hits_p:
        for h in hits_p:
            print(f"  {h['id']}: {h['name']}  [{h['steps']}]")
    else:
        print("  (none)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Awesome Mnemonics CLI – pipeline and search from mnemonics-index.yaml.",
        epilog="Examples:\n  mnemonic pipeline              # list all\n  mnemonic pipeline crisis       # one pipeline\n  mnemonic search network        # mnemonics + pipelines matching 'network'\n  mnemonic search stress -o json",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("pipeline", help="Show pipeline(s). No arg = list all.")
    pp.add_argument("name_or_id", nargs="?", help="Pipeline id or name (e.g. crisis, rapid-triage)")
    pp.add_argument("-o", "--output", choices=["table", "json", "markdown"], default="table", help="Output format (default: table)")

    ps = sub.add_parser("search", help="Mnemonics and pipelines matching a term.")
    ps.add_argument("term", nargs="?", help="Search term (e.g. network, stress, rca)")
    ps.add_argument("-o", "--output", choices=["table", "json", "markdown"], default="table", help="Output format (default: table)")

    args = parser.parse_args()

    path, from_pkg = find_index()
    if not path and not from_pkg:
        print("mnemonics-index.yaml not found. Set AWESOME_MNEMONICS_INDEX, run from repo root, or pip install the package.", file=sys.stderr)
        sys.exit(1)
    data = load_index(path, from_pkg)

    out = getattr(args, "output", "table") or "table"

    if args.cmd == "pipeline":
        cmd_pipeline(data, getattr(args, "name_or_id", None), out)
    elif args.cmd == "search":
        cmd_search(data, (getattr(args, "term", "") or "").strip(), out)


if __name__ == "__main__":
    main()
