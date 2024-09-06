from selenium.webdriver.common.by import By
import Data


class QABugBank:
    create_account = (By.XPATH, ".//div[@id='__next']//button[text()='Registrar']")
    text_full_name = (By.PARTIAL_LINK_TEXT, "Informe seu e-mail")
    text_email = (By.ID, "email")
    set_password = (By.XPATH, "//*[@id='password']")

    def __init__(self, driver):
        self.driver = driver

    def click_sign_up(self):
        self.driver.find_element(*self.create_account).click()

    def set_name(self):
        self.driver.find_element(*self.text_full_name).send_keys(Data.name)

    def set_email(self):
        self.driver.find_element(*self.text_email).send_keys(Data.email)

    def set_new_password(self):
        self.driver.find_element(*self.set_password).send_keys(Data.password_client)
