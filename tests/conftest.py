import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver(request):
    # This is a fixture that is used to create a driver object.
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browser == "firefox":
        my_driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:
        raise TypeError(f"Browser {browser} is not supported")
    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    """
    "Add a command line option to pytest that allows us to specify the browser we want to use for our
    tests."
    :param parser: This is the parser object that holds all the command line options
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Type in browser name (chrome or firefox)",
    )
