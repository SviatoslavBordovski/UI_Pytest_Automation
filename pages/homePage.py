from selenium.webdriver.common.by import By
import logging as logger

class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_linkText = "Logout"
        self.visible_dashboard_id = "div_graph_display_emp_distribution"
        self.dashboard_link_id = "menu_dashboard_index"

    def click_welcome_button(self):
        self.driver.find_element(By.ID, self.welcome_link_id).click()

    def click_logout_button(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()

    def check_dashboard_visibility(self):
        dashboard_graph = self.driver.find_element(By.ID, self.visible_dashboard_id)
        if dashboard_graph.is_displayed():
            dashboard_link = self.driver.find_element(By.ID, self.dashboard_link_id)
            dashboard_link.click()
            logger.info("Dashboard link was clicked")
        else:
            return logger.error("Dashboard link failed to be displayed")
