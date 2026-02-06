import sqlite3
from database import connection
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def n_vocabuliare(vocabulaire: str) -> int:
    conn, c = connection()

    c.execute(f"SELECT COUNT(*) FROM vocabulaire WHERE nature_vocab = ?", (vocabulaire,))
    nb_vocabulaire = c.fetchone()[0]

    conn.close()
    return nb_vocabulaire

def affiche_n(n_mot: int, n_expr: int):
    clear_screen()
    
    n_mot = n_vocabuliare("mot")
    n_expr = n_vocabuliare("expression")

    print("_____--* Statistiques du Vocabulaire *--_____")
    print("|       -----------------------------       |")
    print(f"| Nombre de mots       :  {n_mot}                |")
    print("|                                           |")
    print(f"| Nombre d’expressions :  {n_expr}                |")
    print("|___________________________________________|")
    input("\n")