# -*- coding: utf-8 -*-
"""创作页的UI检查测试用例"""
import inspect
import time
from Android import script_ultils as sc


class TestCreationUI(object):
    """创作页面的测试类，分步截图"""
    width, heigh = sc.get_size()

    @staticmethod
    def test_origin():
        """测试创作页面初始UI状态"""
        sc.logger.info(u'创作页面初始状态检查测试开始')
        time.sleep(2)
        el_home = sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/img_creation')
        el_home.click()
        time.sleep(.500)
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        assert el_home is not None

    def test_refresh(self):
        """测试下拉刷新"""
        sc.logger.info(u'创作页面下拉刷新测试开始')
        start_x = self.width // 2
        start_y = self.heigh // 8
        result = sc.swipe_by_ratio(start_x, start_y, 'down', 0.6, 600)

        time.sleep(.300)
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        assert result is True

    def test_swipe_vertical(self):
        """测试上下方向的滑动"""
        sc.logger.info(u'创作页面上下滑动测试开始')
        start_x = self.width // 2
        start_y = self.heigh // 8
        start_bottom = self.heigh - start_y

        # 先上滑
        sc.logger.info(u'上滑截图开始')
        result_up = sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)
        time.sleep(.300)
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        # 再下滑，同理
        sc.logger.info(u'下滑截图开始')
        result_down = sc.swipe_by_ratio(start_x, start_y, 'down', 0.7, 300)
        time.sleep(.300)
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        assert result_up and result_down is True

    def test_origin_home(self):
        """测试创作页home tab的功能"""
        sc.logger.info(u'创作页面home tab功能检查测试开始')
        start_x = self.width // 2
        start_bottom = self.heigh - self.heigh // 8

        # 先上滑一点
        result_up = sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)
        time.sleep(.300)
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        # 再按home tab
        el_home = sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/img_creation')
        el_home.click()
        time.sleep(.300)
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        assert result_up and el_home is not None
