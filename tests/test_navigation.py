from pages.main_page import MainPage
import allure
from data import Urls

class TestNavigation:

    @allure.title("Проверка навигации на главную страницу")
    def test_navigation_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_order_button()
        main_page.click_on_logo()
        main_page.wait_for_url(Urls.MAIN_PAGE)
        current = main_page.get_current_url()
        assert current == Urls.MAIN_PAGE

    @allure.title("Проверка навигации на страницу Yandex")
    def test_navigation_to_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_yandex_logo()
        main_page.switch_to_new_tab()
        main_page.wait_for_url(Urls.DZEN_PAGE_PATTERN)
        current = main_page.get_current_url()
        assert current == Urls.DZEN_PAGE_PATTERN