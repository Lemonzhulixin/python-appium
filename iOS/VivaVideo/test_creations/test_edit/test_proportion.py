# -*- coding: utf-8 -*-
"""比例与背景的基本操作测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import TimeoutException

class TestProportion(TestCase):
    """比例与背景的基本操作测试类."""

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

    def test_edit_proportion(self):
        '''剪辑-比例&多选.'''
        sc.logger.info('剪辑-比例')
        fun_name = 'test_edit_proportion'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"比例"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("比例")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换到"比例tab"')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_bg_pro)).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('已经在"比例tab"')

        sc.logger.info('选择"1:1 比例"')
        el_proportion = "vivavideo_edit_icon_proportion_1_1"
        ba.clip_proportion(el_proportion)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('进入多选')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath('//XCUIElementTypeStaticText[@name="点击多选"]')).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('当前工程只有一个镜头，无法进入多选')
            return True

        sc.logger.info('多选-删除')
        ba.clip_mult_select()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('剪辑-比例测试完成')