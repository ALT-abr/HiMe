import sqlite3
from datetime import datetime

def get_vocabulary():
    conn = sqlite3.connect("HiMe.db")
    c = conn.cursor()

    print("\nQuel est le mot du jour ? :)")
    
    while True:
        word = input("\nAjouter un mot/expression * : ").lower().strip()
        if word == "":
            print("Champ obligatoire! Veuillez saisir un mot ou une expression.")
        elif not all(part.isalpha() for part in word.split()):
            print("Siasie un mot ou une expression valide")
        else:
            break

    while True:
        nature = input("Type M = mot / E = expression * : ").lower().strip()
        if nature == "m":
            nature = "mot"
            break
        elif nature == "e":
            nature = "expression"
            break
        else:
            print("Réponse invalide! Choisissez M pour mot ou E pour expression.")

    print("Traduction * :")
    while True:
        langue = input("Choisissez la langue K = kabyle / A = anglais / R = arabe :").lower().strip()
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
    
    definition = input("Définition (optionnelle) : ").lower().strip()
    example = input("Exemple d’utilisation (optionnel) : ").lower().strip()

    c.execute("""INSERT INTO vocabulaire
              (mot_expression,nature_vocab,definition_vocab,example_vocab,date_saisie) 
              VALUES(?,?,?,?,?)""", (word,nature,definition,example,datetime.now()))
    
    c.execute("""INSERT INTO traduction
              (traduction,langue_trad,vocabulaire)
              VALUES(?,?,?)""", (traduction, langue,c.lastrowid))
    
    conn.commit()

    print("Yay! le vocabulaire a été ajouté avec succès!")

def supprimer_vocabulaire(nom: str):
    c = sqlite3.connect("HiMe.db").cursor()

    c.execute("DELETE FROM vocabulaire WHERE mot_expression = (?)", nom)