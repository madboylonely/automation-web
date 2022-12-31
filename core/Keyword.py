from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import core.GlobalConstants as GlobalConstants
import time

class Keyword:
    def clickWebElement(webElement):
        wait = WebDriverWait(driver=GlobalConstants.WEBDRIVER, timeout=GlobalConstants.WAIT_EXPLICIT)
        wait.until(EC.element_to_be_clickable(webElement))
        webElement.click()

    def getWebElementByXpath(strXpath, arg = ""):
        for x in range(30):
            if (len(GlobalConstants.WEBDRIVER.find_elements(By.XPATH, strXpath.format(arg))) == 1) :
                element = GlobalConstants.WEBDRIVER.find_element(By.XPATH, strXpath.format(arg));
                return element
            else :
                time.sleep(3)

    def sendKeyWebElement(webElement, keys):
            wait = WebDriverWait(driver=GlobalConstants.WEBDRIVER, timeout=GlobalConstants.WAIT_EXPLICIT)
            wait.until(EC.visibility_of(webElement))
            webElement.clear()
            webElement.send_keys(keys)
    
    def getTextWebElementByXpath(strXpath, arg = ""):
         for x in range(30):
            if (len(GlobalConstants.WEBDRIVER.find_elements(By.XPATH, strXpath.format(arg))) == 1) :
                element = GlobalConstants.WEBDRIVER.find_element(By.XPATH, strXpath.format(arg));
                return element.text
            else :
                time.sleep(3)
