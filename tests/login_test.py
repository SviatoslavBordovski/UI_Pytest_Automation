import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        """Sign in to the website"""
        driver = self.driver   #defines the driver imported from conftest file
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
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("It is finally block")