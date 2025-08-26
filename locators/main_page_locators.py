# Этот файл содержит локаторы, которые используются
# для взаимодействия с элементами на главной странице  веб-приложения.

from selenium.webdriver.common.by import By


class MainPageLocators:

    # Заголовок раздела «Вопросы о важном»
    FAQ_SECTION_TITLE = (
        By.XPATH,
        ".//div[@class='Home_SubHeader__zwi_E' and text()='Вопросы о важном']",
    )

    # Pаздел «Вопросы о важном»
    FAQ_SECTION = (By.CLASS_NAME, "accordion")

    # Локатор заголовка вопроса в выпадающем списке по индексу
    @staticmethod
    def question_number(index):
        return (
            By.XPATH,
            f".//div[@data-accordion-component='AccordionItemHeading']//div[@id='accordion__heading-{index}']",
        )

    # Локатор заголовка ответа в выпадающем списке по индексу
    @staticmethod
    def answer_number(index):
        return (
            By.XPATH,
            f".//div[@data-accordion-component='AccordionItemPanel' and @id='accordion__panel-{index}']/p",
        )
    
    # Кнопка "Заказать" в верхней части страницы (header)
    UP_ORDER_BTN = (
        By.XPATH,
        ".//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']",
    )

    # Кнопка "Заказать" перед блоком FAQ
    DOWN_ORDER_BTN = (
        By.XPATH,
        ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']",
    )
