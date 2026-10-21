import allure
import pytest

from locators.main_locators import Locators as main_locators
from urls import Urls as urls

@allure.feature("Проверка главной страницы")
class TestMain():
    @allure.story("Проверка элементов «Конструктор»")
    @allure.title("Клик на ингредиент открывает окно с деталями ингредиента")
    def test_click_ingredient_open_ingredient_detail(self, init_main_page):
        init_main_page.open_window_ingredient_details()
        with allure.step("Проверить открытие деталей ингредиента"):
            assert init_main_page.get_text_ingredient_details() == "Детали ингредиента"

    @allure.title("Закрытие окна деталей ингредиента по клику на 'X'")
    def test_click_on_x_in_ingredient_detail_close_window(self, init_main_page):
        init_main_page.open_window_ingredient_details()
        init_main_page.close_window_ingredient_details()
        with allure.step("Проверить закрытие окна деталей ингредиента"):
            assert init_main_page.get_name_igredient() == 'Краторная булка N-200i'

    @allure.story("Проверка счетчиков ингредиентов")
    @allure.title("Добавление ингредиентов увеличивает счетчик этих ингредиентов")
    @pytest.mark.parametrize("section, ingredient_add, counter_locator, quantity", [
        (main_locators.button_section_buns, main_locators.button_add_ingredient_bun, main_locators.counter_bun_main_page, 2),
        (main_locators.button_section_sauces, main_locators.button_add_ingredient_sauce, main_locators.counter_sauce_main_page, 1),
        (main_locators.button_section_fillings, main_locators.button_add_ingredient_filling, main_locators.counter_filling_main_page, 1)
    ])
    def test_add_ingredient_increases_counter_this_ingredient(self, init_main_page, section, ingredient_add, counter_locator, quantity):
        init_main_page.click_button(section)
        init_main_page.add_ingredient(ingredient_add)
        with allure.step("Проверить увеличение счетчика ингридиента"):
            assert init_main_page.get_text(counter_locator) == str(quantity)
