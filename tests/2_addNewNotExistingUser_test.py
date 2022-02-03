import random
import string
import logging as logger
import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.loginPage import LoginPage
from pages.adminPage import AdminPage
from utils import utils as utils
#from faker import Faker
#import moment
#from selenium import webdriver
#from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("test_setup")
@pytest.mark.tc2
class TestAdminPage:

    def test_login(self):
        """Sign in to the website"""
        driver = self.driver   #defines the driver imported from conftest file
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login_button()

    def test_addUser(self):
        """Adding not existing user"""
        driver = self.driver  # defines the driver imported from conftest file
        #faker = Faker()
        adminpage = AdminPage(driver)
        adminpage.click_admin_button()

        # Fill form
        adminpage.click_addUser_button()
        adminpage.click_userRole_button()
        adminpage.enter_employeeName(utils.employeeNAME)
        adminpage.employeeName_not_found()
        username_field = driver.find_element(By.ID, "systemUser_userName")
        username_field.send_keys(utils.newUSERNAME)
        time.sleep(3)
        already_exists_error = driver.find_element(By.XPATH, "//*[@id='frmSystemUser']/fieldset/ol/li[3]/span")

        # Check if such username exists and which error is shown
        if already_exists_error.text == "Already exists" or "Should have at least 5 characters" or None:
            username_field.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
            name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            logger.info("Randomly generated username ===> : " + str(name))
            new_username = name
            username_field.send_keys(new_username)

        adminpage.click_status_dropdown()
        adminpage.choose_disabled_option()
        adminpage.enter_password(utils.strongPASSWORD)
        adminpage.confirm_password(utils.strongPASSWORD)
        time.sleep(3)
        adminpage.click_save_button()
        time.sleep(1)
        adminpage.verify_saved_user()

        # Find newly created user and click on the profile of found user (link to profile is shown)
        adminpage.search_new_saved_user(new_username)
        adminpage.click_search_button()
        found_user = driver.find_element(By.LINK_TEXT, new_username)
        found_username_in_the_list = found_user.text
        assert found_username_in_the_list == name, f"New generated username returned wrong response. Username is: {name}"
        time.sleep(3)
        found_user.click()
