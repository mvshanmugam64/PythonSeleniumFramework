import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ber")
time.sleep(2)





results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
productList = []
count = len(results)
assert count > 0

for result in results:
    productName = result.find_element(By.XPATH, "h4[@class='product-name']")
    pList = productName.text
    productList.append(pList)  # Strore the string into list using append
    result.find_element(By.XPATH, "div/button").click()

print(productList)

assert productList == expectedList

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

amounts = driver.find_elements(By.XPATH, "//table[@id='productCartTables']/tbody/tr/td[5]/p[@class='amount']")
amtSum = 0
for amount in amounts:
    print(int(amount.text)) #   Converted Str to int
    amtSum += int(amount.text)
print(f"Total Amount: {amtSum}")

expSum = driver.find_element(By.CSS_SELECTOR, ".totAmt").text

print(f"Expected Amount: {int(expSum)}")

assert int(expSum) == amtSum


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".discountAmt")))
discountAmt = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
print(f"Discount Amount: {discountAmt}")

assert float(discountAmt) < int(expSum)


time.sleep(2)