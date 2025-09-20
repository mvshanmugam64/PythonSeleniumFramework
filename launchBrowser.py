import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# service_obj = Service(EdgeChromiumDriverManager().install())
# driver = webdriver.Edge(service=service_obj)
driver = webdriver.Edge()
driver.get("https://www.rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)