from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service =service_obj)
driver.get('https://rahulshettyacademy.com/AuotomationPractice')
driver.maximize_window()
checkboxes =driver.find_element(By.XPATH,"//input[type='checkbox']")

for checkbox in checkboxes:
    if checkbox.getAtribute("value")=='option2':
        checkbox.click()
        assert checkbox.is_selected()
        break


###
action = ActionChains(driver)
#action.click_and_hold(driver.find_element(By.)).perform()
action.context_click()
action.double_click()
action.key_down()