# -*- coding: utf-8 -*-
"""编辑音乐相关操作测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from Android import script_ultils as sc


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

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()

        el_edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in el_edit_list:
            if el_item.text == '多段配乐':
                sc.logger.info('开始点击“多段配乐”按钮')
                el_item.click()
                break
        while True:
            try:
                sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_add_music').click()
                sc.logger.info('点击添加音乐按钮')
                break
            except NoSuchElementException:
                sc.logger.info('当前视频已经有配乐')
                sc.logger.info('删除原有音乐')
                sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_speed_close').click()
                sc.logger.info('点击删除按钮')
                sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_del_music').click()

        el_download = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_download')
        el_music_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_name')
        sc.logger.info('下载音乐')
        el_download.click()

        sc.logger.info('添加音乐')
        el_music_name.click()

        while True:
            try:
                sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_play_state').click()
                sc.logger.info('点击播放状态')
                break
            except NoSuchElementException:
                time.sleep(5)

        sc.logger.info('使用音乐')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_use').click()
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 100)
        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-多段配乐-添加测试完成')

    def test_edit_music_del(self):
        """剪辑-多段配乐-删除."""
        sc.logger.info('剪辑-多段配乐-删除')
        fun_name = 'test_camera_music_del'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()

        edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for item in edit_list:
            if item.text == '多段配乐':
                sc.logger.info('开始点击多段配乐')
                item.click()
                break
        sc.logger.info('点击编辑按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_speed_close').click()
        sc.logger.info('点击删除按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_del_music').click()
        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-多段配乐-删除测试完成')

    def test_edit_music_cancel(self):
        """剪辑-多段配乐-放弃."""
        sc.logger.info('剪辑-多段配乐-放弃')
        fun_name = 'test_camera_music_cancel'

        start_x = self.width // 2
        start_bottom = self.height // 4

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()

        el_edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in el_edit_list:
            if el_item.text == '多段配乐':
                sc.logger.info('开始点击多段配乐')
                el_item.click()
                break

        while True:
            try:
                time.sleep(1)
                sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_add_music').click()
                sc.logger.info('点击添加音乐按钮')
                break
            except NoSuchElementException:
                sc.logger.info('当前视频已经有配乐')
                sc.logger.info('删除原有音乐')
                sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_speed_close').click()
                sc.logger.info('点击删除按钮')
                sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_del_music').click()

        el_download = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_download')
        el_music_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_name')
        el_download.click()
        time.sleep(5)
        el_music_name.click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_play_state').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_use').click()
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 1000)
        sc.logger.info('点击左上角放弃操作按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.logger.info('确认放弃操作')
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-多段配乐-放弃测试完成')
