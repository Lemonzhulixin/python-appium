# -*- coding: utf-8 -*-
"""创作页面内分享相关的测试用例."""
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from Android import script_ultils as sc


class TestCreationShare(object):
    """创作页面内分享相关的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_share_create(self):
        """分享-创建视频."""
        sc.logger.info('分享-创建视频')
        fun_name = 'test_share_create'

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()
        el_cp = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')

        # 长按拍摄
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()

        next_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(next_btn)).click()

        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('分享-创建视频完成')

    def test_share_edit(self):
        """分享-编辑视频标题/话题相关."""
        sc.logger.info('分享-编辑视频标题/话题相关')
        fun_name = 'test_share_edit'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        sc.logger.info('添加标题')
        text_input = 'com.quvideo.xiaoying:id/share_video_title_text'
        el_title = sc.driver.find_element_by_id(text_input)
        el_title.clear()
        el_title.send_keys('video title test')

        sc.logger.info('添加话题')
        topic_btn = 'com.quvideo.xiaoying:id/share_btn_add_topic'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(topic_btn)).click()

        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)

        name_tag = 'com.quvideo.xiaoying:id/txtview_tag_name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(name_tag)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('隐私设置')
        privacy_btn = 'com.quvideo.xiaoying:id/share_btn_privacy'
        sc.driver.find_element_by_id(privacy_btn).click()

        vis_btn = 'com.quvideo.xiaoying:id/private_setting_visible_btn'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(vis_btn)).click()

        down_btn = 'com.quvideo.xiaoying:id/private_setting_candnload_btn'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(down_btn)).click()

        pos_btn = 'com.quvideo.xiaoying:id/buttonDefaultPositive'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(pos_btn)).click()
        sc.logger.info('导出-导出页编辑测试完成')

    def test_share_upload(self):
        """导出-分享上传."""
        sc.logger.info('导出-分享上传')
        fun_name = 'test_share_upload'

        share_btn = 'com.quvideo.xiaoying:id/share_btn_share'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(share_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        try:
            neg_btn = 'com.quvideo.xiaoying:id/buttonDefaultNegative'
            WebDriverWait(sc.driver, 5).until(
                lambda el: el.find_element_by_id(neg_btn)).click()
        except TimeoutException:
            sc.logger.info('硬件加速已经打开')

        try:
            qq_sns = 'com.quvideo.xiaoying:id/textview_id_sns_qqspace'
            WebDriverWait(sc.driver, 180).until(
                lambda el: el.find_element_by_id(qq_sns)).click()
            time.sleep(5)
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.press_keycode(4)
        except TimeoutError as t:
            sc.logger.error('导出视频超时', t)
            sc.driver.press_keycode(4)
            return False
        time.sleep(1)
        sc.driver.press_keycode(4)
        sc.logger.info('导出-分享上传完成')
