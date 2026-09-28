from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def click_on_element(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()


    def wait_for_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    def send_keys_to_element(self, locator, keys, timeout=5):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(keys)


    def accept_cookies(self):
        self.click_on_element(BasePageLocators.COOKIE_BUTTON)


    def get_current_url(self):
        return self.driver.current_url


    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))