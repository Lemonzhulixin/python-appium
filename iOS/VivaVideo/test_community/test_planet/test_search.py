# -*- coding: utf-8 -*-
"""小影圈搜索页面的测试用例"""
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestCircleSearch(object):
    """小影圈搜索页的测试类，分步截图."""

    width, heigh = sc.get_size()
    img_path = sc.path_lists[0]

    def test_search_page(self):
        """小影圈搜索页面输入状态测试."""
        sc.logger.info('小影圈搜索页面输入状态测试开始')
        fun_name = 'test_search_page'
        start_x = self.width // 2
        start_bottom = self.heigh - self.heigh // 8

        sc.logger.info('点击小影圈主按钮')
        p_btn = 'com.quvideo.xiaoying:id/img_find'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(p_btn)).click()

        sc.logger.info('开始查找小影圈搜索按钮')
        search_btn = 'com.quvideo.xiaoying:id/btn_search'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(search_btn)).click()

        sc.logger.info('开始向小影圈搜索框输入字符a')
        search_frame = 'com.quvideo.xiaoying:id/edittext_search'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(search_frame)).click()
        sc.driver.press_keycode(29)
        sc.logger.info('小影圈搜索框输入文字"a"截图开始')
        sc.capture_screen(fun_name, self.img_path)
        # sc.driver.hide_keyboard()

        # sc.driver.press_keycode(4)
        sc.logger.info('开始查找输入框补全内容')
        keyword_frame = 'com.quvideo.xiaoying:id/textview_keyword'
        sc.logger.info('点击第一条自动联想内容')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(keyword_frame)).click()

        time.sleep(2)
        sc.logger.info('开始查找搜索结果中的用户')
        res_user_id = 'com.quvideo.xiaoying:id/img_simple_user_avatar_click'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(res_user_id))

        sc.logger.info('开始查找搜索结果中的视频')
        res_video_id = 'com.quvideo.xiaoying:id/xiaoying_com_img_video_thumb'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(res_video_id)).click()

        sc.logger.info('小影圈搜索结果截图')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('小影圈搜索结果下滑截图')
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 500)
        sc.capture_screen(fun_name, self.img_path)

    def test_search_result(self):
        """小影圈搜索结果测试，为了简化流程，请与上一条连起来用."""
        sc.logger.info('小影圈搜索结果测试开始')
        fun_name = 'test_search_result'
        start_x = self.width - self.width // 4
        start_bottom = self.heigh - self.heigh // 8

        # 左滑一次
        sc.logger.info('开始左滑至“视频”页面')
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.7, 500)
        time.sleep(1)
        sc.logger.info('开始查找搜索结果视频页面中的视频')
        res_video_id = 'com.quvideo.xiaoying:id/xiaoying_com_img_video_thumb'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(res_video_id)).click()
        sc.logger.info('小影圈搜索结果视频页面截图')
        sc.capture_screen(fun_name, self.img_path)

        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.4, 500)
        time.sleep(1)
        sc.logger.info('小影圈搜索结果视频页面下滑截图')
        sc.capture_screen(fun_name, self.img_path)

        # 再左滑一次
        sc.logger.info('开始滑动至“用户”页面')
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.7, 500)

        sc.logger.info('开始查找搜索结果用户页面中的第一个用户')
        res_user_id = 'com.quvideo.xiaoying:id/fans_name'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(res_user_id))
        sc.logger.info('小影圈搜索结果用户页面截图')
        sc.capture_screen(fun_name, self.img_path)

        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.3, 500)
        sc.logger.info('小影圈搜索结果用户界面下滑截图')
        sc.capture_screen(fun_name, self.img_path)

    def test_search_follow(self):
        """小影圈搜索结果中的关注测试，为了简化流程，请与上一条连起来用."""
        sc.logger.info('小影圈搜索结果，关注测试开始')
        fun_name = 'test_search_follow'
        start_x = self.width // 4
        start_bottom = self.heigh // 2

        # 查找用户关注按钮
        time.sleep(1)
        sc.logger.info('开始查找搜索结果用户页面中的第一个用户关注按钮')
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.3, 500)

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("关注")')).click()

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("已关注")')).click()

        sc.logger.info('小影圈搜索结果，用户页面关注情况截图')
        sc.capture_screen(fun_name, self.img_path)

        # 取消关注
        sc.logger.info('开始取消关注')

        pos_btn = 'com.quvideo.xiaoying:id/buttonDefaultPositive'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(pos_btn)).click()

        sc.logger.info('小影圈搜索结果，用户页面取消关注后情况截图')
        sc.capture_screen(fun_name, self.img_path)

    def test_search_history(self):
        """小影圈搜索页面历史记录搜索测试，为了简化流程，请与上一条连起来用."""
        sc.logger.info('小影圈搜索页面历史记录搜索测试开始')
        fun_name = 'test_search_history'

        time.sleep(1)
        sc.logger.info('开始查找搜索框')
        search_frame = 'com.quvideo.xiaoying:id/edittext_search'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(search_frame)).click()

        sc.logger.info('开始查找清除输入按钮')
        clear_btn = 'com.quvideo.xiaoying:id/btn_clear_edit'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(clear_btn)).click()

        time.sleep(1)
        sc.logger.info('小影圈搜索框历史记录截图开始')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('开始查找第一条历史记录')
        res_his_id = 'com.quvideo.xiaoying:id/text_history_list_item'
        sc.logger.info('点击第一条历史记录')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(res_his_id)).click()

        sc.logger.info('开始查找历史记录搜索结果中的视频')
        try:
            video_id = 'com.quvideo.xiaoying:id/xiaoying_com_img_video_thumb'
            el_res_video = sc.driver.find_element_by_id(video_id)
        except NoSuchElementException:
            video_desc = 'com.quvideo.xiaoying:id/xiaoying_com_text_video_desc'
            el_res_video = sc.driver.find_elements_by_id(video_desc)

        sc.logger.info('小影圈历史记录搜索结果截图')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('测试完成返回主页')
        sc.driver.press_keycode(4)
        assert el_res_video is not None
