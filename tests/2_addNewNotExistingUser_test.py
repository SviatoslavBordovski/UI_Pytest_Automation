import time
import pytest
from pages.loginPage import LoginPage
from pages.adminPage import AdminPage
from utils import utils as utils
#from selenium import webdriver
#from selenium.webdriver.support.ui import Select 

@pytest.mark.usefixtures("test_setup")
class TestAdminPage:

    def test_login(self):
        """Sign in to the Admin CRM"""
        driver = self.driver   #defines the driver imported from conftest file
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login_button()

    def test_addUser(self):
        """Adding new (not existing) user"""
        driver = self.driver  # defines the driver imported from conftest.py file
        #faker = Faker()
        adminpage = AdminPage(driver)
        adminpage.click_admin_button()
        adminpage.click_addUser_button()
        adminpage.click_userRole_button()
        adminpage.enter_employeeName(utils.employeeNAME)
        adminpage.employeeName_not_found()
        adminpage.enter_username(utils.newUSERNAME)
        adminpage.click_status_dropdown()
        adminpage.choose_disabled_option()
        adminpage.enter_password(utils.strongPASSWORD)
        adminpage.confirm_password(utils.strongPASSWORD)
        time.sleep(5)
        adminpage.click_save_button()
        adminpage.verify_saved_user()

    def test_search_created_user(self):
        """Finding newly added user"""
        driver = self.driver
        adminpage = AdminPage(driver)
        adminpage.search_new_saved_user(utils.newUSERNAME)
        adminpage.click_search_button()
        adminpage.verify_found_new_user()
        time.sleep(5)
