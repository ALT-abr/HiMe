import sqlite3

conn = sqlite3.connect("HiMe.db")
c = conn.cursor()

c.execute("DELETE FROM traduction")
c.execute("DELETE FROM quiz_questions")
c.execute("DELETE FROM quiz")
c.execute("DELETE FROM vocabulaire")

conn.commit()
conn.close()

print("\nLa base de données est nettoyée !")