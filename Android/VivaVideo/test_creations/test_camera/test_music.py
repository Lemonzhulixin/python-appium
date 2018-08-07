# -*- coding: utf-8 -*-
"""camera音乐视频的基本操作测试用例."""
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Android_old import script_ultils as sc


class TestCameraMusic(object):
    """camera音乐视频的基本测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]
    c_btn = 'com.quvideo.xiaoying:id/img_creation'

    def test_music_shot(self):
        """拍摄-音乐视频(3:4)."""
        sc.logger.info('拍摄-音乐视频(3:4)')
        fun_name = 'test_music_shot'
        start_x = self.width - self.width // 10
        start_bottom = self.height // 2

        sc.logger.info('点击创作中心主按钮')
        sc.first_step(self.c_btn)

        time.sleep(2)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 500)
        sc.logger.info('点击“音乐视频”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("音乐视频")')).click()
        # sc.driver.find_element_by_android_uiautomator('text("音乐视频")').click()

        sc.logger.info('点击视频比例按钮，切换到3:4')
        ratio_btn = 'com.quvideo.xiaoying:id/cam_btn_ratio'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(ratio_btn)).click()

        sc.logger.info('切换摄像头')
        switch_btn = 'com.quvideo.xiaoying:id/img_switch'
        sc.driver.find_element_by_id(switch_btn).click()

        sc.logger.info('点击“请选择音乐”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("请选择音乐")')).click()

        download_btn = 'com.quvideo.xiaoying:id/music_item_download'
        try:
            el_download = WebDriverWait(sc.driver, 10, 1).until(
                                lambda el: el.find_element_by_id(download_btn))
        except TimeoutException:
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.4, 500)
            el_download = WebDriverWait(sc.driver, 10, 1).until(
                                lambda el: el.find_element_by_id(download_btn))
        sc.logger.info('点击第一个下载按钮')
        el_download.click()

        music_row = 'com.quvideo.xiaoying:id/music_item_name'
        sc.logger.info('点击第一首音乐名')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(music_row)).click()

        sc.logger.info('点击播放/暂停按钮')
        play_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(play_btn)).click()

        sc.logger.info('点击“添加”按钮')
        use_btn = 'com.quvideo.xiaoying:id/music_item_use'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(use_btn)).click()
        el_cp = WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_id('com.quvideo.xiaoying:id/btn_rec'))

        # 长按拍摄5s
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)
        try:
            sc.logger.info('点击确认按钮')
            n_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(n_btn)).click()
        except TimeoutException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        draft_btn = 'com.quvideo.xiaoying:id/editor_draft'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_btn)).click()

        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(left_btn)).click()
        sc.logger.info('拍摄-音乐视频(3:4)完成')

    def test_music_change(self):
        """拍摄-音乐视频-更换音乐重录."""
        sc.logger.info('拍摄-音乐视频-更换音乐重录')
        fun_name = 'test_music_change'
        start_x = self.width - self.width // 10
        start_bottom = self.height // 2

        time.sleep(2)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 500)

        sc.logger.info('点击“音乐视频”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("音乐视频")')).click()

        sc.logger.info('点击“请选择音乐”')
        music_ctr_btn = 'com.quvideo.xiaoying:id/icon_tool_music_control_arrow'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(music_ctr_btn)).click()

        sc.logger.info('点击第一首音乐名')
        music_name_btn = 'com.quvideo.xiaoying:id/music_item_name'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(music_name_btn)).click()

        sc.logger.info('点击播放/暂停按钮')
        play_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(play_btn)).click()

        sc.logger.info('点击“添加”按钮')
        use_btn = 'com.quvideo.xiaoying:id/music_item_use'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(use_btn)).click()

        el_cp = WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id('com.quvideo.xiaoying:id/btn_rec'))

        # 长按拍摄5s
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        try:
            sc.logger.info('点击确认按钮')
            next_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(next_btn)).click()
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角返回按钮')
        left_btn = 'com.quvideo.xiaoying:id/editor_back_btn'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(left_btn)).click()

        sc.logger.info('点击音乐标题')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(music_ctr_btn)).click()
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_android_uiautomator(
                    'text("更换音乐重录")')).click()
        except TimeoutException:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(music_ctr_btn)).click()

            tl = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
            for el_title in tl:
                if el_title.text == '更换音乐重录':
                    sc.logger.info('点击“更换音乐重录”')
                    el_title.click()

        sc.logger.info('点击音乐名')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(music_name_btn)).click()

        sc.logger.info('点击播放/暂停按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(play_btn)).click()

        sc.logger.info('点击“添加”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(use_btn)).click()

        el_cp = WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id('com.quvideo.xiaoying:id/btn_rec'))

        # 长按拍摄5s
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(next_btn)).click()
            sc.logger.info('点击“确认”按钮')
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        draft_btn = 'com.quvideo.xiaoying:id/editor_draft'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_btn)).click()

        sc.logger.info('点击左上角返回按钮返回创作中心主页面')
        back_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(back_btn)).click()
        sc.logger.info('拍摄-音乐视频-更换音乐重录完成')

    def test_music_redo(self):
        """拍摄-音乐视频-重新录制."""
        sc.logger.info('拍摄-音乐视频-直接重录')
        fun_name = 'test_music_redo'

        music_ctr_btn = 'com.quvideo.xiaoying:id/icon_tool_music_control_arrow'
        music_name_btn = 'com.quvideo.xiaoying:id/music_item_name'
        play_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
        use_btn = 'com.quvideo.xiaoying:id/music_item_use'
        next_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
        left_btn = 'com.quvideo.xiaoying:id/editor_back_btn'

        sc.logger.info('点击“音乐视频”')
        sc.driver.find_element_by_android_uiautomator('text("音乐视频")').click()
        sc.logger.info('点击“请选择音乐”')
        sc.driver.find_element_by_id(music_ctr_btn).click()

        el_music_name = sc.driver.find_element_by_id(music_name_btn)
        sc.logger.info('点击音乐标题')
        el_music_name.click()
        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_id(play_btn).click()
        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_id(use_btn).click()
        el_cp = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 长按拍摄5s
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        try:
            sc.logger.info('点击确认按钮')
            sc.driver.find_element_by_id(next_btn).click()
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.logger.info('点击左上角返回按钮返回')
        sc.driver.find_element_by_id(left_btn).click()

        sc.logger.info('点击音乐标题')
        music_title = 'com.quvideo.xiaoying:id/music_title'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda c_btn: c_btn.find_element_by_id(music_title)).click()
        # sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon_tool_music_control_arrow').click()
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda c_btn: c_btn.find_element_by_android_uiautomator(
                    'text("直接重录")')).click()
            # sc.driver.find_element_by_android_uiautomator('text("直接重录")').click()
        except Exception as err:
            sc.driver.find_element_by_id(music_ctr_btn).click()
            sc.capture_screen(fun_name, self.img_path)
            title_el = 'com.quvideo.xiaoying:id/title'
            WebDriverWait(sc.driver, 5, 1).until(
                lambda c_btn: c_btn.find_elements_by_id(title_el))
            el_title_list = sc.driver.find_elements_by_id(title_el)
            for el_title in el_title_list:
                if el_title.text == '直接重录':
                    sc.logger.info('直接重录')
                    el_title.click()
                    break

        sc.capture_screen(fun_name, self.img_path)

        sc.driver.press_keycode(4)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认放弃操作')
        p_btn = 'com.quvideo.xiaoying:id/buttonDefaultPositive'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(p_btn)).click()
        sc.driver.press_keycode(4)
        sc.logger.info('拍摄-音乐视频-直接重录完成')
