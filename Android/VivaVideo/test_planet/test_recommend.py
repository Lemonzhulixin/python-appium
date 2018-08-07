# -*- coding: utf-8 -*-
"""小影圈推荐页面的测试用例."""
import time
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestPlanetRec(object):
    """小影圈推荐页的测试类，分步截图."""

    width, heigh = sc.get_size()
    img_path = sc.path_lists[0]

    def test_planet_page(self):
        """小影圈推荐页面初始状态测试."""
        sc.logger.info('小影圈推荐页面初始状态检查开始')
        fun_name = 'test_planet_page'

        sc.logger.info('点击小影圈主按钮')
        p_btn = 'com.quvideo.xiaoying:id/img_find'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(p_btn)).click()

        sc.logger.info('小影圈推荐页面初始状态截图开始')
        sc.capture_screen(fun_name, self.img_path)

    def test_refresh(self):
        """测试下拉刷新."""
        sc.logger.info('推荐页面下拉刷新测试开始')
        fun_name = 'test_refresh'
        start_x = self.width // 2
        start_y = self.heigh // 8

        time.sleep(1)
        result = sc.swipe_by_ratio(start_x, start_y, 'down', 0.6, 700)

        time.sleep(1)
        sc.logger.info('小影圈推荐页面下拉刷新截图开始')
        sc.capture_screen(fun_name, self.img_path)
        assert result is True

    def test_swipe_vertical(self):
        """测试上下方向的滑动."""
        sc.logger.info('推荐页面滑动测试开始')
        fun_name = 'test_swipe_vertical'
        start_x = self.width // 2
        start_y = self.heigh // 8
        start_bottom = self.heigh - start_y

        # 先上滑
        sc.logger.info('上滑截图开始')
        time.sleep(1)
        result_up = sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 500)
        sc.capture_screen(fun_name, self.img_path)

        # 再下滑，同理
        sc.logger.info('下滑截图开始')
        result_down = sc.swipe_by_ratio(start_x, start_y, 'down', 0.3, 500)
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)
        assert result_up and result_down is True

    def test_origin_home(self):
        """推荐页tab的功能."""
        sc.logger.info('推荐页面tab功能检查测试开始')
        fun_name = 'test_origin_home'
        start_x = self.width // 2
        start_bottom = self.heigh - self.heigh // 8

        # 先上滑一点
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)
        sc.logger.info('小影圈推荐页面轻微上滑截图开始')
        sc.capture_screen(fun_name, self.img_path)
        # 再按推荐tab
        sc.logger.info('开始查找小影圈推荐tab')
        WebDriverWait(sc.driver, 30).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("推荐")')).click()
        time.sleep(1)
        sc.logger.info('小影圈推荐页面点击“推荐”tab截图开始')
        sc.capture_screen(fun_name, self.img_path)

    def test_recommend_video(self):
        """测试推荐页面的视频."""
        sc.logger.info('推荐页面视频检查开始')
        fun_name = 'test_recommend_video'

        thumb_img = 'com.quvideo.xiaoying:id/img_video_thumb'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(thumb_img)).click()
        time.sleep(1)
        sc.logger.info('小影圈推荐页面进入视频feed流截图开始')
        sc.capture_screen(fun_name, self.img_path)
        # sc.driver.back()
        sc.logger.info('点击返回键')
        sc.driver.press_keycode(4)

    def test_recommend_user(self):
        """测试推荐页面的用户."""
        sc.logger.info('推荐页面用户检查开始')
        fun_name = 'test_recommend_user'

        avatar_img = 'com.quvideo.xiaoying:id/img_owner_avatar'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(avatar_img)).click()
        time.sleep(1)
        sc.logger.info('小影圈推荐页面点击用户头像进入用户空间截图开始')
        sc.capture_screen(fun_name, self.img_path)
        # sc.driver.back()
        sc.logger.info('点击返回键')
        sc.driver.press_keycode(4)
