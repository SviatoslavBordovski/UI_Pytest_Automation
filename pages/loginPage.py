from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import utils.utils

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.login_header_id = "logInPanelHeading"
        self.invalid_credentials_flag_id = "spanMessage"
        self.forgot_password_linktext = "Forgot your password?"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

    def panel_header_check(self):
        title = self.driver.find_element(By.ID, self.login_header_id).text
        assert "LOGIN Panel" == title

    def shown_invalid_credentials_flag(self):
        invalid_credentials_flag = self.driver.find_element(By.ID, self.invalid_credentials_flag_id).text
        assert invalid_credentials_flag == utils.utils.expectedInvalidCredentialsFlag

    def click_forgot_password_link(self):
        forgot_password_link = self.driver.find_element(By.LINK_TEXT, self.forgot_password_linktext).click()
        forgot_password_link.is_selected()
