from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SearchPage:
    SEARCH_RESULT = (By.XPATH, "//h3[contains(., 'Searched for: ')]")
    HAMMER_RESULT = (By.XPATH, "//h5[contains(., 'ammer')]")
    CARD_RESULT = (By.CLASS_NAME, "card")
    CARD_TITLE = (By.TAG_NAME, "h5")
    CARD_PRICE = (By.XPATH,"//span[@data-test='product-price']")

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def search_for_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.SEARCH_RESULT))

    def hammer_visible(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.HAMMER_RESULT))
    
    def get_results_hammer(self):
        return self.driver.find_elements(*self.HAMMER_RESULT)
    
    def get_results_hammer_length(self):
        return len(self.get_results_hammer())
    
    def get_results_card(self):
        return self.driver.find_elements(*self.CARD_RESULT)
    
    def get_card_information(self):
        cards = self.get_results_card()
        card_info = []
        for index, card in enumerate(cards):
            try:
                title = card.find_element(self.CARD_TITLE).text.strip()
                price = str(card.find_element(self.CARD_PRICE).text.strip().replace("$",""))
                card_info.append({
                    "index": index,
                    "title": title,
                    "price": price
                })
            except Exception as e:
                print(f"Erreur lors de la récupération des informations de la carte {index + 1} : {e}")
        return card_info
    

    

    