# -*- coding: utf-8 -*-
from Base.BaseLog import myLog
from Base.BaseIosLog import myIosLog
import unittest
from appium import webdriver
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def appium_testcase(devices):
    desired_caps = {}

    if str(devices["platformName"]).lower() == "android":
        desired_caps["systemPort"] = devices["systemPort"]
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
    elif str(devices["platformName"]) == "iOS":
        desired_caps['bundleId'] = devices["bundleId"]
        desired_caps['xcodeOrgId'] = "BMP99N9345"
        desired_caps['xcodeSigningId'] = "iPhone Developer"
        desired_caps['autoLaunch'] = True
    desired_caps['udid'] = devices["udid"]
    desired_caps['app'] = devices["app"]
    desired_caps['deviceName'] = devices["deviceName"]
    desired_caps['platformVersion'] = devices["platformVersion"]
    desired_caps['platformName'] = devices["platformName"]
    desired_caps["automationName"] = devices['automationName']
    desired_caps["noReset"] = "True"
    desired_caps['noSign'] = "True"

    remote = "http://127.0.0.1:" + str(devices["port"]) + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    return driver


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should  
        inherit from this class.  
    """

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        global devicess
        devicess = param

    @classmethod
    def setUpClass(cls):
        pass
        cls.driver = appium_testcase(devicess)
        cls.platformName = devicess["platformName"]
        cls.udid = devicess["udid"]
        if cls.platformName == 'android':
            cls.platformName = 'android'
            cls.logTest = myLog().getLog(cls.udid)  # 每个设备实例化一个日志记录器
        elif cls.platformName == 'iOS':
            cls.platformName = 'iOS'
            cls.logTest = myIosLog().getLog(cls.udid)  # 每个设备实例化一个日志记录器

    @classmethod
    def tearDownClass(cls):
        pass
        cls.driver.close_app()

    @staticmethod
    def parametrize(testcase_klass, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite
