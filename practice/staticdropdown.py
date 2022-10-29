from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
service_obj =Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_index(1)
#dropdown.select_by_value("Female")
dropdown.select_by_visible_text("Male")