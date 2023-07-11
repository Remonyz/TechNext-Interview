import sqlite3

conn = sqlite3.connect('user.db')
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")
table_exists = c.fetchone()
if not table_exists:
    c.execute("""CREATE TABLE user(
        company_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        date INTEGER
    )""")

conn.commit()
conn.close()

def keyword_search(word):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    query = "SELECT * FROM user WHERE company LIKE ?"
    c.execute(query, ('%' + word + '%',))

    results = c.fetchall()
    print(results)
    return results

def add_comp(company_name, date):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO user(company, date) VALUES ('{company_name}', '{date}')")
    conn.commit()

def sort_date(word):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    query = "SELECT * FROM user WHERE company LIKE ? ORDER BY CAST(date AS INTEGER) DESC"
    c.execute(query, ('%' + word + '%',))

    results = c.fetchall()
    return results