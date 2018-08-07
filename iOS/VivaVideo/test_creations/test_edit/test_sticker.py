# -*- coding: utf-8 -*-
"""动画贴纸的测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import TimeoutException


class TestEditSticker(TestCase):
    """动画贴纸的测试类."""

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

    def test_edit_sticker(self):
        """剪辑-动画贴纸-添加."""
        sc.logger.info('剪辑-动画贴纸-添加')
        fun_name = 'test_edit_sticker'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("效果")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“贴纸”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("贴纸")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加一个普通"贴纸"')
        ba.sticker_comm_add()

        sc.logger.info('确认添加')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加第二个贴纸并放弃')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name('添加')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击GIF')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name('GIF')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加一个GIF"贴纸"')
        ba.material_used('下载')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确定')
        time.sleep(0.5)
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()

        sc.logger.info('取消添加')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_cancel_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        # iOS此处有一个bug，贴纸未添加完成时，点击x，未弹出放弃弹窗（7.2.2已修复）
        sc.logger.info('确定放弃')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name('确认')).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.error('iOS此处有一个bug，贴纸未添加完成时，点击x，未弹出放弃弹窗')

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('剪辑-动画贴纸-添加测试完成')