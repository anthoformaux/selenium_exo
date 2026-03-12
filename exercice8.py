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

###### Exercice 8 #######


def test_alert():
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        alert_buton = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
        alert_buton.click()

        alert = wait.until(EC.alert_is_present())
        assert alert.text == "I am a JS Alert", f"Alerte inattendue : {alert.text}"
        alert.accept()

        alert_result = driver.find_element(By.ID, "result")
        assert alert_result.text == "You successfully clicked an alert", f"Résultat alerte incorrect : {alert_result.text}"

        alert_buton_dismiss = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
        alert_buton_dismiss.click()

        alert = wait.until(EC.alert_is_present())
        assert alert.text == "I am a JS Confirm", f"Alerte inattendue : {alert.text}"
        alert.dismiss()

        alert_result = driver.find_element(By.ID, "result")
        assert alert_result.text == "You clicked: Cancel", f"Résultat alerte incorrect : {alert_result.text}"
        print("Validation du test")
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
    test_alert()
