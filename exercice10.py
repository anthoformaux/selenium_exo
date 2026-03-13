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



def test_boucle():
    try:
        driver.get("https://practicesoftwaretesting.com/")
        wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@class = 'card']"))
        )
        card_product = driver.find_elements(By.XPATH, "//a[@class = 'card']")
        
        products = []
        for index, card in enumerate(card_product, start=1):
            name = card.find_element(By.XPATH, ".//*[contains(@class, 'card-title')]").text.strip()
            text_elements = card.find_elements(By.XPATH, ".//span[contains(@data-test, 'product-price')]")
            text_values = [element.text.strip() for element in text_elements if element.text.strip()]

            products.append({
                "index": index,
                "name": name,
                "details": text_values,
            })

        def print_products(product_list):

            for p in product_list:
                print(f"{p['index']}. {p['name']}")
                print(f"    Prix : {p['details']}")
                print("-"*50)

        # 5 premiers
        print("Liste 5 premiers")
        print_products(products[:5])

        print("-"*50)

        # liste complète
        print("Liste complète")
        print_products(products)

        


    except AssertionError as e:
        print(f"Erreur d'assertion: {e}")
        return False

    except Exception as e:
        print(f"Erreur: {e}")
        return False
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_boucle()
