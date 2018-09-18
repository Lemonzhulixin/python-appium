# -*- coding: utf-8 -*-
import sys
import random

sys.path.append("..")
from Base.BaseIosPhone import *
from Base.BaseRunner import ParametrizedTestCase
from TestCase.aheadTest import PrivacySet
from TestCase.settingsTest import SetttingsTest
from TestCase.galleryTest import GalleryTest
from Base.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from Base.BaseInit import mk_file, remove_file
from Base.BaseStatistics import countDate, writeExcel
from Base.BasePickle import *
from datetime import datetime
from Base.BaseIpa import *
from Base import BaseInit
from iOSCrashAnalysis import FileOperate

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
        duid = getDevices[i]["devices"]
        _initApp["deviceName"] = get_ios_product_name(duid)
        _initApp["platformVersion"] = get_ios_version(duid)
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
        _initApp["duid"] = duid
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
    suite.addTest(ParametrizedTestCase.parametrize(PrivacySet, param=devices))  # 加入测试类
    suite.addTest(ParametrizedTestCase.parametrize(GalleryTest, param=devices))
    suite.addTest(ParametrizedTestCase.parametrize(SetttingsTest, param=devices))
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

        # 删除temp文件
        remove_file(PATH("../yamls/temp.yaml"))

        print("============开始导出crashreport==========")
        find_str = 'XiaoYing-'  # 待测app crashreport文件关键字
        file_format1 = [".ips"] # 导出的crash文件后缀
        file_format2 = [".crash"] # 解析后的crash文件后缀

        reportPath = PATH("../Log/CrashInfo/iOS/")
        beforePath = os.path.join(reportPath + '/Before')
        if not os.path.exists(beforePath):
            os.makedirs(beforePath)

        afterPath = os.path.join(reportPath + '/After')
        if not os.path.exists(afterPath):
            os.makedirs(afterPath)
        #导出设备中的所有crash文件
        for i in range(0, len(l_devices)):
            duid = l_devices[i]["devices"]
            exportReport = 'idevicecrashreport -u ' + duid + ' ' + beforePath + '/'
            print(exportReport)
            os.system(exportReport) #导出设备中的crash

        print("============开始过滤并解析待测app相关crashreport==========")
        # .bash_profile中配置以下环境，记得重启下mac
        # DEVELOPER_DIR="/Applications/XCode.app/Contents/Developer"
        # export DEVELOPER_DIR
        f = FileOperate.FileFilt()
        f.FindFile(find_str, file_format1, beforePath)
        for file in f.fileList:
            inputFile = os.path.abspath(file)  # 绝对路径
            # print(inputFile)
            analysisPath = PATH("../iOSCrashAnalysis/")
            cmd_analysis = 'python3 ' + analysisPath + '/BaseIosCrash.py' + ' -i ' + inputFile
            # print(cmd_analysis)
            os.system(cmd_analysis)

        #移动解析完成的crashreport到新的文件夹
        f.MoveFile(find_str, file_format2, beforePath, afterPath)
        print("============crashreport解析完成==========")

        # 删除所有解析之前的crash文件，若不想删除，注掉即可
        print("============删除所有解析之前的crash文件==========")
        f.DelFolder(beforePath)
    else:
        print("没有可用的iOS设备")