import sqlite3
conn = sqlite3.connect(r"thefuck\.code-review-graph\graph.db")
tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")]
print("Tables:", tables)
for t in tables:
    cnt = conn.execute(f"SELECT COUNT(*) FROM [{t}]").fetchone()[0]
    print(f"  {t}: {cnt} rows")
    if cnt > 0:
        cols = [d[0] for d in conn.execute(f"SELECT * FROM [{t}] LIMIT 1").description]
        print(f"    columns: {cols}")
        row = conn.execute(f"SELECT * FROM [{t}] LIMIT 1").fetchone()
        print(f"    sample:  {row[:5] if len(row) > 5 else row}")
conn.close()
