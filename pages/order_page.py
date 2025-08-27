import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data import *


class OrderPage(BasePage):

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def open_order_page(self, order_btn_locator):
        self.scroll_to_element(order_btn_locator)
        self.click_element(order_btn_locator)

    @allure.step("Заполнить форму 'Для кого самокат'")
    def fill_in_user_details_section(self, personal_data: dict):
        self.input_text(OrderPageLocators.FIRST_NAME, personal_data["first_name"])
        self.input_text(OrderPageLocators.LAST_NAME, personal_data["last_name"])
        self.input_text(OrderPageLocators.ADDRESS, personal_data["address"])
        self.select_from_dropdown(
            OrderPageLocators.METRO_STATION,
            OrderPageLocators.METRO_STATION_LST,
            personal_data["metro_station"],
        )
        self.input_text(OrderPageLocators.PHONE_NUMBER, personal_data["phone_number"])
        self.click_element(OrderPageLocators.NEXT_BTN)

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_in_order_details_section(self, order_data: dict):
        self.input_text(OrderPageLocators.START_DATE, order_data["start_date"])
