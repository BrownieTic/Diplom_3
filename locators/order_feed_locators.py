from selenium.webdriver.common.by import By

class Locators:
    # Лента заказов (правая часть страницы)
    counter_order_all_time = [By.XPATH, './/h3[text() = "Выполнено за все время"]/following-sibling::p[@class="pt-15 text text_type_main-medium ISTKLfT0GntaQ5VnHFPC"]']
    counter_order_today = [By.XPATH, './/h3[text() = "Выполнено за сегодня"]/following-sibling::p[@class="pt-15 text text_type_main-medium ISTKLfT0GntaQ5VnHFPC"]']
    section_in_progress = [By.XPATH, './/h3[text() = "В работе"]/following-sibling::ul[@class="pt-6  LjaB7a4JqWnCdfSGztaK"]']