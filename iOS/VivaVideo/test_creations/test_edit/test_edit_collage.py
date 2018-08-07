# -*- coding: utf-8 -*-
"""编辑页面画中画的基本操作测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba


class TestEditCollage(TestCase):
    """编辑页面画中画的基本操作测试类."""

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

    def test_edit_collage_01_img(self):
        """剪辑-画中画-图片添加."""
        sc.logger.info('剪辑-画中画-图片添加')
        fun_name = 'test_edit_collage_img'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("效果")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"画中画"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('画中画')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加图片画中画')
        ba.collage_add('图片')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        ba.effect_add_confirm()
        sc.logger.info('剪辑-画中画-图片添加测试完成')

    def test_edit_collage_02_video(self):
        """剪辑-画中画-视频添加."""
        sc.logger.info('剪辑-画中画-视频添加')
        fun_name = 'test_edit_collage_video'

        sc.logger.info('点击"画中画"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('画中画')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加视频画中画')
        ba.collage_add('视频')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        ba.effect_add_confirm()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('剪辑-画中画-视频添加测试完成')

    def test_edit_collage_03_gif(self):
        """剪辑-画中画-GIF添加."""
        sc.logger.info('剪辑-画中画-GIF添加')
        fun_name = 'test_edit_collage_gif'

        sc.logger.info('点击"画中画"')
        time.sleep(0.5)
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('画中画')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加gif画中画')
        ba.collage_add('GIF')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加')
        ba.effect_add_confirm()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('剪辑-画中画-GIF搜索测试完成')

    def test_edit_collage_04_cancel(self):
        """剪辑-画中画-放弃."""
        sc.logger.info('剪辑-画中画-放弃')
        fun_name = 'test_edit_collage_cancel'

        sc.logger.info('点击"画中画"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('画中画')).click()

        sc.logger.info('添加图片画中画')
        ba.collage_add('图片')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('取消添加')
        ba.effect_add_cancel()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('剪辑-画中画-放弃测试完成')
