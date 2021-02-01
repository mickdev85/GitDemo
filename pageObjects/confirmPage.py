from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    chooseCountry = (By.XPATH, "//select[@style='width: 200px;']")
    agreeCheckbox = (By.CSS_SELECTOR, ".chkAgree")
    proceedButton = (By.XPATH, "//button[contains(text(),'Proceed')]")

    def getChooseCountry(self):
        return self.driver.find_element(*ConfirmPage.chooseCountry)

    def getAgreeCheckbox(self):
        return self.driver.find_element(*ConfirmPage.agreeCheckbox)

    def getProceedButton(self):
        return self.driver.find_element(*ConfirmPage.proceedButton)
