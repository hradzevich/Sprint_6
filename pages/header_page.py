import allure
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

    @allure.step("Найти раздел 'Новости' на главной странице Дзен")
    def find_news_section_dzen(self):
        return self.get_element(HeaderPageLocators.NEWS_SECTION_DZEN)
    
    @allure.step("Найти раздел 'Как это работает' на главной странице Самокат")
    def find_how_it_works_section(self):
        return self.get_element(HeaderPageLocators.HOW_IT_WORKS_SECTION_TITLE)
    

    

    