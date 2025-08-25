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

    # Открывает страницу по адресу, который хранится в переменной PAGE_URL
    def open_page(self):
        self.driver.get(self.PAGE_URL)

    # Ожидает, пока элемент не станет видимым на странице
    def wait_for_element_is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # Ожидает, пока элемент не станет кликабельным
    def wait_for_element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # Находит элемент и ожидает, пока он не станет видимым
    def get_element(self, locator):
        return self.wait_for_element_is_visible(locator)

    # Находит элемент и кликает по нему
    def click_element(self, locator):
        element = self.wait_for_element_is_clickable(locator)
        element.click()

    # Находит элемент и вводит текст в поле ввода
    def input_text(self, locator, text):
        element = self.wait_for_element_is_visible(locator)
        # element.clear()
        element.send_keys(text)

    # Прокручивает страницу до указанного элемента
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

