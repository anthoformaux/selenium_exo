
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


def lancement_exemple():

    try:
        driver.get("https://example.com/")
        time.sleep(1)


        assert driver.title == "Example Domain", f"Titre incorrect : {driver.title}"
        print(f"Titre vérifié : {driver.title}")

        body = driver.find_element(By.TAG_NAME, "body")

        assert "Example Domain" in body.text, "Texte non trouvé dans le titre"
        print(f"Contenu vérifié : {body.text}")

        assert driver.current_url == "https://example.com/", f"URL incorrect : {driver.current_url}"
        print(f"Url vérifié: {driver.current_url}")

    except AssertionError as e:
        print(f"Erreur d'assertion: {e}")

    except Exception as e:
        print(f"Erreur: {e}")


    finally:
        driver.quit()

##### dans ce script ####
if __name__ == "__main__":
    lancement_exemple()

##### autre script#####
import exercice1
exercice1.lancement_exemple()