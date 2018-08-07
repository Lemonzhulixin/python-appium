# -*- coding: utf-8 -*-
"""python命令行参数处理"""
import argparse
from appium import webdriver
import os
import time
from iOS.start_appium import myserver
from concurrent.futures import ThreadPoolExecutor

#定义返回路径（绝对路径）
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p))


# def env_init_iOS():
#     desired_caps = {
#         'platformName': 'iOS',
#         'platformVersion': '11.4',
#         'deviceName': '6s2050',
#         'bundleId': 'com.quvideo.XiaoYing',
#         'app': '',
#         'noReset': True,
#         'automationName': 'XCUITest',
#         'udid': '5214866ccb9342f87f4c2aab093c25f7e252fd85',
#         'xcodeOrgId': 'BMP99N9345',
#         'xcodeSigningId': 'iPhone Developer',
#         'autoLaunch': True,
#     }
#
#     url = "http://localhost:4723/wd/hub"
#
#     drivers = webdriver.Remote(url, desired_caps)
#
#     return drivers
#
# driver = env_init_iOS()


# def dirlist(path, allfile):
#     filelist = os.listdir(path)
#     for filename in filelist:
#         filepath = os.path.join(path, filename)
#         if os.path.isdir(filepath):
#             dirlist(filepath, allfile)
#         else:
#             allfile.append(filepath)
#     return allfile
#
# def get_ipa(path,file_format):
#     files = dirlist(path, [])
#     ipa_list = []
#     for ipa in files:
#         if (os.path.splitext(ipa)[1] in file_format):
#             t = os.path.getctime(ipa)
#             ipa_list.append([ipa, t])
#     order = sorted(ipa_list, key=lambda e: e[1], reverse=True)
#     ipa_path = order[0][0]
#     return ipa_path


# def env_init_iOS(dev, ipa_path, wdaport, port):
#     desired_caps = {
#         'platformName': 'iOS',
#         'platformVersion': '',
#         'deviceName': dev,
#         'bundleId': 'com.quvideo.XiaoYing',
#         'app': ipa_path,
#         'noReset': True,
#         'automationName': 'XCUITest',
#         'udid': 'auto',
#         'xcodeOrgId': 'BMP99N9345',
#         'xcodeSigningId': 'iPhone Developer',
#         'autoLaunch': True,
#         'wdaLocalPort': wdaport
#     }
#
#     remote_url = 'http://localhost:' + str(port) + '/wd/hub'
#     time.sleep(5)
#     drivers = webdriver.Remote(remote_url, desired_caps)
#     return drivers
#
#
# path = "/Users/zhulixin/AppCrawler/"
# file_format = ['.ipa']
# device_list = [('6s2050',8001)]
#
# myserver().create_pools(len(device_list))
# port_list = myserver().ports
#
# dev = device_list[0][0]
# wdaport = device_list[0][1]
# port = port_list[0]
# ipa_path = get_ipa(path,file_format)
#
# print(dev,ipa_path, wdaport, port)
#
# driver = env_init_iOS(dev, ipa_path, wdaport, port)

def env_init_iOS(dev_name, dev_uuid, port):
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '',
        'deviceName': dev_name,
        'bundleId': 'com.quvideo.XiaoYing',
        'app': '',
        'noReset': True,
        'automationName': 'XCUITest',
        'udid': dev_uuid,
        'xcodeOrgId': 'BMP99N9345',
        'xcodeSigningId': 'iPhone Developer',
        'autoLaunch': True,
        'wdaLocalPort': 8001
    }

    remote_url = 'http://localhost:' + str(port) + '/wd/hub'
    time.sleep(5)
    drivers = webdriver.Remote(remote_url, desired_caps)
    return drivers


device_list = [('6s2050','5214866ccb9342f87f4c2aab093c25f7e252fd85')]

myserver().create_pools(len(device_list))
port_list = myserver().ports

dev = device_list[0][0]
uuid = device_list[0][1]
port = port_list[0]

driver = env_init_iOS(dev, uuid, port)
