# Этот файл содержит локаторы элементов страницы оформления заказа самоката.
# Используются в Page Object-классе OrderPage для взаимодействия с полями формы,
# кнопками и другими элементами при написании автотестов для сервиса «Яндекс.Самокат».
# Включают локаторы для ввода личной информации, адреса, даты аренды, выбора самоката и подтверждения заказа.

from selenium.webdriver.common.by import By


class OrderPageLocators:

    # Кнопка "Заказать" в верхней части страницы (header)
    HEADER_ORDER_BTN = (
        By.XPATH,
        ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']",
    )

    # Кнопка "Заказать" перед блоком "Вопросы о важном"
    MAIN_ORDER_BTN = (
        By.XPATH,
        ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']",
    )

    #  Поле "Имя" на форме "Для кого самокат"
    FIRST_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")

    #  Поле "Фамилия" на форме "Для кого самокат"
    LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")

    #  Поле "Адрес" на форме "Для кого самокат"
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")

    #  Поле с выпадающим списком "Станция метро" на форме "Для кого самокат"
    METRO_STATION = (By.CLASS_NAME, "select-search__value")

    #  Выпадающий список "Станция метро" на форме "Для кого самокат"
    METRO_STATION_LST = (By.XPATH, ".//ul[@class='select-search__options']")

    # Локатор опции в выпадающем списке "Станция метро" по значению
    @staticmethod
    def dropdown_metro_option(value_text):
        return (
            By.XPATH,
            f".//div[@class='select-search__select']//div[@class='Order_Text__2broi' and text()='{value_text}']",
        )

    #  Поле "Телефон" на форме "Для кого самокат"
    PHONE_NUMBER = (
        By.XPATH,
        ".//input[@placeholder='* Телефон: на него позвонит курьер']",
    )

    #  Кнопка "Далее" на форме "Для кого самокат"
    NEXT_BTN = (By.XPATH, ".//button[text()='Далее']")

    #  Поле с выпадающим календарем "Когда привезти самокат" на форме "Про аренду"
    DATE_PICKER_FIELD = (By.CLASS_NAME, "react-datepicker__input-container")

    #  Выпадающий календарь "Когда привезти самокат" на форме "Про аренду"
    DATE_PICKER = (By.CLASS_NAME, "react-datepicker__month-container")

    # Локатор даты начала аренды (день)
    @staticmethod
    def start_rent_day(day_value):
        return (
            By.XPATH,
            f"//div[contains(@class,'react-datepicker__day') and text()='{day_value}']",
        )

    # Отображаемый месяц в календаре "Когда привезти самокат"
    MONTH_IN_DATE_PICKER = (By.XPATH, ".//div[@class='react-datepicker__month']")

    NEXT_IN_DATE_PICKER = (By.XPATH, ".//button[@aria-label='Next Month']")

    #  Поле с выпадающим списком "Срок аренды" на форме "Про аренду"
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")

    #  Выпадающий список "Срок аренды" на форме "Про аренду"
    RENTAL_PERIOD_LST = (By.CLASS_NAME, "Dropdown-menu")

    # Локатор опции в выпадающем списке "Срок аренды" по значению
    @staticmethod
    def dropdown_rental_option(value_text):
        return (
            By.XPATH,
            f".//div[@class='Dropdown-option' and text()='{value_text}']",
        )

    # Локатор опции цвета самоката
    @staticmethod
    def color_option(id_value):
        return (
            By.ID,
            f"{id_value}",
        )

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
