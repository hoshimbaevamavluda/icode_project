from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url or ""

    @allure.step("Открываем страницу: {url}")
    def open(self, url=""):
        full_url = self.base_url + url
        self.driver.get(full_url)

    @allure.step("Находим элемент: {by}={value}")
    def find_element(self, by, value, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value)),
            message=f"Не найден элемент по {by}={value}"
        )

    @allure.step("Кликаем по элементу: {by}={value}")
    def click(self, by, value, timeout=5, wait_type=None, scroll_into_view=True):
        """
        Кликает по элементу с ожиданием и обработкой возможных ошибок.

        :param by: Метод поиска (например, By.ID, By.XPATH)
        :param value: Значение локатора
        :param timeout: Таймаут ожидания (в секундах)
        :param wait_type: Тип ожидания: 'element_presence' или 'clickable'
        :param scroll_into_view: Скроллить ли до элемента при ошибке
        """
        if by is None:
            by = By.ID

        # Определяем тип ожидания
        if wait_type == 'element_presence':
            wait_condition = EC.presence_of_element_located
        else:
            wait_condition = EC.element_to_be_clickable

        try:
            element = WebDriverWait(self.driver, timeout).until(
                wait_condition((by, value)),
                message=f"Элемент не найден или не кликабелен: {by}={value}"
            )
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name=f"TimeoutException: {value}",
                attachment_type=allure.attachment_type.PNG
            )
            raise ValueError(f"Элемент '{value}' не найден или не кликабелен за {timeout} секунд.")

        # Попытка кликнуть
        try:
            element.click()
        except WebDriverException:
            try:
                if scroll_into_view:
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                element.click()
            except WebDriverException:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).click().perform()

    @allure.step("Вводим текст '{text}' в элемент: {by}={value}")
    def send_keys(self, by, value, text, timeout=5):
        element = self.find_element(by, value, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step("Получаем текст из элемента: {by}={value}")
    def get_text(self, by, value, timeout=5):
        element = self.find_element(by, value, timeout)
        return element.text

    @allure.step("Проверяем, что элемент отображается: {by}={value}")
    def is_visible(self, by, value, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except:
            return False

