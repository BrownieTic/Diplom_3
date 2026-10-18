import allure
import pytest
from selenium.webdriver.common.by import By

from locators.header_locators import Locators as element
from urls import Urls as urls

@allure.feature("Заказы")
class TestMain():
    @allure.story("Создание заказа")
    @allure.title("Переход по клику на «Конструктор» переход по клику на «Лента заказов»")
    def test_click_ingredient_open_ingredient_detail(self, init_main_page):
        init_main_page.wait_to_be_clickable(element.ingredient_bun_main_page)
        init_main_page.click_button(element.ingredient_bun_main_page)
        with allure.step("Проверить открытие деталей ингредиента"):
            assert init_main_page.wait_to_be_visible(element.ingredient_details)

    @allure.title("Закрытие окна деталей ингредиента по клику на 'X'")
    def test_click_on_X_in_ingredient_detail_close_window(self, init_main_page):
        init_main_page.wait_to_be_clickable(element.ingredient_bun_main_page)
        init_main_page.click_button(element.ingredient_bun_main_page)
        init_main_page.wait_to_be_visible(element.ingredient_details)
        init_main_page.click_button(element.button_close_ingredient_details)
        with allure.step("Проверить закрытие окна деталей ингредиента"):
            assert not init_main_page.is_element_present(element.ingredient_details)
            assert init_main_page.current_url == urls.MAIN_PAGE_URL

