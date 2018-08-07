# -*- coding: utf-8 -*-
"""camera的基本操作测试用例."""
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba

class TestCameraNormal(TestCase):
    """camera的基本操作测试类."""

    # 获取屏幕尺寸
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def setUp(self):
        sc.driver.launch_app()
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        sc.driver.close_app()

    def test_normal_01_filter(self):
        """拍摄-滤镜下载."""
        sc.logger.info('拍摄-滤镜下载')
        fun_name = 'test_normal_filter_download'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击“高清拍摄”按钮')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_home_camera)).click()

        sc.logger.info('点击滤镜图标')
        time.sleep(1)
        ba.find_element_click('name', 5, iOS_elements.el_filter_icon)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载滤镜')
        try:
            sc.logger.info('点击下载按钮')
            sc.driver.find_element_by_xpath(iOS_elements.el_filter_download).click()
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('当前页面已无未下载滤镜')

        sc.logger.info('下载更多')
        try:
            time.sleep(0.5)
            sc.driver.find_element_by_name(iOS_elements.el_filter_more).click()
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('当前页面是vip订阅页面')
            sc.driver.find_element_by_name(iOS_elements.el_vip_close).click()
            sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('重新点击下载更多')
            sc.driver.find_element_by_name(iOS_elements.el_filter_more).click()
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('退出更多页面')
        ba.find_element_click('xpath', 10, iOS_elements.el_studio_back)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('退出拍摄')
        ba.find_element_click('name', 5, iOS_elements.el_cam_close)
        sc.logger.info('拍摄-滤镜下载测试完成')

    def test_normal_02_settings(self):
        """拍摄-设置相关."""
        sc.logger.info('拍摄-设置相关')
        fun_name = 'test_camera_normal_settings'

        sc.logger.info('点击“高清拍摄”按钮')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_home_camera)).click()

        sc.logger.info('点击设置按钮')
        time.sleep(1)
        sc.driver.find_element_by_name(iOS_elements.el_cam_setting).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('闪光灯-开')
        try:
            ba.find_element_click('name', 5, iOS_elements.el_cam_flash)
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('当前为前置拍摄，无闪光灯选项')

        sc.logger.info('网格显示')
        ba.find_element_click('name', 5, iOS_elements.el_cam_grid)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('倒计时')
        for i in range(4):
            ba.find_element_click('name', 5, iOS_elements.el_cam_time)
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('退出设置选项')
        ba.find_element_click('name', 5, iOS_elements.el_cam_setting)

        sc.logger.info('前后置切换')
        ba.find_element_click('name', 5, iOS_elements.el_cam_switch)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('视频尺寸,全屏切换到3:4')
        ba.find_element_click('name', 5, iOS_elements.el_ful)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('视频尺寸,3:4切换到1:1')
        ba.find_element_click('name', 5, iOS_elements.el_fou)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('视频尺寸,1:1切换到全屏')
        ba.find_element_click('name', 5, iOS_elements.el_one)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换拍摄模式:高清相机->自拍美颜')
        el_self = "自拍美颜"
        el_normal = "高清相机"
        el_music = "音乐视频"
        ba.find_element_click('name', 5, el_self)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换拍摄模式:自拍美颜->高清相机')
        ba.find_element_click('name', 5, el_normal)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换拍摄模式:高清相机->音乐视频')
        ba.find_element_click('name', 5, el_music)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('退出拍摄')
        ba.find_element_click('name', 5, iOS_elements.el_cam_close)
        sc.logger.info('拍摄-设置相关测试完成')

    def test_normal_03_shot(self):
        """拍摄-高清相机(前置1:1)."""
        sc.logger.info('拍摄-高清相机(前置1:1)')
        fun_name = 'test_camera_normal_shot'

        sc.logger.info('点击“高清拍摄”按钮')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_home_camera)).click()

        sc.logger.info('切换到前置')
        time.sleep(1)
        sc.driver.find_element_by_name(iOS_elements.el_cam_switch).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换到1:1')
        ba.find_element_click('name', 5, iOS_elements.el_ful)
        ba.find_element_click('name', 5, iOS_elements.el_fou)
        sc.capture_screen(fun_name, self.img_path)

        # 点拍
        sc.logger.info('拍摄一段5s的视频')
        btn_rec = WebDriverWait(sc.driver, 10).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_cp_normal))
        ba.video_capture('点拍', btn_rec, 5)

        sc.logger.info('取消限制弹窗')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.el_cancel)).click()
        except TimeoutException:
            sc.logger.info('限制弹窗已取消')

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('拍摄-高清相机拍摄完成')
