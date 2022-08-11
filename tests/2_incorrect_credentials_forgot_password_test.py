import logging as logger
import pytest
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from asserts.login_page_asserts import LoginAsserts
from pages.loginPage import LoginPage
from utils import utils as utils

@pytest.mark.usefixtures("login_test_setup")
@pytest.mark.tc2
class TestForgotPassword:

    def test_forgot_password_feature(self):
        """Sign in with empty credentials, see the incorrect credentials label, cancel and fill forgot password form"""
        try:
            driver = self.driver
            driver.get(utils.URL)
            login_page = LoginPage(driver)
            login_page_asserts = LoginAsserts(driver)

            # Check if panel header, logo image and 'forgot password' link are present
            login_page_asserts.panel_header_check()
            login_page_asserts.assert_login_page_contains_logo_image()
            login_page_asserts.assert_forgot_password_link_displayed()

            # Login with empty credentials, then with wrong credentials and check 'forgot password' form works
            login_page.sign_in_with_empty_or_incorrect_credentials()
            login_page.cancel_fill_forgot_password_form(utils.forgotPasswordTitle)
            login_page.fill_forgot_password_form(utils.employeeNAME)

        except (NoSuchElementException, AttributeError, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
