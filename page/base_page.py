from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент на странице")
    def find_element_on_page(self, locator):
        element = self.driver.find_element(*locator)
        return element

    @allure.step("Кликнуть по кнопке")
    def click_button(self, locator):
        self.wait_to_be_clickable(locator)
        self.find_element_on_page(locator).click()

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_on_page(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        self.wait_visibility_of_element(locator)
        element = self.find_element_on_page(locator)
        return element.text

    @allure.step("Установить значение элемента")
    def set_value(self, locator, text):
        self.find_element_on_page(locator).send_keys(text)

    @allure.step("Ожидать кликабельности элемента")
    def wait_to_be_clickable(self, locator): 
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step("Ожидать видимости элемента")
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Ожидать загрузки страницы")
    def wait_load_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))

    @allure.step("Ожидать невидимости элемента")
    def invisible_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Получить текущий URL страницы")
    def current_url(self):
        return self.driver.current_url
    