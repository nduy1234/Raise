---
name: raise-onboard
description: Build the founder's startup profile (name, one-liner, sector, stage, raise amount, location, traction). Use on first contact, on "onboard", "update my profile", or when another Raise skill finds a missing profile field.
---

# Onboarding

Set `R` to `/opt/hermes/.venv/bin/python3 /opt/hermes/skills/raise-pipeline/scripts/raise.py`.

1. Run `$R profile`. It prints the profile and a `missing` list.
2. Ask for the missing fields, **two or three per message**, in this order:
   startup name, one-liner, sector, stage, raise amount, location, traction
   (revenue, users, growth, notable customers).
3. Save each answer as soon as you get it:
   `$R profile name="Acme" one_liner="..." sector="devtools" stage="pre-seed" raise_amount="$1.5M" location="SF" traction="..."`
   The field names are `name one_liner sector stage raise_amount location traction`.
4. When `missing` is empty, send a 3-line recap. Offer to run: "Say *find investors* to start."

Only the owner and co-founders can edit the profile. Anyone else can read it.
