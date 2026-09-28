from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import QuestionsLocators
from locators.main_page_locators import AnswersLocators
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
import allure


class MainPage(BasePage):

    @allure.step("Нажимаем на вопрос")
    def click_on_question(self, index):
        by, locator = QuestionsLocators.QUESTION
        self.click_on_element((by, locator.format(index)))


    @allure.step("Берем текст ответа")
    def get_answer_text(self, index):
        by, locator = AnswersLocators.ANSWER
        return self.wait_for_element((by, locator.format(index))).text


    @allure.step("Нажимаем на кнопку заказа")
    def click_on_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)


    @allure.step("Нажимаем на Логотип главной страницы")
    def click_on_logo(self):
        self.click_on_element(BasePageLocators.SAMOKAT_LOGO)


    @allure.step("Нажимаем на кнопку статус заказа")
    def click_on_status_order(self):
        self.click_on_element(BasePageLocators.STATUS_ORDER)


    @allure.step("Нажимаем на логотип яндекса")
    def click_on_yandex_logo(self):
        self.click_on_element(BasePageLocators.YANDEX_LOGO)


    @allure.step("Нажимаем на кнопку заказа в середине страницы")
    def click_on_middle_order_button(self):
        self.click_on_element(MainPageLocators.MIDDLE_ORDER_BUTTON)


    @allure.step("Смена вкладки")
    def switch_to_new_tab(self, timeout=10):
        current = self.driver.current_window_handle
        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
        new_tab = next(h for h in self.driver.window_handles if h != current)
        self.driver.switch_to.window(new_tab)