# -*- coding: utf-8 -*-
"""小影圈发现页面的测试用例."""
import time
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestPlanetExploreUI(object):
    """小影圈发现页UI的测试类，分步截图."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_planet_page(self):
        """小影圈发现页面初始状态测试."""
        sc.logger.info('小影圈发现页面初始状态检查开始')
        fun_name = 'test_planet_page'

        sc.logger.info('点击小影圈主按钮')
        p_btn = 'com.quvideo.xiaoying:id/img_find'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(p_btn)).click()

        time.sleep(1)
        sc.logger.info('开始查找小影圈发现tab')
        el_tab_list = sc.driver.find_elements_by_id('android:id/text1')
        for el_tab in el_tab_list:
            if el_tab.text == '发现':
                sc.logger.info('点击“发现”tab')
                el_tab.click()
                break
        sc.logger.info('小影圈发现页面初始状态截图开始')
        sc.capture_screen(fun_name, self.img_path)
        assert el_tab is not None

    def test_refresh(self):
        """测试下拉刷新."""
        sc.logger.info('发现页面下拉刷新测试开始')
        start_x = self.width // 2
        start_y = self.height // 8
        fun_name = 'test_refresh'

        time.sleep(1)
        result = sc.swipe_by_ratio(start_x, start_y, 'down', 0.6, 600)

        sc.logger.info('小影圈发现页面下拉刷新截图开始')
        sc.capture_screen(fun_name, self.img_path)
        assert result is True

    def test_swipe_vertical(self):
        """测试上下方向的滑动."""
        sc.logger.info('发现页面滑动测试开始')
        start_x = self.width // 2
        start_y = self.height // 8
        start_bottom = self.height - start_y
        fun_name = 'test_swipe_vertical'

        # 先上滑
        sc.logger.info('上滑截图开始')
        result_up = sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        # 再下滑，同理
        sc.logger.info('下滑截图开始')
        result_down = sc.swipe_by_ratio(start_x, start_y, 'down', 0.3, 300)
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)
        assert result_up and result_down is True

    def test_origin_home(self):
        """发现页tab的功能."""
        sc.logger.info('发现页面tab功能检查测试开始')
        start_x = self.width // 2
        start_bottom = self.height - self.height // 8
        fun_name = 'test_origin_home'

        # 先上滑一点
        result_up = sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)
        time.sleep(1)
        sc.logger.info('小影圈发现页面轻微上滑截图开始')
        sc.capture_screen(fun_name, self.img_path)
        # 再按发现tab
        sc.logger.info('开始查找小影圈发现tab')
        el_tab_list = sc.driver.find_elements_by_id('android:id/text1')
        for el_tab in el_tab_list:
            if el_tab.text == '发现':
                sc.logger.info('点击“发现”tab')
                el_tab.click()
                break
        time.sleep(1)
        sc.logger.info('小影圈发现页面点击“发现”tab截图开始')
        sc.capture_screen(fun_name, self.img_path)
        assert result_up and el_tab is not None
