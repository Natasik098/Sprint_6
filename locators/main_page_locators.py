from selenium.webdriver.common.by import By

class MainPageLocators:

    URL = "https://qa-scooter.praktikum-services.ru/"

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
#Вопросы FAQ
    FAQ_QUESTIONS = (By.XPATH, "//div[@class='accordion__button']")
#Блок "Вопросы о важном"
    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")
#Заголовок FAQ
    FAQ_TITLE = (By.XPATH, "//div[text()='Вопросы о важном']")

    @staticmethod
    def FAQ_QUESTION_BUTTON(question_number):
        return (By.ID, f"accordion__heading-{question_number}")
    
    @staticmethod
    def FAQ_ANSWER(answer_number):
        return (By.XPATH, f"//div[@id='accordion__panel-{answer_number}']/p")
    
#Верхняя кнопка "Заказать"
    TOP_ORDER_BUTTON = (By.XPATH,"//div[starts-with(@class, 'Header')]/button[normalize-space()='Заказать']")
#Нижняя кнопка "Заказать"
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[starts-with(@class, 'Home')]/button[normalize-space()='Заказать']")
#Логотип Самоката
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
#Логотип Яндекса
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")