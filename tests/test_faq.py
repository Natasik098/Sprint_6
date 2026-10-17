import allure
import pytest
from pages.main_page import MainPage

FAQ_ANSWERS = [
    "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
    "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
    "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
    "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
    "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
    "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
    "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
    "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
]

@allure.epic("Эпик_Главная страница")
@allure.parent_suite("Parent_suite_Домашняя страница")
@allure.suite("Suite_FAQ")
class TestFAQ:

    @allure.feature("FAQ")
    @allure.story("Проверка раздела 'Вопросы о важном'")
    @allure.title('Проверка ответа на вопрос FAQ')
    @pytest.mark.parametrize("question_number, answer_number",  
        [
            (0,0),
            (1,1),
            (2,2),
            (3,3),
            (4,4),
            (5,5),
            (6,6),
            (7,7),
        ])
    
    def test_faq_question_show_answer(self, driver, question_number, answer_number):
        main_page = MainPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_faq_question(question_number)
        answer = main_page.get_faq_answer(answer_number)

        with allure.step("Проверить текст ответа"):
            assert answer.is_displayed() 
            assert answer.text == FAQ_ANSWERS[answer_number]