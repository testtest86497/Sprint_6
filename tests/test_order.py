from datetime import date, timedelta
import pytest
from pages.order_page import OrderPage
import allure


TOMORROW = (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")
IN_TWO_DAYS = (date.today() + timedelta(days=2)).strftime("%d.%m.%Y")


class TestOrder:

    @allure.title("Оформление заказа через кнопку в загаловке")
    def test_success_order_by_order_header_button(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_order_button()
        order_page.fill_name_field("Иван")
        order_page.fill_surname_field("Иванов")
        order_page.fill_address_field("ул. Пушкина, д. 1")
        order_page.fill_metro_field("Пушкинская")
        order_page.fill_telephone_field("+79999999999")
        order_page.click_next_button()
        order_page.fill_data_field(TOMORROW)
        order_page.click_dropdown_arrow()
        order_page.select_dropdown_option("сутки")
        order_page.select_color_checkbox("black")
        order_page.fill_comment_field("Комментарий для курьера")
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.check_success_order()


    @allure.title("Оформление заказа через в середине страницы в загаловке")
    def test_success_order_by_order_button_in_middle_of_page(self, driver):
        order_page = OrderPage(driver)
        order_page.click_on_middle_order_button()
        order_page.fill_name_field("Петр")
        order_page.fill_surname_field("Петров")
        order_page.fill_address_field("ул. Ленина, д. 2")
        order_page.fill_metro_field("Сокольники")
        order_page.fill_telephone_field("+78888888888")
        order_page.click_next_button()
        order_page.fill_data_field(IN_TWO_DAYS)
        order_page.click_dropdown_arrow()
        order_page.select_dropdown_option("двое суток")
        order_page.select_color_checkbox("grey")
        order_page.fill_comment_field("Комментарий для курьера")
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.check_success_order()
