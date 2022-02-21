from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import utils.utils
import logging as logger

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
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

    def click_forgot_password_link(self):
        self.driver.find_element(By.LINK_TEXT, self.forgot_password_linktext).click()

    def sign_in_with_empty_or_incorrect_credentials(self):
        """ Login with empty credentials, login with wrong credentials, verify flags were shown, user clicked on \
        'Forgot your password link' and was redirected to 'Reset Password' form """
        self.click_login_button()
        credentials_flag = self.driver.find_element(By.ID, self.invalid_credentials_flag_id).text
        logger.info("Credentials flag was fetched")
        if credentials_flag == utils.utils.expectedEmptyCredentialsFlag:
            assert len(credentials_flag) == 24
            entered_username = self.enter_username("username")
            entered_password = self.enter_password("password")
            logger.info("Incorrect credentials entered")
            if entered_username is not int and entered_password is not int:
                self.click_login_button()
                logger.info("'Login' button was clicked")
                current_url = self.driver.current_url
                assert current_url == utils.utils.expectedInvalidCredentialsUrl
                invalid_credentials_flag = utils.utils.expectedInvalidCredentialsFlag
                if invalid_credentials_flag:
                    assert len(invalid_credentials_flag) == 19
                    self.click_forgot_password_link()
                    current_url = self.driver.current_url
                    assert current_url == utils.utils.forgotPasswordFormUrl
                    logger.info("'Forgot your password' link was clicked and user was redirected to 'Reset Password' form")

                    # >>> FINISH TEST <<<
