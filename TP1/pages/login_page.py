from operator import index

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class LoginPage:


    URL = "https://the-internet.herokuapp.com/login"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    LOGIN_PAGE = (By.XPATH, '//h2[text()="Login Page"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
        
    def open(self):
        self.driver.get(self.URL)

    def is_login_page_displayed(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOGIN_PAGE))
    
    def login(self,username,password):
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def check_login_success(self):
        return self.wait.until(EC.url_contains("secure"))
    
    def check_login_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID,"flash"))).text
    
    def check_logout_button(self):
        return self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
    
    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()

    def check_logout_success(self):
        return self.wait.until(EC.url_contains("login"))

    

    
