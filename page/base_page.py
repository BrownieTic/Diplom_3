from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_on_page(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def click_button(self, locator):
        self.wait_to_be_clickable(locator)
        self.find_element_on_page(locator).click()

    def scroll_to_element(self, locator):
        element = self.find_element_on_page(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_text(self, locator):
        element = self.find_element_on_page(locator)
        return element.text

    def set_value(self, locator, text):
        self.find_element_on_page(locator).send_keys(text)

    def wait_to_be_clickable(self, locator): 
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def wait_load_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))

    def invisible_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located(locator))

    def current_url(self):
        return self.driver.current_url
    