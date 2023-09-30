from pathlib import Path
import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv
from selene import browser
from selenium.webdriver.chrome.options import Options

from utils import attach


DEFAULT_BROWSER_VERSION = "100.0"


def path(file_name):
    import test
    return str(Path(test.__file__).parent.joinpath(f'picture/{file_name}').absolute())


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--browser_version', action='store', default="99.0")


@pytest.fixture(scope='function', autouse=True)
def open_browser(request):
    browser_name = request.config.getoption('browser_name')
    browser_version = request.config.getoption('browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": f"{browser_name}",
        "browserVersion": f"{browser_version}",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )
    browser.config.driver = driver
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    if browser_name == 'chrome':
        attach.add_logs(browser)
    browser.quit()
