# -*- coding: utf-8 -*-
"""相册mv测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from iOS import iOS_elements,base as ba

class TestPreviewAlbum(TestCase):
    """相册mv测试类."""

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

    def test_preview_time(self):
        """预览页-时长."""
        sc.logger.info('预览页-时长')
        fun_name = 'test_preview_time'

        sc.logger.info('相册MV')
        ba.home_first_click('相册MV')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加图片')
        ba.gallery_clip_add('图片', 5)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“图片时长”')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("图片时长")).click()
            sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('应用于全部镜头')
            sc.driver.find_element_by_name('应用于全部镜头').click()

            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.info('当前镜头是gif图片，直接存草稿')

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('预览页-时长测试完成')