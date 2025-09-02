# Этот файл содержит локаторы для элементов,
# с которыми происходит взаимодействие при редиректе

from selenium.webdriver.common.by import By


class HeaderPageLocators:

    # Логотип Яндекс
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Логотип "Самоката"
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

    # Раздел "Новости" на главной странице Дзен
    NEWS_SECTION_DZEN = (By.XPATH, ".//div[text()='Новости']")

    # Заголовок раздела "Как это работает" на главной странице
    HOW_IT_WORKS_SECTION_TITLE = (
        By.XPATH,
        ".//div[@class='Home_SubHeader__zwi_E' and text()='Как это работает']",
    )
