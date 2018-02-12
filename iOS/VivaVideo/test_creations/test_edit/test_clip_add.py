# -*- coding: utf-8 -*-
"""镜头添加相关操作的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from appium.webdriver.common.touch_action import TouchAction


class TestEditClipsAdd(TestCase):
    """镜头添加相关操作的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_add_01_clips(self):
        """剪辑-添加镜头-相册添加."""
        sc.logger.info('剪辑-添加镜头-相册添加')
        fun_name = 'test_edit_add_clips'

        time.sleep(5)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"剪辑"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()

        sc.logger.info('向左滑动，点击"添加镜头"')
        start_x = self.width - self.width // 10
        start_bottom = self.height - self.height // 5
        while True:
            try:
                sc.driver.find_element_by_name("添加镜头").click()
                break
            except:
                sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 500)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加视频')
        el_video = sc.driver.find_element_by_accessibility_id("vivavideo_tool_gallery_audio_type_video")
        el_video.click()
        sc.driver.find_element_by_name("添加 0").click()

        sc.logger.info('切换到图片')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()

        sc.logger.info('添加图片')
        el_img = sc.driver.find_element_by_xpath("//*/XCUIElementTypeImage")
        el_img.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"下一步"')
        sc.driver.find_element_by_name("下一步").click()

    def test_edit_clips_02_shot(self):
        """剪辑-添加镜头-拍摄添加."""
        sc.logger.info('剪辑-添加镜头-拍摄添加')
        fun_name = 'test_edit_clips_shot'

        sc.logger.info('点击"添加镜头"')
        time.sleep(5)
        sc.driver.find_element_by_name("添加镜头").click()

        sc.logger.info('点击右上角拍摄按钮')
        sc.driver.find_element_by_name("vivavideo gallery create captu").click()
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('开始录制')
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)

        sc.logger.info('录制5s后点击录制按钮停止录制')
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"下一步"')
        sc.driver.find_element_by_name("下一步").click()

    def test_edit_clips_03_cancel(self):
        """剪辑-添加镜头-放弃."""
        sc.logger.info('剪辑-添加镜头-放弃')
        fun_name = 'test_edit_clips_cancel'

        sc.logger.info('点击"添加镜头"')
        time.sleep(5)
        sc.driver.find_element_by_name("添加镜头").click()

        sc.logger.info('切换到图片')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()

        sc.logger.info('添加图片')
        el_img = sc.driver.find_element_by_xpath("//*/XCUIElementTypeImage")
        el_img.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“左上角按钮”取消')
        sc.driver.find_element_by_name("vivavideo gallery back n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认取消')
        sc.driver.find_element_by_name("确认").click()
        time.sleep(3)

        sc.logger.info('存草稿并返回创作页首页')
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_edit_sort(self):
        """剪辑-排序."""
        sc.logger.info('剪辑-排序')
        fun_name = 'test_edit_sort'

        time.sleep(5)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"剪辑"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()

        sc.logger.info('向左滑动，点击"排序"')
        start_x = self.width - self.width // 10
        start_bottom = self.height - self.height // 5
        while True:
            try:
                sc.driver.find_element_by_name("排序").click()
                break
            except:
                sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 500)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('把特效和动画贴纸位置互换')
        el_fx = sc.driver.find_element_by_name("特效")
        el_sticker = sc.driver.find_element_by_name("动画贴纸")
        actions = TouchAction(sc.driver)
        actions.long_press(el_fx, None, None, 1000).move_to(el_sticker, None, None, 1000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"完成"保存设置')
        sc.driver.find_element_by_name("完成").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('存草稿并返回创作页首页')
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()