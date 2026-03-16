from tests.test_tp1 import login, test_dropdown, test_add_remove
import time
import json
import os
print("Dossier actuel :", os.getcwd())

with open("testeur_python_selenium/03_exos/TP1/users.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def main():
    """Menu principal"""
    print("\n" + ""*60)
    print(" TP 1 SELENIUM")
    print(""*60)

    try:
        print("\nChoisissez la démo:")
        print("1. Login")
        print("2. Dropdown")
        print("3. Add and Remove")
        print("4. All demos")

        choice = input("\nVotre choix (1-4): ").strip()

        if choice == "1":
            username = data["username"]
            print(f"Username: {username}")
            password = data["password"]
            print(f"Password: {password}")
            login(username, password)

        elif choice == "2":
           test_dropdown()
        elif choice == "3":
            number_add = int(input("Please choose a number to add: "))
            test_add_remove(number_add)
        elif choice == "4":
            login(data["username"], data["password"])
            print("\n")
            time.sleep(2)
            test_dropdown()
            print("\n")
            time.sleep(2)
            test_add_remove(5)
        else:
            print("Choix invalide. Veuillez choisir un nombre entre 1 et 4.")

    except KeyboardInterrupt:
        print("\n\n  Interrompu par l'utilisateur")
    except Exception as e:
        print(f"\n Erreur: {e}")

if __name__ == "__main__":
    main()