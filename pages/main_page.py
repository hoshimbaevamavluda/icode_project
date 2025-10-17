import time
import allure

from selenium.webdriver.common.by import By

from api.api import Api
from pages.base_page import BasePage


class MainPage(BasePage):

    def open_events_page(self, facet_index):
        item_block = f'facet_{facet_index}'
        button_see_all = f"facet_{facet_index}_all"

        with (allure.step(f"Переход на страницу ивента {item_block}")):
            self.click(value=button_see_all, by=By.ID)
            time.sleep(3)

        with allure.step("Проверяем заголовок страницы"):
            url = f"https://gw.alifshop.uz/web/client/events/active"
            page = Api()
            response_data = page.fetch_data(url)
            api_title = response_data[facet_index-1]["titles"]["ru"]

            actual_title = self.get_text(
                By.XPATH,
                '//h1[@class="text-2xl md:text-3xl font-medium text-grey-900 mb-4 md:mb-8"]')

            assert api_title == actual_title, f"Ожидали заголовок '{api_title}', но получили '{actual_title}'"


