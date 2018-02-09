# -*- coding: utf-8 -*-
"""用户空间粉丝页面的测试用例"""
import time
from Android import script_ultils as sc


class TestUserFans(object):
    """测试用户空间粉丝的测试类，分步截图."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_user_fans(self):
        """测试用户空间粉丝页面的初始状态."""
        sc.logger.info('用户空间粉丝页面初始状态检查测试开始')
        fun_name = 'test_user_fans'

        time.sleep(1)
        btn_home = 'com.quvideo.xiaoying:id/img_studio'
        el_home = sc.driver.find_element_by_id(btn_home)
        el_home.click()
        time.sleep(.500)

        el_tab_list = sc.driver.find_elements_by_id(
            'com.quvideo.xiaoying:id/text_tab_title')

        for el_tab in el_tab_list:
            if el_tab.text == '粉丝':
                sc.logger.info('点击“粉丝”tab')
                el_tab.click()
        sc.logger.info('粉丝页面初始状态截图开始')
        sc.capture_screen(fun_name, self.img_path)
        assert el_tab is not None

    def test_fans_follow(self):
        """粉丝关注/取消关注测试."""
        sc.logger.info('用户空间粉丝页面关注状态测试开始')
        fun_name = 'test_fans_follow'

        time.sleep(1)
        btn_follow = 'com.quvideo.xiaoying:id/btn_follow_state'
        el_btn_follow = sc.driver.find_element_by_id(btn_follow)
        if el_btn_follow.text == '已关注':
            sc.logger.info('点击第一个已关注状态按钮')
            el_btn_follow.click()
            el_btn_yes = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/buttonDefaultPositive')
            el_btn_yes.click()
            sc.logger.info('第一次取消点击后，关注状态截图')
            sc.capture_screen(fun_name, self.img_path)
        else:
            sc.logger.info('点击第一个关注状态按钮')
            el_btn_follow.click()
            sc.logger.info('第一次点击关注后，关注状态截图')
            sc.capture_screen(fun_name, self.img_path)
        assert el_btn_follow is not None

    def test_fans_home(self):
        """点击粉丝头像进入粉丝空间测试."""
        sc.logger.info('粉丝空间空间测试')
        fun_name = 'test_fans_home'

        time.sleep(.500)
        el_avatar = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/avatar_img')
        el_avatar.click()
        sc.logger.info('点击粉丝头像后，进入粉丝空间截图')
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.press_keycode(4)
        assert el_avatar is not None

    def test_fans_list(self):
        """粉丝页面上下滑动测试."""
        sc.logger.info('用户空间作品页面上下滑动测试开始')
        fun_name = 'test_fans_list'
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
