# Этот файл содержит локаторы элементов страницы оформления заказа самоката.
# Используются в Page Object-классе OrderPage для взаимодействия с полями формы,
# кнопками и другими элементами при написании автотестов для сервиса «Яндекс.Самокат».
# Включают локаторы для ввода личной информации, адреса, даты аренды, выбора самоката и подтверждения заказа.

from selenium.webdriver.common.by import By


class OrderPageLocators:

    #  Поле "Имя" на форме "Для кого самокат"
    FIRST_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")

    #  Поле "Фамилия" на форме "Для кого самокат"
    SECOND_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")

    #  Поле "Адрес" на форме "Для кого самокат"
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")

    #  Выпадающий список с автозаполнением "Станция метро" на форме "Для кого самокат"
    METRO_STATION = (By.CLASS_NAME, "select-search__value")

    #  Поле "Телефон" на форме "Для кого самокат"
    PHONE_NUMBER = (
        By.XPATH,
        ".//input[@placeholder='* Телефон: на него позвонит курьер']",
    )

    #  Кнопка "Далее" на форме "Для кого самокат"
    PHONE_NUMBER = (By.XPATH, ".//button[text()='Далее']")

    #  Выпадающий календарь "Когда привезти самокат" на форме "Про аренду"
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker__input-container")

    #  Выпадающий список "Срок аренды" на форме "Про аренду"
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")

    #  Чексбокс "Черный жемчуг" для выбора цвета самоката на форме "Про аренду"
    BLACK_COLOR_CHOICE = (By.ID, "black")

    #  Чексбокс "Серая безысходность" для выбора цвета самоката на форме "Про аренду"
    GREY_COLOR_CHOICE = (By.ID, "grey")

    #  Поле "Комментарий для курьера" на форме "Про аренду"
    COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    #  Кнопка "Заказать" на форме "Про аренду"
    ORDER_BTN = (
        By.XPATH,
        ".//button[text()='Заказать' and contains(@class, 'Button_Middle__1CSJM')]",
    )
    
    # Всплывающее окно "Хотите оформить заказ?"
    ORDER_CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")

    #  Кнопка "Да" во всплывающем окне "Хотите оформить заказ?"
    SUBMIT_BTN = (
        By.XPATH,
        ".//button[text()='Да']",
    )

    # Всплывающее окно с сообщением об успешном создании заказа
    ORDER_CREATED_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")

    # Сообщение об успешном создании заказа
    ORDER_CREATED_MESSAGE = (By.XPATH, ".//div[text()='Заказ оформлен']")
