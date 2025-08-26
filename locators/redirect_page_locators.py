# Этот файл содержит локаторы для элементов,
# с которыми происходит взаимодействие при редиректе


from selenium.webdriver.common.by import By


class   RedirectPageLocators:
    
    # Логотип Яндекс 
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

    # Логотип "Самоката"
    SAMOKAT_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
