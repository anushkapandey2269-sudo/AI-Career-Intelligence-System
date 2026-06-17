import sqlite3

conn = sqlite3.connect("resume.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS resumes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    score INTEGER,
    role TEXT
)
""")

conn.commit()


def insert_data(name, email, phone, score, role):
    c.execute("""
    INSERT INTO resumes (name, email, phone, score, role)
    VALUES (?, ?, ?, ?, ?)
    """, (name, email, phone, score, role))

    conn.commit()


def get_all_resumes():
    c.execute("""
    SELECT * FROM resumes
    ORDER BY score DESC
    """)
    return c.fetchall()