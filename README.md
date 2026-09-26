# Raise

A fundraising and investor-relations associate for pre-seed founders. You
text it over iMessage. It's built on the Plow Hermes base (OpenClaw 2.0) and
runs in multiplayer threads, so co-founders and advisors can join.

- **Onboard**: builds a startup profile (name, one-liner, sector, stage, raise, location, traction).
- **Find investors**: researches 20-30 real pre-seed angels and funds. Each one comes with a fit reason, recent deals and source links. It never invents investors.
- **Draft intros**: writes a short, personalized email per investor, citing a sourced reason they fit.
- **Pipeline**: tracks each investor as researched → drafted → approved → contacted → replied / passed. Text `status` to see it.
- **Draft update**: writes the monthly investor update (wins, metrics, asks).

**Safety:** Raise never sends email. Anyone in the thread can request research,
but only the owner or a co-founder can approve a draft. It never bulk-sends,
and it never scrapes personal contact info.

## Install (3 steps)

Prerequisites: Docker and the [plow-agents](https://github.com/plow-pbc/plow-agents) CLI on your `PATH`.

1. **Clone and log in**
   ```sh
   git clone https://github.com/nduy1234/Raise.git && cd Raise
   plow-agents login && plow-agents lines   # note a free ln_… line
   ```
2. **Run locally, with usage reporting to the Agent Index**
   ```sh
   plow-agents deploy --local --line ln_xxx
   echo AGENT_ID=raise >> plow-credentials && docker compose up -d --build
   ```
3. **Text it.** Text "hi" to the number `plow-agents lines` shows. Add your
   co-founder to the thread, then tell Raise: "Bo is my co-founder."

For cloud deploys, see [DEMO.md](DEMO.md) and the plow-agents README:
`image push` → `deploy <image@sha256> --line ln_xxx`.

## Layout

| path | what |
|---|---|
| `runtime/persona.md` | Raise's identity, roles and rules. Composed onto the base persona at boot. |
| `skills/raise-*/SKILL.md` | onboard, find-investors, draft-intro, pipeline, update |
| `skills/raise-pipeline/scripts/raise.py` | profile and pipeline state (JSON under `/var/lib/hermes/raise/`) |
| `test_smoke.py` | `python test_smoke.py` |

MIT licensed. See [LICENSE](LICENSE).
