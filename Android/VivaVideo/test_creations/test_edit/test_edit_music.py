# -*- coding: utf-8 -*-
"""编辑音乐相关操作测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
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

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        sc.driver.find_element_by_id(draft_img).click()
        sc.logger.info('点击“剪辑”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("剪辑")')).click()

        t_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in t_list:
            if el_item.text == '多段配乐':
                sc.logger.info('开始点击“多段配乐”按钮')
                el_item.click()
                break
        while True:
            try:
                music_add_btn = 'com.quvideo.xiaoying:id/imgbtn_add_music'
                sc.driver.find_element_by_id(music_add_btn).click()
                sc.logger.info('点击添加音乐按钮')
                break
            except NoSuchElementException:
                sc.logger.info('当前视频已经有配乐')
                sc.logger.info('删除原有音乐')
                speed_close_btn = 'com.quvideo.xiaoying:id/imgbtn_speed_close'
                sc.driver.find_element_by_id(speed_close_btn).click()

                sc.logger.info('点击删除按钮')
                del_btn = 'com.quvideo.xiaoying:id/imgbtn_del_music'
                sc.driver.find_element_by_id(del_btn).click()

        sc.logger.info('下载音乐')
        download_btn = 'com.quvideo.xiaoying:id/music_item_download'
        sc.driver.find_element_by_id(download_btn).click()

        sc.logger.info('添加音乐')
        music_item_name = 'com.quvideo.xiaoying:id/music_item_name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(music_item_name)).click()

        while True:
            try:
                state_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
                sc.driver.find_element_by_id(state_btn).click()
                sc.logger.info('点击播放状态')
                break
            except NoSuchElementException:
                time.sleep(5)

        sc.logger.info('使用音乐')
        use_btn = 'com.quvideo.xiaoying:id/music_item_use'
        sc.driver.find_element_by_id(use_btn).click()

        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 100)
        time.sleep(1)

        sc.logger.info('点击右上角确认按钮')
        right_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_right'
        sc.driver.find_element_by_id(right_btn).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(3):
            time.sleep(2)
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
        sc.driver.find_element_by_id(draft_img).click()

        sc.logger.info('点击“剪辑”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("剪辑")')).click()

        t_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for item in t_list:
            if item.text == '多段配乐':
                sc.logger.info('开始点击多段配乐')
                item.click()
                break
        sc.logger.info('点击编辑按钮')
        speed_close_btn = 'com.quvideo.xiaoying:id/imgbtn_speed_close'
        sc.driver.find_element_by_id(speed_close_btn).click()

        sc.logger.info('点击删除按钮')
        del_btn = 'com.quvideo.xiaoying:id/imgbtn_del_music'
        sc.driver.find_element_by_id(del_btn).click()

        sc.logger.info('点击右上角确认按钮')
        right_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_right'
        sc.driver.find_element_by_id(right_btn).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(3):
            time.sleep(2)
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
        sc.driver.find_element_by_id(draft_img).click()

        sc.logger.info('点击“剪辑”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("剪辑")')).click()

        t_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in t_list:
            if el_item.text == '多段配乐':
                sc.logger.info('开始点击多段配乐')
                el_item.click()
                break

        while True:
            try:
                time.sleep(1)
                music_add_btn = 'com.quvideo.xiaoying:id/imgbtn_add_music'
                sc.driver.find_element_by_id(music_add_btn).click()
                sc.logger.info('点击添加音乐按钮')
                break
            except NoSuchElementException:
                sc.logger.info('当前视频已经有配乐')
                sc.logger.info('删除原有音乐')
                speed_close_btn = 'com.quvideo.xiaoying:id/imgbtn_speed_close'
                sc.driver.find_element_by_id(speed_close_btn).click()

                sc.logger.info('点击删除按钮')
                del_btn = 'com.quvideo.xiaoying:id/imgbtn_del_music'
                sc.driver.find_element_by_id(del_btn).click()

        sc.logger.info('下载音乐')
        download_btn = 'com.quvideo.xiaoying:id/music_item_download'
        sc.driver.find_element_by_id(download_btn).click()

        music_item_name = 'com.quvideo.xiaoying:id/music_item_name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(music_item_name)).click()

        state_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
        sc.driver.find_element_by_id(state_btn).click()

        music_use_btn = 'com.quvideo.xiaoying:id/music_item_use'
        sc.driver.find_element_by_id(music_use_btn).click()

        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 1000)
        time.sleep(1)

        sc.logger.info('点击左上角放弃操作按钮')
        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        sc.driver.find_element_by_id(left_btn).click()

        sc.logger.info('确认放弃操作')
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(3):
            time.sleep(2)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-多段配乐-放弃测试完成')
