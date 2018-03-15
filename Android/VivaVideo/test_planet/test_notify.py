# -*- coding: utf-8 -*-
"""小影圈通知页面的测试用例"""
import time

from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestPlanetNotify(object):
    """小影圈通知页的测试类，分步截图."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_planet_notify_ui(self):
        """小影圈推荐页面初始状态测试."""
        sc.logger.info('小影圈推荐页面初始状态检查开始')
        fun_name = 'test_planet_notify_ui'

        sc.logger.info('点击小影圈主按钮')
        p_btn = 'com.quvideo.xiaoying:id/img_find'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(p_btn)).click()

        sc.logger.info('开始查找小影圈消息中心图标')
        message_btn = 'com.quvideo.xiaoying:id/btn_message'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(message_btn)).click()

        time.sleep(5)
        sc.logger.info('小影圈推荐页面初始状态截图开始')
        sc.capture_screen(fun_name, self.img_path)

    def test_notify_activity(self):
        """测试消息中心动态."""
        sc.logger.info('开始测试消息中心动态')
        fun_name = 'test_notify_activity'

        time.sleep(3)
        pager_tab = 'com.quvideo.xiaoying:id/text_viewpager_tab'
        el_tab_list = sc.driver.find_elements_by_id(pager_tab)
        for el_tab in el_tab_list:
            if el_tab.text == '动态':
                el_tab.click()
                break
        sc.logger.info('消息中心动态页截图')
        sc.capture_screen(fun_name, self.img_path)
        assert el_tab is not None

    def test_notify_info(self):
        """测试消息中心通知页."""
        sc.logger.info('开始测试消息中心通知页.')
        fun_name = 'test_notify_info'

        time.sleep(1)
        pager_tab = 'com.quvideo.xiaoying:id/text_viewpager_tab'
        el_tab_list = sc.driver.find_elements_by_id(pager_tab)
        for el_tab in el_tab_list:
            if el_tab.text == '通知':
                el_tab.click()
                break
        sc.logger.info('消息中心通知页截图')
        sc.capture_screen(fun_name, self.img_path)
        assert el_tab is not None

    def test_notify_message(self):
        """测试消息中心动态."""
        sc.logger.info('开始测试消息中心私信.')
        fun_name = 'test_notify_message'

        time.sleep(1)
        pager_tab = 'com.quvideo.xiaoying:id/text_viewpager_tab'
        el_tab_list = sc.driver.find_elements_by_id(pager_tab)
        for el_tab in el_tab_list:
            if el_tab.text == '私信':
                el_tab.click()
                break
        sc.logger.info('消息中心私信页截图')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('通知中心测试完成，返回主页')
        sc.driver.press_keycode(4)
        assert el_tab is not None
