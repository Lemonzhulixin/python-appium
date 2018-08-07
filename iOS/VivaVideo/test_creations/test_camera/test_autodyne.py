# -*- coding: utf-8 -*-
"""camera美颜趣拍的测试用例."""
from appium.webdriver.common.touch_action import TouchAction
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import TimeoutException

class TestCameraSelf(TestCase):
    """camera美颜趣拍的测试类."""

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

    def test_camera_self(self):
        """拍摄-自拍视频(全屏)."""
        sc.logger.info('拍摄-美颜趣拍(全屏)')
        fun_name = 'test_camera_self'

        sc.logger.info('点击“美颜趣拍”')
        ba.home_first_click("美颜趣拍")
        sc.capture_screen(fun_name, self.img_path)

        # 第一次从次要功能位打开自拍，拍摄按钮是音乐视频的控件，所以先关闭再打开
        sc.logger.info('退出拍摄')
        time.sleep(1)
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_cam_close)).click()

        sc.logger.info('点击“美颜趣拍”')
        WebDriverWait(sc.driver, 5).until(
            lambda x: x.find_element_by_name('美颜趣拍')).click()

        sc.logger.info('点击人脸贴纸icon')
        ba.find_element_click('name', 10, iOS_elements.el_sticker_icon)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载人脸贴纸')
        WebDriverWait(sc.driver, 5).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_sticker_download)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('使用下载的人脸贴纸')
        ba.find_element_click('xpath', 10, iOS_elements.el_sticker_used)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击屏幕消除贴纸控件')
        actions = TouchAction(sc.driver)
        actions.tap(None, 200, 200).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        # 点拍
        sc.logger.info('拍摄一段5s的视频')
        btn_rec = WebDriverWait(sc.driver, 10).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_cp_self))
        ba.video_capture('点拍', btn_rec, 5)

        sc.logger.info('取消限制弹窗')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.el_cancel)).click()
        except TimeoutException:
            sc.logger.info('限制弹窗已取消')

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()
        sc.logger.info('拍摄-美颜趣拍(全屏)测试完成')
