from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
import allure


class OrderPage(MainPage):

    RENTAL_PERIOD_OPTIONS = {
        "сутки": OrderPageLocators.DROPDOWN_OPTION_SUTKI,
        "двое суток": OrderPageLocators.DROPDOWN_OPTION_2_SUTKI,
        "трое суток": OrderPageLocators.DROPDOWN_OPTION_3_SUTKI,
        "четверо суток": OrderPageLocators.DROPDOWN_OPTION_4_SUTKI,
        "пятеро суток": OrderPageLocators.DROPDOWN_OPTION_5_SUTKI,
        "шестеро суток": OrderPageLocators.DROPDOWN_OPTION_6_SUTKI,
        "семеро суток": OrderPageLocators.DROPDOWN_OPTION_7_SUTKI,
    }

    @allure.step("Проверяем заголовок страницы")
    def check_order_header(self):
        return self.wait_for_element(OrderPageLocators.ORDER_HEADER).is_displayed()


    @allure.step("Заполняем поле имя")
    def fill_name_field(self, name):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name)


    @allure.step("Заполняем поле фамилия")
    def fill_surname_field(self, surname):
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname)


    @allure.step("Заполняем поле адресс")
    def fill_address_field(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)


    @allure.step("Заполняем поле метро")
    def fill_metro_field(self, metro):
        self.send_keys_to_element(OrderPageLocators.METRO_FIELD, metro)
        self.click_on_element(OrderPageLocators.METRO_OPTION)


    @allure.step("Заполняем поле номер телефона")
    def fill_telephone_field(self, telephone):
        self.send_keys_to_element(OrderPageLocators.TELEPHONE_FIELD, telephone)


    @allure.step("Нажимаем на кнопку далее")
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)


    @allure.step("Заполняем поле дата")
    def fill_data_field(self, data):
        self.send_keys_to_element(OrderPageLocators.DATA_FIELD, data)
        self.send_keys_to_element(OrderPageLocators.DATA_FIELD, Keys.ENTER)


    @allure.step("Нажимаем на выпадающий список")
    def click_dropdown_arrow(self):
        self.click_on_element(OrderPageLocators.DROPDOWN_ARROW)


    @allure.step("Выбираем параметр из выпадающего списка")
    def select_dropdown_option(self, option):
        if option not in self.RENTAL_PERIOD_OPTIONS:
            raise ValueError(f"Invalid option: {option}")
        self.click_on_element(self.RENTAL_PERIOD_OPTIONS[option])


    @allure.step("Выбираем черный цвет")
    def click_black_color_checkbox(self):
        self.click_on_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)


    @allure.step("Выбираем серый цвет")
    def click_grey_color_checkbox(self):
        self.click_on_element(OrderPageLocators.GREY_COLOR_CHECKBOX)


    @allure.step("Выбираем цвет")
    def select_color_checkbox(self, color):
        if color == "black":
            self.click_black_color_checkbox()
        elif color == "grey":
            self.click_grey_color_checkbox()
        else:
            raise ValueError(f"Invalid color: {color}")


    @allure.step("Заполняем поле комментарий")
    def fill_comment_field(self, comment):
        self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD, comment)


    @allure.step("Нажимаем на кнопку назад")
    def click_back_button(self):
        self.click_on_element(OrderPageLocators.BACK_BUTTON)


    @allure.step("Нажимаем на кнопку заказа")
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)


    @allure.step("Нажимаем на кнопку да")
    def click_yes_button(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON)


    @allure.step("Нажимаем на кнопку нет")
    def click_no_button(self):
        self.click_on_element(OrderPageLocators.NO_BUTTON)


    @allure.step("Проверям статус заявки")
    def check_success_order(self):
        return self.wait_for_element(OrderPageLocators.SUCCESS_ORDER).is_displayed()


    @allure.step("Нажимаем на кнопку проверки статуса заявки")
    def click_check_status_button(self):
        self.click_on_element(OrderPageLocators.CHECK_STATUS_BUTTON)
