import pytest
import allure

from pages.main_page import MainPage


@allure.epic("Ивенты")
@allure.title("Проверка перехода на страницы ивентов")
@allure.description("""
Тест проверяет переход на страницы ивентов с главной страницы.
Осуществляется переход по первым 3 ивентам, чтобы убедиться в корректной навигации.
""")
@pytest.mark.ui
@pytest.mark.parametrize("facet_index", [1])
def test_open_events(browser, base_url, facet_index):
    with allure.step("Открываем главную страницу"):
        browser.get(base_url)
        driver = browser

    # Переход на страницу ивента
    page = MainPage(driver, base_url)
    page.open_events_page(facet_index)


