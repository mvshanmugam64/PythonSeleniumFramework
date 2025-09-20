import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--ignore-certificate-errors')
# chrome_option.add_argument('--incognito')

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# currentWindowtitle = driver.title
# actions = ActionChains(driver)
# actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform()
# time.sleep(4)
# actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()


#iframe and switch back to default page
# driver.switch_to.frame(id)
# driver.switch_to.default_content()


# driver.find_element(By.CSS_SELECTOR, "#opentab").click()
# windowsHandle = driver.window_handles
# driver.switch_to.window(windowsHandle[1])
# time.sleep(5)
# driver.find_element(By.XPATH, "//a[text()='Access all our Courses']").click()
# driver.switch_to.window(windowsHandle[0])

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")

time.sleep(3)