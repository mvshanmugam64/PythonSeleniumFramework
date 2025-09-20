from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.browserUtils import BrowserUtils


class CheckoutPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_btn = (By.XPATH, "//tbody//td//button[@class='btn btn-success']")
        self.location_field = (By.CSS_SELECTOR, "#country")
        self.select_location = (By.LINK_TEXT, "India")
        self.submit_button = (By.CSS_SELECTOR, "input[type='submit']")
        self.success_alert = (By.XPATH, "//div[contains(@class,'alert-success')]")

    def checkout_button(self):
        self.driver.find_element(*self.checkout_btn).click()

    def delivery_location(self, locationName):
        self.driver.find_element(*self.location_field).send_keys(locationName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.select_location))
        self.driver.find_element(*self.select_location).click()

    def submit_validate(self):
        self.driver.find_element(*self.submit_button).click()
        successAlert = self.driver.find_element(*self.success_alert).text
        print(successAlert)