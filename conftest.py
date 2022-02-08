import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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
        from selenium.webdriver.chrome.options import Options
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        ch = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=ch, chrome_options=chrome_options)
        logger.info("Chrome tests run has started")
        # driver = webdriver.Chrome(executable_path=r"path_to_driver")
    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options
        ff = Service(GeckoDriverManager().install())
        ff_options = Options()
        ff_options.add_argument('--headless')
        driver = webdriver.Firefox(service=ff, options=ff_options)
        # driver = webdriver.Firefox(GeckoDriverManager().install(), options=ff_options)
        logger.info("Firefox tests run has started")
        # driver = webdriver.Firefox(executable_path=r"path_to_driver")
    elif browser == "edge":
        from selenium.webdriver.edge.options import Options
        ed = Service(EdgeChromiumDriverManager(log_level=20).install())
        edge_options = Options()
        edge_options.add_argument('--headless')
        driver = webdriver.Edge(service=ed, options=edge_options)
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
