import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service =service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
ExpectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
ActualList = []
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = print(len(results))
for result in results:
    ActualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH,"div/button").click()
assert ExpectedList == ActualList


driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()


driver.find_element(By.XPATH,'//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:

    sum = sum + int(price.text)

print(sum)


totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div/select').send_keys("India")
driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()
#driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/input').click()
warning = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/span/b').text
assert 'Terms & Conditions' in warning
print(warning)

driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/button').click()



