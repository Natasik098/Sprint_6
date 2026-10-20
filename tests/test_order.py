import allure
import pytest

from data import TOP_ORDER_DATA,BOTTOM_ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.epic("Эпик_Создание заказа")
@allure.parent_suite("Parent_suite_Создание заказа")
@allure.suite("Suite_Оформление заказа")
class TestOrderPage:

    @allure.feature("Создание заказа")
    @allure.story("Оформление заказа")
    @allure.title("Оформление заказа с разными данными")
    @pytest.mark.parametrize("data_set", TOP_ORDER_DATA)
    def test_create_order_from_top_button(self, driver, data_set):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_top_order_button()

        order_page.fill_user_data(data_set)
        order_page.click_next()

        order_page.fill_rent_data(data_set)
        order_page.click_order()
        order_page.click_accept_order()

        assert order_page.is_order_created()

    @allure.feature("Фича_Создание заказа")
    @allure.story("Стори_Заказ через нижнюю кнопку")
    @allure.title("Оформление заказа нижнюю кнопку 'Заказать'")
    @pytest.mark.parametrize("data_set", BOTTOM_ORDER_DATA)
    def test_create_order_from_bottom_button(self, driver, data_set):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.accept_cookies()
        main_page.click_bottom_order_button()

        order_page.fill_user_data(data_set)
        order_page.click_next()

        order_page.fill_rent_data(data_set)
        order_page.click_order()
        order_page.click_accept_order()

        assert order_page.is_order_created()