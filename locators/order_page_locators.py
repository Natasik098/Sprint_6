from selenium.webdriver.common.by import By

class OrderPageLocators:

    NAME_FIELD = (By.XPATH,"//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH,"//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH,"//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH,"//input[@placeholder='* Станция метро']") 
    PHONE_FIELD = (By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH,"//button[text()='Далее']")

#Вторая часть формы
    DATE_FIELD = (By.XPATH,"//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.XPATH,"//div[text()='* Срок аренды']")
    COMMENT_FIELD = (By.XPATH,"//input[@placeholder='Комментарий для курьера']")
    #Кнопка "Заказать" внутри формы заказа
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")
    ACCEPT_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[normalize-space()='Да']")
    ORDER_COMPLETED_INFO = (By.XPATH, "//*[contains(text(), 'Номер заказа')]")
    SHOW_STATUS_BUTTON = [By.XPATH, "//button[text() = 'Посмотреть статус']"]
    SUCCESS_MESSAGE = (By.XPATH,"//*[contains(text(), 'Заказ оформлен')]")
    

    @staticmethod
    def METRO_STATION(metro):
        return (By.XPATH, f"//div[text()='{metro}']/parent::button")

    @staticmethod
    def RENTAL_PERIOD_OPTION(period):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")

    @staticmethod
    def COLOR(color):
        return (By.XPATH, f"//label[contains(., '{color}')]")