# -*- coding: utf-8 -*-
"""编辑音乐相关操作测试用例."""
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestEditMusic(object):
    """音乐相关操作测试测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_music_add(self):
        """剪辑-多段配乐-添加."""
        sc.logger.info('剪辑-多段配乐-添加')
        fun_name = 'test_music_add'

        start_x = self.width // 2
        start_bottom = self.height // 4

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

        sc.logger.info('开始点击多段配乐')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("多段配乐")')).click()

        m_add_btn = 'com.quvideo.xiaoying:id/tv_editor_audio_operation'
        sc.logger.info('点击添加音乐按钮')
        el_op = WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(m_add_btn))
        if el_op.text == '删除':
            sc.logger.info('当前视频已经有配乐，删除原有音乐')
            el_op.click()
        el_op.click()

        sc.logger.info('下载音乐')
        download_btn = 'com.quvideo.xiaoying:id/music_item_download'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(download_btn)).click()

        sc.logger.info('添加音乐')
        music_name = 'com.quvideo.xiaoying:id/music_item_name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(music_name)).click()

        while True:
            try:
                state_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda el: el.find_element_by_id(state_btn)).click()
                sc.logger.info('点击播放状态')
                break
            except TimeoutException:
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda c_btn: c_btn.find_element_by_id(music_name)).click()

        sc.logger.info('使用音乐')
        use_btn = 'com.quvideo.xiaoying:id/music_item_use'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(use_btn)).click()

        time.sleep(1)
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 500)

        sc.logger.info('点击“完成”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(m_add_btn)).click()

        sc.logger.info('点击确认箭头按钮')
        right_btn = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(right_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-多段配乐-添加测试完成')

    def test_edit_music_del(self):
        """剪辑-多段配乐-删除."""
        sc.logger.info('剪辑-多段配乐-删除')
        fun_name = 'test_camera_music_del'

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

        sc.logger.info('开始点击多段配乐')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("多段配乐")')).click()

        m_add_btn = 'com.quvideo.xiaoying:id/tv_editor_audio_operation'
        sc.logger.info('点击添加删除配乐按钮')
        el_op = WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(m_add_btn))
        if el_op.text == '删除':
            sc.logger.info('当前视频已经有配乐，删除原有音乐')
            el_op.click()
        else:
            sc.logger.info('当前视频没有配乐，无需删除')

        sc.logger.info('点击确认箭头按钮')
        right_btn = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(right_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-多段配乐-删除测试完成')

    def test_edit_music_cancel(self):
        """剪辑-多段配乐-放弃."""
        sc.logger.info('剪辑-多段配乐-放弃')
        fun_name = 'test_camera_music_cancel'

        start_x = self.width // 2
        start_bottom = self.height // 4

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

        sc.logger.info('开始点击多段配乐')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("多段配乐")')).click()

        m_add_btn = 'com.quvideo.xiaoying:id/tv_editor_audio_operation'
        sc.logger.info('点击添加音乐按钮')
        el_op = WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(m_add_btn))
        if el_op.text == '删除':
            sc.logger.info('当前视频已经有配乐，删除原有音乐')
            el_op.click()
        el_op.click()

        sc.logger.info('下载音乐')
        download_btn = 'com.quvideo.xiaoying:id/music_item_download'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(download_btn)).click()

        sc.logger.info('添加音乐')
        music_name = 'com.quvideo.xiaoying:id/music_item_name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(music_name)).click()

        while True:
            try:
                state_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda el: el.find_element_by_id(state_btn)).click()
                sc.logger.info('点击播放状态')
                break
            except TimeoutException:
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda c_btn: c_btn.find_element_by_id(music_name)).click()

        sc.logger.info('使用音乐')
        use_btn = 'com.quvideo.xiaoying:id/music_item_use'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(use_btn)).click()

        time.sleep(1)
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 500)

        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(m_add_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击放弃操作按钮')
        left_btn = 'com.quvideo.xiaoying:id/terminator_left'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(left_btn)).click()
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(left_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认放弃操作')
        pos_btn = 'com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(pos_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-多段配乐-放弃测试完成')
