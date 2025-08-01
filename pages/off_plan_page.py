from pages.base_page import Page
from selenium.webdriver.common.by import By

class OffPlanPage(Page):

    SETTINGS_BUTTON = (By.CSS_SELECTOR, '[href="/settings"]')

    def click_settings(self):
        self.wait_for_element_to_click(*self.SETTINGS_BUTTON)