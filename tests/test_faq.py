import allure
import pytest

from pages.main_page import MainPage
from data import FAQ_ANSWERS

@allure.epic("Эпик_Главная страница")
@allure.parent_suite("Parent_suite_Домашняя страница")
@allure.suite("Suite_FAQ")
class TestFAQ:

    @allure.feature("FAQ")
    @allure.story("Проверка раздела 'Вопросы о важном'")
    @allure.title('Проверка ответа на вопрос FAQ')
    @allure.description(
        "Проверка соответствия ответов вопросам " 
        "в разделе 'Вопросы о важном'."
    )
    @pytest.mark.parametrize("question_number, expected_answer",  
        [
            (0, FAQ_ANSWERS[0]),
            (1, FAQ_ANSWERS[1]),
            (2, FAQ_ANSWERS[2]),
            (3, FAQ_ANSWERS[3]),
            (4, FAQ_ANSWERS[4]),
            (5, FAQ_ANSWERS[5]),
            (6, FAQ_ANSWERS[6]),
            (7, FAQ_ANSWERS[7]),
        ]
    )
    def test_faq_answer(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Принять cookies"): 
            main_page.accept_cookies()
        with allure.step("Прокрутить до FAQ"):
            main_page.scroll_to_faq()
        with allure.step("Открыть вопрос"):
            main_page.click_faq_question(question_number)

        with allure.step("Проверить ответ"):
            assert main_page.is_faq_answer_correct(
                question_number, 
                expected_answer
            )