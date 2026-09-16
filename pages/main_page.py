from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.main_page_locators import QuestionsLocators
from locators.main_page_locators import AnswersLocators
from locators.main_page_locators import MainPageLocators


# Прокручивает к элементу и проверяет, что в его центре не лежит другой элемент (например, картинка самоката)
SCROLL_AND_CHECK_NOT_OBSCURED = """
    const element = arguments[0];
    element.scrollIntoView({block: 'center', behavior: 'instant'});
    const rect = element.getBoundingClientRect();
    const topElement = document.elementFromPoint(rect.left + rect.width / 2, rect.top + rect.height / 2);
    return element.contains(topElement);
"""


class MainPage(BasePage):

    def click_on_question(self, locator):
        question = self.wait_for_element(locator)
        WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script(SCROLL_AND_CHECK_NOT_OBSCURED, question))
        question.click()


    def click_on_how_much_question(self):
        self.click_on_question(QuestionsLocators.HOW_MUCH_QUESTION)


    def check_how_much_answer(self):
        how_much_answer = self.wait_for_element(AnswersLocators.HOW_MUCH_ANSWER).text
        assert how_much_answer == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."


    def click_on_several_scooter_question(self):
        self.click_on_question(QuestionsLocators.SEVERAL_SCOOTER_QUESTION)


    def check_several_scooter_answer(self):
        several_scooter_answer = self.wait_for_element(AnswersLocators.SEVERAL_SCOOTER_ANSWER).text
        assert several_scooter_answer == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
        

    def click_on_rental_time_question(self):
        self.click_on_question(QuestionsLocators.RENTAL_TIME_QUESTION)


    def check_rental_time_answer(self):
        rental_time_answer = self.wait_for_element(AnswersLocators.RENTAL_TIME_ANSWER).text
        assert rental_time_answer == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."


    def click_on_order_today_question(self):
        self.click_on_question(QuestionsLocators.ORDER_TODAY_QUESTION)


    def check_order_today_answer(self):
        order_today_answer = self.wait_for_element(AnswersLocators.ORDER_TODAY_ANSWER).text
        assert order_today_answer == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."


    def click_on_extend_order_question(self):
        self.click_on_question(QuestionsLocators.EXTEND_ORDER_QUESTION)


    def check_extend_order_answer(self):
        extend_order_answer = self.wait_for_element(AnswersLocators.EXTEND_ORDER_ANSWER).text
        assert extend_order_answer == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."


    def click_on_charger_question(self):
        self.click_on_question(QuestionsLocators.CHARGER_QUESTION)


    def check_charger_answer(self):
        charger_answer = self.wait_for_element(AnswersLocators.CHARGER_ANSWER).text
        assert charger_answer == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."


    def click_on_cancel_order_question(self):
        self.click_on_question(QuestionsLocators.CANCEL_ORDER_QUESTION)


    def check_cancel_order_answer(self):
        cancel_order_answer = self.wait_for_element(AnswersLocators.CANCEL_ORDER_ANSWER).text
        assert cancel_order_answer == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."


    def click_on_live_far_away_question(self):
        self.click_on_question(QuestionsLocators.LIVE_FAR_AWAY_QUESTION)


    def check_live_far_away_answer(self):
        live_far_away_answer = self.wait_for_element(AnswersLocators.LIVE_FAR_AWAY_ANSWER).text
        assert live_far_away_answer == "Да, обязательно. Всем самокатов! И Москве, и Московской области."


    def click_on_order_button(self):
        self.wait_and_click(MainPageLocators.ORDER_BUTTON)
