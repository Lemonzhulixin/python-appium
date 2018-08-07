# -*- coding: utf-8 -*-
"""camera音乐视频的基本操作测试用例."""
from selenium.common.exceptions import TimeoutException
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba


class TestCameraMusic(TestCase):
    """camera音乐视频的基本测试类."""

    # 获取屏幕尺寸
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @classmethod
    def setUpClass(cls):
        sc.driver.launch_app()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        sc.driver.close_app()

    def test_music_01_shot(self):
        """拍摄-音乐视频(3:4)."""
        sc.logger.info('拍摄-音乐视频(3:4)')
        fun_name = 'test_music_shot'

        sc.logger.info('点击音乐视频')
        ba.home_first_click('音乐视频')

        # 第一次从次要功能位打开音乐视频，拍摄按钮是另一个控件，所以先关闭再打开
        sc.logger.info('退出拍摄')
        time.sleep(0.5)
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_cam_close)).click()

        # 退回首页后，常无法再次获取到音乐视频控件，此处重启一次app
        sc.logger.info('重启app')
        sc.driver.close_app()
        time.sleep(1)
        sc.driver.launch_app()

        sc.logger.info('点击音乐视频')
        ba.home_first_click('音乐视频')

        sc.logger.info('切换到3:4拍摄')
        time.sleep(1)
        ba.find_element_click('name', 5, iOS_elements.el_ful)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“点击添加配乐”按钮')
        sc.driver.find_element_by_name("点击添加配乐").click()
        time.sleep(2)

        sc.logger.info('下拉刷新')
        start_x = self.width // 2
        start_bottom = self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'down', 0.3, 300)

        sc.logger.info('下载音乐')
        music_list = sc.driver.find_elements_by_name(iOS_elements.el_mus_download)
        # music_list.pop(0)
        if len(music_list) >= 4:
            music_list = music_list[1:4]
        for el_music in music_list:
            el_music.click()
            time.sleep(0.5)

        time.sleep(10)

        sc.logger.info('点击一首已下载音频试听')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_mus_play)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“添加”按钮')
        time.sleep(5)
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name('添加')).click()
        sc.capture_screen(fun_name, self.img_path)

        # 点拍
        sc.logger.info('拍摄一段5s的视频')
        btn_rec = WebDriverWait(sc.driver, 10).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_cp_music))
        ba.video_capture('点拍', btn_rec, 5)

        sc.logger.info('取消限制弹窗')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.el_cancel)).click()
        except TimeoutException:
            sc.logger.info('限制弹窗已取消')

        sc.logger.info('返回创作页')
        ba.back_to_home()
        sc.logger.info('拍摄-音乐视频(3:4)完成')

    def test_music_02_change(self):
        """拍摄-音乐视频-更换音乐重录."""
        sc.logger.info('拍摄-音乐视频-更换音乐重录')
        fun_name = 'test_music_change'

        sc.logger.info('点击音乐视频')
        time.sleep(1)
        sc.driver.find_element_by_name('音乐视频').click()

        sc.logger.info('点击“点击添加配乐”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name('点击添加配乐')).click()

        sc.logger.info('点击一首已下载音频试听')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_mus_play)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击音乐标题')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_mus_title)).click()

        sc.logger.info('更换音乐重录')
        sc.driver.find_element_by_name("更换音乐重录").click()

        sc.logger.info('点击一首已下载音频试听')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_mus_play)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()
        sc.capture_screen(fun_name, self.img_path)

        # 点拍
        sc.logger.info('开始录制')
        el_capture = WebDriverWait(sc.driver, 10).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_cp_music))
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)
        time.sleep(5)

        sc.logger.info('录制5s后点击录制按钮停止录制')
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)

        try:
            sc.logger.info('点击确认按钮')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_name(iOS_elements.el_cam_next)).click()
        except TimeoutException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('取消限制弹窗')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.el_cancel)).click()
        except TimeoutException:
            sc.logger.info('限制弹窗已取消')

        sc.logger.info('返回创作页')
        ba.back_to_home()
        sc.logger.info('拍摄-音乐视频-更换音乐重录完成')

    def test_music_03_redo(self):
        """拍摄-音乐视频-直接重录."""
        sc.logger.info('拍摄-音乐视频-直接重录')
        fun_name = 'test_music_redo'

        sc.logger.info('点击音乐视频')
        time.sleep(1)
        sc.driver.find_element_by_name('音乐视频').click()

        sc.logger.info('点击“点击添加配乐”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name('点击添加配乐')).click()

        sc.logger.info('点击一首已下载音频试听')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_mus_play)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击音乐标题')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_mus_title)).click()

        sc.logger.info('直接重录')
        sc.driver.find_element_by_name("直接重录").click()

        # 点拍
        sc.logger.info('开始录制')
        el_capture = WebDriverWait(sc.driver, 10).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_cp_music))
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)
        time.sleep(5)

        sc.logger.info('录制5s后点击录制按钮停止录制')
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)

        try:
            sc.logger.info('点击确认按钮')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_name(iOS_elements.el_cam_next)).click()
        except TimeoutException:
            sc.logger.info('音乐时长较短，已自动跳转预览页')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('取消限制弹窗')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.el_cancel)).click()
        except TimeoutException:
            sc.logger.info('限制弹窗已取消')

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('拍摄-音乐视频-直接重录完成')