# -*- coding: utf-8 -*-
"""添加字幕的基本操作测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException


class TestEditText(TestCase):
    """添加字幕的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_text_01_add(self):
        """剪辑-字幕-添加."""
        sc.logger.info('剪辑-字幕-添加')
        fun_name = 'test_edit_text_add'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"字幕"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("字幕").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('**************添加第一个字幕**************')
        sc.logger.info('点击添加按钮')
        sc.driver.find_element_by_name("vivavideo editor subtitle add").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加默认动态字幕')
        time.sleep(3)

        sc.logger.info('选择添加的"动态字幕"')
        sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther/XCUIElementTypeImage[1]").click()

        sc.logger.info('输入字幕')
        el_text_input = sc.driver.find_element_by_ios_predicate(
            "type == 'XCUIElementTypeTextView' AND value == '请输入动态文字'")
        el_text_input.clear()
        el_text_input.send_keys("input text test")
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右侧"确认"按钮')
        sc.driver.find_element_by_name("确认").click()

        sc.logger.info('点击右上角保存')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()

        sc.logger.info('点击左侧"暂停"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar paus").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击底部"确认"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar comp").click()
        sc.capture_screen(fun_name, self.img_path)

    def test_edit_text_02_edit(self):
        """剪辑-字幕-编辑."""
        sc.logger.info('剪辑-字幕-编辑')
        fun_name = 'test_edit_text_edit'

        sc.logger.info('**************添加第二个字幕**************')
        sc.logger.info('点击添加按钮')
        sc.driver.find_element_by_name("vivavideo editor subtitle add").click()

        sc.logger.info('切换到普通字幕')
        sc.driver.find_element_by_name("xiaoying caption bar text n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择一个普通字幕并添加')
        el_com_text = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_com_text.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换到字体页面')
        sc.driver.find_element_by_name("xiaoying caption bar aa n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"下载"按钮')
        try:
            el_text_down = sc.driver.find_element_by_accessibility_id(
                "vivavideo_camera_tool_icon_sticker_download_nrm")
            el_text_down.click()
        except NoSuchElementException:
            sc.logger.info('当前页面已无为下载字体')

        sc.logger.info('切换到描边页面')
        sc.driver.find_element_by_name("xiaoying caption bar font n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换到字体设置页面')
        sc.driver.find_element_by_name("xiaoying caption bar set n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击阴影开关')
        sc.driver.find_element_by_xpath("//*/XCUIElementTypeSwitch[1]").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击字幕动画开关')
        sc.driver.find_element_by_xpath("//*/XCUIElementTypeSwitch[2]").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('左对齐')
        sc.driver.find_element_by_name("xiaoying caption bar set btn l").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('居中对齐')
        sc.driver.find_element_by_name("xiaoying caption bar set btn c").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('右对齐')
        sc.driver.find_element_by_name("xiaoying caption bar set btn r").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角保存')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()

        sc.logger.info('点击左侧"暂停"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar paus").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击底部"确认"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar comp").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角保存')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_edit_text_03_del(self):
        """剪辑-字幕-删除."""
        sc.logger.info('剪辑-字幕-删除')
        fun_name = 'test_edit_text_del'

        time.sleep(1)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"字幕"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("字幕").click()

        sc.logger.info('点击已添加的"字幕"')
        sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击删除按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar dele").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()

    def test_edit_text_04_cancel(self):
        """剪辑-字幕-放弃."""
        sc.logger.info('剪辑-字幕-放弃')
        fun_name = 'test_edit_text_cancel'

        sc.logger.info('点击"字幕"')
        time.sleep(1)
        sc.driver.find_element_by_name("字幕").click()

        sc.logger.info('点击添加按钮')
        sc.driver.find_element_by_name("vivavideo editor subtitle add").click()

        sc.logger.info('添加默认动态字幕')
        time.sleep(3)

        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()

        sc.logger.info('点击左侧"暂停"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar paus").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左侧"撤销"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar undo").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('放弃编辑')
        sc.driver.find_element_by_name("vivavideo editor common cancel").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"确认"放弃添加')
        sc.driver.find_element_by_name("确认").click()

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(3)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()