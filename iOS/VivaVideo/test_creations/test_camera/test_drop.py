# -*- coding: utf-8 -*-
"""camera取消操作相关的测试用例."""
from unittest import TestCase
from iOS import script_ultils as sc
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time


class TestCameraCancel(TestCase):
    """camera取消操作相关的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_cancel_01_shot(self):
        """拍摄-拍摄页放弃."""
        sc.logger.info('拍摄-拍摄页放弃')
        fun_name = 'test_cancel_shot'

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

        sc.logger.info('开始录制')
        # 点拍5s
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()

        # 长按拍摄
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_capture, None, None, 5000).release().perform()

        sc.logger.info('撤销')
        sc.driver.find_element_by_name("撤销").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("撤销").click()

        sc.logger.info('点击左上角取消按钮')
        sc.driver.find_element_by_name('vivavideo camera tool icon clo').click()

        sc.logger.info('点击“丢弃”按钮')
        sc.driver.find_element_by_name("丢弃").click()
        time.sleep(1)

    def test_cancel_02_save(self):
        """拍摄-拍摄页保存."""
        sc.logger.info('拍摄-拍摄页保存')
        fun_name = 'test_cancel_save'

        sc.logger.info('点击高清拍摄')
        try:
            sc.driver.find_element_by_name("高清拍摄").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("拍摄").click()
        time.sleep(1)

        sc.logger.info('开始录制')
        # 点拍5s
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()

        sc.logger.info('点击左上角取消按钮')
        sc.driver.find_element_by_name('vivavideo camera tool icon clo').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“取消”按钮')
        try:
            sc.driver.find_element_by_name("取消").click()
        except NoSuchElementException:
            sc.logger.info('当前设备为pad，无取消按钮')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“保存”按钮')
        sc.driver.find_element_by_name('vivavideo camera tool icon clo').click()
        sc.driver.find_element_by_name("保存").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(2)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_cancel_03_preview(self):
        """拍摄-预览页放弃."""
        sc.logger.info('拍摄-预览页放弃)')
        fun_name = 'test_cancel_preview'

        sc.logger.info('点击高清拍摄')
        try:
            sc.driver.find_element_by_name("高清拍摄").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("拍摄").click()
        time.sleep(1)

        sc.logger.info('开始录制')
        # 点拍5s
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()

        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“左上角返回”按钮')
        time.sleep(0.5)
        sc.driver.find_element_by_name("xiaoying com back").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“左上角x”按钮退出拍摄')
        time.sleep(0.5)
        sc.driver.find_element_by_name("vivavideo camera tool icon clo").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1.5)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()