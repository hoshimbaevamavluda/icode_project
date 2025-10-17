import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# 1. Фикстура base_url
@pytest.fixture(scope="session")
def base_url():
    return "https://alifshop.uz/ru"


# 2. Фикстура браузера (Chrome)
@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()

    # Настройка разрешений для геолокации
    prefs = {
        "profile.default_content_setting_values.geolocation": 2  # 1 = разрешить, 2 = запретить
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Дополнительные опции
    # chrome_options.add_argument("--headless")  # Можно убрать, если хочешь видеть браузер
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


# 3. Хук для создания Allure-отчета (запускать отдельно через CLI)
def pytest_sessionfinish(session, exitstatus):
    print("\nТесты завершены. Для создания отчета выполните:")
    print("allure serve allure-results")
