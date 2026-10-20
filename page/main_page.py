from page.base_page import BasePage
from urls import Urls as url
from locators.main_locators import Locators as main_locators
import allure

class MainPage(BasePage):
        @allure.step("Ожидать загрузки главной страницы")
        def wait_load_main_url(self):
            self.wait_load_url(url.MAIN_PAGE_URL)

        @allure.step("Открыть окно деталей ингредиента")
        def open_window_ingredient_details(self, locator=main_locators.ingredient_bun_main_page):
            self.wait_to_be_clickable(locator)
            self.click_button(locator)

        @allure.step("Получить текст окна деталей ингредиента 'Детали ингредиента'")
        def get_text_ingredient_details(self):
            self.wait_visibility_of_element(main_locators.ingredient_details)
            text = self.get_text(main_locators.ingredient_details)
            return text

        @allure.step("Закрыть окно деталей ингредиента")
        def close_window_ingredient_details(self):
            self.wait_visibility_of_element(main_locators.button_close_ingredient_details)
            self.click_button(main_locators.button_close_ingredient_details)

        @allure.step("Добавить ингредиент")
        def add_ingredient(self, locator=main_locators.button_add_ingredient_bun):
            self.wait_to_be_clickable(locator)
            self.click_button(locator)

        @allure.step("Кликнуть по кнопке 'Оформить заказ'")
        def click_button_order(self):
            self.click_button(main_locators.button_order)

        @allure.step("Получить номер заказа")
        def get_order_number(self, locator=main_locators.order_number):
            order_number = self.get_text(locator)
            return order_number

        @allure.step("Закрыть окно с номером заказа")
        def close_window_order_identifier(self):
            self.click_button(main_locators.button_order_identifier_close)

        @allure.step("Выполнение шагов оформления заказа")
        def place_order(self):
            self.add_ingredient()
            self.click_button_order()
            self.wait_visibility_of_element(main_locators.order_number)
            order_number = self.get_order_number()
            self.close_window_order_identifier()
            return order_number
