# Файл используется для хранения фикстур Pytest,
# которые применяются в автотестах сервиса «Яндекс.Самокат»
import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# Фикстура для запуска Firefox
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--width=1200")
    options.add_argument("--height=800")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
