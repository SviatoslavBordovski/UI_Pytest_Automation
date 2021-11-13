class HomePage:

    def __init__(self, driver):
        """Constructor for initializing all the attributes of class"""
        self.driver = driver
        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"

    def click_welcome_button(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout_button(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()
