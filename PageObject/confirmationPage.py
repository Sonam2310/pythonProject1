from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver
    #driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    confirm = (By.CSS_SELECTOR, "input[type='text']")
    #driver.find_element(By.LINK_TEXT, "India")
    country = (By.LINK_TEXT, "India")
    #driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    #driver.find_element(By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")
    purchase = (By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")



    def Confirmation(self):
        return self.driver.find_element(*ConfirmPage.confirm)


    def ConfirmCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def CheckboxClick(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def PurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchase)