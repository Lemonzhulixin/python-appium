# -*- coding: utf-8 -*-
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
import time


class TestCameraSelf(TestCase):
    """camera美颜趣拍的测试类"""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_camera_self(self):
        """拍摄-自拍视频(全屏)"""
        fun_name = 'test_camera_self'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('点击“美颜趣拍”')
        sc.driver.find_element_by_name("美颜趣拍").click()
        time.sleep(1)

        sc.logger.info('跳过订阅页面')
        try:
            sc.driver.find_element_by_name("跳过").click()
            time.sleep(1)
            sc.driver.find_element_by_name("美颜趣拍").click()
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

        sc.logger.info('下载并使用人脸贴纸')
        el_sticker_download = sc.driver.find_element_by_accessibility_id("vivavideo_camera_tool_icon_sticker_download_nrm")
        el_sticker_download.click()
        sc.capture_screen(fun_name, self.img_path)
        try:
            WebDriverWait(sc.driver,30).until(
                lambda sticker_download: sticker_download.find_element_by_xpath(
                    "//*/XCUIElementTypeCollectionView[1]//*/XCUIElementTypeOther/XCUIElementTypeImage"))

            sc.logger.info('使用下载的人脸贴纸')
            el_sticker = sc.driver.find_elements_by_xpath(
                "//*/XCUIElementTypeCollectionView[1]//*/XCUIElementTypeOther/XCUIElementTypeImage")
            el_sticker[1].click()
            time.sleep(0.5)
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutError as t:
            sc.logger.error('下载自拍贴纸超时',t)
            return False

        sc.logger.info('切换人脸贴纸分类')
        el_sticker_type = sc.driver.find_elements_by_xpath(
            "//*/XCUIElementTypeCollectionView[2]//*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_sticker_type[1].click()
        time.sleep(0.5)
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击屏幕消除贴纸控件')
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 0.5).release().perform()
        time.sleep(0.5)
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击滤镜按钮')
        sc.driver.find_element_by_name("vivavideo camera tool icon fil").click()
        time.sleep(0.5)
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击屏幕消除滤镜控件')
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 0.5).release().perform()
        time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        # 点拍
        sc.logger.info('开始录制')
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)

        sc.logger.info('录制5s后点击录制按钮停止录制')
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()