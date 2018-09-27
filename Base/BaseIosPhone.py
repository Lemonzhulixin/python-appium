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


def get_ios_version(duid):
    command = "ideviceinfo -u %s -k ProductVersion" % duid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]


def get_ios_product_name(duid):
    command = "ideviceinfo -u %s -k DeviceName" % duid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]

def get_ios_product_type(duid):
    command = "ideviceinfo -u %s -k ProductType" % duid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]

def get_ios_product_os(duid):
    command = "ideviceinfo -u %s -k ProductName" % duid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]

def get_ios_PhoneInfo(duid):
    name = get_ios_product_name(duid)
    release = get_ios_version(duid)
    type = get_ios_product_type(duid)
    result = {"release": release, "device": name, "duid": duid, "type": type}
    return result

#编译facebook的wda到真机
def build_wda_ios(duid):
    os.popen(
        "xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination id=" + duid + " test")


if __name__ == '__main__':
    dev_list = []
    devices = get_ios_devices()
    for i in range(len(devices)):
        duid = get_ios_devices()[i]
        dev = get_ios_PhoneInfo(duid)
        dev_list.append(dev)
    print(dev_list)


