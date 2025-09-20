import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Id, xpath, cssselector, classname, name, linkedtext
email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
email.send_keys("mvkishanmu@gmail.com")

#Static Dropdown
dropDown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropDown.select_by_visible_text("Female")


time.sleep(4)