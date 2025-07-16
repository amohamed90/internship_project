from pages.base_page import Page
from selenium.webdriver.common.by import By

class SettingsPage(Page):

    SUBSCRIPTION_PAYMENT = (By.CSS_SELECTOR, '[href="/subscription"]')

    def click_subscription_payment(self):
        self.click(*self.SUBSCRIPTION_PAYMENT)