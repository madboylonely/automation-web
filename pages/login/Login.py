import core.GlobalConstants as GlobalConstants
from core.Keyword import *

class Login:
    txtUsername = "//input[@id='login-username']"
    btnContinue = "//button[text()='Continue']"
    txtPassword = "//input[@id='login-password']"
    btnLogin = "//button[starts-with(@id,'btn-login')]"
    lblPageHeader = "//div[@id='page-wrapper']//label"

    def __init__(self):
        self.webDriver = GlobalConstants.WEBDRIVER

    def navigateToDemoSite(self, step):
        try:
            print(str(step) + ". Navigate to demo site")
            self.webDriver.get(GlobalConstants.LINK_DEMO_PAGE)
            self.webDriver.save_screenshot("image.png")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Navigate to demo site", True))
        except Exception as ex:
            GlobalConstants.LOGGER.error(ex)
            print("Program has some error!!!")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Navigate to demo site", False))
        
    def inputUsername(self, step, username):
        try:
            print(str(step) + ". Input username into text box")
            Keyword.sendKeyWebElement(Keyword.getWebElementByXpath(self.txtUsername), username)
            self.webDriver.save_screenshot("image1.png")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Input username into text box", True))
        except Exception as ex:
            GlobalConstants.LOGGER.error(ex)
            print("Program has some error!!!")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Input username into text box", False))

    def clickContinueButton(self, step):
        try:
            print(str(step) + ". Click on continue button")
            Keyword.clickWebElement(Keyword.getWebElementByXpath(self.btnContinue))
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Click on continue button", True))
        except Exception as ex:
            GlobalConstants.LOGGER.error(ex)
            print("Program has some error!!!")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Click on continue button", False))

    def inputPassword(self, step, password):
        try:
            print(str(step) + ". Input password into text box")
            Keyword.sendKeyWebElement(Keyword.getWebElementByXpath(self.txtPassword), password)
            self.webDriver.save_screenshot("image1.png")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Input password into text box", True))
        except Exception as ex:
            GlobalConstants.LOGGER.error(ex)
            print("Program has some error!!!")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Input password into text box", False))

    def clickLoginButton(self, step):
        try:
            print(str(step) + ". Click on login button")
            Keyword.clickWebElement(Keyword.getWebElementByXpath(self.btnLogin))
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Click on login button", True))
        except Exception as ex:
            GlobalConstants.LOGGER.error(ex)
            print("Program has some error!!!")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Click on login button", False))

    def verifyWalletPage(self, step, expected):
        try:
            print(str(step) + ". Verify wallet page")
            actual = Keyword.getTextWebElementByXpath(self.lblPageHeader)
            assert expected == actual
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Verify wallet page", True))
        except Exception as ex:
            GlobalConstants.LOGGER.error(ex)
            print("Program has some error!!!")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Verify wallet page", False))

    def verifyMaxLengthOfEmail(self, step, expected):
        try:
            print(str(step) + ". Verify mac length of email")
            actual = Keyword.getWebElementByXpath(self.txtUsername).get_attribute("value")
            assert expected == len(actual)
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Verify mac length of email", True))
        except Exception as ex:
            GlobalConstants.LOGGER.error(ex)
            print("Program has some error!!!")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Verify mac length of email", False))

    def verifyContinueButtonDisabled(self, step):
        try:
            print(str(step) + ". Verify continue button disabled")
            actual = Keyword.getWebElementByXpath(self.btnContinue).is_enabled()
            assert actual is False
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Verify continue button disabled", True))
        except Exception as ex:
            GlobalConstants.LOGGER.error(ex)
            print("Program has some error!!!")
            GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Step" + str(step) + ": Verify continue button disabled", False))