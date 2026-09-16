import pytest
from pages.main_page import MainPage


class TestQuestions:

    @pytest.fixture(autouse=True)
    def open_main_page(self, driver):
        self.main_page = MainPage(driver)
        self.main_page.accept_cookies()


    def test_how_much_question(self):
        self.main_page.click_on_how_much_question()
        self.main_page.check_how_much_answer()


    def test_several_scooter_question(self):
        self.main_page.click_on_several_scooter_question()
        self.main_page.check_several_scooter_answer()


    def test_rental_time_question(self):
        self.main_page.click_on_rental_time_question()
        self.main_page.check_rental_time_answer()


    def test_order_today_question(self):
        self.main_page.click_on_order_today_question()
        self.main_page.check_order_today_answer()


    def test_extend_order_question(self):
        self.main_page.click_on_extend_order_question()
        self.main_page.check_extend_order_answer()


    def test_charger_question(self):
        self.main_page.click_on_charger_question()
        self.main_page.check_charger_answer()


    def test_cancel_order_question(self):
        self.main_page.click_on_cancel_order_question()
        self.main_page.check_cancel_order_answer()


    def test_live_far_away_question(self):
        self.main_page.click_on_live_far_away_question()
        self.main_page.check_live_far_away_answer()
