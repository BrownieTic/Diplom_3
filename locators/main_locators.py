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
    ingredient_bun_main_page = [ By.XPATH, '//p[text()="Краторная булка N-200i"]/parent::a']
    button_add_ingredient_bun = [By.XPATH, '//li[@data-testid="ingredient-item"][.//p[text()="Краторная булка N-200i"]]//button[text()="Добавить"]']
    counter_bun_main_page = [By.CSS_SELECTOR,'a[href*="/ingredients/643d69a5c3f7b9001cfa093c"] .counter__num']
    # Раздел Соусы
    button_sauces_main_page = [By.XPATH, './/span[text()="Соусы"]/parent::div']
    section_sauces_main_page = [By.XPATH, './/h2[text()="Соусы"]']
    button_add_ingredient_sauce = [By.XPATH, '//li[@data-testid="ingredient-item"][.//p[text()="Соус Spicy-X"]]//button[text()="Добавить"]']
    counter_sauce_main_page = [By.CSS_SELECTOR,'a[href*="/ingredients/643d69a5c3f7b9001cfa0942"] .counter__num']
    # Раздел Начинки
    button_fillings_main_page = [By.XPATH, './/span[text()="Начинки"]/parent::div']
    section_fillings_main_page = [By.XPATH, './/h2[text()="Начинки"]']
    button_add_ingredient_filling = [By.XPATH, '//li[@data-testid="ingredient-item"][.//p[text()="Биокотлета из марсианской Магнолии"]]//button[text()="Добавить"]']
    counter_filling_main_page = [By.CSS_SELECTOR,'a[href*="/ingredients/643d69a5c3f7b9001cfa0941"] .counter__num']
    # Детали ингредиента
    ingredient_details = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    button_close_ingredient_details = [By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]']
    # Окно идентификатора заказа
    button_order_identifier_close = [By.CSS_SELECTOR, '[data-testid="modal-close"]']
    order_number = [By.XPATH, '//p[contains(text(), "идентификатор заказа")]/preceding-sibling::h2']