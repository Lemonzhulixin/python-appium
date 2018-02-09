# -*- coding: utf-8 -*-
from unittest import TestCase
from iOS import script_ultils as sc
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class TestGallery(TestCase):
    # 获取屏幕尺寸
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_gallery_01_video(self):
        """相册-视频"""
        fun_name = 'test_gallery_video'

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
            sc.driver.find_element_by_name("好").click() #授权相册
            time.sleep(2)
            sc.driver.find_element_by_name("好").click() #授权媒体资料库
        except NoSuchElementException:
            sc.logger.info("已授权")

        sc.logger.info('点击其它相册')
        sc.driver.find_element_by_name("其他相册").click()
        sc.driver.find_element_by_name("全部").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加视频')
        el_video = sc.driver.find_elements_by_accessibility_id("vivavideo_tool_gallery_audio_type_video")
        el_video[0].click()
        time.sleep(1)
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='vivavideo tool gallery rotate ']").click()
        try:
            sc.driver.find_element_by_name('vivavideo tool gallery square').click()
        except NoSuchElementException:
            sc.logger.info('视频尺寸1:1，无此选项')
        sc.driver.find_element_by_name("vivavideo tool gallery trim d").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='添加 1']").click()

        sc.logger.info('导入视频')
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_improt: V_improt.find_element_by_name("下一步"))
        except TimeoutError as t:
            sc.logger.error('导入视频超时', t)
            return False
        except Exception as e:
            sc.logger.error('导入视频出错', e)
            return False
        sc.driver.find_element_by_name("下一步").click()

        sc.logger.info('预览页存草稿')
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_gallery_02_img(self):
        """相册-图片"""
        fun_name = 'test_gallery_img'

        sc.logger.info('点击视频剪辑')
        sc.driver.find_element_by_name("视频剪辑").click()
        time.sleep(1)

        sc.logger.info('切换到相册页面')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()
        sc.driver.find_element_by_name("其他相册").click()
        sc.driver.find_element_by_name("全部").click()

        sc.logger.info('图片操作-旋转')
        el_edit_img = sc.driver.find_elements_by_name("vivavideo edit gallery icon zo")
        el_edit_img[0].click()
        sc.driver.find_element_by_name("vivavideo edit icon rotate n").click()
        sc.driver.find_element_by_name("添加").click()

        sc.logger.info('图片操作-勾选')
        el_edit_img[1].click()
        sc.driver.find_element_by_name("vivavideo gallery icon choose ").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("添加(1)").click()

        sc.logger.info('图片操作-连续多选')
        el_imgs = sc.driver.find_elements_by_xpath("//*/XCUIElementTypeImage")
        i = 1
        while i < len(el_imgs):
            el_imgs[i].click()
            i = i + 1
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('预览页存草稿')
        sc.driver.find_element_by_name("下一步").click()
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_gallery_03_storyboard(self):
        """相册-storyboard"""
        fun_name = 'test_gallery_storyboard'

        sc.logger.info('点击视频剪辑')
        sc.driver.find_element_by_name("视频剪辑").click()
        time.sleep(1)

        sc.logger.info('添加多个视频')
        el_video = sc.driver.find_elements_by_accessibility_id("vivavideo_tool_gallery_audio_type_video")
        for i in range(3):
            el_video[i].click()
            sc.driver.find_element_by_name("添加 0").click()

        sc.logger.info('添加多张图片')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()
        el_imgs = sc.driver.find_elements_by_xpath("//*/XCUIElementTypeImage")
        i = 1
        while i < len(el_imgs):
            el_imgs[i].click()
            i = i + 1

        sc.logger.info('Storyboad操作')
        sc.driver.find_element_by_name("vivavideo tool gallery up n").click()
        sc.capture_screen(fun_name, self.img_path)
        el_del = sc.driver.find_elements_by_name("vivavideo edit video close n")
        for i in range(3):
            el_del[i].click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('预览页存草稿')
        sc.driver.find_element_by_name("下一步").click()
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    @staticmethod
    def test_gallery_04_giveup():
        """相册-放弃操作"""
        sc.logger.info('点击视频剪辑')
        sc.driver.find_element_by_name("视频剪辑").click()
        time.sleep(1)

        sc.logger.info('取消添加视频')
        el_video = sc.driver.find_elements_by_accessibility_id("vivavideo_tool_gallery_audio_type_video")
        el_video[0].click()
        sc.driver.find_element_by_name("xiaoying com cancel").click()

        sc.logger.info('取消添加图片')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()
        el_edit_img = sc.driver.find_elements_by_name("vivavideo edit gallery icon zo")
        el_edit_img[0].click()
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='vivavideo gallery back n']").click()

        sc.logger.info('放弃保存-取消')
        el_edit_img[0].click()
        sc.driver.find_element_by_name("添加").click()
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='vivavideo gallery back n']").click()
        sc.driver.find_element_by_name("取消").click()

        sc.logger.info('放弃保存-丢弃')
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='vivavideo gallery back n']").click()
        sc.driver.find_element_by_name("丢弃").click()