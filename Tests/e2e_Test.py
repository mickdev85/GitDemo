import time

import driver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.confirmPage import ConfirmPage
from pageObjects.shopPage import ShopPage


class TestGreenKart(BaseClass):
    @pytest.mark.regression
    def test_LogoDisplayed(self):
        log = self.getLogger()
        self.shopPage = ShopPage(self.driver)
        logo = self.shopPage.getLogo().text
        log.info("Logo is displayed as expected")
        assert logo == "GREENKART"

    @pytest.mark.regression
    def test_CartIsZero(self):
        self.shopPage = ShopPage(self.driver)
        items = self.shopPage.getCartItem().text
        assert items == "0"

        price = self.shopPage.getCartPrice().text
        assert price == "0"

    @pytest.mark.regression
    def test_CartPriceIncrease(self):
        self.shopPage = ShopPage(self.driver)
        searchBar = self.shopPage.getSearchBar()
        searchBar.send_keys("carrot")
        time.sleep(3)
        self.shopPage.getAddToCart().click()
        searchBar.clear()
        searchBar.send_keys("cauli")
        time.sleep(3)
        self.shopPage.getAddToCart().click()
        time.sleep(4)
        newItems = self.shopPage.getNewCartItems().text
        assert newItems == "2"

        newPrice = self.shopPage.getNewCartPrice().text
        assert newPrice > "0"

        self.shopPage.getCartIcon().click()
        time.sleep(3)
        self.shopPage.getCheckout().click()

    @pytest.mark.regression
    def test_CheckoutListMatch(self):
        log = self.getLogger()
        self.checkoutPage = CheckoutPage(self.driver)
        productList = []
        expectedList = ['Carrot - 1 Kg', 'Cauliflower - 1 Kg']
        time.sleep(3)
        products = self.checkoutPage.getProducts()
        for product in products:
            productList.append(product.text)
        log.info(productList)
        assert productList == expectedList

    @pytest.mark.regression
    def test_DiscountCode(self):
        self.checkoutPage = CheckoutPage(self.driver)
        beforeDiscount = self.checkoutPage.getAmount().text
        self.checkoutPage.getPromoBox().send_keys("rahulshettyacademy")
        self.driver.implicitly_wait(6)
        self.checkoutPage.getPromoButton().click()
        self.verifyPromoButton("span.promoInfo")
        afterDiscount = self.checkoutPage.getDiscountAmount().text
        assert float(afterDiscount) < int(beforeDiscount)

        self.checkoutPage.getConfirmButton().click()
        self.confirmPage = ConfirmPage(self.driver)
        select = Select(self.confirmPage.getChooseCountry())
        select.select_by_visible_text("United Kingdom")
        self.confirmPage.getAgreeCheckbox().click()
        self.confirmPage.getProceedButton().click()
