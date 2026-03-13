from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_exo11 import BookPage
import json
from datetime import datetime

def main():

    """Test de la page des livres"""

    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        print("----Phase 1 : Navigation----") #######Navigation vers la page

        print("Test Book Page")
        page = BookPage(driver,3)

        print("Ouverture de la page")
        page.open()
        print(f"La page {page.URL} est ouverte")

        print("----Phase 2 : Récupération des informations----")    ########Récupération des informations sur les livres

        print("En attente du chargement des livres")
        page.wait_page_load()
        print(f"Les livres de la page sont chargés")

        books = page.books_information()
        page.print_books(books)


        print("----Phase 3 : Statistiques----")     ######### Statistiques sur les livres

        ###Nombre de livres
        books_number = len(page.get_books())
        print(f"Il y a {books_number} livres sur la page")
        assert books_number == 20, f"Le nombre de livres affichés est incorrect : {books_number} au lieu de 20"

        ###Afficher les 5 premiers livres
        page.print_books(books[:5])

        ###Prix moyen des livres
        prix_moyen = sum(float(book['price'][1:]) for book in books) / books_number
        print(f"Prix moyen = {prix_moyen:.2f} €")

        ###Prix minimum et maximum
        prix_min = min(float(book['price'][1:]) for book in books)
        print(f"Prix minimum = {prix_min:.2f} €")

        prix_max = max(float(book['price'][1:]) for book in books)
        print(f"Prix maximum = {prix_max:.2f} €")

        ### quantité de livre avec chaque notation
        notations = {}
        for book in books:
            rating = book['rating']
            notations[rating] = notations.get(rating, 0) + 1

        print("Quantité de livres avec chaque notation :")
        for rating, count in notations.items():
            print(f"  {rating} étoiles : {count}")

    except AssertionError as e:
        print(f"AssertionError : {e}")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
