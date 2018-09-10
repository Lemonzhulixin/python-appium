# -*- coding: utf-8 -*-

import logging
import time
import threading
from Base.BaseAndroidPhone import getPhoneInfo
from Base.BaseRunner import *
import os
import subprocess

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class Log:
    def __init__(self, devices):
        get_phone = getPhoneInfo(devices)
        phone_name = get_phone["brand"] + "_" + get_phone["model"] + "_" + "android" + "_" + get_phone["release"]
        global logger, resultPath, logPath
        resultPath = PATH("../Log/")
        logPath = os.path.join(resultPath, (phone_name + "_" + time.strftime('%Y%m%d%H%M%S', time.localtime())))
        if not os.path.exists(logPath):
            os.makedirs(logPath)
        self.checkNo = 0
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # create handler,write log
        fh = logging.FileHandler(os.path.join(logPath, "outPut.log"))
        # Define the output format of formatter handler
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

        """logcat日志"""
        # 运行之前先清除log
        clear_cmd = 'adb -s ' + devices + ' logcat -c'
        subprocess.run(clear_cmd, shell=True)

        # 重新记录log
        crashPath = os.path.join(PATH("../Log/CrashInfo/Android/"))
        if not os.path.exists(crashPath):
            os.makedirs(crashPath)
        logcat_log = os.path.join(crashPath, "logcat.log")
        cmd_logcat = "adb -s " + devices + " logcat > %s" % (logcat_log)
        os.popen(cmd_logcat)

    def getMyLogger(self):
        """get the logger
        :return:logger
        """
        return self.logger

    def buildStartLine(self, caseNo):
        """build the start log
        :param caseNo:
        :return:
        """
        startLine = "----  " + caseNo + "   " + "   " + \
                    "  ----"
        # startLine = "----  " + caseNo + "   " + "START" + "   " + \
        #             "  ----"
        self.logger.info(startLine)

    def buildEndLine(self, caseNo):
        """build the end log
        :param caseNo:
        :return:
        """
        endLine = "----  " + caseNo + "   " + "END" + "   " + \
                  "  ----"
        self.logger.info(endLine)
        self.checkNo = 0

    def writeResult(self, result):
        """write the case result(OK or NG)
        :param result:
        :return:
        """
        reportPath = os.path.join(logPath, "report.txt")
        flogging = open(reportPath, "a")
        try:
            flogging.write(result + "\n")
        finally:
            flogging.close()
        pass

    def resultOK(self, caseNo):
        self.writeResult(caseNo + ": OK")

    def resultNG(self, caseNo, reason):
        self.writeResult(caseNo + ": NG--" + reason)

    def checkPointOK(self, driver, caseName, checkPoint):
        """write the case's checkPoint(OK)
        :param driver:
        :param caseName:
        :param checkPoint:
        :return:
        """
        self.checkNo += 1

        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": OK")
        print("==用例_%s检查点成功==" % caseName)
        # take shot 默认去掉成功截图
        # self.screenshotOK(driver, caseName)

    def checkPointNG(self, driver, caseName, checkPoint):
        """write the case's checkPoint(NG)
        :param driver:
        :param caseName:
        :param checkPoint:
        :return:
        """
        self.checkNo += 1

        self.logger.info("[CheckPoint_" + str(self.checkNo) + "]: " + checkPoint + ": NG")

        # take shot
        return self.screenshotNG(driver, caseName)

    def screenshotOK(self, driver, caseName):
        """screen shot
        :param driver:
        :param caseName:
        :return:
        """
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_OK.png"

        # wait for animations to complete before taking screenshot
        time.sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath + screenshotName))

    def screenshotNG(self, driver, caseName):
        """screen shot
        :param driver:
        :param caseName:
        :return:
        """
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "CheckPoint_" + str(self.checkNo) + "_NG.png"

        # wait for animations to complete before taking screenshot
        time.sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath + screenshotName))
        return os.path.join(screenshotPath + screenshotName)

    def screenshotERROR(self, driver, caseName):
        """screen shot
        :param driver:
        :param caseName:
        :return:
        """
        screenshotPath = os.path.join(logPath, caseName)
        screenshotName = "ERROR.png"

        # wait for animations to complete before taking screenshot
        time.sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshotPath, screenshotName))

class myLog:
    """
    This class is used to get log
    """

    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def getLog(devices):
        if myLog.log is None:
            myLog.mutex.acquire()
            myLog.log = Log(devices)
            myLog.mutex.release()
        return myLog.log

if __name__ == "__main__":
    logTest = myLog.getLog('4ed397ac')
    # logger = logTest.getMyLogger()
    # time.sleep(2)
    # os.popen("killall adb")
    # logTest.buildStartLine("11111111111111111111111")