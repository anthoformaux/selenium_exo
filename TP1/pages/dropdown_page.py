from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")



    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)

    def select_option(self,option_text):
        dropdown_element = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN))
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(option_text)
    
    def check_selected_option(self,expected_text):
        dropdown_element = self.wait.until(EC.visibility_of_element_located(self.DROPDOWN))
        dropdown = Select(dropdown_element)
        selected_option = dropdown.first_selected_option
        return selected_option.text == expected_text
    
    