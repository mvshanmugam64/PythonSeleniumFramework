import time

from selenium.webdriver.common.by import By

from PageObject.checkout import CheckoutPage
from Utils.browserUtils import BrowserUtils

# pytest -m smoke -->Tagging
# pytest -n <auto/number> --> run in parallel (pytest-xdist)

class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.product_names = (By.XPATH, "//h4[@class='card-title']")
        self.cart_button = (By.XPATH, "//a[contains(@class,'btn-primary')]")



    def shop_product(self, product_title):
        productList = []
        productName = self.driver.find_elements(*self.product_names)
        print("Product Name: " +product_title)
        for product in productName:
            pName = product.text
            productList.append(pName)
            if pName == product_title:
                cart = product.find_element(By.XPATH, "parent::div/following::div/button")
                cart.click()


    def go_to_cart(self):
        time.sleep(1)
        self.driver.find_element(*self.cart_button).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page