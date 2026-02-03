import os
from dictionnaire import get_vocabulary, supprimer_vocabulaire, get_choix, get_list
from progression import n_mots, n_expressions, affiche_n

def clrean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def affiche_menu():
    print("bienvenue ! HiMe est a votre service.")

    print("\nA - ajouter un vocabulaire")
    print("B - voir ma liste de vocabulaire")
    print("C - jouer un quiz")
    print("S - supprimer un vocabulaire")
    print("D - voir l'historique de mes quiz")
    print("E - voir mes statistiques")
    print("Q - quitter")

def main():
    while True:
        clrean_screen()
        affiche_menu()

        user_input = input("\nVotre demande : ").lower()

        if user_input.lower() == "q":
            print("Au revoir !")
            break

        if user_input == "a":
            get_vocabulary()
        elif user_input == "b":
            nature = get_choix()
            get_list(nature)
        elif user_input == "s":
            supprimer_vocabulaire()
        elif user_input == "c":
            print("la fonction C est en cours de développement.")
        elif user_input == "d":
            print("la fonction D est en cours de développement.")
        elif user_input == "e":
            n_mot = n_mots()
            n_expr = n_expressions()
            affiche_n(n_mot, n_expr)
        else:
            print("Commande non reconnue. Veuillez réessayer.")

if __name__ == "__main__":
    main()