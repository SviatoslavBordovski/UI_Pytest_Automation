import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser Chrome or Firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        #driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        #driver = webdriver.Firefox(executable_path="/drivers/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path="/drivers/operadriver")
    else:
        print("Such desktop browser is not supported, please contact AQA Team to learn more about that issue")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test successfully passed")
