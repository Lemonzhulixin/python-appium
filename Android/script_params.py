# -*- coding: utf-8 -*-
"""python命令行参数处理"""
import argparse
from appium import webdriver


# Android脚本请加上下面这一段，用于命令行参数解析
def params_init():
    """从命令行获取参数，初始化"""
    parser = argparse.ArgumentParser(description='***Appium Python-Client Script Paramas***')
    parser.add_argument('-p', '--port', help='The port for appium to listen on')
    parser.add_argument('-pl', '--platform', help='Device system platform')
    parser.add_argument('-v', '--version', help='Device system version')
    parser.add_argument('-pk', '--package', help='Package of the Android app you want to run')
    parser.add_argument('-ac', '--activity', help='Activity you want to launch from your package')

    args = parser.parse_args()
    remote_url = 'http://localhost:{}/wd/hub'.format(args.port)

    desired_caps = {
        'appPackage': args.package,
        'appActivity': args.activity,
        'platformName': args.platform,
        'platformVersion': args.version
    }

    print('Params init!!!')
    drivers = webdriver.Remote(command_executor=remote_url, desired_capabilities=desired_caps)
    return drivers


driver = params_init()
