import allure
import pytest


@allure.epic("Главная страница")
@allure.title("Проверка заголовка главной страницы")
@allure.description("Открываем главную страницу и проверяем, что заголовок соответствует ожидаемому")
@pytest.mark.ui
def test_open_main_page(browser, base_url):
    with allure.step("Открываем главную страницу"):
        browser.get(base_url)

    with allure.step("Проверяем заголовок страницы"):
        expected_title = "alifshop.uz - маркетплейс с возможностью покупки в рассрочку."
        actual_title = browser.title
        assert expected_title == actual_title, f"Ожидали заголовок '{expected_title}', но получили '{actual_title}'"
