# -*- coding: utf-8 -*-
"""预览页面的theme测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from iOS import iOS_elements,base as ba


class TestPreviewTheme(TestCase):
    """预览页面的theme测试类."""

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

    def test_preview_theme(self):
        """预览页-主题页面."""
        sc.logger.info('预览页-主题页面')
        fun_name = 'test_preview_theme'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“主题”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("主题")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('使用“主题”')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_theme_use)).click()
        except TimeoutException:
            sc.logger.info('当前页面无已下载的主题')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_theme_download)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('预览页-主题测试完成')
