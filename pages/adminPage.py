from selenium.webdriver.support.ui import Select

class AdminPage:

    def __init__(self, driver):
        """Constructor for initializing all the attributes of class"""
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
        self.customer_list_table = "customerList"
        self.username_search_field = "searchSystemUser_userName"
        self.username_search_button = "searchBtn"
        self.found_new_username = "qwerty2024"

    def click_admin_button(self):
        self.driver.find_element_by_id(self.view_users_button_id).click()

    def click_addUser_button(self):
        self.driver.find_element_by_id(self.add_user_button_id).click()

    def click_userRole_button(self):
        self.driver.find_element_by_id(self.userRole_dropdown_id).click()

    def choose_admin_option(self):
        self.driver.find_element_by_name(self.userRole_option_name_admin).click()

    def enter_employeeName(self, emp_name):
        self.driver.find_element_by_id(self.employeeName_textbox_id).clear()
        self.driver.find_element_by_id(self.employeeName_textbox_id).send_keys(emp_name)

    def employeeName_not_found(self):
        self.driver.find_element_by_css_selector(self.error_notFoundEmployee_validation_error).is_displayed()

    def enter_username(self, username):
        self.driver.find_element_by_id(self.new_username_textbox_id).clear()
        self.driver.find_element_by_id(self.new_username_textbox_id).send_keys(username)

    def click_status_dropdown(self):
        self.driver.find_element_by_id(self.userStatus_dropdown_id).click()

    def choose_disabled_option(self):
        statusSelect = Select(self.driver.find_element_by_name(self.userStatus_option_disabled))
        statusSelect.select_by_value("0")

    def enter_password(self, new_password):
        self.driver.find_element_by_id(self.new_user_password_textbox_id).clear()
        self.driver.find_element_by_id(self.new_user_password_textbox_id).send_keys(new_password)

    def confirm_password(self, confirmed_password):
        self.driver.find_element_by_id(self.confirm_password_textbox_id).clear()
        self.driver.find_element_by_id(self.confirm_password_textbox_id).send_keys(confirmed_password)

    def click_save_button(self):
        self.driver.find_element_by_id(self.save_newUser_button_id).click()

    def verify_saved_user(self):
        assert self.driver.find_element_by_id(self.customer_list_table)

    def search_new_saved_user(self, saved_new_username):
        self.driver.find_element_by_id(self.username_search_field).clear()
        self.driver.find_element_by_id(self.username_search_field).send_keys(saved_new_username)

    def click_search_button(self):
        self.driver.find_element_by_id(self.username_search_button).click()

    def verify_found_new_user(self):
        self.driver.find_element_by_link_text(self.found_new_username).click()
