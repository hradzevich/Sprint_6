# Файл используется для хранения фикстур Pytest,
# которые применяются в автотестах сервиса «Яндекс.Самокат»
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


# Фикстура для запуска Firefox
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--width=1200")
    options.add_argument("--height=800")
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()