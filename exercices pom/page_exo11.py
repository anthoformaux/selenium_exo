from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BookPage:
    URL = "https://books.toscrape.com/"
    BOOKS = (By.XPATH, "//article[@class='product_pod']")
    TITRE = (By.XPATH, ".//h3/a")
    PRIX = (By.XPATH, ".//p[@class='price_color']")
    NOTATION = (By.XPATH, ".//p[contains(@class,'star')]")
    STOCK = (By.XPATH, ".//p[@class = 'instock availability']")


    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)
        print(f"La page {self.URL} s'est ouverte")

    def wait_page_load(self):
        self.wait.until(EC.presence_of_all_elements_located(*self.BOOKS))
        print(f"Les livres de la page sont bien tous chargés")

    def get_books(self):
        return self.driver.find_elements(*self.BOOKS)

    def books_information(self):
        products = []
        books = self.get_books()
        for index, book in enumerate(books):
            try:
                title = book.find_element(*self.TITRE).get_attribute("title").strip()
                price = book.find_element(*self.PRIX).text.strip()
                rating = book.find_element(*self.NOTATION).get_attribute("class").split()[-1].strip()
                stock = book.find_element(*self.STOCK).text.strip()
            
                products.append({
                    "index": index,
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "stock": stock
                })
            except Exception as e:
                print(f"Erreur lors de la récupération des informations du livre {index + 1} : {e}")

        return products
    
    def print_books(self,product_list):
        for index, book_info in enumerate(product_list):
            print(f"Livre {index + 1}. {book_info['title']}")
            print(f"    Prix : {book_info['price']}")
            print(f"    Notation : {book_info['rating']}")
            print(f"    Stock : {book_info['stock']}")
            print("-"*50)

    