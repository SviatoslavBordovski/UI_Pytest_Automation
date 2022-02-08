import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import logging as logger

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser Chrome or Firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    global driver
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
#         ch = Service(ChromeDriverManager().install())  # does not work on ci, locally only
#         driver = webdriver.Chrome(service=ch)
        logger.info("Chrome tests run has started")
        # driver = webdriver.Chrome(executable_path=r"path_to_driver")
    elif browser == "firefox":
        ff = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=ff)
        logger.info("Firefox tests run has started")
        # driver = webdriver.Firefox(executable_path=r"path_to_driver")
    elif browser == "edge":
        ed = Service(EdgeChromiumDriverManager(log_level=20).install())
        driver = webdriver.Edge(service=ed)
        # driver = webdriver.Edge(executable_path=r"path_to_driver")
        logger.info("Edge tests run has started")
    # elif browser == "opera":
        # options = Options()
        # options.add_argument('allow-elevated-browser')
        # options.binary_location = "C:\\Users\\sbord_iu0ld13\\AppData\\Local\\Programs\\Opera\\opera.exe"
        # driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        # logger.info("Opera tests run has started")
        # driver = webdriver.Opera(executable_path="/home/sviatoslav/PytestFrameworkProject/drivers/operadriver")
    else:
        logger.info("Such browser is not supported, please contact QA Automation Team to learn more about the issue")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    logger.info("Test execution finished")
