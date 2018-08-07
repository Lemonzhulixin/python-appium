# -*- coding: utf-8 -*-
"""镜头编辑相关操作的测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import NoSuchElementException,TimeoutException


class TestEditClip(TestCase):
    """镜头编辑相关操作的测试类."""

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

    def test_clip_edit_function(self):
        """剪辑-镜头编辑-功能遍历."""
        sc.logger.info('剪辑-镜头编辑-功能遍历')
        fun_name = 'test_clip_edit_function'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_home_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('功能遍历')
        ba.clip_fun_loop()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()

        sc.logger.info('剪辑-镜头编辑-功能遍历完成')