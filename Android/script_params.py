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


def env_init():
    desired_caps = {
                'platformName': 'Android',
                'platformVersion': '',
                'deviceName': 'Lemontest',
                'udid':'NZ6T8TJ7INH6CI6L',
                'appPackage': "com.quvideo.xiaoying",
                'appActivity': "com.quvideo.xiaoying.app.SplashActivity",
                # 'app': '/Users/zhulixin/Downloads/XiaoYing_V6.3.5_0-xiaoyingtest.apk',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'automationName': 'Appium',
                'noReset': True
            }

    url = "http://localhost:4723/wd/hub"
    drivers = webdriver.Remote(url, desired_caps)
    return drivers

driver = env_init()