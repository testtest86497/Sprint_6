from selenium.webdriver.common.by import By

class QuestionsLocators:
    QUESTION_HEADER = (By.CLASS_NAME, "Home_SubHeader__zwi_E")
    HOW_MUCH_QUESTION = (By.ID, "accordion__heading-0")
    SEVERAL_SCOOTER_QUESTION = (By.ID, "accordion__heading-1")
    RENTAL_TIME_QUESTION = (By.ID, "accordion__heading-2")
    ORDER_TODAY_QUESTION = (By.ID, "accordion__heading-3")
    EXTEND_ORDER_QUESTION = (By.ID, "accordion__heading-4")
    CHARGER_QUESTION = (By.ID, "accordion__heading-5")
    CANCEL_ORDER_QUESTION = (By.ID, "accordion__heading-6")
    LIVE_FAR_AWAY_QUESTION = (By.ID, "accordion__heading-7")


class AnswersLocators:
    HOW_MUCH_ANSWER = (By.ID, "accordion__panel-0")
    SEVERAL_SCOOTER_ANSWER = (By.ID, "accordion__panel-1")
    RENTAL_TIME_ANSWER = (By.ID, "accordion__panel-2")
    ORDER_TODAY_ANSWER = (By.ID, "accordion__panel-3")
    EXTEND_ORDER_ANSWER = (By.ID, "accordion__panel-4")
    CHARGER_ANSWER = (By.ID, "accordion__panel-5")
    CANCEL_ORDER_ANSWER = (By.ID, "accordion__panel-6")
    LIVE_FAR_AWAY_ANSWER = (By.ID, "accordion__panel-7")


class MainPageLocators:
    ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    