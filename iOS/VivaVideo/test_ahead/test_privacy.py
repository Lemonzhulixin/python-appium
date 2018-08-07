# -*- coding: utf-8 -*-
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from iOS import iOS_elements
from iOS import base as ba


class TestPrivacy(TestCase):
    """权限获取测试类."""

    # 获取屏幕尺寸
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @classmethod
    def setUpClass(cls):
        sc.driver.launch_app()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        sc.driver.close_app()

    def test_Privacy(self):
        """权限获取"""
        sc.logger.info('权限获取')
        fun_name = 'test_Privacy'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击视频剪辑')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_home_edit)).click()

        try:
            sc.driver.find_element_by_name("跳过").click()
            sc.capture_screen(fun_name, self.img_path)

            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_home_edit)).click()
        except NoSuchElementException:
            sc.logger.info('已跳过订阅页面')

        sc.logger.info("授权小影访问相册和媒体资料")
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("好")).click()
            sc.capture_screen(fun_name, self.img_path)

            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("好")).click()
        except TimeoutException:
            sc.logger.info("已授权")

        sc.logger.info('返回首页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_gallery_back)).click()

        sc.logger.info('点击“高清拍摄”按钮')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_home_camera)).click()

        sc.logger.info("授权小影访问相机和麦克风")
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("好")).click()
            sc.capture_screen(fun_name, self.img_path)

            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("好")).click()
        except TimeoutException:
            sc.logger.info("已授权")

        sc.logger.info('授权测试完成')