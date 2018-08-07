# -*- coding: utf-8 -*-
"""编辑滤镜的基本操作测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba

class TestEditFilter(TestCase):
    """编辑滤镜的基本操作测试类."""

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

    def test_edit_filter(self):
        """剪辑-滤镜."""
        sc.logger.info('剪辑-滤镜')
        fun_name = 'test_edit_filter'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"滤镜"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("滤镜")).click()

        sc.logger.info('点击"下载更多"')
        btn_more = '下载更多'
        ba.more_download(btn_more)

        sc.logger.info('使用滤镜')
        ba.material_used(iOS_elements.el_store_download2)

        sc.logger.info('确认添加')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('剪辑-滤镜测试完成')
