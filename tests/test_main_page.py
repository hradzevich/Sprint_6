import allure
import pytest
from pages.main_page import MainPage
from data import *


class TestMainPage:
    @allure.title(
        "Проверка соответствия текста ответа вопросу в выпадающем списке 'Вопросы о важном'"
    )
    @allure.description(
        "На странице ищем вопрос по его индексу, кликаем на стрелочку, получаем текст ответа и проверяем его соответствие вопросу"
    )
    @pytest.mark.parametrize("index, expected_question, expected_answer", faq_section_data_pytest)
    def test_faq_questions_answers_match(self, driver, index, expected_question, expected_answer):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.scroll_to_faq_section()
        main_page.expand_accordion_item(index)

        assert main_page.get_accordion_item_question(index) == expected_question
        assert main_page.get_accordion_item_answer(index) == expected_answer
