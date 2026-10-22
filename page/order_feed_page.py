from page.base_page import BasePage
from locators.order_feed_locators import Locators as feed_locator
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class OrderFeedPage(BasePage):
        @allure.step("Дождаться появления заказа в секции «В работе»")
        def get_order_number_from_progress_section(self, order_number, locator=feed_locator.section_in_progress):
            order_reference = f"0{int(order_number)}"
            WebDriverWait(self.driver, 10).until(
                expected_conditions.text_to_be_present_in_element(
                    locator,
                    order_reference
                )
            )
            return self.get_text(locator)