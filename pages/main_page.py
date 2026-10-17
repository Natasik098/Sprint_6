import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Открыть главную страницу')
    def open(self):
        self.driver.get(MainPageLocators.URL)

    @allure.step('Принять cookies')
    def accept_cookies(self):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON))
            cookie_button.click()
        except Exception:
            pass

#FAQ
    @allure.step('Нажать на вопрос FAQ #{question_number}')
    def click_faq_question(self, question_number):
        question = self.wait.until(EC.presence_of_element_located(MainPageLocators.FAQ_QUESTION_BUTTON(question_number)))
        question.location_once_scrolled_into_view
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.FAQ_QUESTION_BUTTON(question_number))).click()

    @allure.step('Получить ответ на вопрос FAQ #{answer_number}')
    def get_faq_answer(self, answer_number): 
        return self.wait.until(EC.visibility_of_element_located(MainPageLocators.FAQ_ANSWER(answer_number)))

#Заказ 
    @allure.step('Нажать верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.TOP_ORDER_BUTTON)).click()

    @allure.step('Нажать нижнюю кнопку "Заказать"')
    def click_bottom_order_button(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON)).click()

    @allure.step('Нажать логотип "Самокат"')
    def click_scooter_logo(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO)).click()

    @allure.step('Нажать логотип "Яндекс"')
    def click_yandex_logo(self):
        self.wait.until(EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)).click()

    @allure.step("Получить текущий URL")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, old_windows):
        self.wait.until(lambda driver: len(driver.window_handles) > len(old_windows))
        new_windows = self.driver.window_handles
        for window in new_windows:
            if window not in old_windows:
                self.driver.switch_to.window(window)
                break