import sqlite3

conn = sqlite3.connect('moods.sqlite')
cur = conn.cursor()


def fetch():
	cur.execute("SELECT * FROM moods_db")
	rows = cur.fetchall()
	for row in rows:
		print(row)
	conn.close()


def clear():
	cur.execute("DELETE FROM moods_db")
	conn.commit()
	conn.close()

