from selenium.webdriver.common.by import By
from utils import utils as utils

class LoginAsserts:
    def __init__(self, driver):
        self.driver = driver
        self.login_logo_image_id = 'divLogo'
        self.forgot_password_link_id = 'forgotPasswordLink'
        self.login_header_id = "logInPanelHeading"

    def assert_login_page_contains_logo_image(self):
        visible_logo = self.driver.find_element(By.ID, self.login_logo_image_id).is_displayed()
        assert visible_logo is True

    def panel_header_check(self):
        title = self.driver.find_element(By.ID, self.login_header_id).text
        assert "LOGIN Panel" == title

    def assert_forgot_password_link_displayed(self):
        password_link_locator = self.driver.find_element(By.ID, self.forgot_password_link_id)
        assert password_link_locator.is_displayed()
        assert password_link_locator.text == utils.forgotPassword
 
