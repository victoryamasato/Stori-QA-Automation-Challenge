from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope='class')
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser
@pytest.fixture(scope='class')
def init_driver(request, get_browser):
    driver = None
    print(get_browser)
    if get_browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield driver
    driver.quit()