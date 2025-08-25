import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OrderPage(BasePage):

    PAGE_URL = "https://qa-scooter.praktikum-services.ru/order"

    def fill_in_user_details(self):
        pass
        