from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import Data


class QABugBank:
    create_account = (By.XPATH, ".//div[@id='__next']//button[text()='Registrar']")
    input_name = (By.XPATH, "//input[@name='name']")
    def __init__(self, driver):
        self.driver = driver

    def click_sign_up(self):
        self.driver.find_element(*self.create_account).click()

    def set_email(self):
        self.driver.find_element(*self.input_name).click()
        self.driver.find_element(*self.input_name).send_keys(Data.name)