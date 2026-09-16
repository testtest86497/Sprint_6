from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    RENTAL_PERIOD_OPTIONS = {
        "сутки": OrderPageLocators.DROPDOWN_OPTION_SUTKI,
        "двое суток": OrderPageLocators.DROPDOWN_OPTION_2_SUTKI,
        "трое суток": OrderPageLocators.DROPDOWN_OPTION_3_SUTKI,
        "четверо суток": OrderPageLocators.DROPDOWN_OPTION_4_SUTKI,
        "пятеро суток": OrderPageLocators.DROPDOWN_OPTION_5_SUTKI,
        "шестеро суток": OrderPageLocators.DROPDOWN_OPTION_6_SUTKI,
        "семеро суток": OrderPageLocators.DROPDOWN_OPTION_7_SUTKI,
    }

    def check_order_header(self):
        return self.wait_for_element(OrderPageLocators.ORDER_HEADER).is_displayed()


    def fill_name_field(self, name):
        self.wait_for_element(OrderPageLocators.NAME_FIELD).send_keys(name)


    def fill_surname_field(self, surname):
        self.wait_for_element(OrderPageLocators.SURNAME_FIELD).send_keys(surname)


    def fill_address_field(self, address):
        self.wait_for_element(OrderPageLocators.ADDRESS_FIELD).send_keys(address)


    def fill_metro_field(self, metro):
        self.wait_for_element(OrderPageLocators.METRO_FIELD).send_keys(metro)
        self.wait_and_click(OrderPageLocators.METRO_OPTION)


    def fill_telephone_field(self, telephone):
        self.wait_for_element(OrderPageLocators.TELEPHONE_FIELD).send_keys(telephone)


    def click_next_button(self):
        self.wait_and_click(OrderPageLocators.NEXT_BUTTON)


    def fill_data_field(self, data):
        data_field = self.wait_for_element(OrderPageLocators.DATA_FIELD)
        data_field.send_keys(data)
        data_field.send_keys(Keys.ENTER)


    def click_dropdown_arrow(self):
        self.wait_and_click(OrderPageLocators.DROPDOWN_ARROW)


    def select_dropdown_option(self, option):
        if option not in self.RENTAL_PERIOD_OPTIONS:
            raise ValueError(f"Invalid option: {option}")
        self.wait_and_click(self.RENTAL_PERIOD_OPTIONS[option])


    def click_black_color_checkbox(self):
        self.wait_and_click(OrderPageLocators.BLACK_COLOR_CHECKBOX)


    def click_grey_color_checkbox(self):
        self.wait_and_click(OrderPageLocators.GREY_COLOR_CHECKBOX)


    def select_color_checkbox(self, color):
        if color == "black":
            self.click_black_color_checkbox()
        elif color == "grey":
            self.click_grey_color_checkbox()
        else:
            raise ValueError(f"Invalid color: {color}")


    def fill_comment_field(self, comment):
        self.wait_for_element(OrderPageLocators.COMMENT_FIELD).send_keys(comment)


    def click_back_button(self):
        self.wait_and_click(OrderPageLocators.BACK_BUTTON)


    def click_order_button(self):
        self.wait_and_click(OrderPageLocators.ORDER_BUTTON)


    def click_yes_button(self):
        self.wait_and_click(OrderPageLocators.YES_BUTTON)


    def click_no_button(self):
        self.wait_and_click(OrderPageLocators.NO_BUTTON)


    def check_success_order(self):
        return self.wait_for_element(OrderPageLocators.SUCCESS_ORDER).is_displayed()


    def click_check_status_button(self):
        self.wait_and_click(OrderPageLocators.CHECK_STATUS_BUTTON)
