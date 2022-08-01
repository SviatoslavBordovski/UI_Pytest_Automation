import time
import random
import string
import utils.utils as utils
import logging as logger
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from locators.admin_page_locators import AdminPageLocators

AP_LOCATORS = AdminPageLocators()

class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def click_admin_button(self):
        self.driver.find_element(By.ID, AP_LOCATORS.view_users_button_id).click()

    def click_addUser_button(self):
        self.driver.find_element(By.ID, AP_LOCATORS.add_user_button_id).click()

    def click_userRole_button(self):
        self.driver.find_element(By.ID, AP_LOCATORS.userRole_dropdown_id).click()

    def choose_admin_option(self):
        self.driver.find_element(By.NAME, AP_LOCATORS.userRole_option_name_admin).click()

    def enter_employeeName(self, emp_name):
        self.driver.find_element(By.ID, AP_LOCATORS.employeeName_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, AP_LOCATORS.employeeName_textbox_id).send_keys(emp_name)

    def employeeName_not_found(self):
        self.driver.find_element(By.CSS_SELECTOR, AP_LOCATORS.error_notFoundEmployee_validation_error).is_displayed()

    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, AP_LOCATORS.new_username_textbox_id)
        username_field.send_keys(username)

    def choose_disabled_option(self):
        time.sleep(3)
        self.driver.find_element(By.ID, AP_LOCATORS.userStatus_dropdown_id).click()
        status_select = Select(self.driver.find_element(By.NAME, AP_LOCATORS.userStatus_option_disabled))
        status_select.select_by_value("0")

    def enter_password(self, new_password):
        self.driver.find_element(By.ID, AP_LOCATORS.new_user_password_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, AP_LOCATORS.new_user_password_textbox_id).send_keys(new_password)

    def confirm_password(self, confirmed_password):
        self.driver.find_element(By.ID, AP_LOCATORS.confirm_password_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, AP_LOCATORS.confirm_password_textbox_id).send_keys(confirmed_password)

    def click_save_button(self):
        time.sleep(3)
        self.driver.find_element(By.ID, AP_LOCATORS.save_newUser_button_id).click()

    def verify_opened_users_list(self):
        table_shown = self.driver.find_element(By.ID, AP_LOCATORS.customer_list_table).is_displayed()
        assert table_shown is True, f"Table not found, boolean => {table_shown}"

    def search_new_saved_user(self, saved_new_username):
        self.driver.find_element(By.NAME, AP_LOCATORS.username_search_field_name).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.NAME, AP_LOCATORS.username_search_field_name).send_keys(saved_new_username)

    def click_search_button(self):
        self.driver.find_element(By.ID, AP_LOCATORS.username_search_button).click()

    def verify_found_new_user(self):
        self.driver.find_element(By.LINK_TEXT, AP_LOCATORS.found_new_username).click()

    def check_saved_user_success_label_shown(self):
        time.sleep(1)
        shown_label = self.driver.find_element(By.XPATH, AP_LOCATORS.new_user_success_label_xpath).is_displayed()
        assert shown_label is True, f"ERROR! Actual found label boolean => {shown_label}"

    def add_new_user(self, employee_name, new_password, confirm_password):
        self.click_admin_button()

        # Fill form
        self.click_addUser_button()
        self.click_userRole_button()
        self.enter_employeeName(employee_name)
        self.employeeName_not_found()
        username_field = self.driver.find_element(By.ID, AP_LOCATORS.new_username_textbox_id)
        username_field.send_keys(utils.newUSERNAME)
        already_exists_error = self.driver.find_element(By.XPATH, "//*[@id='frmSystemUser']/fieldset/ol/li[3]/span")

        if already_exists_error.text == "Already exists" or "Should have at least 5 characters" or None:
            username_field.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
            new_username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            logger.info("Randomly generated username ===> : " + " test_user_" + str(new_username) + "@github.com")
            username_field.send_keys(new_username)
            assert len(new_username) == 10, f"Actual found username length is {len(new_username)}"

        self.choose_disabled_option()
        self.enter_password(new_password)
        self.confirm_password(confirm_password)
        self.click_save_button()
        self.check_saved_user_success_label_shown()
        self.search_new_saved_user(new_username)
        self.find_newly_created_user(new_username)

    def find_newly_created_user(self, username):
        self.verify_opened_users_list()
        self.click_search_button()
        found_user = self.driver.find_element(By.XPATH, AP_LOCATORS.new_created_user % username)
        assert found_user.text == username, f"New generated username returned wrong response. " \
                                            f"Username is: {found_user.text}"
