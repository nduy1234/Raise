---
name: raise-update
description: Draft the monthly investor update (wins, metrics, asks) from what the team tells you in the thread. Use on "draft update", "investor update", "monthly update".
---

# Investor update

Set `R` to `/opt/hermes/.venv/bin/python3 /opt/hermes/skills/raise-pipeline/scripts/raise.py`.

1. `$R profile` gives the name and one-liner. `$R status` gives fundraising progress.
2. If the team hasn't said this month's wins, metrics and asks, ask for all
   three in one message. Use only numbers the team gave you. Never estimate.
3. Draft, 200 words maximum:
   `Subject: <Startup> — <Month YYYY> update`
   **TL;DR** (1 line) · **Wins** (3 bullets) · **Metrics** (metric: value, change) ·
   **Fundraising** (from status: "N investors in conversation") · **Asks** (2-3 specific intros or hires)
4. Save: `$R update --text "<draft>"`. Post it in the thread for review. You never send it.
