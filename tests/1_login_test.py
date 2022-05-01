import time
import pytest
import selenium
from selenium.common.exceptions import NoSuchElementException
from asserts.login_page_asserts import LoginAsserts
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
from tc_params import login_params
import logging as logger

@pytest.mark.usefixtures("login_test_setup")
@pytest.mark.tc1
class TestLoginLogout:

    @pytest.mark.parametrize("username, password", login_params.first_tc_login_params())
    def test_login(self, username, password):
        """Sign in to the website"""
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        homepage = HomePage(driver)
        login_page_asserts = LoginAsserts(driver)

        time.sleep(3)
        login_page_asserts.panel_header_check()
        login_page_asserts.assert_login_page_contains_logo_image()
        login_page_asserts.assert_forgot_password_link_displayed()

        login.login_crm_system(username, password)
        login.click_login_button()
        homepage.check_dashboard_visibility()

    def test_logout(self):
        """Sign out from the website"""
        global driver
        try:
            driver = self.driver  # defines the driver imported from conftest.py file
            homepage = HomePage(driver)
            login_page_asserts = LoginAsserts(driver)

            homepage.click_welcome_button()
            homepage.click_logout_button()
            time.sleep(3)
            login_page_asserts.assert_login_page_contains_logo_image()
            login_page_asserts.assert_forgot_password_link_displayed()

        except AttributeError as error:  # refactor exceptions https://youtu.be/KX5miQRROJU
            logger.error("Locator issue")
            raise error

        except selenium.common.exceptions.NoSuchElementException as error:
            logger.error("Locator was not shown or found by driver")
            raise error

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
