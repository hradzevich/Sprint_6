# Этот файл содержит базовый класс для работы с веб-страницами при помощи Selenium.
# Класс BasePage предоставляет основные функции для взаимодействия с элементами на странице,
# такие как открытие страницы, ожидание видимости или кликабельности элементов, ввод текста,
# прокрутка страницы и другие действия, которые могут быть использованы в тестах для сервиса «Яндекс.Самокат».
import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    # Инициализация страницы, создание объекта ожидания
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу")
    def open_page(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

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
