from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from data import Urls

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))


    def wait_and_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()


    def click_on_order_button(self):
        self.wait_and_click(BasePageLocators.BUTTON_ORDER)


    def click_on_logo(self):
        self.wait_and_click(BasePageLocators.SAMOKAT_LOGO)


    def click_on_status_order(self):
        self.wait_and_click(BasePageLocators.STATUS_ORDER)


    def accept_cookies(self):
        self.wait_and_click(BasePageLocators.COOKIE_BUTTON)


    def click_on_yandex_logo(self):
        self.wait_and_click(BasePageLocators.YANDEX_LOGO)


    def switch_to_new_tab(self, timeout=10):
        main_tab = self.driver.current_window_handle
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        new_tab = [tab for tab in self.driver.window_handles if tab != main_tab][0]
        self.driver.switch_to.window(new_tab)


    def check_order_page_url(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(Urls.ORDER_PAGE))


    def check_main_page_url(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(Urls.MAIN_PAGE))


    def check_yandex_url(self, timeout=15):
        # Яндекс редиректит через промежуточные sso-страницы, поэтому ждём именно домен dzen.ru в начале адреса
        return WebDriverWait(self.driver, timeout).until(EC.url_matches(Urls.DZEN_PAGE_PATTERN))
