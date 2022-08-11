import logging as logger
import pytest
from pages.adminPage import AdminPage
from tc_params import new_not_existing_user_params
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

@pytest.mark.usefixtures("standard_test_setup_teardown")
class TestAdminPage:

    tc_three_params = new_not_existing_user_params.third_tc_new_user_params()

    @pytest.mark.tc3
    @pytest.mark.parametrize("employee_name, new_password, confirm_password", tc_three_params)
    def test_addUser(self, employee_name, new_password, confirm_password):
        """Adding not existing user"""
        try:
            adminpage = AdminPage(self.driver)
            adminpage.add_new_user(employee_name, new_password, confirm_password)

        except (NoSuchElementException, AttributeError, StaleElementReferenceException) as e:
            logger.error("Locator issue, maybe it was not shown or found by driver")
            raise e

        else:
            logger.info("In case if something mysterious happens => please check logs in CLI")
