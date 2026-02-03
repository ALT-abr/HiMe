import os
import sqlite3
from datetime import datetime

def clrean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def r_menu(code: str) -> bool:
    if code == "r":
        return True
    return False

def get_vocabulary():
    clrean_screen()

    conn = sqlite3.connect("HiMe.db")
    c = conn.cursor()

    print("\nQuel est le mot du jour ? :)")
    
    #recuperation du vocabulaire
    while True:
        word = input("\nAjouter un mot/expression * : ").lower().strip()

        if r_menu(word):
            return

        if word == "":
            print("Champ obligatoire! Veuillez saisir un mot ou une expression.")
            continue
        elif not all(part.isalpha() for part in word.split()):
            print("Siasie un mot ou une expression valide")
            continue

        c.execute("SELECT mot_expression FROM vocabulaire WHERE mot_expression = ?" ,(word,))
        existe_w = c.fetchone()
        if existe_w is not None:
            print(f"Le vocabulaire \"{existe_w[0]}\" est existe deja !")
            continue

        break
    
    #recupere la nature du vocabulaire mot ou exprestion
    while True:
        nature = input("Type M = mot / E = expression * : ").lower().strip()

        if r_menu(nature):
            return

        if nature == "m":
            nature = "mot"
            break
        elif nature == "e":
            nature = "expression"
            break
        else:
            print("Réponse invalide! Choisissez M pour mot ou E pour expression.")

    #recupere la traduction et la langue a traduire
    print("Traduction * :")
    while True:
        langue = input("Choisissez la langue K = kabyle / A = anglais / R = arabe :").lower().strip()

        if r_menu(langue):
            return
        
        if langue == "":
            print("Champ obligatoire!")
            continue

        if langue == "k":
            langue = "kabyle"
        elif langue == "a":
            langue = "anglais"
        elif langue == "r":
            langue = "arabe"
        else:
            print("Choix invalide! Veuillez entrer K, A ou R")
            continue

        traduction = input(f"Saisissez la traduction en \"{langue}\" : ").lower().strip()
        if traduction == "":
            print("La traduction est obligatoire!")
            continue
        elif not all(part.isalpha() for part in word.split()):
            print("La traduction doit contenir uniquement des lettres!")
            continue

        break
    
    #recupere la definition du vocabulaire
    definition = input("Définition (optionnelle) : ").lower().strip()
    if r_menu(definition):
            return

    #recupere un exmple avec le vocabulaire
    example = input("Exemple d’utilisation (optionnel) : ").lower().strip()
    if r_menu(example):
            return

    c.execute("""INSERT INTO vocabulaire
              (mot_expression,nature_vocab,definition_vocab,example_vocab,date_saisie) 
              VALUES(?,?,?,?,?)""", (word,nature,definition,example,datetime.now()))
    
    c.execute("""INSERT INTO traduction
              (traduction,langue_trad,vocabulaire)
              VALUES(?,?,?)""", (traduction, langue,c.lastrowid))
    
    conn.commit()
    conn.close()

    print("Yay! le vocabulaire a été ajouté avec succès!")
    input("")

def supprimer_vocabulaire():
    clrean_screen()

    conn = sqlite3.connect("HiMe.db")
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    while True:
        nom = input("quelle vocabulaire souhite vous a supprimer : ").lower().strip()
        if nom == "":
            break

        c.execute("SELECT id_vocab FROM vocabulaire WHERE mot_expression = ?", (nom,))
        ver = c.fetchone()
        if ver is None:
            print("Mot ou expression introuvable.")
        else:
            break

    c.execute("DELETE FROM vocabulaire WHERE mot_expression = ?", (nom,))

    conn.commit()
    conn.close()
    print("\nMot / expression supprimé avec succès.")

def get_choix():
    while True:
        choix = input("voire M = ma listes des mots ou E = ma listes des expresions : ").lower()
        if choix == "m":
            choix = "mot"
            break
        elif choix == "e":
            choix = "expression"
            break
        else:
            print("choix invalide! resaye.")
    return choix

def get_list(nature: str):
    clrean_screen()
    
    conn = sqlite3.connect("HiMe.db")
    c = conn.cursor()

    if nature == "mot":
        c.execute("SELECT mot_expression, definition_vocab, example_vocab FROM vocabulaire WHERE nature_vocab = ?" ,(nature,))
        items = c.fetchall()
    elif nature == "expression":
        c.execute("SELECT mot_expression, definition_vocab, example_vocab FROM vocabulaire WHERE nature_vocab = ?" ,(nature,))
        items = c.fetchall()

    if not items:
        print("La liste est vide pour l'instant.")
        conn.close()
        input("")
        return
    
    print("-" *50)
    for i, (mot, definition, example) in enumerate(items, 1):
        print(f"{i} | {mot} | {definition or '-'} | {example or '-'}")
        print("-" *50)

    conn.close()

    input("")