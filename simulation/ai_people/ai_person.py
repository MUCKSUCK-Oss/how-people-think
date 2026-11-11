"""Shared helper: ask one AI person one question.

Each call is a separate, fresh Claude (Haiku) run through the `claude` command-line tool
(Claude Pro plan, no API key). The AI person gets only its system prompt (its life story)
and the page it is shown: no tools, no memory, no project files, and it is never told this
is an experiment. Calls run from an empty folder so no project context can leak in.
"""
import os
import subprocess
import time

HERE = os.path.dirname(os.path.abspath(__file__))
EMPTY_DIR = os.path.join(HERE, "_empty_workdir")
os.makedirs(EMPTY_DIR, exist_ok=True)
MODEL = "haiku"


def ask(system, user, model=MODEL):
    """Return the AI person's reply text (or 'ERROR: ...' after 3 failed tries)."""
    cmd = ["claude", "-p", user, "--model", model, "--system-prompt", system, "--tools", "",
           "--strict-mcp-config", "--setting-sources", "", "--disable-slash-commands",
           "--no-session-persistence", "--output-format", "text"]
    for attempt in range(3):
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=EMPTY_DIR, timeout=180)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
        time.sleep(5 * (attempt + 1))
    return "ERROR: " + (r.stderr or r.stdout)[:300]
