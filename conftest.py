import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser Chrome or Firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="/home/sviatoslav-bordovski/PycharmProjects/PytestFrameworkProject/drivers/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="/home/sviatoslav-bordovski/PycharmProjects/PytestFrameworkProject/drivers/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path="/home/sviatoslav-bordovski/PycharmProjects/PytestFrameworkProject/drivers/operadriver")
    else:
        print("Such desktop browser is not supported, please contact AQA Team to learn more about that issue")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test successfully passed")
