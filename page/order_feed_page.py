from page.base_page import BasePage
from urls import Urls as url
from locators.order_feed_locators import Locators as feed_locator
import allure

class OrderFeedPage(BasePage):
        @allure.step("Получить номер заказа из секции 'В работе'")
        def get_order_number_from_progress_section(self, locator=feed_locator.section_in_progress):
            order_in_progress_section = self.get_text(locator)
            return order_in_progress_section