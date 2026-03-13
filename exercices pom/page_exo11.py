from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BookPage:
    URL = "https://books.toscrape.com/"
    BOOKS = "//article[@class='product_pod']"
    TITRE = ".//h3/a"
    PRIX = ".//p[@class='price_color']"
    NOTATION = ".//p[contains(@class,'star')]"
    STOCK = ".//p[@class = 'instock availability']"


    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)
        print(f"La page {self.URL} s'est ouverte")

    def wait_page_load(self):
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, self.BOOKS)))
        print(f"Les livres de la page sont bien tous chargés")

    def get_books(self):
        return self.driver.find_elements(By.XPATH, self.BOOKS)

    def books_information(self):
        products = []
        books = self.driver.find_elements(By.XPATH, self.BOOKS)
        for index, book in enumerate(books):
            titre = book.find_element(By.XPATH,self.TITRE).get_attribute("title").strip()
            prix = book.find_element(By.XPATH,self.PRIX).text.strip()
            score = book.find_element(By.XPATH,self.NOTATION).get_attribute("class").split()[-1].strip()
            stock = book.find_element(By.XPATH,self.STOCK).text.strip()
        
            products.append({
                "index": index,
                "title": titre,
                "price": prix,
                "rating": score,
                "stock": stock
            })

        return products
    
    def print_books(self,product_list):
        for index, book_info in enumerate(product_list):
            print(f"Livre {index + 1}. {book_info['title']}")
            print(f"    Prix : {book_info['price']}")
            print(f"    Notation : {book_info['rating']}")
            print(f"    Stock : {book_info['stock']}")
            print("-"*50)

    