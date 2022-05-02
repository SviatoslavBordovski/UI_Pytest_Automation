import time
import utils.utils
import logging as logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.invalid_credentials_flag_id = "spanMessage"
        self.forgot_password_linktext = "Forgot your password?"
        self.title_name_xpath = "//h1[text()='%s']"
        self.cancel_button_xpath = "//input[@class='cancel']"
        self.security_user_name = "securityAuthentication[userName]"
        self.reset_password_btn_xpath = "//input[@value='Reset Password']"
        self.contact_hr_xpath = "//a[@class='messageCloseButton']"

    def login_crm_system(self, username, password):
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_button_id).click()
        time.sleep(3)

    def click_forgot_password_link(self):
        self.driver.find_element(By.LINK_TEXT, self.forgot_password_linktext).click()

    def sign_in_with_empty_or_incorrect_credentials(self):
        """ Login with empty credentials, login with wrong credentials, verify flags were shown, user clicked on \
        'Forgot your password link' and was redirected to 'Reset Password' form """
        self.click_login_button()
        credentials_flag = self.driver.find_element(By.ID, self.invalid_credentials_flag_id).text
        logger.info("Credentials flag was fetched")
        if credentials_flag == utils.utils.expectedEmptyCredentialsFlag:
            assert len(credentials_flag) == 24, f"ERROR! Actual invalid credentials flag length" \
                                                f" => {len(credentials_flag)}"
            entered_credentials = self.login_crm_system("username", "password")
            if entered_credentials is not int:
                self.click_login_button()
                logger.info("Incorrect credentials entered")
                current_url = self.driver.current_url
                assert current_url == utils.utils.expectedInvalidCredentialsUrl, f"Url after wrong credentials " \
                                                                                 f"is wrong, found {current_url}"
                invalid_credentials_flag = utils.utils.expectedInvalidCredentialsFlag
                if invalid_credentials_flag:
                    assert len(invalid_credentials_flag) == 19, f"ERROR! Actual invalid credentials flag length" \
                                                                f" => {len(invalid_credentials_flag)}"
                    self.click_forgot_password_link()
                    current_url = self.driver.current_url
                    assert current_url == utils.utils.forgotPasswordFormUrl, f"Url after click on 'forgot password'" \
                                                                             f" link is wrong, found {current_url}"
                    logger.info("'Forgot your password' link was clicked and user was redirected to 'Reset Password' form")
                else:
                    raise Exception("Flag for invalid credentials not found, please debug the issue")

            else:
                raise Exception("Something wrong on with entered credentials, please debug the issue")

    def click_cancel_button_forgot_password_form(self):
        self.driver.find_element(By.XPATH, self.cancel_button_xpath).click()

    def cancel_fill_forgot_password_form(self, title):
        custom_page_title = self.driver.find_element(By.XPATH, self.title_name_xpath % title).text
        assert custom_page_title == utils.utils.forgotPasswordTitle, f"Actual found title => {custom_page_title}"
        self.click_cancel_button_forgot_password_form()
        current_redirection_url = self.driver.current_url
        assert current_redirection_url == utils.utils.cancelForgotPasswordUrl, f"Url after wrong credentials " \
                                                                         f"is wrong, found {current_redirection_url}"

    def fill_username_forgot_password_input(self, user):
        self.driver.find_element(By.NAME, self.security_user_name).send_keys(Keys.CONTROL + 'a', Keys.DELETE)
        self.driver.find_element(By.NAME, self.security_user_name).send_keys(user)
        logger.info("User filled 'Username' input")

    def click_reset_password_button(self):
        self.driver.find_element(By.XPATH, self.reset_password_btn_xpath).click()
        logger.info("User clicked 'Reset Password' button")

    def verify_banner_shown_and_closed(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.contact_hr_xpath)))
        assert element.text == "Close", f"ERROR! Actual found text => {element.text}"
        element.click()
        logger.info("User closed 'Please contact HR...' banner")
        banner_elem = self.driver.find_element(By.XPATH, self.contact_hr_xpath).is_displayed()
        assert banner_elem is True, f"ERROR! Actual boolean => {banner_elem}"

    def fill_forgot_password_form(self, user):
        self.click_forgot_password_link()
        self.fill_username_forgot_password_input(user)
        self.click_reset_password_button()
        self.verify_banner_shown_and_closed()
