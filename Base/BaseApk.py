import re
from math import floor
import subprocess
import os

'''
apk文件的读取信息
'''
class ApkInfo():
    def __init__(self, apkPath):
        self.apkPath = apkPath

# 得到app的文件大小
    def getApkSize(self):
        size = floor(os.path.getsize(self.apkPath) / (1024 * 1000))
        return str(size) + "M"


    def getApkBaseInfo(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        appKey = match.group(2)
        appVersion = match.group(3)

        print("=====getApkInfo=========")
        print('packageName:', packagename)
        print('appKey:', appKey)
        print('appVersion:', appVersion)
        return packagename, appKey, appVersion

    #得到启动类

    def getApkActivity(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        # print("=====getApkActivity=========")
        match = re.compile("launchable-activity: name=(\S+)").search(output.decode())
        # print("match=%s" %match)
        if match is not None:
            # print('launchable-activity:', match.group(1))
            return match.group(1)

    # 得到应用名字
    def getApkName(self):
        cmd = "aapt dump badging " + self.apkPath + " | grep application-label: "
        result = ""
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        # print(output)
        if output != "":
            # print(output)
            result = output.split()[0].decode()[19:-1]
        return result

if __name__ == '__main__':
    pass
    apkPath = '../app/VivaVideo_7.3.1.apk'
    litePath = '/Users/zhulixin/Downloads/XiaoYing_lite.apk'

    info = ApkInfo(apkPath)
    apk = info.getApkBaseInfo()
    size = info.getApkSize()
    activity = info.getApkActivity()
    appname = info.getApkName()

    print('appName:', appname)
    print('size:', size)
    print('launchActivity:', activity)

