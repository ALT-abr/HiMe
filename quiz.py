import sqlite3
import random
import os
from datetime import datetime

conn = sqlite3.connect("HiMe.db")
c = conn.cursor()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def r_menu(code: str) -> bool:
    if code == "r":
        return True
    return False

def quiz_menu():
    clear_screen()

    print("\nQ U I Z")
    print("1. Quiz un mot - trouve traductions")
    print("2. Quiz une exprestion - trouve traductions")
    print("3. Quiz une definition - trouve mots")
    
    quiz_choix()

def quiz_choix():
    while True:
        choix = input("\nQuelle quiz vous vollez jouer aujourduit : ")

        if r_menu(choix):
            return
        
        if choix == "":
            print("choix invalid, vous devez saisie quelle quiz vous vollez joue!")
            continue
        
        if choix == "1":
            vocab_traductions("mot")
        elif choix == "2":
            vocab_traductions("expression")
        elif choix == "3":
            definition_traduction()
        else:
            print("choix invalide! saisie 1, 2 ou 3")
            continue

def vocab_traductions(q_types: str):
    clear_screen()
    c.execute("SELECT COUNT(*) FROM vocabulaire WHERE nature_vocab = ?", (q_types,))
    ids = c.fetchone()[0]

    if ids == 0:
        print("la base de donne vide! on a trouve aucun vocabulaire!")
        input()
        return
    
    if ids < 5:
        print("on a pas un assie du vocabulaire pour fiare le quiz! :(")
        input()
        return
    
    score = 0

    c.execute("SELECT id_vocab, mot_expression FROM vocabulaire WHERE nature_vocab = ? ORDER BY RANDOM() LIMIT 5", (q_types,))
    vocaburaires = c.fetchall()

    for i, (id_v, vocaburaire) in enumerate(vocaburaires, start=1):
        print(f"Q. {i}/5 : quelle est la traduction du \"{vocaburaire}\"?")

        c.execute("SELECT traduction from traduction WHERE vocabulaire = ?" ,(id_v,))
        tradc = c.fetchone()

        rep = input("saisie la : ").lower().strip()
        if rep == tradc[0]:
            print("vous avez gange +2 , Yaay!")
            score += 2
        else:
            print("Oops! movais reponse")

    if q_types == "mot":
        q_type = "mot-traduction"
    else:
        q_type = "expression-traduction"

    c.execute("INSERT INTO quiz (type_quiz, score_quiz, date_quiz) VALUES(?, ?, ?)", (q_type, score, datetime.now()))
    conn.commit()

    print(f"Quiz terminé ! Score: {score}/10")
    input()

def definition_traduction():
    clear_screen()

    c.execute("""SELECT COUNT(*) FROM vocabulaire 
                WHERE nature_vocab = 'mot' 
                And definition_vocab IS NOT NULL
                AND definition_vocab != ''""")
    ids = c.fetchone()[0]

    if ids == 0:
        print("la base de donne vide! on a trouve aucun definition!")
        input()
        return
    
    if ids < 5:
        print("on a pas un assie du definition pour fiare le quiz! :(")
        input()
        return
    
    score = 0

    c.execute("""SELECT mot_expression, definition_vocab FROM vocabulaire 
              WHERE nature_vocab = 'mot' 
              ORDER BY RANDOM() LIMIT 5""")
    vocaburaires = c.fetchall()

    for i, (vocaburaire, definition) in enumerate(vocaburaires, start=1):
        print(f"Q. {i}/5 : quelle est la traduction du \"{definition}\"?")

        rep = input("saisie la : ").lower().strip()
        if rep == vocaburaire:
            print("vous avez gange +2 , Yaay!")
            score += 2
        else:
            print("Oops! movais reponse")

    c.execute("INSERT INTO quiz (type_quiz, score_quiz, date_quiz) VALUES(?, ?, ?)", ("definition-mot", score, datetime.now()))
    conn.commit()

    print(f"Quiz terminé ! Score: {score}/10")
    input()

def q_history():
    c.execute("SELECT type_quiz, score_quiz, date_quiz FROM quiz")
    rows = c.fetchall()

    if not rows:
        print("y a aucun hestorique pour le memant")
        input()
        return

    for row in rows:
        print(row)

    input()