# -*- coding: utf-8 -*-
"""用户空间作品的测试用例."""
import inspect
import time
from selenium.common.exceptions import NoSuchElementException
from Android import script_ultils as sc


class TestUserWorks(object):
    """测试用户空间作品的测试类，分步截图."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_works_ui(self):
        """测试用户空间作品页面的初始状态."""
        sc.logger.info('用户空间作品页面初始状态检查测试开始')
        fun_name = 'test_works_ui'

        time.sleep(1)
        btn_home = 'com.quvideo.xiaoying:id/img_studio'
        el_home = sc.driver.find_element_by_id(btn_home)
        el_home.click()
        time.sleep(.500)

        el_tab_list = sc.driver.find_elements_by_id(
            'com.quvideo.xiaoying:id/text_tab_title')

        for el_tab in el_tab_list:
            if el_tab.text == '作品':
                sc.logger.info('点击“作品”tab')
                el_tab.click()
        sc.logger.info('作品页面初始状态截图开始')
        sc.capture_screen(fun_name, self.img_path)
        assert el_tab is not None

    def test_works_list(self):
        """作品页面list view测试."""
        sc.logger.info('用户空间作品页面list view测试开始')
        fun_name = 'test_works_list'
        start_x = self.width // 2
        start_y = self.height // 4
        start_bottom = self.height - start_y

        time.sleep(1)

        # 先上滑
        sc.logger.info('上滑截图开始')
        result_up = sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)
        time.sleep(.300)
        sc.capture_screen(fun_name, self.img_path)

        # 再下滑，同理
        sc.logger.info('下滑截图开始')
        result_down = sc.swipe_by_ratio(start_x, start_y, 'down', 0.3, 300)
        time.sleep(.300)
        sc.capture_screen(fun_name, self.img_path)

        assert result_up and result_down is True

    def test_works_list_function(self):
        """作品页面list view内功能测试."""
        sc.logger.info('作品页面list view功能测试开始')
        fun_name = 'test_works_list'

        start_x = self.width // 2
        start_bottom = self.height - self.height // 8
        try:
            el_like_btn = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_like')
        except NoSuchElementException:
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)
            time.sleep(.300)
            el_like_btn = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_like')
        # 操作前先截图记录
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击点赞按钮')
        el_like_btn.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击分享按钮')
        el_share_btn = 'com.quvideo.xiaoying:id/xiaoying_com_text_share_count'
        el_share = sc.driver.find_element_by_id(el_share_btn)
        el_share.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击下载按钮')
        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator('text("下载")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.press_keycode(4)

        sc.logger.info('点击公开/不公开按钮')
        time.sleep(1)
        el_more_btn = 'com.quvideo.xiaoying:id/btn_more'
        el_more = sc.driver.find_element_by_id(el_more_btn)
        el_more.click()
        sc.capture_screen(fun_name, self.img_path)
        try:
            el_privacy = sc.driver.find_element_by_android_uiautomator(
                'text("设置为不公开")')
        except NoSuchElementException:
            el_privacy = sc.driver.find_element_by_android_uiautomator(
                'text("设置为公开")')
        el_privacy.click()
        assert el_privacy is not None
