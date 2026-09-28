from selenium.webdriver.common.by import By

class QuestionsLocators:
    QUESTION = (By.ID, "accordion__heading-{}")


class AnswersLocators:
    ANSWER = (By.ID, "accordion__panel-{}")


class MainPageLocators:
    ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    MIDDLE_ORDER_BUTTON = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")
    