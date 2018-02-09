# -*- coding: utf-8 -*-
"""小影圈搜索页面的测试用例"""
import inspect
import time
from selenium.common.exceptions import NoSuchElementException
from Android import script_ultils as sc


class TestCircleSearch(object):
    """小影圈搜索页的测试类，分步截图."""

    width, heigh = sc.get_size()

    def test_search_page(self):
        """小影圈搜索页面输入状态测试."""
        start_x = self.width // 2
        start_bottom = self.heigh - self.heigh // 8
        sc.logger.info('小影圈搜索页面输入状态测试开始')
        time.sleep(2)
        sc.logger.info('开始查找小影圈按钮')
        el_cicle = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_find')
        el_cicle.click()

        time.sleep(.500)
        sc.logger.info('开始查找小影圈搜索按钮')
        el_search_btn = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_search')
        el_search_btn.click()

        time.sleep(1)
        sc.logger.info('开始向小影圈搜索框输入字符a')
        el_search_edit = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/edittext_search')
        el_search_edit.click()
        sc.driver.press_keycode(29)

        time.sleep(.500)
        sc.logger.info('开始查找输入框补全内容')
        el_search_sup = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/textview_keyword')
        sc.logger.info('小影圈搜索框输入文字"a"截图开始')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        sc.logger.info('点击第一条自动联想内容')
        el_search_sup.click()

        time.sleep(2)
        sc.logger.info('开始查找搜索结果中的用户')
        res_user_id = 'com.quvideo.xiaoying:id/img_simple_user_avatar_click'
        el_res_user = sc.driver.find_element_by_id(res_user_id)

        sc.logger.info('开始查找搜索结果中的视频')
        res_video_id = 'com.quvideo.xiaoying:id/xiaoying_com_img_video_thumb'
        el_res_video = sc.driver.find_element_by_id(res_video_id)

        sc.logger.info('小影圈搜索结果截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)
        sc.logger.info('小影圈搜索结果下滑截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        assert el_res_user and el_res_video is not None

    def test_search_result(self):
        """小影圈搜索结果测试，为了简化流程，请与上一条连起来用."""
        sc.logger.info('小影圈搜索结果测试开始')
        start_x = self.width - self.width // 4
        start_bottom = self.heigh - self.heigh // 8

        # 左滑一次
        sc.logger.info('开始左滑至“视频”页面')
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.7, 300)
        time.sleep(.500)
        sc.logger.info('开始查找搜索结果视频页面中的视频')
        res_video_id = 'com.quvideo.xiaoying:id/xiaoying_com_img_video_thumb'
        el_res_videos = sc.driver.find_element_by_id(res_video_id)
        sc.logger.info('小影圈搜索结果视频页面截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.3, 300)
        time.sleep(.500)
        sc.logger.info('小影圈搜索结果视频页面下滑截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        # 再左滑一次
        sc.logger.info('开始滑动至“用户”页面')
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.7, 300)
        time.sleep(.500)
        sc.logger.info('开始查找搜索结果用户页面中的第一个用户')
        res_user_id = 'com.quvideo.xiaoying:id/fans_name'
        el_res_users = sc.driver.find_element_by_id(res_user_id)
        sc.logger.info('小影圈搜索结果用户页面截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.3, 300)
        sc.logger.info('小影圈搜索结果用户界面下滑截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        assert el_res_videos and el_res_users is not None

    def test_search_follow(self):
        """小影圈搜索结果中的关注测试，为了简化流程，请与上一条连起来用."""
        sc.logger.info('小影圈搜索结果，关注测试开始')
        start_x = self.width // 4
        start_bottom = self.heigh // 2

        # 查找用户关注按钮
        time.sleep(.500)
        sc.logger.info('开始查找搜索结果用户页面中的第一个用户关注按钮')
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.3, 300)
        el_fol_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/btn_follow_state')
        # sc.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")')
        for el_res_fol in el_fol_list:
            if el_res_fol.text == '关注':
                sc.logger.info('开始点击关注')
                el_res_fol.click()
                break
        el_res_fol = sc.driver.find_element_by_android_uiautomator('new UiSelector().text("已关注")')
        sc.logger.info('小影圈搜索结果，用户页面关注情况截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        # 取消关注
        time.sleep(.500)
        sc.logger.info('开始取消关注')
        el_res_fol.click()

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/buttonDefaultPositive').click()
        el_res_fol = sc.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")')
        sc.logger.info('小影圈搜索结果，用户页面取消关注后情况截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        # 切换到视频页面
        sc.logger.info('开始滑动至“视频”页面')
        sc.swipe_by_ratio(start_x, start_bottom, 'right', 0.7, 300)

        # 查找关注按钮
        time.sleep(.500)
        sc.logger.info('开始查找搜索结果视频页面中的第一个关注按钮')

        el_follow = 'com.quvideo.xiaoying:id/btn_follow_state'
        while sc.driver.find_elements_by_id(el_follow) is None:
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.3, 300)
            sc.driver.find_elements_by_id(el_follow)

        el_vf_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/btn_follow_state')
        fl_flag = True
        for el_res_vf in el_vf_list:
            if el_res_vf.text == '关注':
                sc.logger.info('开始点击关注')
                el_res_vf.click()
                fl_flag = True if el_res_vf.text == '已关注' else False
                break
        # el_res_vf = sc.driver.find_element_by_android_uiautomator('new UiSelector().text("已关注")')
        sc.logger.info('小影圈搜索结果，视频页面关注情况截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        assert el_res_fol and fl_flag is not None

    @staticmethod
    def test_search_history():
        """小影圈搜索页面历史记录搜索测试，为了简化流程，请与上一条连起来用."""
        sc.logger.info('小影圈搜索页面历史记录搜索测试开始')

        time.sleep(1)
        sc.logger.info('开始查找搜索框')
        el_search_edit = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/edittext_search')
        el_search_edit.click()

        sc.logger.info('开始查找清除输入按钮')
        el_search_edit = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_clear_edit')
        el_search_edit.click()

        time.sleep(.500)
        sc.logger.info('小影圈搜索框历史记录截图开始')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])
        sc.logger.info('开始查找第一条历史记录')
        res_his_id = 'com.quvideo.xiaoying:id/text_history_list_item'
        el_search_his = sc.driver.find_element_by_id(res_his_id)
        sc.logger.info('点击第一条历史记录')
        el_search_his.click()

        time.sleep(2)
        sc.logger.info('开始查找历史记录搜索结果中的视频')
        try:
            res_video_id = 'com.quvideo.xiaoying:id/xiaoying_com_img_video_thumb'
            el_res_video = sc.driver.find_element_by_id(res_video_id)
        except NoSuchElementException:
            res_video_desc = 'com.quvideo.xiaoying:id/xiaoying_com_text_video_desc'
            el_res_video = sc.driver.find_elements_by_id(res_video_desc)

        sc.logger.info('小影圈历史记录搜索结果截图')
        sc.capture_screen(inspect.stack()[0][3], sc.path_lists[0])

        sc.logger.info('测试完成返回主页')
        sc.driver.press_keycode(4)
        assert el_res_video is not None
