# -*- coding: utf-8 -*-
"""封面编辑相关的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException


class TestCoverText(TestCase):
    """封面编辑相关的测试用例类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_text_01_use(self):
        """更换封面-使用字幕."""
        sc.logger.info('更换封面-使用字幕')
        fun_name = 'test_text_use'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('点击"高清拍摄"按钮')
        try:
            sc.driver.find_element_by_name("高清拍摄").click()
        except NoSuchElementException:
            sc.logger.info('当前版本为测试版，点击默认"拍摄"按钮')
            sc.driver.find_element_by_name("拍摄").click()

        # 点拍
        sc.logger.info('开始录制')
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(10)

        sc.logger.info('录制10s后点击录制按钮停止录制')
        el_capture.click()

        sc.logger.info('点击确认按钮进入预览页')
        sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()

        sc.logger.info('点击"更换封面"')
        sc.driver.find_element_by_name("更换封面").click()
        time.sleep(3)

        sc.logger.info('点击"字幕"按钮')
        sc.driver.find_element_by_name("cover tool preview caption n").click()

        sc.logger.info('添加一个字幕')
        el_text_select = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_text_select.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('编辑字幕')
        sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther/XCUIElementTypeImage[2]").click()

        sc.logger.info('输入字幕')
        el_text_input = sc.driver.find_element_by_ios_predicate(
            "type == 'XCUIElementTypeTextView' AND value == '点击输入字幕…'")
        el_text_input.clear()
        el_text_input.send_keys("input text test")

        sc.logger.info('保存输入的字幕')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Done']").click()
        except NoSuchElementException:
            sc.logger.info("当前键盘为中文键盘")
            sc.driver.find_element_by_xpath("完成").click()

        sc.logger.info('等待2s并截图')
        time.sleep(2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换字幕分类')
        el_text_type = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[1]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_text_type.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('保存已添加的封面字幕')
        sc.driver.find_element_by_name("xiaoying itembar finish").click()
        time.sleep(0.5)
        sc.driver.find_element_by_name("vivavideo editor common ok").click()
        sc.capture_screen(fun_name, self.img_path)

    def test_text_02_download(self):
        """更换封面-下载字幕/字体."""
        sc.logger.info('更换封面-下载字幕/字体')
        fun_name = 'test_text_download'

        time.sleep(1)
        sc.logger.info('点击"更换封面"')
        sc.driver.find_element_by_name("更换封面").click()
        time.sleep(3)

        sc.logger.info('点击"字幕"按钮')
        sc.driver.find_element_by_name("cover tool preview caption n").click()

        sc.logger.info('点击"下载更多"字幕')
        sc.driver.find_element_by_name("xiaoying itembar down more").click()

        sc.logger.info('点击"下载"按钮')
        el_text_download = sc.driver.find_element_by_name("vivavideo material download n")
        el_text_download.click()
        time.sleep(10)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('使用下载的字幕')
        el_text_use = sc.driver.find_element_by_name("使用")
        try:
            el_text_use.click()
            time.sleep(0.5)
        except NoSuchElementException:
            sc.logger.info('字幕下载未完成，继续等待5s')
            time.sleep(5)
            el_text_use.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"字体"按钮')
        sc.driver.find_element_by_name("字体").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载任意"字体"')
        el_text_download = sc.driver.find_element_by_accessibility_id("vivavideo_camera_tool_icon_sticker_download_nrm")
        try:
            el_text_download.click()
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('当前页面已无为下载"字体"')

        sc.logger.info('放弃编辑并返回发布页')
        sc.driver.find_element_by_name("xiaoying itembar close").click()
        sc.driver.find_element_by_name("vivavideo editor common cancel").click()
        sc.capture_screen(fun_name, self.img_path)

    def test_text_03_delete(self):
        """更换封面-删除添加的字幕."""
        sc.logger.info('更换封面-删除添加的字幕')
        fun_name = 'test_text_delete'

        time.sleep(1)
        sc.logger.info('点击"更换封面"')
        sc.driver.find_element_by_name("更换封面").click()
        time.sleep(3)

        sc.logger.info('点击"字幕"按钮')
        sc.driver.find_element_by_name("cover tool preview caption n").click()

        sc.logger.info('添加一个字幕')
        el_text_select = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_text_select.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除已添加的字幕')
        el_text_del = sc.driver.find_element_by_accessibility_id(
            "XiaoYingResource.bundle/xiaoying_subtitle_delete")
        el_text_del.click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('保存编辑并返回首页')
        sc.driver.find_element_by_name("xiaoying itembar finish").click()
        time.sleep(0.5)
        sc.driver.find_element_by_name("vivavideo editor common ok").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()