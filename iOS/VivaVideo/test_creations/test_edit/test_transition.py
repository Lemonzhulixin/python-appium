# -*- coding: utf-8 -*-
"""转场的基本操作测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import TimeoutException


class TestEditTransition(TestCase):
    """转场的基本操作测试类."""

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

    def test_edit_transition(self):
        """剪辑-转场-添加."""
        sc.logger.info('剪辑-转场-添加')
        fun_name = 'test_edit_transition'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“转场icon”')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.btn_transition_icon)).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('只有一个镜头，无法使用转场')
            return True

        sc.logger.info('下载并使用转场')
        ba.clip_transition()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('剪辑-转场-添加测试完成')
