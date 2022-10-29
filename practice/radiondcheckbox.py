

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes= driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option1":
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

assert driver.find_element(By.CSS_SELECTOR, "#displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()


