import json
import os
import sys
import time

import pytest

# pytest -n -2 -m smoke --browser_name edge --html=Reports/report.html

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PageObject.login import LoginPage

test_data_path = '../Data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):

    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shop_Page = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_Page.shop_product(test_list_item["productName"])
    print(shop_Page.getTitle())
    checkout_page = shop_Page.go_to_cart()
    checkout_page.checkout_button()
    checkout_page.delivery_location("ind")
    checkout_page.submit_validate()

    time.sleep(2)