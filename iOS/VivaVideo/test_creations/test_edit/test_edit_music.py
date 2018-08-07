# -*- coding: utf-8 -*-
"""编辑音乐相关操作测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba


class TestEditMusic(TestCase):
    """音乐相关操作测试测试类."""

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

    def test_edit_music_01(self):
        """剪辑-多段配乐-添加."""
        sc.logger.info('剪辑-多段配乐-添加')
        fun_name = 'test_music_add'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("效果")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("添加一段'配乐'")
        ba.effects_music()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        ba.effect_add_confirm()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('剪辑-多段配乐-添加测试完成')

    def test_edit_music_02(self):
        """剪辑-多段配乐-删除."""
        sc.logger.info('剪辑-多段配乐-删除')
        fun_name = 'test_camera_music_del'

        sc.logger.info('点击草稿封面')
        try:
            ba.open_draft(iOS_elements.el_studio_draft)
            sc.capture_screen(fun_name, self.img_path)
        except:
            sc.logger.info('关闭广告')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_name(iOS_elements.btn_ad_clo)).click()

            ba.open_draft(iOS_elements.el_studio_draft)
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("效果")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"多段配乐"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('多段配乐')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('当前视频已经有配乐，删除原有音乐')
        sc.driver.find_element_by_name('删除').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确定')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
        sc.logger.info('剪辑-多段配乐-删除测试完成')

    def test_edit_music_03(self):
        """剪辑-多段配乐-放弃."""
        sc.logger.info('剪辑-多段配乐-放弃')
        fun_name = 'test_camera_music_cancel'

        sc.logger.info('点击"多段配乐"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('多段配乐')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("添加一段'配乐'")
        ba.effects_music()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('取消添加')
        ba.effect_add_cancel()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('剪辑-多段配乐-放弃测试完成')
