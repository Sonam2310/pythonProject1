from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("ind")

time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text=="India":
       country.click()
       break
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))

