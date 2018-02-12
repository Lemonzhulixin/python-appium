# -*- coding: utf-8 -*-
"""编辑滤镜的基本操作测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException


class TestEditFilter(TestCase):
    """编辑滤镜的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_filter(self):
        """剪辑-滤镜."""
        sc.logger.info('剪辑-滤镜')
        fun_name = 'test_edit_filter'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(0.5)

        sc.logger.info('点击一个草稿工程封面')
        el_draft = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView//*/XCUIElementTypeImage[1]")
        el_draft.click()

        time.sleep(0.5)
        sc.logger.info('点击"滤镜"')
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("滤镜").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择一个"滤镜"')
        el_filter = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther/XCUIElementTypeImage")
        el_filter.click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('切回"空滤镜"')
        time.sleep(1)
        el_empty = sc.driver.find_element_by_accessibility_id(
            "XiaoYingResource.bundle/vivavideo_tool_camera_none_n")
        el_empty.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“下载更多”按钮')
        time.sleep(1)
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

        sc.logger.info('存草稿并返回创作页首页')
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()


