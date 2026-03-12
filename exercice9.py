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

####Exercice 9 #####

def test_explicit():
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
        button_start = driver.find_element(By.XPATH, "//button[contains(., 'Start')]")
        button_start.click()

        resultat = wait.until(EC.visibility_of_element_located((By.ID,"finish")))
        resultat_text = resultat.text
        assert "Hello World!" in resultat_text, f"Le résultat est {resultat}"
        print("Le test est correct!")

        assert "It's gone!" not in resultat_text, f"Le texte est erronné"

    except AssertionError as e:
        print(f"Erreur d'assertion: {e}")
        return False

    except Exception as e:
        print(f"Erreur: {e}")
        return False
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_explicit()
