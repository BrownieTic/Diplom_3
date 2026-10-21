from selenium.webdriver.common.by import By

class Locators:
#Главная страница
    # Кнопка «Войти в аккаунт» на главной
    button_input_main_page = [By.CSS_SELECTOR, '.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg']
    # Кнопка Оформить заказ
    button_order = [By.XPATH, './/button[text()="Оформить заказ"]']
    # Раздел Булки
    button_section_buns = [By.XPATH, './/span[text()="Булки"]/parent::div']
    start_of_section_buns = [By.XPATH, './/h2[text()="Булки"]']
    window_bun_main_page = [By.XPATH, '//p[text()="Краторная булка N-200i"]/parent::a']
    name_bun = [By.XPATH, '//p[text()="Краторная булка N-200i"]']
    button_add_ingredient_bun = [By.XPATH, '//li[@data-testid="ingredient-item"][.//p[text()="Краторная булка N-200i"]]//button[text()="Добавить"]']
    counter_bun_main_page = [By.CSS_SELECTOR,'a[href="/ingredient/6acef97852135b001b21a32b"]']
    # Раздел Соусы
    button_section_sauces = [By.XPATH, './/span[text()="Соусы"]/parent::div']
    start_of_section_sauces = [By.XPATH, './/h2[text()="Соусы"]']
    button_add_ingredient_sauce = [By.XPATH, '//li[@data-testid="ingredient-item"][.//p[text()="Соус Spicy-X"]]//button[text()="Добавить"]']
    counter_sauce_main_page = [By.CSS_SELECTOR,'a[href="/ingredient/6acef97852135b001b21a332"]']
    # Раздел Начинки
    button_section_fillings = [By.XPATH, './/span[text()="Начинки"]/parent::div']
    start_of_section_fillings = [By.XPATH, './/h2[text()="Начинки"]']
    button_add_ingredient_filling = [By.XPATH, '//li[@data-testid="ingredient-item"][.//p[text()="Биокотлета из марсианской Магнолии"]]//button[text()="Добавить"]']
    counter_filling_main_page = [By.CSS_SELECTOR,'a[href="/ingredient/6acef97852135b001b21a32e"]']
    # Детали ингредиента
    ingredient_details = [By.XPATH, './/h2[text()="Детали ингредиента"]']
    button_close_ingredient_details = [By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK"]
    # Окно идентификатора заказа
    button_order_identifier_close = [By.CSS_SELECTOR, '[data-testid="modal-close"]']
    order_number = [By.XPATH, '//p[contains(text(), "идентификатор заказа")]/preceding-sibling::h2']