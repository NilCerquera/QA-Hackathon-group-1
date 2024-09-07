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
        name = Data.name
        email = Data.email
        password_client = Data.password_client
        confirm_password = Data.confirm_password
        routes_page.click_sign_up()
        routes_page.set_name()
        routes_page.set_confirmation()
        routes_page.set_email()
        routes_page.set_password()
        routes_page.click_balance_option()
        routes_page.click_submit_register()
        assert routes_page.get_name() == name
        assert routes_page.get_email() == email
        assert routes_page.get_password_client() == password_client
        assert routes_page.get_confirm_password() == confirm_password
        assert routes_page.is_balance_selected()
        routes_page.click_close()

    def test_login(self):
        self.driver.implicitly_wait(5)
        routes_page = QABugBank(self.driver)
        email_login = Data.email
        password_login = Data.password_client
        routes_page.set_email_login()
        routes_page.set_password_login()
        routes_page.click_login()
        assert routes_page.get_email_login() == email_login
        assert routes_page.get_password_login() == password_login
        self.driver.implicitly_wait(5)

    def test_transfer_money(self):
        self.driver.implicitly_wait(5)
        routes_page = QABugBank(self.driver)
        account_number = Data.account_number
        code_number = Data.digit
        quantity_money = Data.money
        description_transfer = Data.description
        routes_page.click_transfer()
        self.driver.implicitly_wait(5)
        routes_page.set_account_number()
        routes_page.set_digit_number()
        routes_page.set_money_quantity()
        routes_page.set_description()
        assert routes_page.get_account_number() == account_number
        assert routes_page.get_digit_code_number() == code_number
        assert routes_page.get_quantity_of_money() == quantity_money
        assert routes_page.get_description_comments() == description_transfer
        self.driver.implicitly_wait(10)
        routes_page.confirm_transfer()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
