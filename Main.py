import os
import core.GlobalConstants as GlobalConstants
from pages.login.Login import *
import logging
import time
from long.generateReport import *
from threading import Thread
import threading

try:
    from selenium import webdriver
except ImportError:
    os.system('pip install selenium==4.7.2')

try:
    import configparser
except ImportError:
    os.system('pip install configparser==5.3.0')

def initLogger():
    logging.basicConfig(filename="myLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    GlobalConstants.LOGGER = logging.getLogger()
    GlobalConstants.LOGGER.setLevel(logging.DEBUG)
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Init Loger", True))

def getParamsIniFile():
    # print("Read configs")
    config = configparser.ConfigParser()
    config.read('resource/test.ini')
    GlobalConstants.LINK_DEMO_PAGE = config.get('DEFAULT', 'demo_page')
    GlobalConstants.WAIT_IMPLICIT = config.get('DEFAULT', 'wait_implicit')
    GlobalConstants.WAIT_EXPLICIT = config.get('DEFAULT', 'wait_explicit')
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Get parameters in Ini file", True))

def initPage():
    # print("Init page")
    capabilities = webdriver.DesiredCapabilities().CHROME
    capabilities['acceptSslCerts'] = True
    capabilities['acceptInsecureCerts'] = True
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--disable-notifications')
    global chromeDriver
    chromeDriver = webdriver.Chrome(options=chromeOptions, desired_capabilities=capabilities)
    chromeDriver.maximize_window()
    chromeDriver.delete_all_cookies()
    chromeDriver.implicitly_wait(GlobalConstants.WAIT_IMPLICIT)
    GlobalConstants.WEBDRIVER = chromeDriver
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas("Init page", True))

def TC13():
    tcName = "TC13: Verify leading dot in the login identifier text box is invalid."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "          ")
    generateReport("TC13")

def TC12():
    tcName = "TC12: Verify the login identifier field without entering any value."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.verifyContinueButtonDisabled(step)
    generateReport("TC12")

def TC11():
    tcName = "TC11: Verify the login identifier field by entering only 10 blank spaces."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "          ")
    step = 3
    login.verifyContinueButtonDisabled(step)
    generateReport("TC11")

def TC10():
    tcName = "TC10: Verify the login identifier field by entering the blank space between the number."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "8585 85858")
    step = 3
    login.verifyContinueButtonDisabled(step)
    generateReport("TC10")

def TC9():
    tcName = "TC9: Verify the login identifier field by entering a more 12 digits mobile number."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "5858585858585")
    step = 3
    login.verifyContinueButtonDisabled(step)
    generateReport("TC9")

def TC8():
    tcName = "TC8: Verify the login identifier field by entering the Less than 9 digits mobile number."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "89858585")
    step = 3
    login.verifyContinueButtonDisabled(step)
    generateReport("TC8")

def TC7():
    tcName = "TC7: Verify unicode char in the address in the login identifier text box."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "& #12362; @ gmail.com")
    step = 3
    login.verifyContinueButtonDisabled(step)
    generateReport("TC7")


def TC6():
    tcName = "TC6: Verify encoded HTML within the login identifier field is invalid."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "catna<anct304@gmail.com>")
    step = 3
    login.verifyContinueButtonDisabled(step)
    generateReport("TC6")


def TC5():
    tcName = "TC5: Verify the missing username in the login identifier field."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "@gmail.com")
    step = 3
    login.verifyContinueButtonDisabled(step)
    generateReport("TC5")

def TC4():
    tcName = "TC4: Verify the missing domain in the login identifier field."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "anct304@")
    step = 3
    login.verifyContinueButtonDisabled(step)
    generateReport("TC4")

def TC3():
    tcName = "TC3: Verify the missing @ symbol in the login identifier field."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "abc.gmail.com")
    step = 3
    login.verifyContinueButtonDisabled(step)
    generateReport("TC3")

def TC2():
    tcName = "TC2: Verify an login identifier cannot exceed 250 characters."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    username = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas et dolor id nisi maximus euismod eu a lacus. Aliquam eu fermentum est. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut tempor odio vitae el."
    login.inputUsername(step, username)
    step = 3
    login.verifyMaxLengthOfEmail(step, 250)
    generateReport("TC2")

def TC1():
    tcName = "TC1: Verify the input login identifier field accepts a valid email address."
    GlobalConstants.g_reportRawData.append(GlobalConstants.ReportRawDatas(tcName, True))
    print(tcName)
    initLogger()
    getParamsIniFile()
    initPage()
    login = Login()
    step = 1
    login.navigateToDemoSite(step)
    step = 2
    login.inputUsername(step, "anct304@gmail.com")
    step = 3
    login.clickContinueButton(step)
    step = 4
    login.inputPassword(step, "Abc@1234")
    step = 5
    login.clickLoginButton(step)
    step = 6
    login.verifyWalletPage(step, "Wallet")
    generateReport("TC1")

# if __name__ == "__main__":
#     print("Program start!!!")
#     TC1()
#     TC2()
#     TC3()
#     TC4()
#     TC5()
#     TC6()
#     TC7()
#     TC8()
#     TC9()
#     TC10()
#     TC11()
#     TC12()
#     time.sleep(60)

def main():
    print("Program start!!!")
    TC1()
    TC2()
    TC3()
    TC4()
    TC5()
    TC6()
    TC7()
    TC8()
    TC9()
    TC10()
    TC11()
    TC12()
    # time.sleep(60)
    stopRecordScreen(5)

try:
    t1 = threading.Thread(target=startRecordScreen, args=("report",))
    t2 = threading.Thread(target=main, args=()) #startRecordScreen("report", 500)
    t1.start()
    time.sleep(3)
    t2.start()
    t1.join()
    t2.join()
except:
 	print("Error")