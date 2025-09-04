import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def open_order_page(self, order_btn_locator):
        self.scroll_to_element(order_btn_locator)
        self.click_element(order_btn_locator)

    @allure.step("Заполнить форму 'Для кого самокат' и кликнуть на кнопку 'Далее'")
    def fill_in_user_details_section(self, personal_data: dict):
        self.input_text(OrderPageLocators.FIRST_NAME, personal_data["first_name"])
        self.input_text(OrderPageLocators.LAST_NAME, personal_data["last_name"])
        self.input_text(OrderPageLocators.ADDRESS, personal_data["address"])
        self.select_from_dropdown(
            OrderPageLocators.METRO_STATION,
            OrderPageLocators.METRO_STATION_LST,
            OrderPageLocators.dropdown_metro_option(personal_data["metro_station"]),
        )
        self.input_text(OrderPageLocators.PHONE_NUMBER, personal_data["phone_number"])

        self.click_element(OrderPageLocators.NEXT_BTN)

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_in_order_details_section(self, order_data: dict):
        self.click_element(OrderPageLocators.DATE_PICKER_FIELD)
        self.wait_for_element_is_visible(OrderPageLocators.DATE_PICKER)
        start_day = order_data["start_date"].day
        start_month = order_data["start_date"].month
        start_year = order_data["start_date"].year

        for _ in range(12):
            if (
                self.get_attribute_value(
                    OrderPageLocators.MONTH_IN_DATE_PICKER, "aria-label"
                )
                == f"month  {start_year}-{start_month:02}"
            ):
                break
            else:
                self.click_element(OrderPageLocators.NEXT_IN_DATE_PICKER)

        self.click_element(OrderPageLocators.start_rent_day(start_day))
        self.select_from_dropdown(
            OrderPageLocators.RENTAL_PERIOD,
            OrderPageLocators.RENTAL_PERIOD_LST,
            OrderPageLocators.dropdown_rental_option(order_data["rental_days"]),
        )
        if order_data["color"] is not None:
            self.click_element(OrderPageLocators.color_option(order_data["color"]))
        if order_data["comment"] is not None:
            self.input_text(OrderPageLocators.COMMENT, order_data["comment"])

    @allure.step("Кликнуть кнопку 'Заказать' на форме 'Про аренду'")
    def click_place_order_btn(self):
        self.click_element(OrderPageLocators.ORDER_BTN)

    @allure.step(
        "Подтвердить оформление заказа кликом на кнопку 'Да' в окне 'Хотите оформить заказ?'"
    )
    def submit_order(self):
        self.wait_for_element_is_visible(OrderPageLocators.ORDER_CONFIRMATION_MODAL)
        self.click_element(OrderPageLocators.SUBMIT_BTN)

    @allure.step("Получить сообщение о успешности оформления заказа")
    def get_message_about_order(self):
        self.wait_for_element_is_visible(OrderPageLocators.ORDER_CREATED_MODAL)
        return self.get_text_on_element(OrderPageLocators.ORDER_CREATED_MESSAGE)
