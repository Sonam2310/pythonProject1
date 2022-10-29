import password as password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service =service_obj)
driver.get('https://rahulshettyacademy.com/client')
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
user = driver.find_element(By.XPATH,"//form/div[1]/input")
password = driver.find_element(By.ID,"userPassword")
confirmpassword = driver.find_element(By.ID,"confirmPassword")
user.send_keys("demo@gmail.com")
password.send_keys("Hello@1234")
confirmpassword.send_keys("Hello@12345")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
message = driver.find_element(By.XPATH,"//form/div/div").text
print(message)

assert 'must match'in message
confirmpassword.click()
confirmpassword.clear()
confirmpassword.send_keys("Hello@1234")


#driver.find_element(By.ID,"confirmPassword").click()
#driver.find_element(By.ID,"confirmPassword").clear()
#password.send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
wait(2)
driver.close()


