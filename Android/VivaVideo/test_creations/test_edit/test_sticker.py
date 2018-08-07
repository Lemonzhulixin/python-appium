# -*- coding: utf-8 -*-
"""动画贴纸的测试用例."""
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from Android_old import script_ultils as sc


class TestEditSticker(object):
    """动画贴纸的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_sticker_add(self):
        """剪辑-动画贴纸-添加."""
        sc.logger.info('剪辑-动画贴纸-添加')
        fun_name = 'test_edit_sticker_add'

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_img)).click()

        sc.logger.info('尝试点击“编辑该视频”')
        edit_btn = 'com.quvideo.xiaoying:id/edit_this_video_text'
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(edit_btn)).click()
        except TimeoutException:
            sc.logger.info('该视频已经在编辑页，跳过此步骤')

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("效果")')).click()

        sc.logger.info('开始点击贴纸')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("贴纸")')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击一张贴纸')
        stick_class = 'android.widget.RelativeLayout'
        stick_id = 'com.quvideo.xiaoying:id/item_layout'
        s_list = sc.driver.find_elements_by_class_name(stick_class)
        st_list = list()
        for item in s_list:
            if item.get_attribute('resourceId') == stick_id:
                st_list.append(item)
        st_list[-2].click()
        sc.capture_screen(fun_name, self.img_path)

        btn_right = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(btn_right)).click()

        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(btn_right)).click()

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)

        sc.logger.info('剪辑-动画贴纸-添加测试完成')

    def test_edit_sticker_cancel(self):
        """剪辑-动画贴纸-放弃."""
        sc.logger.info('剪辑-动画贴纸-放弃')
        fun_name = 'test_edit_sticker_cancel'

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_img)).click()

        sc.logger.info('尝试点击“编辑该视频”')
        edit_btn = 'com.quvideo.xiaoying:id/edit_this_video_text'
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(edit_btn)).click()
        except TimeoutException:
            sc.logger.info('该视频已经在编辑页，跳过此步骤')

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("效果")')).click()

        sc.logger.info('开始点击贴纸')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("贴纸")')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击一张贴纸')
        stick_class = 'android.widget.RelativeLayout'
        stick_id = 'com.quvideo.xiaoying:id/item_layout'
        s_list = sc.driver.find_elements_by_class_name(stick_class)
        st_list = list()
        for item in s_list:
            if item.get_attribute('resourceId') == stick_id:
                st_list.append(item)
        st_list[-1].click()
        sc.capture_screen(fun_name, self.img_path)

        btn_right = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(btn_right)).click()

        btn_left = 'com.quvideo.xiaoying:id/terminator_left'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(btn_left)).click()
        sc.capture_screen(fun_name, self.img_path)

        pos_btn = 'com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(pos_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-动画贴纸-放弃测试完成')
