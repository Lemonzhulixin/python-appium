# -*- coding: utf-8 -*-
"""预览页面的theme测试用例."""
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
import time


class TestPreviewTheme(TestCase):
    """预览页面的theme测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_preview_download(self):
        """预览页-下载主题."""
        sc.logger.info('预览页-下载主题')
        fun_name = 'test_preview_download'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('打开草稿工程')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeImage[1]")
        el_draft.click()

        time.sleep(1)
        sc.logger.info('点击“主题”按钮')
        sc.driver.find_element_by_name("vivavideo tool preview filter ").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载“主题”')
        el_theme_download = sc.driver.find_element_by_accessibility_id("vivavideo_tool_preview_download_n")
        try:
            el_theme_download.click()
            sc.capture_screen(fun_name,self.img_path)
        except NoSuchElementException:
            sc.logger.info('当前页面主题已全部下载，需要向左滑动到下一页')
            start_x = self.width - self.width // 10
            start_bottom = self.height - self.height // 5
            sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 500)
            el_theme_download.click()
            sc.capture_screen(fun_name, self.img_path)

    def test_preview_more(self):
        """预览页-下载更多."""
        sc.logger.info('预览页-下载更多')
        fun_name = 'test_more_download'

        sc.logger.info('点击“下载更多”按钮')
        el_more = sc.driver.find_element_by_xpath(
            "//XCUIElementTypeImage[@name='vivavideo_tool_camera_store_n']")
        try:
            el_more.click()
            time.sleep(2)
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('当前页面主题已全部下载，需要向右滑动切换到第一页')
            start_x = self.width // 10
            start_bottom = self.height - self.height // 5
            sc.swipe_by_ratio(start_x, start_bottom, 'right', 0.8, 500)
            el_more.click()
            time.sleep(2)
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“下载”按钮')
        el_theme_download = sc.driver.find_element_by_name("vivavideo material download n")
        el_theme_download.click()
        time.sleep(5)
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击“左上角”按钮返回预览页')
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()
