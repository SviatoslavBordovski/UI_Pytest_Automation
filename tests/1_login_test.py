import time
import pytest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from asserts.login_page_asserts import LoginAsserts
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
from tc_params import login_params
import logging as logger

@pytest.mark.usefixtures("login_test_setup")
class TestLoginLogout:

    tc_one_params = login_params.first_tc_login_params()

    @pytest.mark.tc1
    @pytest.mark.parametrize("username, password", tc_one_params)
    def test_login(self, username, password):
        """Sign in to the website"""

        try:
            driver = self.driver
            driver.get(utils.URL)
            login = LoginPage(driver)
            homepage = HomePage(driver)
            login_page_asserts = LoginAsserts(driver)

            # Check elements are shown
            time.sleep(3)
            login_page_asserts.panel_header_check()
            login_page_asserts.assert_login_page_contains_logo_image()
            login_page_asserts.assert_forgot_password_link_displayed()

            # Sign in and check if user was successfully signed in
            login.login_crm_system(username, password)
            login.click_login_button()
            homepage.check_dashboard_visibility()

            # Sign out and check user was signed out
            homepage.click_welcome_button()
            homepage.click_logout_button()
            time.sleep(3)
            login_page_asserts.assert_login_page_contains_logo_image()
            login_page_asserts.assert_forgot_password_link_displayed()

        except (NoSuchElementException, AttributeError, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
