import allure
import pytest

from pages.cart_page import CardPage


@allure.epic("Корзина")
@allure.feature("Добавление товара в корзину")
@allure.description("Тест проверяет, что пользователь может добавить товар в корзину с главной страницы.")
@pytest.mark.ui
def test_add_to_card(browser, base_url):
    """
    Тестовый сценарий:
    1. Открыть главную страницу.
    2. Добавить товар в корзину.
    3. Проверить, что товар успешно появился в корзине.
    """
    with allure.step("Открываем главную страницу"):
        browser.get(base_url)
        page = CardPage(browser, base_url)

    with allure.step("Добавляем товар в корзину"):
        page.add_to_card()
