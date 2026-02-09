from database import connection
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def r_menu(code: str) -> bool:
    if code == "r":
        return True
    return False

def get_vocabulary():
    clear_screen()

    conn, c = connection()

    print("\nAjout d’un nouveau vocabulaire :)")

    #recupere la nature du vocabulaire mot ou exprestion
    while True:
        print("\nSaisie M pour mot *")
        print("Saisie E pour expression *")
        nature = input("--> ").lower().strip()

        if r_menu(nature):
            conn.close()
            return

        if nature == "m":
            nature = "mot"
            break
        elif nature == "e":
            nature = "expression"
            break
        else:
            print("Réponse invalide! Choisissez M pour mot ou E pour expression.")
    
    #recuperation du vocabulaire
    while True:
        print("\nVeuillez saisir un mot ou une expression valide *")
        word = input("--> ").lower().strip()

        if r_menu(word):
            conn.close()
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
            print(f"Ce vocabulaire existe déjà !")
            continue

        break

    #recupere la traduction et la langue a traduire
    while True:
        print("\nTraduction * :")
        traduction = input("--> ").lower().strip()

        if traduction == "":
            print("La traduction est obligatoire!")
            continue
        elif not all(part.isalpha() for part in traduction.split()):
            print("La traduction doit contenir uniquement des lettres!")
            continue

        break
    
    #recupere la definition du vocabulaire
    print("\nDéfinition (optionnelle)")
    definition = input("--> : ").lower().strip()
    if r_menu(definition):
            conn.close()
            return

    #recupere un exmple avec le vocabulaire
    print("\nExemple d’utilisation (optionnel)")
    example = input("--> : ").lower().strip()
    if r_menu(example):
            conn.close()
            return

    c.execute("""INSERT INTO vocabulaire
              (mot_expression,nature_vocab,definition_vocab,example_vocab,date_saisie) 
              VALUES(?,?,?,?,?)""", (word,nature,definition,example,datetime.now()))
    
    c.execute("""INSERT INTO traduction
              (traduction,vocabulaire)
              VALUES(?,?)""", (traduction, c.lastrowid))
    
    conn.commit()
    conn.close()

    print("Yaay! Le vocabulaire a été ajouté avec succès.")
    input("")

def supprimer_vocabulaire():
    clear_screen()

    conn, c = connection()

    while True:
        print("Quel vocabulaire souhaitez-vous supprimer ?")
        nom = input("--> ").lower().strip()
        if nom == "":
            conn.close()
            return

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
    input()

def get_choix():
    while True:
        print("E pour affiche la liste des expressions")
        print("M pour affiche la liste des mots")
        choix = input("--> : ").lower()
        if choix == "m":
            choix = "mot"
            break
        elif choix == "e":
            choix = "expression"
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
    return choix

def get_list(nature: str):
    clear_screen()
    
    conn, c = connection()

    if nature == "mot":
        c.execute("SELECT mot_expression, definition_vocab, example_vocab FROM vocabulaire WHERE nature_vocab = ?" ,(nature,))
        items = c.fetchall()
    elif nature == "expression":
        c.execute("SELECT mot_expression, definition_vocab, example_vocab FROM vocabulaire WHERE nature_vocab = ?" ,(nature,))
        items = c.fetchall()

    if not items:
        print("Aucun vocabulaire disponible pour le moment.")
        conn.close()
        input("")
        return
    
    print("-" *70)
    for i, (mot, definition, example) in enumerate(items, 1):
        print(f"| {i} | {mot} | {definition or '-'} | {example or '-'}")
        print("-" *70)

    conn.close()
    input("")