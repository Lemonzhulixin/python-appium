# -*- coding: utf-8 -*-
"""edit创建视频的测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import TimeoutException


class TestEditCreate(TestCase):
    """edit创建视频的测试类."""

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

    # sc.driver.getPageSource()

    def test_create_draft(self):
        """创建一个草稿视频."""
        sc.logger.info('创建一个草稿视频')
        fun_name = 'test_create_craft'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击“视频剪辑”按钮')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_home_edit)).click()

        sc.logger.info('添加视频')
        ba.gallery_clip_add('视频', 2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换到图片')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()

        sc.logger.info('添加图片')
        ba.gallery_clip_add('图片', 2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击下一步')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('创建一个草稿视频完成')