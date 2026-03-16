
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
import logging
from pages.add_remove_page import AddRemovePage
from pages.dropdown_page import DropdownPage
from selenium.webdriver.chrome.options import Options

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
options = webdriver.ChromeOptions()
wait = WebDriverWait(driver, 10)

prefs = {
        "profile.password_manager_leak_detection": False
    }
options.add_experimental_option("prefs", prefs)

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('testeur_python_selenium/03_exos/TP1/TP_test.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)



def login(username,password):
    try:
        pages = LoginPage(driver)
        pages.open()
        logger.info("Page de login ouverte")

        pages.is_login_page_displayed()
        assert "The Internet" in driver.title, "La page de login n'est pas affichée"
        logger.info("Page de login affichée avec succès")

        pages.login(username, password)
        assert pages.check_login_success(), "La connexion a échoué"
        logger.info("Connexion réussie")

        message = pages.check_login_message()
        assert "You logged into a secure area!" in message, "Message de succès de connexion incorrect"
        logger.info("Message de succés de connexion vérifié")

        assert pages.check_logout_button(), "Le bouton de déconnexion n'est pas visible"
        logger.info("Bouton de déconnexion visible")

        pages.logout()
        assert pages.check_logout_success(), "La déconnexion a échoué"
        logger.info("Déconnexion réussie")

    except AssertionError as e:
        logger.error(f"Erreur d'assertion: {e}")
        return False

    except Exception as e:
        logger.error(f"Une erreur inattendue s'est produite: {e}")
        return False
    

def test_dropdown():
    try:
        dropdown = DropdownPage(driver)
        dropdown.open()
        logger.info("Page du dropdown ouverte")

        dropdown.select_option("Option 1")
        assert dropdown.check_selected_option("Option 1"), "L'option sélectionnée n'est pas correcte"
        logger.info("Option sélectionnée vérifiée avec succès")

        dropdown.select_option("Option 2")
        assert dropdown.check_selected_option("Option 2"), "L'option sélectionnée n'est pas correcte"
        logger.info("Changement d'option vérifié avec succès")


    except AssertionError as e:
        logger.error(f"Erreur d'assertion: {e}")
        return False

    except Exception as e:
        logger.error(f"Une erreur inattendue s'est produite: {e}")
        return False
    

def test_add_remove(number):
    try:
        add_remove = AddRemovePage(driver)
        add_remove.open()
        logger.info("Page d'ajout/suppression ouverte")

        count_add = 0
        for i in range(number):
            add_remove.add_element()
            count_add += 1
            logger.info(f"{i+1} Element ajouté ")

        delete_count = add_remove.delete_button_count()
        assert delete_count == number, f"Le nombre de bouttons delete affiché est de {delete_count}"
        logger.info("Le nombre de boutons delete affiché est correct")

        add_remove.delete_element()
        delete_count = add_remove.delete_button_count()
        assert delete_count == number - 1, f"Le nombre de bouttons delete affiché après suppression est de {delete_count}"
        logger.info("Le nombre de boutons delete affiché après suppression est correct")

        while add_remove.delete_button_count() > 0:
            add_remove.delete_element()
            logger.info("Un élément a été supprimé")

        delete_count_ = add_remove.delete_button_count()
        assert delete_count_ == 0, f"Le nombre de bouttons delete affiché après suppression de tous les éléments est de {delete_count_}"
        logger.info("Tous les éléments ont été supprimés avec succès")

    except AssertionError as e:
        logger.error(f"Erreur d'assertion: {e}")
        return False

    except Exception as e:
        logger.error(f"Une erreur inattendue s'est produite: {e}")
        return False
    
    finally:
        driver.quit()


if __name__ == "__main__":
    login()
    test_dropdown()
    test_add_remove()
