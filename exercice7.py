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



########## Exercice 7 ############

def locate_xpath():
    try:
        driver.get("https://practicesoftwaretesting.com/")
        card_product = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@class = 'card'][position ( ) > 2]"))
        )

        title_product = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class,'card')]//descendant::h5[contains(@class,'card-title')]"))
        )

        amount_card = len(card_product)
        print(f"Il y a {amount_card} cartes produit.")

        visible_card = [card for card in card_product if card.is_displayed()]
        assert len(visible_card) == amount_card, f"Nombre de boutons visibles incorrect : {len(visible_card)}"
        print(f"Les {len(visible_card)} cartes produits sont bien visibiles")

        amount_title = len(title_product)
        print(f"Il y a {amount_title} titres produit.")

        visible_title = [title for title in title_product if title.is_displayed()]
        assert len(visible_title) == amount_title, f"Nombre de boutons visibles incorrect : {len(visible_title)}"
        print(f"Les {len(visible_title)} cartes produits sont bien visibiles")

    except AssertionError as e:
        print(f"Erreur d'assertion: {e}")
        return False

    except Exception as e:
        print(f"Erreur: {e}")
        return False
    
    finally:
        driver.quit()

if __name__ == "__main__":
    locate_xpath()
