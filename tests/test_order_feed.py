import allure
import pytest

from page.header_page import HeaderPage
from page.main_page import MainPage
from page.order_feed_page import OrderFeedPage

from locators.order_feed_locators import Locators as order_feed_locators

@allure.feature("Проверка страницы «Лента заказов»")
class TestOrderFeed():
    @allure.story("Проверка счетчиков на странице «Лента заказов»")
    @allure.title("Все счетчики заказов увеличиваются при создании нового заказа")
    @pytest.mark.parametrize("counter", [
        order_feed_locators.counter_order_all_time, 
        order_feed_locators.counter_order_today])
    def test_counter_all_time_increase_when_a_new_order_is_created(self, driver_with_registered_user, counter):
        header_page = HeaderPage(driver_with_registered_user)
        main_page = MainPage(driver_with_registered_user)
        order_feed_page = OrderFeedPage(driver_with_registered_user)
        header_page.click_order_feed_button()
        old_counter = order_feed_page.get_text(counter)
        header_page.click_constructor_button()
        main_page.place_order()
        header_page.click_order_feed_button()
        new_counter = order_feed_page.get_text(counter)
        with allure.step("Проверить успешное увеличение счетчика"):
            assert new_counter == str(int(old_counter) + 1)

    @allure.story("Проверка отображения заказов на странице «Лента заказов»")
    @allure.title("Номер нового заказа отображается на странице «Лента заказов»")
    def test_after_new_order_his_number_is_displayed_in_order_feed(self, driver_with_registered_user):
        header_page = HeaderPage(driver_with_registered_user)
        main_page = MainPage(driver_with_registered_user)
        order_feed_page = OrderFeedPage(driver_with_registered_user)
        order_number = main_page.place_order()
        header_page.click_order_feed_button()
        order_in_progress_section = order_feed_page.get_order_number_from_progress_section()
        with allure.step("Проверить успешное отображение номера заказа"):
            assert str(order_number) in order_in_progress_section