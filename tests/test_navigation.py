from pages.base_page import BasePage


class TestNavigation:

    def test_navigation_to_main_page(self, driver):
        base_page = BasePage(driver)
        base_page.accept_cookies()
        base_page.click_on_order_button()
        assert base_page.check_order_page_url()
        base_page.click_on_logo()
        assert base_page.check_main_page_url()


    def test_navigation_to_yandex(self, driver):
        base_page = BasePage(driver)
        base_page.accept_cookies()
        base_page.click_on_yandex_logo()
        base_page.switch_to_new_tab()
        assert base_page.check_yandex_url()
