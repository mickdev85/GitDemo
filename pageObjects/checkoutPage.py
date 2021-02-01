from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, "p.product-name")
    amount = (By.XPATH, "//span[@class='discountAmt']")
    promoBox = (By.CSS_SELECTOR, ".promoCode")
    promoButton = (By.CSS_SELECTOR, ".promoBtn")
    discountAmount = (By.CSS_SELECTOR, ".discountAmt")
    confirmOrder = (By.XPATH, "//button[contains(text(),'Place Order')]")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getAmount(self):
        return self.driver.find_element(*CheckoutPage.amount)

    def getPromoBox(self):
        return self.driver.find_element(*CheckoutPage.promoBox)

    def getPromoButton(self):
        return self.driver.find_element(*CheckoutPage.promoButton)

    def getDiscountAmount(self):
        return self.driver.find_element(*CheckoutPage.discountAmount)

    def getConfirmButton(self):
        return self.driver.find_element(*CheckoutPage.confirmOrder)
