from pages.main_page import MainPage
from pages.sign_in_page import SignIn
from pages.off_plan_page import OffPlanPage
from pages.settings_page import SettingsPage
from pages.subscription_payments_page import Subscription

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.sign_in_page = SignIn(driver)
        self.off_plan_page = OffPlanPage(driver)
        self.settings_page = SettingsPage(driver)
        self.subscription_payments_page = Subscription(driver)

