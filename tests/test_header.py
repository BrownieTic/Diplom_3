import allure
import pytest
from selenium.webdriver.common.by import By

from locators.header_locators import Locators as element
from urls import Urls as urls

@allure.feature("Заказы")
class TestHeader():
    @allure.story("Создание заказа")
    @allure.title("переход по клику на «Конструктор» переход по клику на «Лента заказов»")
    @pytest.mark.parametrize('button_locator, url', [
        (element.button_header_constructor, urls.MAIN_PAGE_URL),
        (element.button_order_feed, urls.url_feed)
    ])
    def test_transition_to_constructor_from_profile(self, init_login_page, button_locator, url):
        init_login_page.wait_to_be_clickable(button_locator)
        init_login_page.click_button(button_locator)
        with allure.step("Проверить успешное "):
            assert init_login_page.current_url == url
