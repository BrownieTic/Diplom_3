import pytest
from selenium import webdriver
from urls import Urls as url

from page.main_page import MainPage
from page.base_page import BasePage

@pytest.fixture(scope="class", params=["chrome", "firefox"])
def driver(request):
    if "chrome" in request.param:
        driver = webdriver.Chrome()
    elif "firefox" in request.param:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_main_page(driver):
    driver.get(url.MAIN_PAGE_URL)
    return driver

@pytest.fixture(scope="function")
def driver_login_page(driver):
    driver.get(url.url_login)
    return driver

@pytest.fixture(scope="function")
def init_main_page(driver_main_page):
    page = MainPage(driver_main_page)
    return page

@pytest.fixture(scope="function")
def init_login_page(driver_login_page):
    page = BasePage(driver_login_page)
    return page
