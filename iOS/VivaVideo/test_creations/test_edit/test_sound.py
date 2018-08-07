# -*- coding: utf-8 -*-
"""配音的基本操作测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class TestEditSound(TestCase):
    """配音的基本操作测试类."""

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

    def test_edit_sound_01_rec(self):
        """剪辑-配音-录制."""
        sc.logger.info('剪辑-配音-录制')
        fun_name = 'test_edit_sound_rec'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("效果")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('左滑并点击"配音和音效"')
        el_loc = WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('画中画'))
        ba.swipe_left(el_loc, 0.3, 300)

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('配音和音效')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除已添加的配音或音效')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_accessibility_id(iOS_elements.btn_rec_start))
        except TimeoutException:
            sc.logger.info('当前位置已添加配音或音效，删除后录制')
            sc.driver.find_element_by_name('删除').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('"录制"一段音频')
        ba.sound_rec_add()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('剪辑-配音-录制添加测试完成')

    def test_edit_sound_02_audio(self):
        """剪辑-配音-音效."""
        sc.logger.info('剪辑-配音-音效')
        fun_name = 'test_edit_sound_audio'

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('配音和音效')).click()

        sc.logger.info('删除已添加的配音或音效')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_accessibility_id(iOS_elements.btn_rec_start))
        except TimeoutException:
            sc.logger.info('当前位置已添加配音或音效，删除后录制')
            sc.driver.find_element_by_name('删除').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加一段音效')
        ba.sound_audio_add()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        time.sleep(2)
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('剪辑-配音-音效添加测试完成')

    def test_edit_sound_03_cancel(self):
        """剪辑-配音-放弃."""
        sc.logger.info('剪辑-配音-放弃')
        fun_name = 'test_edit_sound_cancel'

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('配音和音效')).click()

        sc.logger.info('删除已添加的配音或音效')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_accessibility_id(iOS_elements.btn_rec_start))
        except TimeoutException:
            sc.logger.info('当前位置已添加配音或音效，删除后录制')
            sc.driver.find_element_by_name('删除').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('"录制"一段音频')
        ba.sound_rec_add()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('取消添加')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_cancel_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确定放弃')
        sc.driver.find_element_by_name('确认').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('剪辑-配音-放弃测试完成')