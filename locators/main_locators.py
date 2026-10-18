from selenium.webdriver.common.by import By

class Locators:
#Главная страница
    # Кнопка «Войти в аккаунт» на главной
    button_input_main_page = [By.CSS_SELECTOR, '.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg']
    # Кнопка Оформить заказ
    button_order = [By.XPATH, './/button[text()="Оформить заказ"]']
    # Раздел Булки
    button_buns_main_page = [By.XPATH, './/span[text()="Булки"]/parent::div']
    section_buns_main_page = [By.XPATH, './/h2[text()="Булки"]']
    ingredient_bun_main_page = [By.CSS_SELECTOR, 'a[href*="/ingredients/643d69a5c3f7b9001cfa093c"]']
    # Раздел Соусы
    button_sauces_main_page = [By.XPATH, './/span[text()="Соусы"]/parent::div']
    section_sauces_main_page = [By.XPATH, './/h2[text()="Соусы"]']
    # Раздел Начинки
    button_fillings_main_page = [By.XPATH, './/span[text()="Начинки"]/parent::div']
    section_fillings_main_page = [By.XPATH, './/h2[text()="Начинки"]']

    # Детали ингредиента
    ingredient_details = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    button_close_ingredient_details = [By.CSS_SELECTOR, '[data-testid="modal-close"]']