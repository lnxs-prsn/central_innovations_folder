#!/usr/bin/env python3
"""Live situation for this project's executive, gathered by program, not by memory.

  start  SessionStart hook: inventory of means, intake, questions, method edition,
         subordinate runs, uncommitted work. Injected before the first act.
  stop   Stop hook: blocks ending a turn while objective due work is open.
  ack    Record that the listed indexes' questions have been read.
Standard library only; reads only published parts and this folder.
"""
import json, os, platform, re, shutil, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / ".knowhow" / "situation_state.json"
LOG = ROOT / ".knowhow" / "situation_log.jsonl"
CAPABILITY = ROOT / "published" / "capability" / "capability-003" / "knowhow.py"
TOOLS = ["uv", "codex", "claude", "qodercli", "cao", "unworldly", "gitleaks", "tu-projects",
         "git", "docker", "podman", "wine", "qemu-system-x86_64", "gh", "go", "cargo", "node", "pwsh"]


def run(cmd, timeout=60, cwd=ROOT):
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except (OSError, subprocess.TimeoutExpired) as e:
        return -1, "", str(e)


def load_state():
    try:
        return json.loads(STATE.read_text())
    except (OSError, ValueError):
        return {}


def means():
    found = {t: bool(shutil.which(t)) for t in TOOLS}
    rc, out, _ = run(["uv", "python", "list", "--only-installed"], 20) if found["uv"] else (1, "", "")
    pythons = sorted({m.group(1) for m in re.finditer(r"cpython-(\d+\.\d+\.\d+)", out)})
    docker = "absent"
    if found["docker"]:
        docker = "usable" if run(["docker", "info"], 15)[0] == 0 else "installed, not usable by this user"
    return {"have": [t for t, v in found.items() if v], "missing": [t for t, v in found.items() if not v],
            "pythons": pythons, "docker": docker, "os": f"{platform.system()} {platform.machine()}",
            "cpus": os.cpu_count()}


def parts():
    lst = ROOT / ".knowhow" / "parts.json"
    base = lst.parent
    return [(p, (base / p / "INDEX.md").resolve()) for p in json.loads(lst.read_text())["published_parts"]]


def intake():
    rc, out, err = run([sys.executable, str(CAPABILITY), "ingest", "--project", ".",
                        "--published-parts", ".knowhow/parts.json", "--json"], 120)
    try:
        return json.loads(out).get("counts", {})
    except ValueError:
        return {"error": (err or out)[:300]}


def changed_indexes(state):
    seen = state.get("indexes", {})
    changed, current = [], {}
    for name, idx in parts():
        if idx.exists():
            current[str(idx)] = idx.stat().st_mtime
            if seen.get(str(idx)) != current[str(idx)]:
                changed.append(str(idx))
    return changed, current


def edition():
    local = (ROOT / "directed_opportunism" / "LOCAL.md").read_text()
    applied = re.search(r"^Edition: (\S+)", local, re.M).group(1)
    src = (ROOT / "directed_opportunism" / "source").read_text().strip()
    pub_index = (ROOT / "directed_opportunism" / src).parent / "INDEX.md"
    m = re.search(r"^Current edition: (\S+)", pub_index.read_text(), re.M) if pub_index.exists() else None
    return applied, (m.group(1) if m else "unreadable")


def subordinates():
    rc, out, _ = run(["pgrep", "-af", "codex exec|qodercli -p|claude -p"], 5)
    return [l for l in out.splitlines() if str(os.getpid()) not in l][:5]


IGNORED = ("curator/catalog.sqlite",)  # rewritten by every intake; committed with decisions


def uncommitted():
    return [l for l in run(["git", "status", "--porcelain"], 10)[1].splitlines()
            if not l.strip().endswith(IGNORED)]


def due_items(state, counts, changed, applied, current_ed, dirty):
    due = []
    if current_ed not in (applied, "unreadable"):
        due.append(f"Method edition {current_ed} published, {applied} applied: read its UPDATE.md, tell the CEO if significant, take it.")
    if counts.get("new_contents"):
        due.append(f"Intake found {counts['new_contents']} new content(s): independent read, then decide.")
    if changed:
        due.append("Listed indexes changed since last read (questions?): " + ", ".join(changed)
                   + ". Read them, answer, then run: python3 tools/situation.py ack")
    if dirty:
        due.append(f"{len(dirty)} uncommitted change(s): judge and commit them.")
    return due


def gather():
    state = load_state()
    counts = intake()
    changed, current = changed_indexes(state)
    applied, current_ed = edition()
    dirty = uncommitted()
    return state, counts, changed, current, applied, current_ed, dirty


def start():
    state, counts, changed, current, applied, current_ed, dirty = gather()
    m = means()
    due = due_items(state, counts, changed, applied, current_ed, dirty)
    last = state.get("unresolved_at_last_stop")
    lines = [f"LIVE SITUATION (tools/situation.py, {time.strftime('%Y-%m-%d %H:%M')}) — facts, not records:",
             f"- Means present: {', '.join(m['have'])}. Pythons via uv: {', '.join(m['pythons']) or 'none'}. "
             f"Docker: {m['docker']}. Absent: {', '.join(m['missing'])}. {m['os']}, {m['cpus']} CPUs.",
             f"- Intake: {json.dumps(counts)}",
             f"- Method: applied {applied}; publisher's current {current_ed}.",
             f"- Subordinate runs live: {subordinates() or 'none'}",
             f"- Uncommitted: {len(dirty)}"]
    if last:
        lines.append(f"- PREVIOUS SESSION ENDED WITH DUE WORK OPEN: {last}")
    lines.append("- DUE NOW: " + (" | ".join(due) if due else "nothing objective; choose your own next act toward the stage's done-when."))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "\n".join(lines)}}))


def stop():
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except ValueError:
        payload = {}
    state, counts, changed, current, applied, current_ed, dirty = gather()
    due = due_items(state, counts, changed, applied, current_ed, dirty)
    state["unresolved_at_last_stop"] = due or None
    STATE.write_text(json.dumps(state, indent=1))
    if due and not payload.get("stop_hook_active"):
        print(json.dumps({"decision": "block", "reason": "Due work is open; do it before ending:\n- " + "\n- ".join(due)}))
    elif due:
        with LOG.open("a") as f:
            f.write(json.dumps({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "ended_with_due": due}) + "\n")


def ack():
    state = load_state()
    state["indexes"] = changed_indexes(state)[1]
    STATE.write_text(json.dumps(state, indent=1))
    print("indexes acknowledged:", len(state["indexes"]))


if __name__ == "__main__":
    {"start": start, "stop": stop, "ack": ack}[sys.argv[1] if len(sys.argv) > 1 else "start"]()
