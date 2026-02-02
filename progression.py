import sqlite3
import os

def clrean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def n_mots() -> int:
    conn = sqlite3.connect("HiMe.db")
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM vocabulaire WHERE nature_vocab = 'mot'")
    nb_mot = c.fetchone()[0]
    return nb_mot

def n_expressions() -> int:
    conn = sqlite3.connect("HiMe.db")
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM vocabulaire WHERE nature_vocab = 'expression'")
    nb_express = c.fetchone()[0]
    return nb_express

def affiche_n(n_mot: int, n_expr: int):
    clrean_screen()

    print("Statique de vocabulaire")
    print(f"le nombre des mots :       {n_mot}")
    print(f"Le nombre des expression : {n_expr}")

    input("")