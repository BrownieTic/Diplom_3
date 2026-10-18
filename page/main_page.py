from page.base_page import BasePage
from urls import Urls as url
from locators.main_locators import Locators as main_locators

class MainPage(BasePage):
        def wait_load_main_url(self):
            self.wait_load_url(self, url.MAIN_PAGE_URL)

        def add_ingredient(self):
            self.click_button(main_locators.button_add_ingredient)

        def click_button_order(self):
             self.click_button(main_locators.button_order)

        def get_order_number(self):
            order_number = self.get_text(main_locators.order_number)
            return order_number

        def close_window_order_identifier(self):
            self.click_button(main_locators.button_order_identifier_close)

        def place_order(self):
            self.add_ingredient()
            self.click_button_order()
            order_number = self.get_order_number()
            self.close_window_order_identifier()
            return order_number
