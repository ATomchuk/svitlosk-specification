import sqlite3
import json

DB = r"C:\Users\ATom\.local\share\mimocode\mimocode.db"
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
c = conn.cursor()

PROJECT_ID = "0c519d09-174f-4d87-8f6e-a0972cfb249e"

# 1. Tasks (use created_at not time_created)
print("=== TASKS ===")
c.execute("""
    SELECT t.id, t.session_id, t.status, t.summary, t.created_at
    FROM task t
    JOIN session s ON t.session_id = s.id
    WHERE s.project_id = ?
    ORDER BY t.created_at DESC
    LIMIT 20
""", (PROJECT_ID,))
for row in c.fetchall():
    d = dict(row)
    print(f"  {d['id']} | session={d['session_id'][:25]}... | status={d['status']} | {d['summary'][:80]}")

# 2. Task events
print("\n=== TASK EVENTS (this project, last 30) ===")
c.execute("""
    SELECT te.task_id, te.kind, te.summary, te.at
    FROM task_event te
    JOIN session s ON te.session_id = s.id
    WHERE s.project_id = ?
    ORDER BY te.at DESC
    LIMIT 30
""", (PROJECT_ID,))
for row in c.fetchall():
    d = dict(row)
    print(f"  task={d['task_id'][:20]} | kind={d['kind']} | at={d['at']} | {(d.get('summary') or '')[:70]}")

# 3. Subagents (actor_registry)
print("\n=== SUBAGENTS (this project) ===")
c.execute("""
    SELECT ar.actor_id, ar.agent, ar.status, ar.description, ar.time_created
    FROM actor_registry ar
    JOIN session s ON ar.session_id = s.id
    WHERE s.project_id = ?
    ORDER BY ar.time_created DESC
    LIMIT 20
""", (PROJECT_ID,))
for row in c.fetchall():
    d = dict(row)
    print(f"  {d['actor_id'][:30]} | agent={d['agent']} | status={d['status']} | {(d.get('description') or '')[:60]}")

# 4. Let's find the main work sessions (non-checkpoint-writer)
print("\n=== MAIN WORK SESSIONS ===")
c.execute("""
    SELECT id, title, time_created
    FROM session
    WHERE project_id = ?
      AND title NOT LIKE 'checkpoint-writer%'
    ORDER BY time_created DESC
    LIMIT 10
""", (PROJECT_ID,))
for row in c.fetchall():
    d = dict(row)
    print(f"  {d['id'][:35]} | created={d['time_created']} | title={d['title'][:60]}")

# 5. User messages in the most recent substantive session (ses_0a442f331ffeo5BwqKq9f62BDm)
print("\n=== USER MESSAGES in ses_0a442f331ffeo5BwqKq9f62BDm ===")
c.execute("""
    SELECT m.id as mid, m.time_created
    FROM message m
    WHERE m.session_id = 'ses_0a442f331ffeo5BwqKq9f62BDm'
      AND json_extract(m.data, '$.role') = 'user'
    ORDER BY m.time_created
""")
for row in c.fetchall():
    mid = row["mid"]
    ts = row["time_created"]
    c2 = conn.cursor()
    c2.execute("SELECT data FROM part WHERE message_id=? ORDER BY time_created LIMIT 1", (mid,))
    part = c2.fetchone()
    text = ""
    if part:
        pd = json.loads(part[0])
        text = pd.get("text", "")[:400].replace("\n", " ")
    if text:
        print(f"  [{ts}] {text[:350]}")

# 6. Assistant tool calls in the most recent substantive session
print("\n=== ASSISTANT TOOL CALLS in ses_0a442f331ffeo5BwqKq9f62BDm (last 10 assistant turns) ===")
c.execute("""
    SELECT m.id as mid, m.time_created
    FROM message m
    WHERE m.session_id = 'ses_0a442f331ffeo5BwqKq9f62BDm'
      AND json_extract(m.data, '$.role') = 'assistant'
    ORDER BY m.time_created DESC
    LIMIT 10
""")
for row in c.fetchall():
    mid = row["mid"]
    ts = row["time_created"]
    c2 = conn.cursor()
    c2.execute("SELECT data FROM part WHERE message_id=? ORDER BY time_created", (mid,))
    tools_used = []
    for part in c2.fetchall():
        pd = json.loads(part[0])
        if pd.get("type") == "tool":
            tools_used.append(pd.get("tool", "?"))
    if tools_used:
        print(f"  [{ts}] tools: {', '.join(tools_used)}")
    else:
        c2.execute("SELECT data FROM part WHERE message_id=? ORDER BY time_created LIMIT 1", (mid,))
        part = c2.fetchone()
        if part:
            pd = json.loads(part[0])
            text = pd.get("text", "")[:200].replace("\n", " ")
            print(f"  [{ts}] text: {text}")

# 7. Look at the latest user request that started the current session
print("\n=== LATEST USER MESSAGES (all sessions, last 5) ===")
c.execute("""
    SELECT m.id as mid, m.session_id, m.time_created
    FROM message m
    WHERE json_extract(m.data, '$.role') = 'user'
      AND m.session_id NOT LIKE '%checkpoint%'
    ORDER BY m.time_created DESC
    LIMIT 5
""")
for row in c.fetchall():
    mid = row["mid"]
    sid = row["session_id"]
    ts = row["time_created"]
    c2 = conn.cursor()
    c2.execute("SELECT data FROM part WHERE message_id=? ORDER BY time_created LIMIT 1", (mid,))
    part = c2.fetchone()
    text = ""
    if part:
        pd = json.loads(part[0])
        text = pd.get("text", "")[:500].replace("\n", " ")
    if text:
        print(f"  [{ts}] sid={sid[:30]}... : {text[:400]}")

conn.close()
