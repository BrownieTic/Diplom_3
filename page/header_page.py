from locators.header_locators import Locators
from urls import Urls as url
from page.base_page import BasePage

class HeaderPage(BasePage):

    def click_constructor_button(self):
        self.click_button(Locators.button_header_constructor)
        self.wait_load_url(url.MAIN_PAGE_URL)

    def click_logo_button(self):
        self.click_button(Locators.button_header_logo)

    def click_profile_button(self):
        self.click_button(Locators.button_header_profile)
        self.wait_load_url(url.url_profile)

    def click_order_feed_button(self):
        self.click_button(Locators.button_order_feed)
        self.wait_load_url(url.url_feed)