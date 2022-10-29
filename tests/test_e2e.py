from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from PageObject.HomePage import HomePage
from PageObject.checkoutpage import CheckOutPage
from PageObject.confirmationPage import ConfirmPage
from utilities.BaseClass import BaseClass


class TestDemo(BaseClass):
    def test_Demo_e2e(self):

        
        homePage.ShopItems().click()
        checkOutPage = CheckOutPage(self.driver)
        products =checkOutPage.productTitle()
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == 'Blackberry':
                product.find_element(By.XPATH, "div/button").click()
        checkOutPage.CheckoutItems().click()
        checkOutPage.CheckOutOption().click()

        confirmPage = ConfirmPage(self.driver)
        confirmPage.Confirmation().send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        confirmPage.ConfirmCountry().click()
        confirmPage.CheckboxClick().click()
        confirmPage.PurchaseBtn().click()
        successMessage = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you" in successMessage