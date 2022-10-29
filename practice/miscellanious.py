from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certification_errors")
service_obj = Service("/Users/rajiv/chromedriver")
driver = webdriver.Chrome(service = service_obj, options= chrome_options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
#driver.explicitly_wait(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")
