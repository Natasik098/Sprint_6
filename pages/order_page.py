import re
import allure

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Заполнить имя: {name}')
    def input_first_name(self, name):
        field = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.NAME_FIELD))
        field.clear()
        field.send_keys(name)

    @allure.step('Заполнить фамилию: {surname}')
    def input_last_name(self, surname):
        field = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SURNAME_FIELD))
        field.clear()
        field.send_keys(surname)

    @allure.step('Заполнить адрес: {address}')
    def input_address(self, address):
        field = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.ADDRESS_FIELD))
        field.clear()
        field.send_keys(address)
        
    @allure.step('Выбрать станцию метро: {metro}')
    def choose_subway(self, metro):
        field = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_FIELD))
        field.click()
        field.send_keys(metro)
        metro_locator = (OrderPageLocators.METRO_STATION(metro))
        self.wait.until(EC.element_to_be_clickable(metro_locator)).click()

    @allure.step('Заполнить телефон: {phone}')
    def input_telephone_number(self, phone):
        field = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.PHONE_FIELD))
        field.click()
        field.clear()
        field.send_keys(phone)

    @allure.step('Нажать "Далее"')
    def click_next(self):
        next_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.NEXT_BUTTON))
        next_button.click()

    @allure.step('Заполнить данные на этапе "Для кого самокат"')
    def fill_user_data(self, data_set):
        self.input_first_name(data_set["name"])
        self.input_last_name(data_set["surname"])
        self.input_address(data_set["address"])
        self.choose_subway(data_set["metro"])
        self.input_telephone_number(data_set["phone"])

    @allure.step('Заполнить дату доставки: {date}')
    def input_date(self, date):
        field = self.wait.until(EC.visibility_of_element_located(OrderPageLocators.DATE_FIELD))
        field.click()
        field.send_keys(date)
        field.send_keys(Keys.ENTER)

    @allure.step('Выбрать срок аренды: {period}')
    def choose_rental_period(self, period):
        rental_period = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_FIELD))
        rental_period.click()
        period_locator = (OrderPageLocators.RENTAL_PERIOD_OPTION(period))
        self.wait.until(EC.element_to_be_clickable(period_locator)).click()

    @allure.step('Выбрать цвет: {color}')
    def choose_color(self, color):
        color_locator = (OrderPageLocators.COLOR(color))
        self.wait.until(EC.element_to_be_clickable(color_locator)).click()

    @allure.step('Заполнить комментарий: {comment}') 
    def input_comment(self, comment): 
        field = self.wait.until( EC.visibility_of_element_located(OrderPageLocators.COMMENT_FIELD))
        field.clear()
        field.send_keys(comment)
            
    @allure.step('Заполнить данные на этапе "Про аренду"') 
    def fill_rent_data(self, data_set): 

        self.input_date(data_set["date"]) 
        self.choose_rental_period(data_set["rental_period"]) 
        self.choose_color(data_set["color"]) 
        self.input_comment(data_set["comment"]) 
        
    @allure.step('Нажать "Заказать"') 
    def click_order(self): 
        order_button = self.wait.until( EC.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON))
        order_button.click() 
    
    @allure.step('Подтвердить заказ кнопкой "Да"') 
    def click_accept_order(self): 
        accept_button = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.ACCEPT_ORDER_BUTTON))
        accept_button.click() 
        
    @allure.step('Проверить успешное оформление заказа')
    def is_order_created(self):
        return self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE)).is_displayed()

    @allure.step("Получить сообщение о заказе")
    def get_order_completed_info(self): 
        return self.wait.until(EC.visibility_of_element_located( OrderPageLocators.ORDER_COMPLETED_INFO)).text 

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        order_text = self.get_order_completed_info()
        numbers = re.findall(r"\d+", order_text)
        return "".join(numbers)

    @allure.step('Перейти к статусу заказа') 
    def click_go_to_status(self): 
        status_button = self.wait.until( EC.element_to_be_clickable(OrderPageLocators.SHOW_STATUS_BUTTON))
        status_button.click()

   