import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

#Dynamic DropDown
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
dropDowns = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
for dropDown in dropDowns:
    if dropDown.text == "India":
        dropDown.click()
        break
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
time.sleep(4)