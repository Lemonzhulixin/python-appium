# -*- coding: utf-8 -*-
"""转场的基本操作测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc


class TestEditTransition(TestCase):
    """转场的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_transition(self):
        """剪辑-转场."""
        sc.logger.info('剪辑-转场')
        fun_name = 'test_edit_transition'

        time.sleep(5)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"剪辑"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()

        sc.logger.info('向左滑动')
        start_x = self.width - self.width // 10
        start_bottom = self.height - self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 800)

        sc.logger.info('点击"转场"')
        sc.driver.find_element_by_name("转场").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择一个"转场"')
        el_tran = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther/XCUIElementTypeImage")
        el_tran.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切回"无转场"')
        time.sleep(0.5)
        el_empty = sc.driver.find_element_by_accessibility_id(
            "XiaoYingResource.bundle/vivavideo_tool_camera_none_n")
        el_empty.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“下载更多”按钮')
        time.sleep(0.5)
        el_more = sc.driver.find_element_by_accessibility_id(
            "XiaoYingResource.bundle/vivavideo_tool_camera_store_n")
        el_more.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“左上角”返回预览页')
        time.sleep(0.5)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击“多选”')
        sc.driver.find_element_by_name("多选").click()

        sc.logger.info('点击“全选”')
        sc.driver.find_element_by_name("全选").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“随机”')
        sc.driver.find_element_by_name("随机").click()

        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name("确认").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“右上角”保存')
        sc.driver.find_element_by_name("xiaoying com ok").click()

        # sc.logger.info('再次点击"转场"')
        # sc.driver.find_element_by_name("转场").click()

        # sc.logger.info('切回"无转场"')
        # el_empty = sc.driver.find_element_by_accessibility_id(
        #     "XiaoYingResource.bundle/vivavideo_tool_camera_none_n")
        # el_empty.click()
        # sc.capture_screen(fun_name, self.img_path)
        #
        # sc.logger.info('点击“左上角X”取消')
        # sc.driver.find_element_by_name("xiaoying com cancel").click()
        # sc.capture_screen(fun_name, self.img_path)
        #
        # sc.logger.info('确认取消')
        # sc.driver.find_element_by_name("确认").click()
        # time.sleep(3)

        sc.logger.info('存草稿并返回创作页首页')
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()