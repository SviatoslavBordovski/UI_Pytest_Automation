import logging as logger
import time
import pytest
import selenium
import utils.utils as utils
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.adminPage import AdminPage

@pytest.mark.usefixtures("standard_test_setup_teardown")
@pytest.mark.tc3
@pytest.mark.regression
class TestAdminPage:

    def test_addUser(self):  # PARAMETRIZE THIS TEST !!!
        """Adding not existing user"""
        try:
            adminpage = AdminPage(self.driver)
            adminpage.add_new_user(utils.employeeNAME)

        except AttributeError as error:  # refactor exceptions https://youtu.be/KX5miQRROJU
            logger.error("Locator issue")
            raise error

        except selenium.common.exceptions.NoSuchElementException as error:
            logger.error("Locator was not shown or found by driver")
            raise error

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
