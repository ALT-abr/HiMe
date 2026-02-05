import sqlite3
import os

def clrean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def n_vocabuliare(vocabulaire: str) -> int:
    conn = sqlite3.connect("HiMe.db")
    c = conn.cursor()

    c.execute(f"SELECT COUNT(*) FROM vocabulaire WHERE nature_vocab = ?", (vocabulaire,))
    nb_vocabulaire = c.fetchone()[0]
    return nb_vocabulaire

def affiche_n(n_mot: int, n_expr: int):
    clrean_screen()
    
    n_mot = n_vocabuliare("mot")
    n_expr = n_vocabuliare("expression")

    print("Statique de vocabulaire")
    print(f"le nombre des mots :       {n_mot}")
    print(f"Le nombre des expression : {n_expr}")

    input("")