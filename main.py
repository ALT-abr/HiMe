from dictionnaire import get_vocabulary

print("bienvenue ! HiMe est a votre service.")

def affiche_menu():
    print("\nA - ajouter un vocabulaire")
    print("B - voir ma liste de vocabulaire")
    print("C - jouer un quiz")
    print("D - voir l'historique de mes quiz")
    print("E - voir mes statistiques")
    print("Q - quitter")

def main():
    while True:
        affiche_menu()
        user_input = input("\nVotre demande : ").lower()

        if user_input.lower() == "q":
            print("Au revoir !")
            break

        if user_input == "a":
            get_vocabulary()
        elif user_input == "b":
            print("la fonction B est en cours de développement.")
        elif user_input == "c":
            print("la fonction C est en cours de développement.")
        elif user_input == "d":
            print("la fonction D est en cours de développement.")
        elif user_input == "e":
            print("la fonction E est en cours de développement.")
        else:
            print("Commande non reconnue. Veuillez réessayer.")

if __name__ == "__main__":
    main()