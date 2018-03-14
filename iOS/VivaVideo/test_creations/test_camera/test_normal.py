# -*- coding: utf-8 -*-
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import time


class TestCameraNormal(TestCase):
    # 获取屏幕尺寸
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_normal_01_filter(self):
        """拍摄-滤镜下载"""
        fun_name = 'test_normal_filter'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_accessibility_id("camerta_n").click()
        except NoSuchElementException:
            sc.driver.find_element_by_accessibility_id("camerta_f").click()

        sc.logger.info('点击高清拍摄')
        try:
            sc.driver.find_element_by_name("高清拍摄").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("拍摄").click()
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('跳过订阅页面')
        try:
            sc.driver.find_element_by_name("跳过").click()
            time.sleep(1)
            try:
                sc.driver.find_element_by_name("高清拍摄").click()
            except NoSuchElementException:
                sc.driver.find_element_by_name("拍摄").click()
                time.sleep(1)
        except NoSuchElementException:
            sc.logger.info('已跳过订阅页面')

        sc.logger.info("授权小影访问相机和麦克风")
        try:
            sc.driver.find_element_by_name("好").click()  # 授权访问相机
            time.sleep(1)
            sc.driver.find_element_by_name("好").click()  # 授权访问麦克风
            time.sleep(1)
        except NoSuchElementException:
            sc.logger.info("已授权")

        sc.logger.info('点击滤镜图标')
        sc.driver.find_element_by_name("vivavideo camera tool icon fil").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('滤镜下载-点击下载按钮')
        try:
            el_filter_download = sc.driver.find_element_by_accessibility_id("vivavideo_camera_tool_icon_download_nrm")
            el_filter_download.click()
            sc.capture_screen(fun_name, self.img_path)
            time.sleep(10)
        except NoSuchElementException:
            sc.logger.info('当前页面滤镜已下载')

        sc.logger.info('下载更多')
        sc.driver.find_element_by_accessibility_id("vivavideo_camera_bg_filter_store").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("使用滤镜")
        sc.driver.find_element_by_name('使用').click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo camera tool icon clo").click()

    def test_normal_02_settings(self):
        """拍摄-设置相关"""
        fun_name = 'test_normal_settings'

        time.sleep(2)
        sc.logger.info('点击高清拍摄')
        try:
            sc.driver.find_element_by_name("高清拍摄").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("拍摄").click()
        time.sleep(1)

        sc.logger.info('点击设置按钮')
        sc.driver.find_element_by_name("vivavideo camera tool icon set").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('闪光灯-开')
        try:
            sc.driver.find_element_by_name("vivavideo camera tool icon fla").click()
        except NoSuchElementException:
            sc.logger.info('当前为后置拍摄，无闪光灯选项')

        sc.logger.info('网格显示')
        sc.driver.find_element_by_name("vivavideo camera tool icon gri").click()

        sc.logger.info('倒计时')
        el_timer = sc.driver.find_element_by_name("vivavideo camera tool icon tim")
        for i in range(3):
            el_timer.click()

        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('退出设置选项')
        sc.driver.find_element_by_name("vivavideo camera tool icon set").click()

        sc.logger.info('前后置切换')
        sc.driver.find_element_by_name("vivavideo camera tool icon cha").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('视频尺寸,全屏切换到3:4')
        el_ful = sc.driver.find_element_by_name("vivavideo camera tool icon ful")
        el_ful.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('视频尺寸,3:4切换到1:1')
        el_fou = sc.driver.find_element_by_name("vivavideo camera tool icon fou")
        el_fou.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('视频尺寸,1:1切换到全屏')
        el_one = sc.driver.find_element_by_name("vivavideo camera tool icon one")
        el_one.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换拍摄模式:高清相机->自拍美颜')
        sc.driver.find_element_by_name("自拍美颜").click()
        time.sleep(1)

        sc.logger.info('切换拍摄模式:自拍美颜->高清相机')
        sc.driver.find_element_by_name("高清相机").click()
        time.sleep(1)

        sc.logger.info('切换拍摄模式:高清相机->音乐视频')
        sc.driver.find_element_by_name("音乐视频").click()
        time.sleep(1)

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo camera tool icon clo").click()

    def test_normal_03_shot(self):
        """拍摄-高清相机(1:1)"""
        fun_name = 'test_normal_shot'

        sc.logger.info('点击高清拍摄')
        try:
            sc.driver.find_element_by_name("高清拍摄").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("拍摄").click()
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('视频尺寸,全屏切换到3:4')
        el_ful = sc.driver.find_element_by_name("vivavideo camera tool icon ful")
        el_ful.click()

        sc.logger.info('视频尺寸,3:4切换到1:1')
        el_fou = sc.driver.find_element_by_name("vivavideo camera tool icon fou")
        el_fou.click()
        sc.capture_screen(fun_name, self.img_path)

        # 点拍
        sc.logger.info('开始录制')
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)

        sc.logger.info('录制5s后点击录制按钮停止录制')
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)

        # 长按拍摄
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_capture, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()