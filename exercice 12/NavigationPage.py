from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class NavigationPage:
    URL = "https://practicesoftwaretesting.com/"
    SEARCH_INPUT = (By.ID, "search_query")
    SEARCH_BAR = (By.XPATH,'(//button[@data-test="search-submit"])')
    SEARCH_FORM = (By.ID,'filters')

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)
        print(f"La page {self.URL} s'est ouverte")

    def element_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def search_hammer(self, name):
        search_input = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(name)

        search_button = self.element_visible(self.SEARCH_BAR)
        search_button.click()