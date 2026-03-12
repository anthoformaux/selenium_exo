from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialiser le driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

def exercice06():


    try:

        # Accédez à https://practicesoftwaretesting.com/
        print("Navigation vers practicesoftwaretesting.com...")
        driver.get("https://practicesoftwaretesting.com/")

        # Attendez que les produits se chargent
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.card")))

        # Localisez les cartes produit en utilisant le sélecteur CSS `.card`
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".card")
        assert len(product_cards) == 9, f"Nombre de cartes incorrect : {len(product_cards)}"
        print(f" il  y a {len(product_cards)}")

        # Localisez les titres de produits en utilisant le sélecteur CSS `.card-title`
        title_cards = driver.find_elements(By.CSS_SELECTOR, ".card-title")
        assert len(title_cards) == 9, f"Nombre de cartes incorrect : {len(title_cards)}"

        # Vérifiez que tous les éléments sont visibles
        product = driver.find_elements(By.CSS_SELECTOR, "img.card-img-top")
        assert len(product) == 9, f"Nombre de produits incorrect : {len(product)}"
        visible_product = [product for product in product if product.is_displayed()]
        assert len(visible_product) == 9, f"Nombre de boutons visibles incorrect : {len(visible_product)}"
        


        print("Exercice06 localiser des Éléments avec CSS OK")

    except AssertionError as e:
        print(f"Erreur d'assertion : {e}")

    except Exception as e:
        print(f"Erreur : {e}")

    finally:
        # Fermez le navigateur
        driver.quit()


if __name__ == "__main__":
    exercice06()