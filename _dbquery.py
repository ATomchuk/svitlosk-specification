import sqlite3, json

DB = r"C:\Users\ATom\.local\share\mimocode\mimocode.db"
conn = sqlite3.connect(DB)
c = conn.cursor()

# Get ALL task events for session ses_0a442f331ffeo5BwqKq9f62BDm to see full A-series completion
c.execute("""
    SELECT te.task_id, te.kind, te.summary, t.status
    FROM task_event te
    JOIN task t ON te.task_id = t.id
    WHERE t.session_id = 'ses_0a442f331ffeo5BwqKq9f62BDm'
    ORDER BY te.at
""")
print("=== All task events for ses_0a442f331ffeo5BwqKq9f62BDm ===")
for tid, kind, summary, status in c.fetchall():
    if kind == 'done' and summary:
        print(f"  {tid} DONE: {summary}")

# Look for user rules/decisions in ses_07ca48cf4ffeA6Tl7qxovdrRm6
sid = "ses_07ca48cf4ffeA6Tl7qxovdrRm6"
c.execute("""
    SELECT m.id, p.data
    FROM message m
    JOIN part p ON p.message_id = m.id
    WHERE m.session_id = ? AND json_extract(m.data, '$.role') = 'user'
    ORDER BY m.time_created, p.time_created
""", (sid,))
rows = c.fetchall()
print(f"\n=== User messages in C-1 session ===")
for mid, pdata in rows:
    if pdata:
        pd = json.loads(pdata)
        text = pd.get('text', '')
        if text:
            print(f"  USER: {text[:500]}")

# Check recent checkpoint for the ses_07ca40494ffeIqi2W6KFwf7kVC (checkpoint writer at 2026-07-21)
sid2 = "ses_07ca40494ffeIqi2W6KFwf7kVC"
c.execute("""
    SELECT m.id, p.data
    FROM message m
    JOIN part p ON p.message_id = m.id
    WHERE m.session_id = ? AND json_extract(m.data, '$.role') = 'assistant'
    ORDER BY m.time_created DESC, p.time_created DESC
    LIMIT 5
""", (sid2,))
rows = c.fetchall()
print(f"\n=== Latest checkpoint-writer session assistant messages ===")
for mid, pdata in rows:
    if pdata:
        pd = json.loads(pdata)
        ptype = pd.get('type', '?')
        text = pd.get('text', '')
        tool = pd.get('tool', '')
        if ptype == 'text' and text:
            print(f"  TEXT: {text[:300]}...")
        elif ptype == 'tool':
            state = pd.get('state', {})
            inp = state.get('input', {})
            if 'file_path' in inp:
                print(f"  TOOL: {tool} -> {inp.get('file_path', '')}")

conn.close()
