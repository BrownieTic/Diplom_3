from page.base_page import BasePage

class MainPage(BasePage):
        def get_answer_text(self, locator):
            return self.find_sibling_element(locator)