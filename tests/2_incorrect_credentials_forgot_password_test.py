import logging as logger
import pytest
import selenium
from selenium.common.exceptions import NoSuchElementException
from asserts.login_page_asserts import LoginAsserts
from pages.loginPage import LoginPage
from utils import utils as utils

@pytest.mark.usefixtures("login_test_setup")
@pytest.mark.tc2
@pytest.mark.regression
class TestForgotPassword:

    def test_forgot_password_feature(self):
        """Sign in to the website"""
        try:
            driver = self.driver
            driver.get(utils.URL)
            login_page = LoginPage(driver)
            login_page_asserts = LoginAsserts(driver)

            # Check if panel header, logo image and 'forgot password' link are present
            login_page_asserts.panel_header_check()
            login_page_asserts.assert_login_page_contains_logo_image()
            login_page_asserts.assert_forgot_password_link_displayed()

            # Login with empty credentials, then login with wrong credentials and check 'forgot password' form works
            login_page.sign_in_with_empty_or_incorrect_credentials()
            login_page.cancel_fill_forgot_password_form(utils.forgotPasswordTitle)
            login_page.fill_forgot_password_form(utils.employeeNAME)

        except AttributeError as error:  # refactor exceptions https://youtu.be/KX5miQRROJU
            logger.error("Locator issue")
            raise error

        except selenium.common.exceptions.NoSuchElementException as error:
            logger.error("Locator was not shown or found by driver")
            raise error

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
