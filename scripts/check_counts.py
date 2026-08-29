import sqlite3

def check():
    con = sqlite3.connect('data/app.db')
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    for t in tables:
        name = t[0]
        if not name.startswith('sqlite_'):
            cnt = cur.execute(f"SELECT count(*) FROM {name}").fetchone()[0]
            print(f"{name}: {cnt}")

if __name__ == '__main__':
    check()
