from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)



def changement_page():
    try:
        driver.get("https://practicesoftwaretesting.com/")
        button_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='product-01KKH902ASKEVXNT8SZWSEBSRN']")))
        button_item.click()


        original_url = driver.current_url

    except AssertionError as e:
        print(f"Erreur d'assertion: {e}")
        return False

    except Exception as e:
        print(f"Erreur: {e}")
        return False
    
    finally:
        driver.quit()

if __name__ == "__main__":
    changement_page()
