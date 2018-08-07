# -*- coding: utf-8 -*-
"""创作页面内分享相关的测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import TimeoutException
from appium.webdriver.connectiontype import ConnectionType

class TestCreationShare(TestCase):
    """创作页面内分享相关的测试类."""

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

    def test_share_01_edit(self):
        """分享-编辑视频标题/话题相关."""
        sc.logger.info('分享-编辑视频标题/话题相关')
        fun_name = 'test_share_edit'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击第一个草稿封面')
        ba.find_element_click('xpath', 5, iOS_elements.el_home_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('保存/上传')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("保存/上传")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('关闭定位服务')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_loc_clo)).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('不是第一次点击保存/上传按钮')

        sc.logger.info('输入标题和描述')
        ba.publish_input()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('隐私设置')
        ba.publish_privacy()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('更换封面')
        ba.publish_cover_add()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('位置和话题')
        ba.publish_other()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('导出-导出页编辑测试完成')

    def test_share_02_publish(self):
        """导出-分享上传."""
        sc.logger.info('导出-分享上传')
        fun_name = 'test_share_publish'

        sc.logger.info('保存并上传')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("保存/上传")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('关闭定位服务')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_loc_clo)).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('不是第一次点击保存/上传按钮')

        sc.logger.info('数据网络时，取消上传')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_xpath('//XCUIElementTypeButton[@name="取消"]')).click()

            sc.logger.error('当前是数据网络，取消上传，请手动执行相关测试')
            return False
        except TimeoutException:
            sc.logger.info('Wi-Fi可用')

        sc.logger.info('发布')
        ba.publish()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('导出-分享上传完成')
