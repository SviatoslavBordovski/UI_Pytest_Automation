import time
import pytest
import selenium
import logging as logger
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from asserts.login_page_asserts import LoginAsserts
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils
from pytest_html_reporter import attach

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in CLI --browser=Chrome or Firefox")

@pytest.fixture(scope="class")
def login_test_setup(request):
    global driver
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        ch = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=ch, options=chrome_options)
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


@pytest.fixture(scope="class")
def standard_test_setup_teardown(request):
    global driver
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        ch = Service(ChromeDriverManager().install())
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=ch, options=chrome_options)
        logger.info("Chrome tests run has started")
        # driver = webdriver.Chrome(executable_path=r"path_to_driver")
    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options
        ff = Service(GeckoDriverManager().install())
        ff_options = Options()
        ff_options.add_argument('--headless')
        driver = webdriver.Firefox(service=ff, options=ff_options)
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
        
    else:
        logger.info("Such browser is not supported, please contact QA Automation Team to learn more about the issue")

    driver.get(utils.URL)
    logger.info("Requested website has been opened")
    actual_login_page_title = driver.title
    assert actual_login_page_title == 'OrangeHRM'

    login_page = LoginPage(driver)
    login_page.enter_username(utils.USERNAME)
    login_page.enter_password(utils.PASSWORD)
    login_page.click_login_button()
    logger.info("User logged in")

    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver

    yield

    try:
        homepage = HomePage(driver)
        login_page_asserts = LoginAsserts(driver)
        homepage.click_welcome_button()
        homepage.click_logout_button()
        time.sleep(3)
        login_page_asserts.panel_header_check()
        logger.info("User has logged out and was redirected to Login Page")

    except AttributeError as error:
        logger.error("Locator issue")
        print(error)
        attach(data=driver.get_screenshot_as_png())
        raise

    except selenium.common.exceptions.NoSuchElementException as error:
        logger.error("Locator was not shown or found by driver")
        print(error)
        attach(data=driver.get_screenshot_as_png())
        raise
   
    else:
        logger.info("Teardown point reached")
        attach(data=driver.get_screenshot_as_png())

    driver.close()
    driver.quit()
    logger.info("Test execution finished")
