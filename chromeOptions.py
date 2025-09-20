import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-extensions')
# chrome_options.add_argument('--disable-dev-tools')

chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_options)


time.sleep(5)