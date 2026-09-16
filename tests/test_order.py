from datetime import date, timedelta
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage


TOMORROW = (date.today() + timedelta(days=1)).strftime("%d.%m.%Y")
IN_TWO_DAYS = (date.today() + timedelta(days=2)).strftime("%d.%m.%Y")


class TestOrder:

    @pytest.mark.parametrize("name,surname,address,metro,phone,date,rental_period,color,comment", [
        ("Иван", "Иванов", "ул. Пушкина, д. 1", "Пушкинская", "+79999999999", TOMORROW, "сутки", "black", "Комментарий для курьера"),
        ("Петр", "Петров", "ул. Ленина, д. 2", "Сокольники", "+78888888888", IN_TWO_DAYS, "двое суток", "grey", "Комментарий для курьера"),
    ])
    def test_order_by_header_button(self, driver, name, surname, address, metro, phone, date, rental_period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.click_on_order_button()
        assert order_page.check_order_header()
        order_page.click_on_logo()
        main_page.click_on_order_button()
        order_page.fill_name_field(name)
        order_page.fill_surname_field(surname)
        order_page.fill_address_field(address)
        order_page.fill_metro_field(metro)
        order_page.fill_telephone_field(phone)
        order_page.click_next_button()
        order_page.fill_data_field(date)
        order_page.click_dropdown_arrow()
        order_page.select_dropdown_option(rental_period)
        order_page.select_color_checkbox(color)
        order_page.fill_comment_field(comment)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.check_success_order()
