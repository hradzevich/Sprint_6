import allure
import pytest
from pages.order_page import OrderPage
from data import *
from helper import *
from urls import MAIN_URL
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    test_data = [
        (
            OrderPageLocators.HEADER_ORDER_BTN,
            generate_personal_data("Чистые пруды"),
            generate_order_data(),
        ),
        (
            OrderPageLocators.MAIN_ORDER_BTN,
            generate_personal_data("Лубянка"),
            generate_order_data(),
        ),
    ]

    @allure.title("Проверка успешного оформления заказа")
    @allure.description(
        "На главной старнице кликаем на кнопку 'Заказать', заполняем все поля валидными данными"
        "на форме 'Для кого самокат', кликаем на конпку 'Далее', заполняем валидными данными поля"
        "формы 'Про аренду', кликаем на кнопку 'Заказать', кликаем на кнопку 'Да' "
        "во всплывающем окне 'Хотите оформить заказ?' и проверяем, что появилось всплывающее окно"
        "с сообщением об успешном создании заказа."
    )
    @pytest.mark.parametrize("order_btn_locator, personal_data, order_data", test_data)
    def test_place_order_success(self, driver, order_btn_locator, personal_data, order_data):
        order_page = OrderPage(driver)
        order_page.open_page(MAIN_URL)
        order_page.open_order_page(order_btn_locator)
        order_page.fill_in_user_details_section(personal_data)
        order_page.fill_in_order_details_section(order_data)
        order_page.click_place_order_btn()
        order_page.click_submit_btn()
        actual_message = order_page.get_message_about_order()

        assert (
            ORDER_CREATED_SUCCESS_MESSAGE in actual_message
        ), f"Ожидалось сообщение об успешном создании заказа, но получили: '{actual_message}'"
