from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_HEADER = (By.CLASS_NAME, "Order_Header__BZXOb")
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    TELEPHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO_OPTION = (By.CLASS_NAME, "select-search__option")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    #rental_page_locators
    DATA_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_ARROW = (By.CLASS_NAME, "Dropdown-arrow")
    DROPDOWN_OPTION_SUTKI = (By.XPATH, "//div[text()='сутки']")
    DROPDOWN_OPTION_2_SUTKI = (By.XPATH, "//div[text()='двое суток']")
    DROPDOWN_OPTION_3_SUTKI = (By.XPATH, "//div[text()='трое суток']")
    DROPDOWN_OPTION_4_SUTKI = (By.XPATH, "//div[text()='четверо суток']")
    DROPDOWN_OPTION_5_SUTKI = (By.XPATH, "//div[text()='пятеро суток']")
    DROPDOWN_OPTION_6_SUTKI = (By.XPATH, "//div[text()='шестеро суток']")
    DROPDOWN_OPTION_7_SUTKI = (By.XPATH, "//div[text()='семеро суток']")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, "//button[text()='Назад']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    #ACCESS WINDOW
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    NO_BUTTON = (By.XPATH, "//button[text()='Нет']")

    #CONFIRMATION WINDOW
    SUCCESS_ORDER = (By.XPATH, "//div[text()='Заказ оформлен']")
    ORDER_INFORMATION = (By.XPATH, "//div[@class='Order_Text__2broi']")
    CHECK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
