import allure 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить открытие окна браузера")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, old_windows):
        self.wait.until(EC.number_of_windows_to_be(len(old_windows) + 1))
        new_window = next(
            window 
            for window in self.driver.window_handles 
            if window not in old_windows
        )
        self.driver.switch_to.window(new_window)

    @allure.step("Дождаться URL, содержащего: {url_part}")
    def wait_for_url_contains(self, url_part):
        return self.wait.until(EC.url_contains(url_part))

    @allure.step("Прокрутить страницу к элементу")
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)