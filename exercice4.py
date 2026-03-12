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

#### EXERCICE 4 ####

def test_dropdown():
    try:
        driver.get("https://the-internet.herokuapp.com/dropdown")
        dropdown_main = driver.find_element(By.ID, 'dropdown')
        dropdown = Select(dropdown_main)

        dropdown.select_by_visible_text('Option 1')
        selected_option = dropdown.first_selected_option
        selected_text = selected_option.text
        assert selected_text == 'Option 1', f"L'option sélectionnée n'est pas correcte"
        print("L'Option 1 a bien été sélectionnée")

        dropdown.select_by_visible_text('Option 2')
        selected_option = dropdown.first_selected_option
        selected_text = selected_option.text
        assert selected_text == 'Option 2', f"L'option sélectionnée n'est pas correcte"
        print("L'Option 2 a bien été sélectionnée")
        return True

    except AssertionError as e:
        print(f"Erreur d'assertion: {e}")
        return False

    except Exception as e:
        print(f"Erreur: {e}")
        return False
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_dropdown()