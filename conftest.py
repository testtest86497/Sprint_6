import pytest
from selenium import webdriver
from data import Urls
from pages.base_page import BasePage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(0)
    driver.get(Urls.MAIN_PAGE)
    BasePage(driver).accept_cookies() 
    yield driver
    driver.quit()
