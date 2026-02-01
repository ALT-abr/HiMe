print("bienvenue ! HiMe est a votre service.")

def menu():
    print("\nA - ajouter un vocabulaire")
    print("B - voir ma liste de vocabulaire")
    print("C - jouer un quiz")
    print("D - voir l'historique de mes quiz")
    print("E - voir mes statistiques")
    print("Q - quitter")

def main():
    while True:
        menu()
        user_input = input("\nVotre demande : ")

        if user_input.lower() == "q":
            print("Au revoir !")
            break

        if user_input.lower() == "a":
            print("la fonction A est en cours de développement.")
        elif user_input.lower() == "b":
            print("la fonction B est en cours de développement.")
        elif user_input.lower() == "c":
            print("la fonction C est en cours de développement.")
        elif user_input.lower() == "d":
            print("la fonction D est en cours de développement.")
        elif user_input.lower() == "e":
            print("la fonction E est en cours de développement.")
        else:
            print("Commande non reconnue. Veuillez réessayer.")

if __name__ == "__main__":
    main()