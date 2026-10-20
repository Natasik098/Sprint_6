import allure

from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from constants import BASE_URL

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(BASE_URL)

    @allure.step('Принять cookies')
    def accept_cookies(self):
        cookie_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON))
        cookie_button.click()

    @allure.step('Нажать верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        order_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.TOP_ORDER_BUTTON))
        order_button.click()

    @allure.step('Нажать нижнюю кнопку "Заказать"')
    def click_bottom_order_button(self):
        order_button = self.wait.until(EC.element_to_be_clickable(MainPageLocators.BOTTOM_ORDER_BUTTON))
        order_button.click()

    @allure.step('Нажать логотип "Самокат"')
    def click_scooter_logo(self):
        scooter_logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.SCOOTER_LOGO))
        scooter_logo.click()

    @allure.step('Нажать логотип "Яндекс"')
    def click_yandex_logo(self):
        yandex_logo = self.wait.until(EC.element_to_be_clickable(MainPageLocators.YANDEX_LOGO))
        yandex_logo.click()

    @allure.step("Прокрутить страницу до FAQ")
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step("Нажать на вопрос FAQ")
    def click_faq_question(self, question_number):
        question = self.wait.until(EC.element_to_be_clickable(MainPageLocators.FAQ_QUESTION_BUTTON(question_number)))
        question.click()

    @allure.step("Проверить ответ FAQ")
    def is_faq_answer_correct(self, answer_number, expected_answer): 
        answer_locator = (MainPageLocators.FAQ_ANSWER(answer_number))
        return self.wait.until(EC.text_to_be_present_in_element(answer_locator, expected_answer))