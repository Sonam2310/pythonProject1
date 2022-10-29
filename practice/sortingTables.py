from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
list_of_browsed_Elements =[]

service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service =service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()



driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
list_of_elements = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(1)")
for element in list_of_elements:

    list_of_browsed_Elements.append(element.text)

list_of_original_browsed_items = list_of_browsed_Elements.copy()
list_of_browsed_Elements.sort()
assert list_of_browsed_Elements == list_of_original_browsed_items
