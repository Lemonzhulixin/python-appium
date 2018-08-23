# -*- coding: utf-8 -*-
import sys
import random

sys.path.append("..")
from Base.BaseIosPhone import *
from Base.BaseRunner import ParametrizedTestCase
from TestCase.HomeTest import HomeTest
from Base.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from Base.BaseInit import mk_file
from Base.BaseStatistics import countDate, writeExcel
from Base.BasePickle import *
from datetime import datetime
from Base.BaseIpa import *
from Base import BaseInit

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def runnerPool(getDevices):
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        print("=====runnerPool=========")
        print(getDevices)
        _initApp = {}
        udid = getDevices[i]["devices"]
        _initApp["deviceName"] = get_ios_product_name(udid)
        _initApp["platformVersion"] = get_ios_version(udid)
        _initApp["platformName"] = "iOS"
        _initApp["xcodeOrgId"] = "BMP99N9345"
        _initApp["xcodeSigningId"] = "iPhone Developer"
        _initApp["autoLaunch"] = True
        # _initApp["app"] = ''
        _initApp["app"] = getDevices[i]["app"]
        _initApp["port"] = getDevices[i]["port"]
        ipaInfo = getIpaInfo(_initApp["app"])
        # print(ipaInfo)
        _initApp["bundleId"] = ipaInfo[1]
        _initApp["udid"] = udid
        _initApp["automationName"] = "XCUITest"
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()

def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")


if __name__ == '__main__':

    devicess = get_ios_devices()
    if len(devicess) > 0:
        mk_file('iOS')
        l_devices = []

        for dev in devicess:
            app = {}
            app["devices"] = dev
            app["port"] = str(random.randint(4700, 4900))
            app["bport"] = str(random.randint(4700, 4900))
            app["app"] = BaseInit.ipaPath
            l_devices.append(app)

        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runnerPool(l_devices)
        writeExcel()
        appium_server.stop_server(l_devices)
    else:
        print("没有可用的iOS设备")