# -*- coding: utf-8 -*-
"""添加字幕的基本操作测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba


class TestEditText(TestCase):
    """添加字幕的基本操作测试类."""

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

    def test_edit_text(self):
        """剪辑-字幕-添加."""
        sc.logger.info('剪辑-字幕-添加')
        fun_name = 'test_edit_text'

        sc.logger.info('点击视频剪辑')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_home_edit)).click()

        sc.logger.info('添加视频')
        ba.gallery_clip_add('视频', 2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击下一步')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("效果")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“字幕”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("字幕")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('默认动态字幕添加')
        ba.effect_add_confirm()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加第二个字幕并放弃')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("字幕")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加一个普通字幕')
        ba.text_comm_add()

        sc.logger.info('其他设置')
        ba.text_other()

        sc.logger.info('确认添加')
        ba.effect_add_confirm()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('剪辑-字幕-添加测试完成')