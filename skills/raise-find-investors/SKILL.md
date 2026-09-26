---
name: raise-find-investors
description: Research 20-30 real pre-seed investors (angels and funds) that fit the startup's sector, stage and check size, with sources. Use on "find investors", "more investors", "research <investor>". Any member of the thread may ask.
---

# Investor research

Set `R` to `/opt/hermes/.venv/bin/python3 /opt/hermes/skills/raise-pipeline/scripts/raise.py`.

1. Run `$R profile`. If anything is missing, run `raise-onboard` first.
2. Search the web with your search tool. Good queries:
   `"pre-seed" <sector> investors <year>`, `<sector> angel investor pre-seed`,
   `<similar startup> pre-seed round led by`, and fund portfolio pages.
   Then **open** each candidate's firm page, portfolio page or a news article
   with your extract/fetch tool. Only keep a candidate if an opened page shows:
   - that they invest at pre-seed or seed, with a check size that fits the raise
     if the page states one, and
   - at least one relevant deal in the sector or an adjacent one (company name
     and year).
3. For each keeper, record it with every URL that supports a claim:
   `$R add --name "Fund Name" --kind fund --fit "one line: why they fit" --deals "Co A (2025), Co B (2024)" --source https://... --source https://... --by "<speaker>"`
   The tool refuses entries without URLs and refuses duplicates.
4. Aim for 20-30. If you verify fewer, say how many and stop. Never pad the list.
5. Reply with a ranked top 10, best fit first, one line each, plus the total:
   `i3  Fund Name — fit reason — Co A '25 — source.url`
   Then add: "Full list: *status*. Say *draft intros* for the top 5."

No personal contact details. Firm and public profile pages only.
