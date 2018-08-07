# -*- coding: utf-8 -*-
"""镜头添加相关操作的测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import TimeoutException

class TestEditClipsAdd(TestCase):
    """镜头添加相关操作的测试类."""

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

    def test_clips_add_01(self):
        """剪辑-添加镜头-相册添加."""
        sc.logger.info('剪辑-添加镜头-相册添加')
        fun_name = 'test_edit_add_clips'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('从相册添加')
        ba.clip_add('相册')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('退出预览页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_pre_clo)).click()
        sc.logger.info('剪辑-添加镜头-相册添加测试完成')

    def test_clips_add_02(self):
        """剪辑-添加镜头-拍摄添加."""
        sc.logger.info('剪辑-添加镜头-拍摄添加')
        fun_name = 'test_edit_clips_shot'

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_home_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('拍摄添加镜头')
        ba.clip_add('拍摄')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('退出预览页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_pre_clo)).click()

        sc.logger.info('剪辑-添加镜头-拍摄添加测试完成')

    def test_clips_add_03(self):
        """剪辑-添加镜头-放弃."""
        sc.logger.info('剪辑-添加镜头-放弃')
        fun_name = 'test_edit_clips_cancel'

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_home_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头编辑")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"添加镜头"按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_clip_add)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择相册')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('相册')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('勾选镜头')
        ba.gallery_clip_add('视频', 2)

        sc.logger.info('左上角返回')
        sc.driver.find_element_by_name(iOS_elements.el_gallery_back).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确定放弃')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name('确认')).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.logger.error('没有勾选中镜头，需要手动再验证！')
            return False

        sc.logger.info('剪辑-放弃添加镜头-测试完成')