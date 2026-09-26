---
name: raise-draft-intro
description: Write a short personalized intro email to one investor already in the pipeline, citing a real sourced reason they fit. Use on "draft intros", "draft for <investor or id>". Drafting only; never sends.
---

# Intro drafts

Set `R` to `/opt/hermes/.venv/bin/python3 /opt/hermes/skills/raise-pipeline/scripts/raise.py`.

1. `$R profile` and `$R show <id>` (use `$R status` to find ids).
2. Write the email in 120 words or fewer:
   - Subject: `<Startup>: <one-liner>` (8 words max)
   - Line 1: the specific reason they fit, taken from their recorded `fit` or
     `deals` (for example "You backed Co A in 2025..."). Use only facts the
     record's sources support.
   - 2-3 lines: what the startup does, the traction, the raise amount.
   - Ask: a 20-minute call. Sign with the founder's first name.
3. Save it: `$R draft <id> --text "<subject + body>" --by "<speaker>"`
4. Post the draft in the thread with its id. End with:
   "Owner or a co-founder: reply *approve <id>* to approve. I never send. You send from your own inbox."

For "draft intros" with no id, draft the top 5 `researched` investors, one message each.
