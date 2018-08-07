# -*- coding: utf-8 -*-
"""配音的基本操作测试用例."""
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from Android_old import script_ultils as sc


class TestEditSound(object):
    """配音的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_sound_add(self):
        """剪辑-配音-添加."""
        sc.logger.info('剪辑-配音-添加')
        fun_name = 'test_edit_sound_add'

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

        sc.logger.info('开始点击配音和音效')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("配音和音效")')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('开始录音')
        record_btn = 'com.quvideo.xiaoying:id/ll_editor_audio_record_touch'

        try:
            sc.logger.info('点击录音按钮')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda c_btn: c_btn.find_element_by_android_uiautomator(
                    'text("删除")')).click()
        except TimeoutException:
            el_record = WebDriverWait(sc.driver, 10, 1).until(
                lambda c_btn: c_btn.find_element_by_id(record_btn))

        co_x = el_record.location.get('x') + el_record.size.get('width') / 2
        co_y = el_record.location.get('y') + el_record.size.get('height') / 2

        sc.driver.tap([(co_x, co_y)], 3000)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认')
        right_btn = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 60, 1).until(
            lambda el: el.find_element_by_id(right_btn)).click()

        """
        x = record.location.get('x')
        y = record.location.get('y')
        sc.driver.swipe(x, y, x, y, 5000)

        sc.logger.info('点击添加音频的按钮')
        au_add_btn = 'com.quvideo.xiaoying:id/xiaoying_ve_imgbtn_add_audio_dub'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(au_add_btn)).click()

        music_row = 'com.quvideo.xiaoying:id/musiclist_title'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(music_row)).click()

        music_add_btn = 'com.quvideo.xiaoying:id/btn_add_music'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(music_add_btn)).click()
        """

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-配音-添加测试完成')

    def test_edit_sound_del(self):
        """剪辑-配音-删除."""
        sc.logger.info('剪辑-配音-删除')
        fun_name = 'test_edit_sound_del'

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

        sc.logger.info('开始点击配音和音效')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("配音和音效")')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除原有音效')
        try:
            sc.capture_screen(fun_name, self.img_path)
            WebDriverWait(sc.driver, 5, 1).until(
                lambda c_btn: c_btn.find_element_by_android_uiautomator(
                    'text("删除")')).click()
        except TimeoutException:
            sc.logger.info('该视频没有添加音效，跳过')

        sc.logger.info('点击确认')
        right_btn = 'com.quvideo.xiaoying:id/terminator_right'
        sc.capture_screen(fun_name, self.img_path)
        WebDriverWait(sc.driver, 60, 1).until(
            lambda el: el.find_element_by_id(right_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-配音-删除测试完成')

    def test_edit_sound_cancel(self):
        """剪辑-配音-放弃."""
        sc.logger.info('剪辑-配音-放弃')
        fun_name = 'test_edit_sound_cancel'

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

        sc.logger.info('开始点击配音和音效')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("配音和音效")')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('开始录音')
        record_btn = 'com.quvideo.xiaoying:id/ll_editor_audio_record_touch'
        try:
            sc.logger.info('点击录音按钮')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda c_btn: c_btn.find_element_by_android_uiautomator(
                    'text("删除")')).click()
        except TimeoutException:
            el_record = WebDriverWait(sc.driver, 10, 1).until(
                lambda c_btn: c_btn.find_element_by_id(record_btn))

        co_x = el_record.location.get('x') + el_record.size.get('width') / 2
        co_y = el_record.location.get('y') + el_record.size.get('height') / 2

        sc.driver.tap([(co_x, co_y)], 3000)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认')
        left_btn = 'com.quvideo.xiaoying:id/terminator_left'
        WebDriverWait(sc.driver, 60, 1).until(
            lambda el: el.find_element_by_id(left_btn)).click()

        pos_btn = 'com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive'
        WebDriverWait(sc.driver, 60, 1).until(
            lambda el: el.find_element_by_id(pos_btn)).click()

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-配音-放弃测试完成')
