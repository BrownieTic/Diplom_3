from page.base_page import BasePage
from locators.login_locators import Locators as login_locator

class LoginPage(BasePage):

    def enter_email(self, email):
        self.find_element_on_page(login_locator.login_for_input_page).send_keys(email)

    def enter_password(self, password):
        self.find_element_on_page(login_locator.password_for_input_page).send_keys(password)

    def click_login_button(self):
        self.click_button(login_locator.button_input_page_input_path)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()