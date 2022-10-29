from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service =service_obj)
driver.get('https://rahulshettyacademy.com/angularpractice')
driver.maximize_window()
driver.find_element(By.NAME,"name").send_keys('sonam')
driver.find_element(By.XPATH,"//input[@name='email']").send_keys('sonam.gmail.com')
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys('abcd')
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
driver.find_element(By.XPATH,"//div/input[@name='bday']").send_keys('08/08/1990')
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)
assert "Success" in message

