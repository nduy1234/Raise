"""One smoke test: the demo flow end to end against a temp state dir."""
import os, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).parent
CLI = ROOT / "skills/raise-pipeline/scripts/raise.py"


def run(env, *args):
    return subprocess.run([sys.executable, str(CLI), *args], env=env, capture_output=True, text=True)


def test_demo_flow():
    env = {**os.environ, "RAISE_DIR": tempfile.mkdtemp()}
    assert run(env, "profile", "name=Acme", "sector=devtools").returncode == 0
    assert run(env, "add", "--name", "X", "--kind", "fund", "--fit", "f", "--source", "not-a-url").returncode == 1
    iid = run(env, "add", "--name", "Seed Fund", "--kind", "fund", "--fit", "devtools pre-seed",
              "--source", "https://example.com/portfolio").stdout.strip()
    assert run(env, "move", iid, "contacted").returncode == 1          # not approved yet
    assert run(env, "draft", iid, "--text", "Hi").returncode == 0
    assert run(env, "approve", iid, "--by", "Ann", "--role", "advisor").returncode == 1
    assert run(env, "approve", iid, "--by", "Bo", "--role", "co-founder").returncode == 0
    assert "approved 1" in run(env, "status").stdout
    # every skill the Dockerfile ships exists
    for s in ["raise-onboard", "raise-find-investors", "raise-draft-intro", "raise-pipeline", "raise-update"]:
        assert (ROOT / "skills" / s / "SKILL.md").exists(), s
    assert (ROOT / "runtime/persona.md").exists()


if __name__ == "__main__":
    test_demo_flow(); print("smoke ok")
