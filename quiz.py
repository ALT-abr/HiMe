from database import connection
import random
import os
from datetime import datetime

NB_QUESTIONS = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def r_menu(code: str) -> bool:
    if code == "r":
        return True
    return False

def quiz_menu():
    while True:
        clear_screen()

        print("\n_---------------------------------- Q U I Z ----------------------------------_")
        print("| 1. Q u i z  u n    m o t               - t r o u v e  t r a d u c t i o n s |")
        print("| 2. Q u i z  u n e  e x p r e s t i o n - t r o u v e  t r a d u c t i o n s |")
        print("| 3. Q u i z  u n e  d e f i n i t i o n - t r o u v e  m o t s               |")
        print("-------------------------------------------------------------------------------")
    
        choix = input("\nQuel quiz souhaitez-vous lancer : ")

        if r_menu(choix):
            return
        
        if choix == "1":
            vocab_traductions("mot")
        elif choix == "2":
            vocab_traductions("expression")
        elif choix == "3":
            definition_traduction()
        else:
            print("Choix invalide! saisie 1, 2 ou 3")
            continue

def vocab_traductions(q_types: str):
    clear_screen()

    conn, c = connection()

    c.execute("SELECT COUNT(*) FROM vocabulaire WHERE nature_vocab = ?", (q_types,))
    ids = c.fetchone()[0]

    if ids == 0:
        print("La base de données est vide. Aucun vocabulaire disponible !")
        input()
        return
    
    if ids < NB_QUESTIONS:
        print("Il n’y a pas assez de vocabulaire pour lancer ce quiz :(")
        input()
        return
    
    score = 0

    c.execute("SELECT id_vocab, mot_expression FROM vocabulaire WHERE nature_vocab = ? ORDER BY RANDOM() LIMIT ?", (q_types, NB_QUESTIONS))
    vocaburaires = c.fetchall()

    for i, (id_v, vocaburaire) in enumerate(vocaburaires, start=1):
        print(f"Q. {i}/{NB_QUESTIONS} : quelle est la traduction du \"{vocaburaire}\"?")

        c.execute("SELECT traduction from traduction WHERE vocabulaire = ?" ,(id_v,))
        tradc = c.fetchone()

        rep = input("Votre réponse : ").lower().strip()
        if rep == tradc[0]:
            print("Bonne réponse! +2 points.")
            score += 2
        else:
            print("Oops! Réponse incorrecte.")

    if q_types == "mot":
        q_type = "mot-traduction"
    else:
        q_type = "expression-traduction"

    c.execute("INSERT INTO quiz (type_quiz, score_quiz, date_quiz) VALUES(?, ?, ?)", (q_type, score, datetime.now()))

    print(f"Quiz terminé ! Score: {score}/{NB_QUESTIONS * 2}")

    conn.commit()
    conn.close()
    input()

def definition_traduction():
    clear_screen()

    conn, c = connection()

    c.execute("""SELECT COUNT(*) FROM vocabulaire 
                WHERE nature_vocab = 'mot' 
                And definition_vocab IS NOT NULL
                AND definition_vocab != ''""")
    ids = c.fetchone()[0]

    if ids == 0:
        print("la base de donne vide! on a trouve aucun definition!")
        input()
        return
    
    if ids < NB_QUESTIONS:
        print("on a pas un assie du definition pour fiare le quiz! :(")
        input()
        return
    
    score = 0

    c.execute("""SELECT mot_expression, definition_vocab FROM vocabulaire 
              WHERE nature_vocab = 'mot' 
              AND definition_vocab IS NOT NULL
              AND definition_vocab != ''
              ORDER BY RANDOM() LIMIT ?"""
              ,(NB_QUESTIONS,))
    vocaburaires = c.fetchall()

    for i, (vocaburaire, definition) in enumerate(vocaburaires, start=1):
        print(f"Q. {i}/{NB_QUESTIONS} : quelle est le mot de cette definition \"{definition}\" ?")

        rep = input("saisie la : ").lower().strip()
        if rep == vocaburaire:
            print("vous avez gange +2 , Yaay!")
            score += 2
        else:
            print("Oops! movais reponse")

    c.execute("INSERT INTO quiz (type_quiz, score_quiz, date_quiz) VALUES(?, ?, ?)", ("definition-mot", score, datetime.now()))

    print(f"Quiz terminé ! Score: {score}/{NB_QUESTIONS * 2}")

    conn.commit()
    conn.close()
    input()

def q_history():
    clear_screen()
    conn, c = connection()

    c.execute("SELECT type_quiz, score_quiz, date_quiz FROM quiz ORDER BY date_quiz DESC")
    rows = c.fetchall()

    if not rows:
        print("Aucun historique de quiz disponible pour le moment.")
        input()
        return
    
    print("---------------- HISTORIQUE DES QUIZ ----------------")
    print("-" *53)
    for i, (type_q, score_q, date_q) in enumerate(rows, 1):
        print(f" {i} | {type_q} | {score_q} | {date_q}")
        print("-" *53)

    conn.close()
    input()