from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import CheckoutPage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    logo = (By.XPATH, "//div[@class='brand greenLogo']")
    cartItem = (By.XPATH, "//div[@class='cart-info']/table/tbody/tr[1]/td[3]")
    cartPrice = (By.XPATH, "//div[@class='cart-info']/table/tbody/tr[2]/td[3]")
    searchBar = (By.XPATH, "//input[@class='search-keyword']")
    addToCart = (By.XPATH, "//div[@class='product']/div/button")
    newCartItem = (By.XPATH, "//div[@class='cart-info']/table/tbody/tr[1]/td[3]")
    newCartPrice = (By.XPATH, "//div[@class='cart-info']/table/tbody/tr[2]/td[3]")
    cartIcon = (By.XPATH, "//a[@class='cart-icon']")
    checkout = (By.XPATH, "//div[@class='cart-preview active']/div/button")

    def getLogo(self):
        return self.driver.find_element(*ShopPage.logo)

    def getCartItem(self):
        return self.driver.find_element(*ShopPage.cartItem)

    def getCartPrice(self):
        return self.driver.find_element(*ShopPage.cartPrice)

    def getSearchBar(self):
        return self.driver.find_element(*ShopPage.searchBar)

    def getAddToCart(self):
        return self.driver.find_element(*ShopPage.addToCart)

    def getNewCartItems(self):
        return self.driver.find_element(*ShopPage.newCartItem)

    def getNewCartPrice(self):
        return self.driver.find_element(*ShopPage.newCartPrice)

    def getCartIcon(self):
        return self.driver.find_element(*ShopPage.cartIcon)

    def getCheckout(self):
        return self.driver.find_element(*ShopPage.checkout)
