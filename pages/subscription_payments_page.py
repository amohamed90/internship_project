from pages.base_page import Page
from selenium.webdriver.common.by import By

class Subscription(Page):

    SUBSCRIPTION_TEXT = (By.CSS_SELECTOR, '.lotion-your-h3--price')
    UPGRADE_PLAN_BTN = (By.CSS_SELECTOR, '[wized="upgradePlanButton"]')
    BACK_BTN = (By.CSS_SELECTOR, 'a[href="/settings"] .next-step--.black')

    expected_text = 'Subscription & payments'
    expected_url = 'https://soft.reelly.io/subscription'

    def verify_page_opens(self):
        self.verify_url(self.expected_url)

    def verify_text_visibility(self):
        self.verify_text(self.expected_text, *self.SUBSCRIPTION_TEXT)

    def verify_upgrade_btn(self):
        self.find_element(*self.UPGRADE_PLAN_BTN)

    def verify_back_btn(self):
        self.find_element(*self.BACK_BTN)