import sqlite3

conn = sqlite3.connect('moods.sqlite')
cur = conn.cursor()
cur.execute("SELECT * FROM moods_db")
rows = cur.fetchall()
for row in rows:
	print(row)
