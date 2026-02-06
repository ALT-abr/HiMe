import os
from dictionnaire import get_vocabulary, supprimer_vocabulaire, get_choix, get_list
from progression import affiche_n
from quiz import quiz_menu, q_history

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def affiche_menu():
    print("---------------_ Bienvenue sur HiMe ! _--------------")
    print("|                                                   |")
    print("|  Pour revenir au menu principal, saisissez : r    |")
    print("|                                                   |")
    print("|  A - ajouter un vocabulaire                       |")
    print("|  B - voir ma liste de vocabulaire                 |")
    print("|  C - supprimer un vocabulaire                     |")
    print("|  D - jouer un quiz                                |")
    print("|  E - voir l'historique de mes quiz                |")
    print("|  F - voir mes statistiques                        |")
    print("|  Q - quitter                                      |")
    print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")

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
        elif user_input == "c":
            supprimer_vocabulaire()
        elif user_input == "d":
            quiz_menu()
        elif user_input == "e":
            q_history()
        elif user_input == "f":
            affiche_n("mot", "expression")
        else:
            print("Commande non reconnue. Veuillez réessayer.")
            input()

if __name__ == "__main__":
    main()