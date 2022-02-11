import time
import pytest
import selenium
from selenium.common.exceptions import NoSuchElementException
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import logging as logger
from pytest_html_reporter import attach
# import allure
# import moment

@pytest.mark.usefixtures("login_test_setup")
@pytest.mark.tc1
class TestLoginLogout:
    @pytest.mark.parametrize("username, password",
                             [
                                 ("Admin", "admin123"),
                                 pytest.param("random_username", "admin123",
                                              marks=pytest.mark.xfail(reason="Non-existing username entered")),
                                 pytest.param("Admin", "qwerty123!",
                                              marks=pytest.mark.xfail(reason="Incorrect password entered")),
                                 pytest.param("qwertyADMIN", "qwertyADMIN",
                                              marks=pytest.mark.xfail(reason="Wrong credentials")),
                                 pytest.param("", "admin123",
                                              marks=pytest.mark.xfail(reason="Empty username")),
                                 pytest.param("Admin", "",
                                              marks=pytest.mark.xfail(reason="Empty password")),
                                 pytest.param("", "",
                                              marks=pytest.mark.xfail(reason="Empty credentials"))
                             ]
                             )
    def test_login(self, username, password):
        """Sign in to the website"""
        driver = self.driver   #defines the driver imported from conftest file
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.panel_header_check()
        login.enter_username(username)
        login.enter_password(password)
        login.click_login_button()

    def test_logout(self):
        """Sign out from the website"""
        global driver
        try:
            driver = self.driver  # defines the driver imported from conftest file
            homepage = HomePage(driver)
            login = LoginPage(driver)

            time.sleep(3)
            homepage.check_dashboard_visibility()
            homepage.click_welcome_button()
            homepage.click_logout_button()
            time.sleep(3)
            login.panel_header_check()

        except AssertionError as error:
            logger.error("This test should be failed due to assertion error")
            print(error)
            attach(data=self.driver.get_screenshot_as_png())
            # currentTime = moment.now().strftime("_%d-%m-%Y_%H-%M-%S")  #moment library starts magic here :)
            # testName = utils.whoami()  #declaring the function which gives name of test function that fails
            # screenshotName = testName + currentTime  #make screenshot name with that function
            # allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
            #               attachment_type=allure.attachment_type.PNG)
            # driver.get_screenshot_as_file("/home/sviatoslav/PytestFrameworkProject/screenshots/" + screenshotName + ".png")
            raise

        except selenium.common.exceptions.NoSuchElementException as error:
            logger.error("Logout button was not found but test has been passed because it is allowed to fail")
            print(error)
            attach(data=self.driver.get_screenshot_as_png())
            # currentTime = moment.now().strftime("_%d-%m-%Y_%H-%M-%S")  # moment library starts magic here :)
            # testName = utils.whoami()
            # screenshotName = testName + currentTime
            # allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
            #               attachment_type=allure.attachment_type.PNG)
            # driver.get_screenshot_as_file("/home/sviatoslav/PytestFrameworkProject/screenshots/" + screenshotName + ".png")
            raise
            
        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
            attach(data=self.driver.get_screenshot_as_png())
