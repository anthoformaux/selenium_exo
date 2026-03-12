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

###### EXERCICE 5 ########

def test_checkbox():
    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = driver.find_elements(By.XPATH, "//input[@type = 'checkbox']")
        assert len(checkboxes) == 2, f" Il n'y a pas 2 checkboxes mais {len(checkboxes)}"

        checkbox_1 = checkboxes[0]
        checkbox_2 = checkboxes[1]

        assert not checkbox_1.is_selected(), "La checkbox 1 est sélectionnée"
        assert checkbox_2.is_selected(), "La checkbox 2 n'est pas sélectionnée"

        print("Les deux checkbox sont dans le bon état initial")


        if not checkbox_1.is_selected():
            checkbox_1.click()
        assert checkbox_1.is_selected(), "La checkbox 1 n'est pas sélectionnée"

        
        if checkbox_2.is_selected():
            checkbox_2.click()
        assert not checkbox_2.is_selected(), "La checkbox 2 est sélectionnée"

        print("Les deux checkbox sont dans le bon état final")

    except AssertionError as e:
        print(f"Erreur d'assertion: {e}")
        return False

    except Exception as e:
        print(f"Erreur: {e}")
        return False
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_checkbox()
