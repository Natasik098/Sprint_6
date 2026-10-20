import allure

from pages.main_page import MainPage
from constants import BASE_URL, DZEN_URL 

@allure.epic("Эпик_Главная страница")
@allure.parent_suite("Parent_suite_Домашняя страница")
@allure.suite("Suite_Логотипы")
class TestHomePage:

    @allure.feature('Фича_Переход на главную страницу по логотипу "Самокат"')
    @allure.story('Стори_При нажатии на логотип "Самокат" открывается главная страница')
    @allure.title('Переход на главную страницу по логотипу "Самокат"')
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_scooter_logo()

        assert (
                main_page.get_current_url().rstrip("/")
                == BASE_URL.rstrip("/")
        )

    @allure.feature('Фича_Переход на Яндекс по логотипу')
    @allure.story('Стори_При нажатии на логотип Яндекса открывается новое окно')
    @allure.title('Переход на Яндекс по логотипу')
    def test_click_yandex_logo(self, driver):

        main_page = MainPage(driver)

        main_page.open()
        main_page.accept_cookies()
        old_windows = (main_page.get_window_handles())

        main_page.click_yandex_logo()
        main_page.switch_to_new_window(old_windows)

        assert main_page.wait_for_url_contains(DZEN_URL.rstrip("/"))