from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service = service_object)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowhandle = driver.window_handles

driver.switch_to.window(windowhandle[1])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.switch_to.window(windowhandle[0])
print(driver.find_element(By.TAG_NAME, "h3").text)