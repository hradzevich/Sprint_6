import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators
from data import *


class HeaderPage(BasePage):

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(HeaderPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекс")
    def click_yandex_logo(self):
        self.click_element(HeaderPageLocators.YANDEX_LOGO)

    

    