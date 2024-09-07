from selenium.webdriver.common.by import By
import Data


class QABugBank:
    create_account = (By.XPATH, ".//div[@id='__next']//button[text()='Registrar']")
    input_name = (By.XPATH, "//input[@name='name']")
    confirm_name = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[3]/input")
    input_confirmation = (By.XPATH, "//input[@name='passwordConfirmation']")
    confirm_password_confirmation = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[5]/div/input")
    input_email = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[2]/input")
    confirm_email = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[2]/input")
    input_password = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[4]/div/input")
    confirm_password = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[4]/div/input")
    click_balance = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[6]/label/label")
    confirm_selection = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/div[6]/label")
    click_submit = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/form/button")
    click_close_page = (By.ID, "btnCloseModal")
    input_email_login = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[1]/input")
    input_password_login = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[2]/div/input")
    submit_login = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[3]/button[1]")
    confirm_email_login = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[1]/input")
    confirm_password_login = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/form/div[2]/div/input")
    click_button_transfer = (By.ID, "btn-TRANSFERÊNCIA")
    input_number_account = (By.XPATH, "/html/body/div/div/div[3]/form/div[1]/div[1]/input")
    confirm_account_number = (By.XPATH, "//input[@name='accountNumber']")
    input_digit = (By.XPATH, "/html/body/div/div/div[3]/form/div[1]/div[2]/input")
    confirm_code_number = (By.XPATH, "/html/body/div/div/div[3]/form/div[1]/div[2]/input")
    input_money = (By.XPATH, "/html/body/div/div/div[3]/form/div[2]/input")
    confirm_money_quantity = (By.XPATH, "/html/body/div/div/div[3]/form/div[2]/input")
    comment_description = (By.XPATH, "/html/body/div/div/div[3]/form/div[3]/input")
    confirm_description = (By.XPATH, "/html/body/div/div/div[3]/form/div[3]/input")
    press_transfer = (By.XPATH, "/html/body/div/div/div[3]/form/button")
    return_button_transfer = (By.XPATH, "/html/body/div/div/div[2]/div/a")
    def __init__(self, driver):
        self.driver = driver

    def click_sign_up(self):
        self.driver.find_element(*self.create_account).click()

    def set_name(self):
        self.driver.find_element(*self.input_name).send_keys(Data.name)

    def get_name(self):
        confirmation_name = self.driver.find_element(*self.confirm_name).get_property('value')
        return confirmation_name
    def set_confirmation(self):
        self.driver.find_element(*self.input_confirmation).send_keys(Data.confirm_password)

    def get_confirm_password(self):
        confirmation_password = self.driver.find_element(*self.confirm_password_confirmation).get_property('value')
        return confirmation_password

    def set_email(self):
        self.driver.find_element(*self.input_email).send_keys(Data.email)

    def get_email(self):
        confirmation_email = self.driver.find_element(*self.confirm_email).get_property('value')
        return confirmation_email
    def set_password(self):
        self.driver.find_element(*self.input_password).send_keys(Data.password_client)

    def get_password_client(self):
        confirmation_password = self.driver.find_element(*self.confirm_password).get_property('value')
        return confirmation_password
    def click_balance_option(self):
        self.driver.find_element(*self.click_balance).click()

    def is_balance_selected(self):
        container = self.driver.find_element(*self.confirm_selection)
        return container
    def click_submit_register(self):
        self.driver.find_element(*self.click_submit).click()

    def click_close(self):
        self.driver.find_element(*self.click_close_page).click()

    def set_email_login(self):
        self.driver.find_element(*self.input_email_login).send_keys(Data.email)

    def get_email_login(self):
        confirmation_email_login = self.driver.find_element(*self.confirm_email_login).get_property('value')
        return confirmation_email_login

    def set_password_login(self):
        self.driver.find_element(*self.input_password_login).send_keys(Data.password_client)

    def get_password_login(self):
        confirmation_password_login = self.driver.find_element(*self.confirm_password_login).get_property('value')
        return confirmation_password_login
    def click_login(self):
        self.driver.find_element(*self.submit_login).click()

    def click_transfer(self):
        self.driver.find_element(*self.click_button_transfer).click()

    def set_account_number(self):
        self.driver.find_element(*self.input_number_account).send_keys(Data.account_number)

    def get_account_number(self):
        account_number_confirm = self.driver.find_element(*self.confirm_account_number).get_property('value')
        return account_number_confirm
    def set_digit_number(self):
        self.driver.find_element(*self.input_digit).send_keys(Data.digit)

    def get_digit_code_number(self):
        account_code_number_confirm = self.driver.find_element(*self.confirm_code_number).get_property('value')
        return account_code_number_confirm
    def set_money_quantity(self):
        self.driver.find_element(*self.input_money).send_keys(Data.money)

    def get_quantity_of_money(self):
        quantify_money = self.driver.find_element(*self.confirm_money_quantity).get_property('value')
        return quantify_money
    def set_description(self):
        self.driver.find_element(*self.comment_description).send_keys(Data.description)

    def get_description_comments(self):
        quantify_money = self.driver.find_element(*self.confirm_description).get_property('value')
        return quantify_money
    def confirm_transfer(self):
        self.driver.find_element(*self.press_transfer).click()

    def return_transfer(self):
        self.driver.find_element(*self.return_button_transfer).click()