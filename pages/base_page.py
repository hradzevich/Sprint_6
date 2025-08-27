# Этот файл содержит базовый класс для работы с веб-страницами при помощи Selenium.
# Класс BasePage предоставляет основные функции для взаимодействия с элементами на странице,
# такие как открытие страницы, ожидание видимости или кликабельности элементов, ввод текста,
# прокрутка страницы и другие действия, которые могут быть использованы в тестах для сервиса «Яндекс.Самокат».
import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

class BasePage:

    # Инициализация страницы, создание объекта ожидания
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Подождать видимости элемента")
    def wait_for_element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать кликабельности элемента")
    def wait_for_element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Найти элемент")
    def get_element(self, locator):
        return self.wait_for_element_is_visible(locator)

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        element = self.wait_for_element_is_clickable(locator)
        element.click()

    @allure.step("Ввести данные")
    def input_text(self, locator, text):
        element = self.wait_for_element_is_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator):
        element = self.wait_for_element_is_visible(locator)
        return element.text

    @allure.step("Проскроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.wait_for_element_is_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переключиться на новую вкладку")
    def switch_tab(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    @allure.step("Подождать загрузки страницы")
    def wait_for_url(self, url):
        return self.wait.until(EC.url_contains(url))

    @allure.step("Получить url текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

    # Локатор опции в выпадающем списке по значению
    @staticmethod
    def dropdown_option(value_text):
        return (
            By.XPATH,
            f".//*[contains(text(), '{value_text}')]",
        )

    @allure.step("Выбрать значение из выпадающего списка")
    def select_from_dropdown(self, field_locator, list_locator, value_text):
        self.click_element(field_locator)
        self.wait_for_element_is_visible(list_locator)
        value_locator = self.dropdown_option(value_text)
        self.wait_for_element_is_visible(value_locator)
        self.scroll_to_element(value_locator)
        self.click_element(value_locator)
