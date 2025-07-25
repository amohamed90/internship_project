from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_to_click(self, *locator):
        self.wait.until(EC.element_to_be_clickable(locator), message='element is not clickable').click()

    def wait_for_element_visibility(self, *locator):
        self.wait.until(EC.visibility_of_element_located(locator), message='Element does not exist')

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f'{actual_url} does not match {expected_url}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text[:20] == expected_text[:20], f'{actual_text} does not match {expected_text}'