import allure
import pytest
from data import ORDER_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.epic("Эпик_Создание заказа")
@allure.parent_suite("Parent_suite_Создание заказа")
@allure.suite("Suite_Оформление заказа")
class TestOrderPage:

    @allure.feature("Создание заказа")
    @allure.story("Оформление заказа")
    @allure.title("Оформление заказа с разными данными")
    @allure.description("Проверка полного сценария оформления заказа")
    @pytest.mark.parametrize("data_set", ORDER_DATA)
    def test_create_order(self, driver, data_set):

        main_page = MainPage(driver)
        order_page = OrderPage(driver)

# Открываем главную страницу
        with allure.step('Открыть главную страницу'):
            main_page.open()

# Закрываем окно с cookies
        with allure.step("Закрыть окно cookies"):
            main_page.accept_cookies()

        with allure.step(f'Нажать кнопку "Заказать": '
                         f'{data_set["order_button"]}'):
            if data_set["order_button"] == "top":
                main_page.click_top_order_button()
            else:
                main_page.click_bottom_order_button()

        with allure.step('Заполнить этап "Для кого самокат"'):
            order_page.fill_user_data(data_set)
        with allure.step('Нажать "Далее"'):
            order_page.click_next()
        with allure.step('Заполнить этап "Про аренду"'):
            order_page.fill_rent_data(data_set)
        with allure.step('Нажать "Заказать"'):
            order_page.click_order()
        with allure.step('Подтвердить заказ кнопкой "Да"'):
            order_page.click_accept_order()
        with allure.step("Проверить  сообщение об успешном оформлении"):
            assert order_page.is_order_created(), ("Сообщение об успешном оформлении " "заказа не найдено")
        with allure.step("Проверить, что номер заказа получен"):
            order_number = order_page.get_order_number()
        with allure.step("Проверить наличие номера заказа"):
            assert order_number.isdigit(), "Номер заказа должен состоять из цифр"