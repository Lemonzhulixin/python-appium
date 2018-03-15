# -*- coding: utf-8 -*-
"""创作页的UI检查测试用例"""
import time
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestCreationUI(object):
    """创作页面的测试类，分步截图"""
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_origin(self):
        """测试创作页面初始UI状态"""
        sc.logger.info('创作页面初始状态检查测试开始')
        fun_name = 'test_origin'

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.capture_screen(fun_name, self.img_path)

    def test_refresh(self):
        """测试下拉刷新"""
        sc.logger.info('创作页面下拉刷新测试开始')
        fun_name = 'test_refresh'
        start_x = self.width // 2
        start_y = self.height // 8
        result = sc.swipe_by_ratio(start_x, start_y, 'down', 0.6, 600)

        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)
        assert result is True

    def test_swipe_vertical(self):
        """测试上下方向的滑动"""
        sc.logger.info('创作页面上下滑动测试开始')
        fun_name = 'test_swipe_vertical'
        start_x = self.width // 2
        start_y = self.height // 8
        start_bottom = self.height - start_y

        # 先上滑
        sc.logger.info('上滑截图开始')
        result_up = sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        # 再下滑，同理
        sc.logger.info('下滑截图开始')
        result_down = sc.swipe_by_ratio(start_x, start_y, 'down', 0.7, 300)
        time.sleep(.300)
        sc.capture_screen(fun_name, self.img_path)
        assert result_up and result_down is True

    def test_origin_home(self):
        """测试创作页home tab的功能"""
        sc.logger.info('创作页面home tab功能检查测试开始')
        fun_name = 'test_origin_home'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 8

        # 先上滑一点
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)
        # 再按home tab
        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.capture_screen(fun_name, self.img_path)
