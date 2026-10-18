import allure

from locators.header_locators import Locators as header_locators
from urls import Urls as urls

@allure.feature("Проверка главной страницы")
class TestMain():
    @allure.story("Проверка элементов «Конструктор»")
    @allure.title("Клик на ингридиент открывает окно с деталями ингредиента")
    def test_click_ingredient_open_ingredient_detail(self, init_main_page):
        init_main_page.wait_to_be_clickable(header_locators.ingredient_bun_main_page)
        init_main_page.click_button(header_locators.ingredient_bun_main_page)
        with allure.step("Проверить открытие деталей ингредиента"):
            assert init_main_page.wait_to_be_visible(header_locators.ingredient_details)

    @allure.title("Закрытие окна деталей ингредиента по клику на 'X'")
    def test_click_on_X_in_ingredient_detail_close_window(self, init_main_page):
        init_main_page.wait_to_be_clickable(header_locators.ingredient_bun_main_page)
        init_main_page.click_button(header_locators.ingredient_bun_main_page)
        init_main_page.wait_to_be_visible(header_locators.ingredient_details)
        init_main_page.click_button(header_locators.button_close_ingredient_details)
        with allure.step("Проверить закрытие окна деталей ингредиента"):
            assert not init_main_page.is_element_present(header_locators.ingredient_details)
            assert init_main_page.current_url == urls.MAIN_PAGE_URL

    @allure.title("Добавление ингредиента увеличивает счетчик этого ингредиента")
    def test_add_ingredient_increases_counter_this_ingredient(self, init_main_page):
        init_main_page.wait_to_be_clickable(header_locators.ingredient_bun_main_page)
        init_main_page.add_ingredient()
        with allure.step("Проверить увеличение счетчика ингредиента"):
            assert init_main_page.wait_to_be_visible(header_locators.counter_bun_main_page)
            assert init_main_page.get_text(header_locators.counter_bun_main_page) == '2'
