import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def test_sort(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Click column header
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    # Collect all veggie list -> browsersortedlist
    browserSortedVeggies = []
    veggiesList = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")
    for veggies in veggiesList:
        veggies = veggies.text
        browserSortedVeggies.append(veggies)

    originalSortVeggies = browserSortedVeggies.copy()
    print(originalSortVeggies)
    # Sort the veggie browsersortedlist -> newSortedList
    browserSortedVeggies.sort()

    # browsersortedlist == newSortedList
    assert browserSortedVeggies == originalSortVeggies

    time.sleep(4)