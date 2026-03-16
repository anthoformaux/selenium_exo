from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class AddRemovePage:
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"
    ADD_BUTTON = (By.XPATH, "//button[contains(.,'Add')]")
    DELETE_BUTTONS = (By.XPATH, "//button[text()='Delete']")

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)

    def add_element(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def delete_button_count(self):
        delete_buttons = self.driver.find_elements(*self.DELETE_BUTTONS)
        return len(delete_buttons)
    
    def delete_element(self):
        delete_buttons = self.wait.until(EC.element_to_be_clickable(self.DELETE_BUTTONS))
        if delete_buttons:
            delete_buttons.click()
