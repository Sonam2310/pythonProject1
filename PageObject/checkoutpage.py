from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    products = (By.XPATH, "//div[@class='card h-100']")

    #driver.find_element(By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    checkout = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    #driver.find_element(By.XPATH, "//tr/td[5]/button[@class='btn btn-success']").click(
    checkoutOption = (By.XPATH, "//tr/td[5]/button[@class='btn btn-success']")


    def productTitle(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def CheckoutItems(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def CheckOutOption(self):
        return self.driver.find_element(*CheckOutPage.checkoutOption)


