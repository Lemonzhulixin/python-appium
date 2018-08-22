import subprocess

import os

'''
获取ios下的硬件信息
'''


def get_ios_devices():
    devices = []
    result = subprocess.Popen("ideviceinfo -k UniqueDeviceID", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()

    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            devices.append(t[0])
    return devices


def get_ios_version(udid):
    command = "ideviceinfo -u %s -k ProductVersion" % udid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]


def get_ios_product_name(udid):
    command = "ideviceinfo -u %s -k DeviceName" % udid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]

def get_ios_product_type(udid):
    command = "ideviceinfo -u %s -k ProductType" % udid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]

def get_ios_product_os(udid):
    command = "ideviceinfo -u %s -k ProductName" % udid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]


def get_ios_PhoneInfo(udid):
    name = get_ios_product_name(udid)
    release = get_ios_version(udid)
    # type = get_ios_product_type(udid)
    result = {"release": release, "device": name, "udid": udid}
    # print(result)
    return result

#编译facebook的wda到真机
def build_wda_ios(udid):
    os.popen(
        "xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination id=" + udid + " test")


if __name__ == '__main__':
    devices = get_ios_devices()
    print(devices)
    udid = get_ios_devices()[0]
    get_ios_PhoneInfo(udid)

