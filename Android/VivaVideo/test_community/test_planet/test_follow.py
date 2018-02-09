# -*- coding: utf-8 -*-
"""小影圈关注页面的测试用例"""
import inspect
import time
from Android import script_ultils as sc


class TestPlanetExploreUI(object):
    """小影圈关注页UI的测试类，分步截图."""

    width, heigh = sc.get_size()

    @staticmethod
    def test_planet_page():
        """小影圈关注页面初始状态测试."""
        sc.logger.info('小影圈关注页面初始状态检查开始')
        time.sleep(2)
        sc.logger.info('开始查找小影圈按钮')
        el_planet = sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/img_find')
        el_planet.click()
        time.sleep(.500)
        sc.logger.info('开始查找小影圈关注tab')
        el_tab_list = sc.driver.find_elements_by_id('android:id/text1')
        for el_tab in el_tab_list:
            if el_tab.text == '关注':
                sc.logger.info('点击“关注”tab')
                el_tab.click()
                break
        sc.logger.info('小影圈关注页面初始状态截图开始')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        assert el_tab is not None

    def test_refresh(self):
        """测试下拉刷新."""
        sc.logger.info('关注页面下拉刷新测试开始')
        start_x = self.width // 2
        start_y = self.heigh // 8
        result = sc.swipe_by_ratio(start_x, start_y, 'down', 0.6, 600)

        time.sleep(.300)
        sc.logger.info('小影圈关注页面下拉刷新截图开始')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        assert result is True

    def test_swipe_vertical(self):
        """测试上下方向的滑动."""
        sc.logger.info('关注页面滑动测试开始')
        start_x = self.width // 2
        start_y = self.heigh // 8
        start_bottom = self.heigh - start_y

        # 先上滑
        sc.logger.info('上滑截图开始')
        result_up = sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)
        time.sleep(.300)
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        # 再下滑，同理
        sc.logger.info('下滑截图开始')
        result_down = sc.swipe_by_ratio(start_x, start_y, 'down', 0.3, 300)
        time.sleep(.300)
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        assert result_up and result_down is True

    def test_origin_home(self):
        """关注页tab的功能."""
        sc.logger.info('关注页面tab功能检查测试开始')
        start_x = self.width // 2
        start_bottom = self.heigh - self.heigh // 8

        # 先上滑一点
        result_up = sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)
        time.sleep(.300)
        sc.logger.info('小影圈关注页面轻微上滑截图开始')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        # 再按关注tab
        sc.logger.info('开始查找小影圈关注tab')
        el_tab_list = sc.driver.find_elements_by_id('android:id/text1')
        for el_tab in el_tab_list:
            if el_tab.text == '关注':
                sc.logger.info('点击“关注”tab')
                el_tab.click()
                break
        time.sleep(.300)
        sc.logger.info('小影圈关注页面点击“关注”tab截图开始')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        assert result_up and el_tab is not None
