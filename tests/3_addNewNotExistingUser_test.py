import random
import string
import logging as logger
import time
import pytest
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.adminPage import AdminPage
from utils import utils as utils
from pytest_html_reporter import attach

@pytest.mark.usefixtures("standard_test_setup_teardown")
@pytest.mark.tc3
class TestAdminPage:

    def test_addUser(self):  # PARAMETRIZE THIS TEST !!! 
        """Adding not existing user"""
        try:
            driver = self.driver  # defines the driver imported from conftest file
            adminpage = AdminPage(driver)
            time.sleep(3)
            adminpage.click_admin_button()

            # Fill new user form
            adminpage.click_addUser_button()
            adminpage.click_userRole_button()
            adminpage.enter_employeeName(utils.employeeNAME)
            adminpage.employeeName_not_found()
            username_field = driver.find_element(By.ID, "systemUser_userName")
            username_field.send_keys(utils.newUSERNAME)
            time.sleep(3)
            already_exists_error = driver.find_element(By.XPATH, "//*[@id='frmSystemUser']/fieldset/ol/li[3]/span")

            if already_exists_error.text == "Already exists" or "Should have at least 5 characters" or None:
                username_field.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
                name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                logger.info("Randomly generated username ===> : " + str(name))
                new_username = name
                username_field.send_keys(new_username)
                assert len(new_username) == 10

            adminpage.click_status_dropdown()
            adminpage.choose_disabled_option()
            adminpage.enter_password(utils.strongPASSWORD)
            adminpage.confirm_password(utils.strongPASSWORD)
            time.sleep(3)
            adminpage.click_save_button()
            time.sleep(1)
            adminpage.verify_saved_user()

            # Find newly created user
            adminpage.search_new_saved_user(new_username)
            adminpage.click_search_button()
            found_user = driver.find_element(By.LINK_TEXT, new_username)
            found_username_in_the_list = found_user.text
            assert found_username_in_the_list == name, f"New generated username returned wrong response. Username is: {name}"
            time.sleep(3)
            found_user.click()

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
            logger.info("In case if something mysterious happens => please check logs in CLI")
            attach(data=self.driver.get_screenshot_as_png())
