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
        """Sign in to the website"""
        try:
            driver = self.driver
            driver.get(utils.URL)
            login_page = LoginPage(driver)
            login_page_asserts = LoginAsserts(driver)

            # Check if panel header, logo image and 'forgot password' link are present
            login_page.panel_header_check()
            login_page_asserts.assert_login_page_contains_logo_image()
            login_page_asserts.assert_forgot_password_link_displayed()

            # Fill credentials
            login_page.enter_username("username")
            login_page.enter_password("password")
            login_page.click_login_button()

            # Check changed url
            current_url = driver.current_url
            assert current_url == utils.expectedInvalidCredentialsUrl

            if login_page.shown_invalid_credentials_flag():
                login_page.click_forgot_password_link()
            else:
                logger.error("Invalid credentials flag is not visible")

        except AssertionError as error:
            logger.error("This test failed due to assertion error")
            print(error)
            attach(data=self.driver.get_screenshot_as_png())
            raise

        except selenium.common.exceptions.NoSuchElementException as error:
            logger.error("Logout button was not found but test has been passed because it is allowed to fail")
            print(error)
            attach(data=self.driver.get_screenshot_as_png())
            raise

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
            attach(data=self.driver.get_screenshot_as_png())
