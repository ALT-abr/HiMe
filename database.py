import sqlite3

def connection():
    conn = sqlite3.connect("HiMe.db")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()
    return conn, c

conn, c = connection()

c.execute("""CREATE TABLE IF NOT EXISTS vocabulaire(
        id_vocab INTEGER PRIMARY KEY,
        mot_expression TEXT NOT NULL,
        nature_vocab TEXT NOT NULL,    /*("mot","expression")*/
        definition_vocab TEXT,
        example_vocab TEXT,
        date_saisie DATETIME
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS traduction(
        id_trad INTEGER PRIMARY KEY,
        traduction TEXT NOT NULL,
        vocabulaire INTEGER NOT NULL,
        FOREIGN KEY(vocabulaire) REFERENCES vocabulaire(id_vocab) ON DELETE CASCADE
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS quiz(
        id_quiz INTEGER PRIMARY KEY,
        type_quiz TEXT NOT NULL,       /*("mot-traduction","expression-traduction","definition-mot")*/
        score_quiz INTEGER NOT NULL,
        date_quiz DATETIME NOT NULL
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS quiz_questions(
        id_vocab INTEGER NOT NULL,
        id_quiz INTEGER NOT NULL,
        PRIMARY KEY(id_vocab, id_quiz),
        FOREIGN KEY(id_vocab) REFERENCES vocabulaire(id_vocab),
        FOREIGN KEY(id_quiz) REFERENCES quiz(id_quiz)
        )""")

conn.commit()
conn.close()

print("Base de données HiMe initialisée avec succès :)")