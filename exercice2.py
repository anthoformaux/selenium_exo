
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def test_tag():
    try:
        driver.get("https://example.com/")
        time.sleep(1)
        element = driver.find_element(By.TAG_NAME, "a")
        print(f"Élément trouvé : {element.text}")

        element = driver.find_element(By.CSS_SELECTOR, "p > a")
        print(f"Élément trouvé en CSS: {element.text}")

        element = driver.find_element(By.XPATH, "//a[contains(.,'Learn more')]")
        print(f"Élément trouvé en XPATH: {element.text}")


        tag_name = element.tag_name
        assert tag_name == "a", f"L'élément n'est pas un lien, tag trouvé : {tag_name}"
        print(f"Type d'élément vérifié : <{tag_name}>")

        a_type = element.get_attribute("href")
        assert a_type.startswith("http"), f"href invalide:{a_type}"
        assert a_type is not None and len()>0, f"Le lien est vide : {a_type}"
        print("Le lien est valide")
        assert a_type == "https://iana.org/domains/example", f"Le lien n'est pas correct : {a_type}"
        print(f"Attribut href vérifié : {a_type}")

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
    test_tag()
