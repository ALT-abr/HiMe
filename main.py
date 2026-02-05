import os
from dictionnaire import get_vocabulary, supprimer_vocabulaire, get_choix, get_list
from progression import affiche_n
from quiz import quiz_menu, q_history

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def affiche_menu():
    print("bienvenue ! HiMe est a votre service.")

    print("\nPour returne au menu principale saisie : r")

    print("\nA - ajouter un vocabulaire")
    print("B - voir ma liste de vocabulaire")
    print("C - jouer un quiz")
    print("S - supprimer un vocabulaire")
    print("D - voir l'historique de mes quiz")
    print("E - voir mes statistiques")
    print("Q - quitter")

def main():
    while True:
        clear_screen()
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
            quiz_menu()
        elif user_input == "d":
            q_history()
        elif user_input == "e":
            affiche_n("mot", "expression")
        else:
            print("Commande non reconnue. Veuillez réessayer.")
            input()

if __name__ == "__main__":
    main()