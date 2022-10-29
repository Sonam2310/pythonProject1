
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys('i am in frame')

