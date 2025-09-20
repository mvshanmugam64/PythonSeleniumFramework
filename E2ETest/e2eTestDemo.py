import time

import openpyxl
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

productList = []

driver.find_element(By.XPATH, "//a[text()='Shop']").click()

productName = driver.find_elements(By.XPATH, "//h4[@class='card-title']")

product_name = "Samsung Note 8"

for product in productName:
    pName = product.text
    productList.append(pName)
    if product == product_name:
        product.find_element(By.XPATH, "parent::div/following::div/button").click()

print(productList)

driver.find_element(By.XPATH, "//a[contains(@class,'btn-primary')]").click()
driver.find_element(By.XPATH, "//tbody//td//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Ind")


wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()


# driver.find_element(By.CSS_SELECTOR, "#checkbox2").click()

driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
successAlert = driver.find_element(By.XPATH, "//div[contains(@class,'alert-success')]").text
print(successAlert)

# //h4[@class='card-title']/parent::div/following::div/button


time.sleep(5)