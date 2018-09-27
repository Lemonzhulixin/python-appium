# -*- coding: utf-8 -*-

from Base.BaseElements import Element
from Base.BasePickle import *
from Base.BaseFile import *
from Base.BaseApk import *
from Base.BaseIpa import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

apkPath = PATH("../app/VivaVideo_7.3.6.apk")  # 测试的app路径
ipaPath = PATH("../app/xiaoying.ipa")  # 测试的app路径

def mk_file(platform):
    destroy()
    mkdir_file(PATH("../Log/"+Element.INFO_FILE))
    mkdir_file(PATH("../Log/"+Element.SUM_FILE))
    mkdir_file(PATH("../Log/" + Element.DEVICES_FILE))

    data = read(PATH("../Log/"+Element.INFO_FILE))
    if platform == 'android':
        apkInfo = ApkInfo(apkPath).getApkBaseInfo()
        data["appName"] = ApkInfo(apkPath).getApkName()
        data["packageName"] = apkInfo[0]
        data["appVersion"] = apkInfo[2]

        data["sum"] = 0
        data["pass"] = 0
        data["fail"] = 0
        write(data=data, path=PATH("../Log/"+Element.SUM_FILE))
    elif platform == 'iOS':
        ipaInfo = getIpaInfo(ipaPath)
        data["appName"] = ipaInfo[0]
        data["packageName"] = ipaInfo[1]
        data["appVersion"] = ipaInfo[2]

        data["sum"] = 0
        data["pass"] = 0
        data["fail"] = 0
        write(data=data, path=PATH("../Log/" + Element.SUM_FILE))


def init(devices):
    # 每次都重新安装uiautomator2都两个应用
    os.popen("adb -s %s uninstall io.appium.uiautomator2.server.test" % devices)
    os.popen("adb -s %s uninstall io.appium.uiautomator2.server" % devices)
    os.popen("adb -s %s install -r %s" % (devices, PATH("../app/appium-uiautomator2-server-v0.1.9.apk")))
    os.popen("adb -s %s install -r %s" % (devices, PATH("../app/appium-uiautomator2-server-debug-androidTest.apk")))


def destroy():
    remove_file(PATH("../Log/"+Element.INFO_FILE))
    remove_file(PATH("../Log/"+Element.SUM_FILE))
    remove_file(PATH("../Log/"+Element.DEVICES_FILE))


if __name__ == '__main__':
    print(destroy())
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
