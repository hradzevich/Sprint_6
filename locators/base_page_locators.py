# Этот файл содержит локаторы, которые используются на базовой странице 
# для взаимодействия с элементами, общими для всех страниц веб-приложения.

from selenium.webdriver.common.by import By


class BasePageLocators:

    # Логотип Яндекс 
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Логотип "Самоката"
    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    # Кнопка "Заказать" в верхней части страницы (header)
    UP_ORDER_BTN = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")

    # Кнопка "Заказать" перед блоком FAQ
    DOWN_ORDER_BTN = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")
