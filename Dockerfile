# Raise: a variant of the Plow Hermes base image (plow-pbc/plow-hermes-agent).
# The base brings the Hermes gateway, the plow_chat plugin (iMessage and
# multiplayer threads), and the Agent Index usage reporter, which runs when
# AGENT_ID is set. This image adds only a persona and skills.
FROM public.ecr.aws/e1h7x4a2/plow-cloud-agents:base-67021a7029e33e80bcb27899be6515a5a0e9b37b@sha256:0c3892e93c1a001c61fb7106396e0a4b7e0219008184fd90719caa84a3390ff0

# plow-init composes SOUL.md at boot as the base persona followed by this file.
COPY --chmod=0644 runtime/persona.md /opt/hermes/plow-seed/persona.md
COPY LICENSE /usr/share/doc/raise/

# Skills live outside the agent's home and stay root-owned. The runtime seeds
# them into the home.
COPY skills/ /opt/hermes/skills/
RUN find /opt/hermes/skills -mindepth 1 -type d -exec chmod 0755 {} + \
 && find /opt/hermes/skills -mindepth 1 -type f -exec chmod 0644 {} + \
 && install -d -o 10000 -g 10000 -m 0700 /var/lib/hermes/raise
