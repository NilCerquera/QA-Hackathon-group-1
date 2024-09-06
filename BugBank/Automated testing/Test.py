import time

from selenium.webdriver.chrome import webdriver
import Data
from selenium import webdriver
from QABugBank import QABugBank


# Aqui iniciamos las pruebas automatizadas

class TestQA:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    # En esta prueba  registramos un usuario con nombre, email y contraseña válidos

    def test_create_user(self):
        self.driver.get(Data.bug_bank_url)
        routes_page = QABugBank(self.driver)
        self.driver.implicitly_wait(5)
        routes_page.click_sign_up()
        self.driver.implicitly_wait(10)
        routes_page.set_email()
        self.driver.implicitly_wait(5)
        time.sleep(10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()