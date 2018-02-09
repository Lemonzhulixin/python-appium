# -*- coding: utf-8 -*-
"""camera音乐视频的基本操作测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from Android import script_ultils as sc


class TestCameraMusic(object):
    """camera音乐视频的基本测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_music_shot(self):
        """拍摄-音乐视频(3:4)."""
        sc.logger.info('拍摄-音乐视频(3:4)')
        fun_name = 'test_music_shot'
        start_x = self.width - self.width // 10
        start_bottom = self.height // 2

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()

        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 500)
        sc.logger.info('点击“音乐视频”')
        sc.driver.find_element_by_android_uiautomator('text("音乐视频")').click()
        time.sleep(1)
        sc.logger.info('点击视频比例按钮，切换到3:4')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_ratio').click()
        sc.logger.info('切换摄像头')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_switch').click()
        time.sleep(2)
        sc.logger.info('点击“请选择音乐”按钮')
        sc.driver.find_element_by_android_uiautomator('text("请选择音乐")').click()
        time.sleep(2)
        try:
            el_download = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_download')
        except NoSuchElementException:
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.4, 500)
            el_download = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_download')
        sc.logger.info('点击第一个下载按钮')
        el_download.click()
        time.sleep(5)
        el_music_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_name')
        sc.logger.info('点击第一首音乐名')
        el_music_name.click()
        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_play_state').click()
        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_use').click()
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍5s
        sc.logger.info('点击录制按钮')
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()
        try:
            sc.logger.info('点击确认按钮')
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.logger.info('拍摄-音乐视频(3:4)完成')

    def test_music_change(self):
        """拍摄-音乐视频-更换音乐重录."""
        sc.logger.info('拍摄-音乐视频-更换音乐重录')
        fun_name = 'test_music_change'
        start_x = self.width - self.width // 10
        start_bottom = self.height // 2
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 500)

        sc.logger.info('点击“音乐视频”')
        sc.driver.find_element_by_android_uiautomator('text("音乐视频")').click()
        sc.logger.info('点击“请选择音乐”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon_tool_music_control_arrow').click()
        # sc.driver.find_element_by_android_uiautomator('text("请选择音乐")').click()
        el_music_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_name')
        sc.logger.info('点击第一首音乐名')
        el_music_name.click()
        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_play_state').click()
        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_use').click()
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        sc.logger.info('点击录制按钮')
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()
        try:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
            sc.logger.info('点击确认按钮')
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角返回按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.logger.info('点击音乐标题')

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon_tool_music_control_arrow').click()
        try:
            sc.driver.find_element_by_android_uiautomator('text("更换音乐重录")').click()
        except NoSuchElementException:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon_tool_music_control_arrow').click()
            el_title_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
            for el_title in el_title_list:
                if el_title.text == '更换音乐重录':
                    sc.logger.info('点击“更换音乐重录”')
                    el_title.click()

        sc.logger.info('点击音乐名')
        time.sleep(2)
        el_music_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_name')
        el_music_name.click()
        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_play_state').click()
        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_use').click()
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        sc.logger.info('点击录制按钮')
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()
        try:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
            sc.logger.info('点击“确认”按钮')
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()

        sc.logger.info('点击左上角返回按钮返回创作中心主页面')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.logger.info('拍摄-音乐视频-更换音乐重录完成')

    def test_music_redo(self):
        """拍摄-音乐视频-重新录制."""
        sc.logger.info('拍摄-音乐视频-直接重录')
        fun_name = 'test_music_redo'

        sc.logger.info('点击“音乐视频”')
        sc.driver.find_element_by_android_uiautomator('text("音乐视频")').click()
        sc.logger.info('点击“请选择音乐”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon_tool_music_control_arrow').click()

        el_music_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_name')
        sc.logger.info('点击音乐标题')
        el_music_name.click()
        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_play_state').click()
        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_use').click()
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍5s
        el_capture.click()
        sc.logger.info('点击拍摄按钮')
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()
        try:
            sc.logger.info('点击确认按钮')
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.logger.info('点击左上角返回按钮返回')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.logger.info('点击音乐标题')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon_tool_music_control_arrow').click()
        try:
            sc.driver.find_element_by_android_uiautomator('text("直接重录")').click()
        except NoSuchElementException:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon_tool_music_control_arrow').click()
            sc.capture_screen(fun_name, self.img_path)
            el_title_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
            for el_title in el_title_list:
                if el_title.text == '直接重录':
                    sc.logger.info('直接重录')
                    el_title.click()

        sc.capture_screen(fun_name, self.img_path)

        sc.driver.press_keycode(4)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击确认放弃操作')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/buttonDefaultPositive').click()
        sc.driver.press_keycode(4)
        sc.logger.info('拍摄-音乐视频-直接重录完成')
