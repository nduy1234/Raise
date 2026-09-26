#!/usr/bin/env python3
"""Raise state CLI: founder profile + investor pipeline, two JSON files.

Nothing here sends anything. It only records state, and refuses moves the
rules forbid (no investor without a source link, no approval by anyone but the
owner or a co-founder, no "contacted" before "approved").
"""
import argparse, json, os, sys, time
from pathlib import Path

DIR = Path(os.environ.get("RAISE_DIR", "/var/lib/hermes/raise"))
PROFILE, PIPE = DIR / "profile.json", DIR / "pipeline.json"
STAGES = ["researched", "drafted", "approved", "contacted", "replied", "passed"]
APPROVERS = {"owner", "co-founder", "cofounder"}
PROFILE_KEYS = ["name", "one_liner", "sector", "stage", "raise_amount", "location", "traction"]


def load(p, default):
    return json.loads(p.read_text()) if p.exists() else default


def save(p, data):
    DIR.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2))
    tmp.replace(p)


def die(msg):
    print(f"refusing: {msg}", file=sys.stderr)
    sys.exit(1)


def find(pipe, iid):
    for inv in pipe["investors"]:
        if inv["id"] == iid:
            return inv
    die(f"no investor {iid}")


def log(inv, stage, by):
    inv["stage"] = stage
    inv.setdefault("history", []).append({"stage": stage, "by": by, "at": time.strftime("%Y-%m-%dT%H:%M:%S")})


def main(argv=None):
    ap = argparse.ArgumentParser(prog="raise.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pr = sub.add_parser("profile"); pr.add_argument("pairs", nargs="*", help="key=value")
    a = sub.add_parser("add")
    a.add_argument("--name", required=True); a.add_argument("--kind", choices=["angel", "fund"], required=True)
    a.add_argument("--fit", required=True); a.add_argument("--deals", default="")
    a.add_argument("--source", action="append", required=True); a.add_argument("--by", default="")
    d = sub.add_parser("draft"); d.add_argument("id"); d.add_argument("--text", required=True); d.add_argument("--by", default="")
    p = sub.add_parser("approve"); p.add_argument("id"); p.add_argument("--by", required=True); p.add_argument("--role", required=True)
    m = sub.add_parser("move"); m.add_argument("id"); m.add_argument("stage", choices=["contacted", "replied", "passed"]); m.add_argument("--by", default="")
    sub.add_parser("status")
    s = sub.add_parser("show"); s.add_argument("id")
    u = sub.add_parser("update"); u.add_argument("--text", required=True)
    args = ap.parse_args(argv)

    if args.cmd == "profile":
        prof = load(PROFILE, {})
        for kv in args.pairs:
            k, _, v = kv.partition("=")
            if k not in PROFILE_KEYS:
                die(f"unknown field {k}; fields: {', '.join(PROFILE_KEYS)}")
            prof[k] = v
        if args.pairs:
            save(PROFILE, prof)
        missing = [k for k in PROFILE_KEYS if not prof.get(k)]
        print(json.dumps({"profile": prof, "missing": missing}, indent=2))
        return

    pipe = load(PIPE, {"investors": []})
    if args.cmd == "add":
        if not all(u.startswith(("http://", "https://")) for u in args.source):
            die("every investor needs a real source URL")
        if any(i["name"].lower() == args.name.lower() for i in pipe["investors"]):
            die(f"{args.name} already in pipeline")
        iid = f"i{len(pipe['investors']) + 1}"
        inv = {"id": iid, "name": args.name, "kind": args.kind, "fit": args.fit,
               "deals": args.deals, "sources": args.source}
        log(inv, "researched", args.by)
        pipe["investors"].append(inv); save(PIPE, pipe); print(iid)
    elif args.cmd == "draft":
        inv = find(pipe, args.id)
        if STAGES.index(inv["stage"]) > 1:
            die(f"{inv['name']} is already {inv['stage']}")
        inv["draft"] = args.text; log(inv, "drafted", args.by); save(PIPE, pipe)
    elif args.cmd == "approve":
        inv = find(pipe, args.id)
        if args.role.lower() not in APPROVERS:
            die(f"{args.by} is {args.role}; only the owner or a co-founder can approve")
        if inv["stage"] != "drafted":
            die(f"{inv['name']} is {inv['stage']}, not drafted")
        log(inv, "approved", f"{args.by} ({args.role})"); save(PIPE, pipe)
    elif args.cmd == "move":
        inv = find(pipe, args.id)
        if args.stage == "contacted" and inv["stage"] != "approved":
            die(f"{inv['name']} is {inv['stage']}; approve before contacting")
        log(inv, args.stage, args.by); save(PIPE, pipe)
    elif args.cmd == "show":
        print(json.dumps(find(pipe, args.id), indent=2))
    elif args.cmd == "status":
        counts = {s: 0 for s in STAGES}
        for i in pipe["investors"]:
            counts[i["stage"]] += 1
            print(f"{i['id']:>4}  {i['stage']:<10}  {i['name']} ({i['kind']})")
        print(" | ".join(f"{s} {n}" for s, n in counts.items()))
    elif args.cmd == "update":
        DIR.mkdir(parents=True, exist_ok=True)
        f = DIR / f"update-{time.strftime('%Y-%m')}.md"
        f.write_text(args.text); print(f)


if __name__ == "__main__":
    main()
