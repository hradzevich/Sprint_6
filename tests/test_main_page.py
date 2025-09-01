import allure
import pytest
from pages.main_page import MainPage
from helper import faq_section_data_pytest
from urls import MAIN_URL


class TestMainPage:
    @allure.title(
        "Проверка соответствия текста ответа вопросу в выпадающем списке 'Вопросы о важном'"
    )
    @allure.description(
        "На странице ищем вопрос по его индексу, кликаем на стрелочку, получаем текст ответа "
        "и проверяем его соответствие вопросу"
    )
    @pytest.mark.parametrize(
        "index, expected_question, expected_answer", faq_section_data_pytest
    )
    def test_faq_questions_answers_match(
        self, driver, index, expected_question, expected_answer
    ):
        main_page = MainPage(driver)
        main_page.open_page(MAIN_URL)
        main_page.scroll_to_faq_section()
        main_page.expand_accordion_item(index)
        actual_question = main_page.get_accordion_item_question(index)
        actual_answer = main_page.get_accordion_item_answer(index)

        assert (
            actual_question == expected_question
        ), f"Фактический вопрос: {actual_question}"
        assert actual_answer == expected_answer, f"Фактический ответ: {actual_answer}"
