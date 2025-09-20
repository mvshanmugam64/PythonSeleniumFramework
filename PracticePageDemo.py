import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkBoxs = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for checkbox in checkBoxs:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected()

assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()
name = "shanmu"
driver.find_element(By.CSS_SELECTOR, "input[name='enter-name']").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
time.sleep(2)
alert.accept()
time.sleep(2)