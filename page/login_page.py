from page.base_page import BasePage
from locators.login_locators import Locators as login_locator

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = login_locator()

    def enter_email(self, email):
        self.find_element(self.locators.login_for_input_page).send_keys(email)

    def enter_password(self, password):
        self.find_element(self.locators.password_for_input_page).send_keys(password)

    def click_login_button(self):
        self.find_element(self.locators.button_input_page_input_path).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()