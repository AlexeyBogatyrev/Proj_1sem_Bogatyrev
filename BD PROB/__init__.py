
import sqlite3 as sq
with sq.connect('saper.db') as con:
 cur = con.cursor()
 #cur.execute("DROP TABLE IF EXISTS users")
 cur.execute("""CREATE TABLE IF NOT EXISTS users (
 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 sex INTEGER NOT NULL DEFAULT 1,
 old INTEGER,
 score INTEGER
 )""")
cur.execute("SELECT * FROM users")
con.commit()
cur.execute("SELECT * FROM users WHERE sex > 2")
con.commit()
cur.execute("SELECT * FROM users WHERE score < 1000")
con.commit()
cur.execute("SELECT * FROM users ORDER BY score DESC LIMIT 1")
con.commit()
cur.execute("SELECT * FROM users WHERE old BETWEEN 18 AND 20")
con.commit()
cur.execute("UPDATE users SET old = 20  WHERE old = 19")
con.commit()
cur.execute("UPDATE users SET score = score + 300  WHERE score < 1000")
con.commit()
cur.execute("UPDATE users SET score = score + 100  WHERE old >= 20")
con.commit()
cur.execute("DELETE FROM users WHERE score < 1000")
con.commit()
