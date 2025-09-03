import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Проскроллить до раздела 'Вопросы о важном'")
    def scroll_to_faq_section(self):
        self.wait_for_element_is_visible(MainPageLocators.FAQ_SECTION)
        self.scroll_to_element(MainPageLocators.FAQ_SECTION_TITLE)

    @allure.step("Раскрыть элемент выпадающего списка")
    def expand_accordion_item(self, index):
        self.scroll_to_element(MainPageLocators.question_number(index))
        self.click_element(MainPageLocators.question_number(index))

    @allure.step("Получить текст вопроса №{index} в разделе FAQ")
    def get_accordion_item_question(self, index):
        self.wait_for_element_is_visible(MainPageLocators.question_number(index))
        return self.get_text_on_element(MainPageLocators.question_number(index))

    @allure.step("Получить текст ответа на вопрос №{index} в разделе FAQ")
    def get_accordion_item_answer(self, index):
        self.wait_for_element_is_visible(MainPageLocators.answer_number(index))
        return self.get_text_on_element(MainPageLocators.answer_number(index))
