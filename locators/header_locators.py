from selenium.webdriver.common.by import By

class Locators:
#Шапка
    # Конструктор
    button_header_constructor = [By.CSS_SELECTOR, '.AppHeader_header__link__3D_hX']
    # Логотип
    button_header_logo = [By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2']
    # Личный кабинет
    button_header_profile = [By.CSS_SELECTOR, 'a[href*="/account"]']
    # Лента заказов
    button_order_feed = [By.XPATH, './/p[text() = "Лента заказов"]']


#Страница регистрации
    # Поля для регистрации
    name_for_registration_path = './/label[text() = "Имя"]/following-sibling::input'
    login_for_registration_path = './/label[text() = "Email"]/following-sibling::input'
    password_for_registration_path = './/input[@name="Пароль"]'
    # Кнопка «Зарегистрироваться»
    button_register_path = './/button[text()="Зарегистрироваться"]'
    # Сообщение об ошибке с паролем
    password_erroror_registration_selector = '.input__error.text_type_main-default'
    button_input_from_registration_selector = 'a[href*="/login"]'

#Страница входа
    # Кнопка «Войти»
    button_input_page_input_path = [By.XPATH, './/button[text()="Войти"]']
    # Поля для входа
    login_for_input_page_input_name = 'name'
    password_for_input_page_input_name = 'Пароль'

#Страница восстановления пароля
    # Кнопка "Войти" в форме восстановления пароля
    button_input_password_recovery_form_selector = 'a[href*="/login"]'

#Страница профиля
    # Кнопка Выход
    button_out_profile_page_path = '//button[text()="Выход"]'
