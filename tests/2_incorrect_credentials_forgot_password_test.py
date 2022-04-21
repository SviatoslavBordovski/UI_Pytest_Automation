import logging as logger
import pytest
import selenium
from selenium.common.exceptions import NoSuchElementException
from asserts.login_page_asserts import LoginAsserts
from pages.loginPage import LoginPage
from utils import utils as utils
from pytest_html_reporter import attach

@pytest.mark.usefixtures("login_test_setup")
@pytest.mark.tc2
class TestForgotPassword:

    def test_forgot_password_feature(self):
        """Sign in to the CRM website"""
        try:
            driver = self.driver
            driver.get(utils.URL)
            login_page = LoginPage(driver)
            login_page_asserts = LoginAsserts(driver)

            # Check if panel header, logo image and 'forgot password' link are present
            login_page_asserts.panel_header_check()
            login_page_asserts.assert_login_page_contains_logo_image()
            login_page_asserts.assert_forgot_password_link_displayed()

            # Login with empty credentials, then login with wrong credentials and check if 'forgot password' form works
            login_page.sign_in_with_empty_or_incorrect_credentials()
            login_page.cancel_fill_forgot_password_form(utils.forgotPasswordTitle)
            login_page.fill_forgot_password_form(utils.employeeNAME)

        except AssertionError as error:
            logger.error("This test failed due to assertion error")
            print(error)
            attach(data=self.driver.get_screenshot_as_png())
            raise

        except AttributeError as error:
            logger.error("Locator issue")
            print(error)
            attach(data=self.driver.get_screenshot_as_png())
            raise

        except selenium.common.exceptions.NoSuchElementException as error:
            logger.error("Locator was not shown or found by driver")
            print(error)
            attach(data=self.driver.get_screenshot_as_png())
            raise

        else:
            logger.info("In case if something mysterious happens => please check logs in the CLI")
            attach(data=self.driver.get_screenshot_as_png())
