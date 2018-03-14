# -*- coding: utf-8 -*-
"""预览页面的theme测试用例."""
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
import time


class TestPreviewUI(TestCase):
    """预览页面的theme测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_preview_01_create(self):
        """创建草稿视频."""
        sc.logger.info('创建草稿视频')
        fun_name = 'test_preview_create'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('点击视频剪辑')
        sc.driver.find_element_by_name("视频剪辑").click()
        time.sleep(1)
        try:
            sc.driver.find_element_by_name("跳过").click()
            time.sleep(1)
            sc.driver.find_element_by_name("视频剪辑").click()
        except NoSuchElementException:
            sc.logger.info('已跳过订阅页面')

        sc.logger.info("授权小影访问相册和媒体资料")
        try:
            sc.driver.find_element_by_name("好").click()  # 授权相册
            time.sleep(2)
            sc.driver.find_element_by_name("好").click()  # 授权媒体资料库
        except NoSuchElementException:
            sc.logger.info("已授权")

        sc.logger.info('添加视频')
        el_video = sc.driver.find_element_by_accessibility_id("vivavideo_tool_gallery_audio_type_video")
        el_video.click()
        sc.driver.find_element_by_name("添加 0").click()

        sc.logger.info('添加图片')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()
        el_imgs = sc.driver.find_elements_by_xpath("//*/XCUIElementTypeImage")
        i = 1
        while i < len(el_imgs):
            el_imgs[i].click()
            i = i + 1

        sc.logger.info('点击下一步，进入预览页')
        sc.driver.find_element_by_name("下一步").click()
        sc.capture_screen(fun_name,self.img_path)

    def test_preview_02_ui(self):
        """预览页-UI."""
        sc.logger.info('预览页-UI')
        fun_name = 'test_preview_create'

        time.sleep(1)
        sc.logger.info('点击“主题”按钮')
        sc.driver.find_element_by_name("vivavideo tool preview filter ").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“配乐”按钮')
        sc.driver.find_element_by_name("vivavideo tool preview music n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“剪辑”按钮')
        sc.driver.find_element_by_name("vivavideo tool preview edit n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“全屏”按钮')
        try:
            el_fullscreen = sc.driver.find_element_by_name("vivavideo playerview fullscree")
            el_fullscreen.click()
            sc.capture_screen(fun_name, self.img_path)
            time.sleep(1)
            sc.logger.info('点击“左上角返回”按钮退出全屏')
            el_fullscreen.click()
        except NoSuchElementException:
            sc.logger.info('该草稿工程为1:1视频，无全屏按钮')

        sc.logger.info('点击“小影水印”按钮')
        time.sleep(1)
        try:
            el_watermark = sc.driver.find_element_by_name("vivavideo watermark edit cn n")
            el_watermark.click()
            time.sleep(0.5)
            sc.capture_screen(fun_name,self.img_path)
            sc.driver.find_element_by_name("vivavideo popup close").click()
        except NoSuchElementException:
            sc.logger.info('会员账号已登录，水印已去除')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“保存并上传”按钮')
        sc.driver.find_element_by_name("保存/上传").click()
        sc.capture_screen(fun_name, self.img_path)
        time.sleep(1)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_preview_03_time(self):
        """预览页-时长."""
        sc.logger.info('预览页-时长')
        fun_name = 'test_preview_time'

        time.sleep(1)
        sc.logger.info('点击相册MV')
        sc.driver.find_element_by_name("相册MV").click()

        sc.logger.info('添加图片')
        el_imgs = sc.driver.find_elements_by_xpath("//*/XCUIElementTypeImage")
        i = 1  # 第0个为顶部的下拉框
        while i < len(el_imgs):
            el_imgs[i].click()
            i = i + 1

        sc.logger.info('进入预览页')
        sc.driver.find_element_by_name("下一步").click()

        sc.logger.info('点击“时长”')
        sc.driver.find_element_by_name("vivavideo tool preview imageti").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()