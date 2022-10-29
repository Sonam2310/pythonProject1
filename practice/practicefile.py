import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name = 'sonam'
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value")== "option2":
        checkbox.click()
        assert checkbox.is_selected()


radiobuttons = driver.find_elements(By.CSS_SELECTOR, "input[class='radioButton']")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()


dropdowns = Select(driver.find_element(By.CSS_SELECTOR, "#dropdown-class-example"))
dropdowns.select_by_value("option2")
driver.find_element(By.CSS_SELECTOR, "#autocomplete").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")
print(len(countries))

for country in countries:
    if country.text=="India":
        country.click()
        break

print(driver.find_element(By.CSS_SELECTOR, "#autocomplete").get_attribute("value"))

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert
AlertText= alert.text
print(AlertText)
assert name in AlertText
alert.accept()

driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alert1 = driver.switch_to.alert
alertText1 =alert1.text
print(alertText1)
assert 'confirm' in alertText1
alert1.dismiss()

driver.find_element(By.CSS_SELECTOR, "#openwindow").click()

print(driver.find_element(By.TAG_NAME, "h3").text)

windowHandle = driver.window_handles
driver.switch_to.window(windowHandle[0])

driver.get_screenshot_as_file("screen.png")
driver.execute_script("window.scrollBy(0,500)")





