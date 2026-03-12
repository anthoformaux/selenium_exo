from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)


def input_text():
    try:
        driver.get("https://demoqa.com/text-box/")
        fullname_field = driver.find_element(By.ID, "userName")
        email_field = driver.find_element(By.ID,"userEmail")
        current_adress_field = driver.find_element(By.XPATH,"//textarea[@id = 'currentAddress' and @class = 'form-control' ]")

        lien = driver.find_element(By.TAG_NAME,"a")
        lien_type = lien.get_attribute("href")
        assert lien_type in "https://demoqa.com/text-box/", f"le lien est mauvais: {lien_type}"
        #assert lien_type is not None and len() > 0, "Le lien est vide"
        print(f"Le lien est corret: {lien_type}")


        fullname_field.send_keys('John Doe')
        email_field.send_keys('john@example.com')
        current_adress_field.send_keys('123 Main Street')


        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        wait.until(EC.presence_of_element_located((By.ID, "output")))

        output = driver.find_element(By.ID, "output")
        output_text = output.text

        assert 'John Doe' in output_text, "Nom non trouvé dans l'output"
        assert 'john@example.com' in output_text, "Email non trouvé dans l'output"
        assert '123 Main Street' in output_text, "Adresse non trouvée dans l'output"

        print(f"Résultat vérifié: {output_text}")

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
    input_text()






