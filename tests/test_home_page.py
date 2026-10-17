import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

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

        with allure.step("Проверить, что открылась главная страница"):
            assert (
                main_page.current_url().rstrip("/")
                == MainPageLocators.URL.rstrip("/")
            )

    @allure.feature('Фича_Переход на Яндекс по логотипу')
    @allure.story('Стори_При нажатии на логотип Яндекса открывается новое окно')
    @allure.title('Переход на Яндекс по логотипу')
    def test_click_yandex_logo(self, driver):

        main_page = MainPage(driver)

        main_page.open()
        main_page.accept_cookies()
        old_windows = driver.window_handles
        main_page.click_yandex_logo()
        main_page.switch_to_new_window(old_windows)

        with allure.step("Дождаться редиректа на главную страницу Дзена"):
            WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))

        with allure.step("Проверить, что открылась главная страница Дзена"):
            current_url = main_page.current_url().lower()
            assert "dzen.ru" in current_url, f"Ожидался Дзен, но URL: {current_url}"
        