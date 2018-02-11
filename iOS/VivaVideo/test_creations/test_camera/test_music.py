# -*- coding: utf-8 -*-
"""camera音乐视频的基本操作测试用例."""
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
import time


class TestCameraMusic(TestCase):
    """camera音乐视频的基本测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_music_01_shot(self):
        """拍摄-音乐视频(3:4)."""
        fun_name = 'test_music_shot'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('向左滑动')
        start_x = self.width - self.width // 5
        start_bottom = self.height // 2
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击音乐视频')
        sc.driver.find_element_by_name("音乐视频").click()

        sc.logger.info('跳过订阅页面')
        try:
            sc.driver.find_element_by_name("跳过").click()
            time.sleep(1)
            sc.driver.find_element_by_name("音乐视频").click()
        except NoSuchElementException:
            sc.logger.info('已跳过订阅页面')

        sc.logger.info("授权小影访问相机和麦克风")
        try:
            sc.driver.find_element_by_name("好").click()  # 授权访问相机
            time.sleep(1)
            sc.driver.find_element_by_name("好").click()  # 授权访问麦克风
            time.sleep(1)
        except NoSuchElementException:
            sc.logger.info("已授权")

        sc.logger.info('切换到3:4拍摄')
        time.sleep(1)
        el_ful = sc.driver.find_element_by_name("vivavideo camera tool icon ful")
        el_ful.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“点击添加配乐”按钮')
        sc.driver.find_element_by_name("点击添加配乐").click()
        time.sleep(2)

        sc.logger.info('点击下载按钮')
        el_download = sc.driver.find_element_by_name('vivavideo material download3 n')
        el_download.click()
        sc.capture_screen(fun_name, self.img_path)
        time.sleep(10)

        sc.logger.info('点击第一首已下载音频试听')
        el_music_name = sc.driver.find_element_by_xpath("//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        try:
            el_music_name.click()
        except NoSuchElementException:
            sc.logger.error('音频下载未完成，继续等待5s')
            time.sleep(5)
            el_music_name.click()

        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_name("vivavideo tool camera pause n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()

        sc.logger.info('开始录制')
        # 点拍5s
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()

        sc.logger.info('录制完成，进入预览页')
        try:
            sc.logger.info('点击确认按钮')
            sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(0.5)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_music_02_change(self):
        """拍摄-音乐视频-更换音乐重录."""
        sc.logger.info('拍摄-音乐视频-更换音乐重录')
        fun_name = 'test_music_change'

        sc.logger.info('点击音乐视频')
        sc.driver.find_element_by_name("音乐视频").click()
        time.sleep(1)

        sc.logger.info('点击“点击添加配乐”按钮')
        sc.driver.find_element_by_name("点击添加配乐").click()
        time.sleep(1)

        sc.logger.info('点击第一首已下载音频试听')
        el_music_name = sc.driver.find_element_by_xpath("//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        el_music_name.click()

        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_name("vivavideo tool camera pause n").click()

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('开始录制')
        # 点拍5s
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()

        sc.logger.info('录制完成，进入预览页')
        try:
            sc.logger.info('点击确认按钮')
            sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')

        sc.logger.info('点击左上角返回按钮')
        sc.driver.find_element_by_name("xiaoying com back").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击音乐标题')
        time.sleep(1)
        sc.driver.find_element_by_accessibility_id("vivavideo_camera_tool_icon_music_nrm").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('更换音乐重录')
        sc.driver.find_element_by_name("更换音乐重录").click()

        sc.logger.info('点击音乐名')
        time.sleep(1)
        el_music_name = sc.driver.find_element_by_xpath("//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        el_music_name.click()

        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_name("vivavideo tool camera pause n").click()

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()

        sc.logger.info('开始录制')
        # 点拍5s
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()

        sc.logger.info('录制完成，进入预览页')
        try:
            sc.logger.info('点击确认按钮')
            sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(0.5)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_music_03_redo(self):
        """拍摄-音乐视频-重新录制."""
        sc.logger.info('拍摄-音乐视频-直接重录')
        fun_name = 'test_music_redo'

        sc.logger.info('点击音乐视频')
        sc.driver.find_element_by_name("音乐视频").click()
        time.sleep(1)

        sc.logger.info('点击“点击添加配乐”按钮')
        sc.driver.find_element_by_name("点击添加配乐").click()
        time.sleep(1)

        sc.logger.info('点击第一首已下载音频试听')
        el_music_name = sc.driver.find_element_by_xpath("//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        el_music_name.click()

        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_name("vivavideo tool camera pause n").click()

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('开始录制')
        # 点拍5s
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()

        sc.logger.info('录制完成，进入预览页')
        try:
            sc.logger.info('点击确认按钮')
            sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')

        sc.logger.info('点击左上角返回按钮')
        sc.driver.find_element_by_name("xiaoying com back").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击音乐标题')
        time.sleep(1)
        sc.driver.find_element_by_accessibility_id("vivavideo_camera_tool_icon_music_nrm").click()

        sc.logger.info('取消重录')
        sc.driver.find_element_by_name("取消").click()

        sc.logger.info('直接重录')
        sc.driver.find_element_by_accessibility_id("vivavideo_camera_tool_icon_music_nrm").click()
        sc.driver.find_element_by_name("直接重录").click()

        sc.logger.info('开始录制')
        # 点拍5s
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()

        sc.logger.info('录制完成，进入预览页')
        try:
            sc.logger.info('点击确认按钮')
            sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()
        except NoSuchElementException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')

        sc.logger.info('点击“左上角返回”按钮')
        time.sleep(0.5)
        sc.driver.find_element_by_name("xiaoying com back").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击“左上角x”按钮退出拍摄')
        time.sleep(0.5)
        sc.driver.find_element_by_name("vivavideo camera tool icon clo").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()