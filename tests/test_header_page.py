import allure
from pages.header_page import HeaderPage
from urls import MAIN_URL, DZEN_URL, ORDER_URL


@allure.parent_suite("UI тесты Яндекс.Самокат")
@allure.suite("Header")
@allure.sub_suite("Редиректы при нажатии на логотип")
class TestHeaderPage:
    @allure.title(
        "Проверка редиректа на главную страницу Дзена в новой вкладке при нажатии на логотип Яндекса."
    )
    @allure.description(
        "На странице ищем логотип Яндекс, кликаем на него, переходим в новую вкладку "
        "и проверяем, что URL соответствует главной странице Дзен"
    )
    def test_redirect_to_dzen_via_yandex_logo(self, driver):
        header_page = HeaderPage(driver)
        header_page.open_page(MAIN_URL)
        header_page.click_yandex_logo()
        header_page.switch_tab()
        header_page.wait_for_url(DZEN_URL)
        current_url = header_page.get_current_url()
        news_dzen_section = header_page.find_news_section_dzen()

        assert current_url.startswith(
            DZEN_URL
        ), f"Фактический URL страницы: {current_url}"
        assert (
            news_dzen_section.is_displayed()
        ), "На текущей странице нет раздела 'Новости'"

    @allure.title(
        "Проверка редиректа со страницы заказа на главную страницу Самокат при нажатии на логотип Самоката."
    )
    @allure.description(
        "На странице заказа ищем логотип Самокат, кликаем на него и проверяем, "
        "что URL соответствует главной странице Самоката"
    )
    def test_redirect_to_main_via_scooter_logo(self, driver):
        header_page = HeaderPage(driver)
        header_page.open_page(ORDER_URL)
        header_page.click_scooter_logo()
        header_page.wait_for_url(MAIN_URL)
        current_url = header_page.get_current_url()
        how_it_works_section_title = header_page.find_how_it_works_section()

        assert current_url == MAIN_URL, f"Фактический URL страницы: {current_url}"
        assert (
            how_it_works_section_title.is_displayed()
        ), "Раздел 'Как это работает' не отображается на странице"
