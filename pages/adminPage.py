import time
import random
import string
import utils.utils as utils
import logging as logger
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class AdminPage:

    def __init__(self, driver):
        self.driver = driver

        self.view_users_button_id = "menu_admin_viewAdminModule"
        self.add_user_button_id = "btnAdd"
        self.userRole_dropdown_id = "systemUser_userType"
        self.userRole_option_name_admin = "Admin"
        self.employeeName_textbox_id = "systemUser_employeeName_empName"
        self.error_notFoundEmployee_validation_error = "span.validation-error"
        self.new_username_textbox_id = "systemUser_userName"
        self.userStatus_dropdown_id = "systemUser_status"
        self.userStatus_option_disabled = "systemUser[status]"
        self.new_user_password_textbox_id = "systemUser_password"
        self.confirm_password_textbox_id = "systemUser_confirmPassword"
        self.save_newUser_button_id = "btnSave"
        self.customer_list_table = "resultTable"
        self.username_search_field_name = "searchSystemUser[userName]"  #send_keys
        self.username_search_button = "searchBtn"  #click to find
        self.found_new_username = "qwerty2018"
        self.new_created_user = "//a[text()='%s']"

    def click_admin_button(self):
        self.driver.find_element(By.ID, self.view_users_button_id).click()

    def click_addUser_button(self):
        self.driver.find_element(By.ID, self.add_user_button_id).click()

    def click_userRole_button(self):
        self.driver.find_element(By.ID, self.userRole_dropdown_id).click()

    def choose_admin_option(self):
        self.driver.find_element(By.NAME, self.userRole_option_name_admin).click()

    def enter_employeeName(self, emp_name):
        self.driver.find_element(By.ID, self.employeeName_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, self.employeeName_textbox_id).send_keys(emp_name)

    def employeeName_not_found(self):
        self.driver.find_element(By.CSS_SELECTOR, self.error_notFoundEmployee_validation_error).is_displayed()

    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, self.new_username_textbox_id)
        username_field.send_keys(username)

    def choose_disabled_option(self):
        time.sleep(3)
        self.driver.find_element(By.ID, self.userStatus_dropdown_id).click()
        statusSelect = Select(self.driver.find_element(By.NAME, self.userStatus_option_disabled))
        statusSelect.select_by_value("0")

    def enter_password(self, new_password):
        self.driver.find_element(By.ID, self.new_user_password_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, self.new_user_password_textbox_id).send_keys(new_password)

    def confirm_password(self, confirmed_password):
        self.driver.find_element(By.ID, self.confirm_password_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, self.confirm_password_textbox_id).send_keys(confirmed_password)

    def click_save_button(self):
        self.driver.find_element(By.ID, self.save_newUser_button_id).click()

    def verify_opened_users_list(self):
        table_shown = self.driver.find_element(By.ID, self.customer_list_table).is_displayed()
        assert table_shown is True, f"Table not found, boolean => {table_shown}"

    def search_new_saved_user(self, saved_new_username):
        self.driver.find_element(By.NAME, self.username_search_field_name).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.NAME, self.username_search_field_name).send_keys(saved_new_username)

    def click_search_button(self):
        self.driver.find_element(By.ID, self.username_search_button).click()

    def verify_found_new_user(self):
        self.driver.find_element(By.LINK_TEXT, self.found_new_username).click()

    def add_new_user(self, employee_name):
        self.click_admin_button()

        # Fill form
        self.click_addUser_button()
        self.click_userRole_button()
        self.enter_employeeName(employee_name)
        self.employeeName_not_found()
        username_field = self.driver.find_element(By.ID, "systemUser_userName")
        username_field.send_keys(utils.newUSERNAME)
        already_exists_error = self.driver.find_element(By.XPATH, "//*[@id='frmSystemUser']/fieldset/ol/li[3]/span")

        if already_exists_error.text == "Already exists" or "Should have at least 5 characters" or None:
            username_field.send_keys(Keys.CONTROL + 'a', Keys.DELETE)
            new_username: str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            logger.info("Randomly generated username ===> : " + " test_user_" + str(new_username) + "@github.com")
            username_field.send_keys(new_username)
            assert len(new_username) == 10, f"Found username length is {len(new_username)}"

        self.choose_disabled_option()
        self.enter_password(utils.strongPASSWORD)
        self.confirm_password(utils.strongPASSWORD)
        time.sleep(1)
        self.click_save_button()
        # add assert func about 'successfully saved' label show up
        self.search_new_saved_user(new_username)
        self.find_newly_created_user(new_username)

    def find_newly_created_user(self, username):
        self.verify_opened_users_list()
        self.click_search_button()
        found_user = self.driver.find_element(By.XPATH, self.new_created_user % username)
        assert found_user.text == username, f"New generated username returned wrong response. " \
                                            f"Username is: {found_user.text}"
