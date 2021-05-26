import allure
import pytest
import moment
import selenium
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLoginLogout:

    def test_login(self):
        """Sign in to the website"""
        driver = self.driver   #defines the driver imported from conftest.py file
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login_button()

    def test_logout(self):
        """Sign out from the website"""
        try:
            driver = self.driver  # defines the driver imported from conftest file
            homepage = HomePage(driver)
            homepage.click_welcome_button()
            homepage.click_logout_button()
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("This test should be failed due to assertion error")
            print(error)
            currentTime = moment.now().strftime("_%d-%m-%Y_%H-%M-%S")  #moment library starts magic here :)
            testName = utils.whoami()  #declaring the function which gives name of test function that fails
            screenshotName = testName + currentTime  #make screenshot name with that function
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/home/sviatoslav-bordovski/PycharmProjects/PytestFrameworkProject/screenshots/" + screenshotName + ".png")
            raise

        except selenium.common.exceptions.NoSuchElementException as error:
            print("Logout button was not found but test has been passed because it is allowed to fail")
            print(error)
            currentTime = moment.now().strftime("_%d-%m-%Y_%H-%M-%S")  #moment library starts magic here :)
            testName = utils.whoami()
            screenshotName = testName + currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/home/sviatoslav-bordovski/PycharmProjects/PytestFrameworkProject/screenshots/" + screenshotName + ".png")
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("It is finally block")
