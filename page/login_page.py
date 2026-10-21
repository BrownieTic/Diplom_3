from page.base_page import BasePage
from locators.login_locators import Locators as login_locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import allure

class LoginPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.find_element_on_page(login_locator.login_for_input_page).send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.find_element_on_page(login_locator.password_for_input_page).send_keys(password)

    @allure.step("Кликнуть по кнопке 'Войти'")
    def click_login_button(self):
        self.click_button(login_locator.button_input_page_input_path)

    @allure.step("Выполнить авторизацию")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Ожидание сокрытия оверлея")
    def overlay(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(login_locator.overlay))