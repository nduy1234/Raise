---
name: raise-pipeline
description: The investor pipeline (researched, drafted, approved, contacted, replied, passed). Use on "status", "pipeline", "approve <id>", "sent <id>", "<investor> replied", "<investor> passed".
---

# Pipeline

Set `R` to `/opt/hermes/.venv/bin/python3 /opt/hermes/skills/raise-pipeline/scripts/raise.py`.

| ask | command |
|---|---|
| status / pipeline | `$R status`: send it as-is, then counts |
| approve <id> | `$R approve <id> --by "<speaker name>" --role "<speaker's roster relationship>"` |
| sent <id> / "I emailed them" | `$R move <id> contacted --by "<speaker>"` |
| replied / passed | `$R move <id> replied` or `$R move <id> passed` |
| details on <id> | `$R show <id>`: include its source links |

## Approval

- Take `--role` from the roster only: `owner` for the row marked `(your owner)`,
  otherwise the recorded relationship (for example `co-founder`, `advisor`). If
  there is no recorded relationship, pass `none`.
- The tool refuses anyone except the owner or a co-founder, and refuses
  drafts that aren't in the `drafted` stage. Relay the refusal in one line.
- After approval, post the final draft text so the founder can copy it into
  their own email. **Approval never sends anything.** Mark `contacted` only
  after a human says it went out, and one investor at a time. Never bulk-mark.
