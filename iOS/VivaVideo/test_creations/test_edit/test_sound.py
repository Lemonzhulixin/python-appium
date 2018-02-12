# -*- coding: utf-8 -*-
"""配音的基本操作测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait

class TestEditSound(TestCase):
    """配音的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_sound_01_add(self):
        """剪辑-配音-添加."""
        sc.logger.info('剪辑-配音-添加')
        fun_name = 'test_edit_sound_add'

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

        sc.logger.info('点击"配音"')
        sc.driver.find_element_by_name("配音").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右侧预置"配音"图标')
        sc.driver.find_element_by_name("vivavideo tool sound list n").click()

        sc.logger.info('选择一个"音频"试听')
        el_sound_name = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeTable/*/XCUIElementTypeButton[2]")
        el_sound_name.click()

        sc.logger.info('添加')
        sc.driver.find_element_by_name("添加").click()

    def test_edit_sound_02_record(self):
        """剪辑-配音-录音."""
        sc.logger.info('剪辑-配音-录音')
        fun_name = 'test_edit_sound_record'

        try:
            WebDriverWait(sc.driver,20).until(
                lambda el_record:el_record.find_element_by_name("vivavideo tool sound start n"))
            el_record = sc.driver.find_element_by_name("vivavideo tool sound start n")

            sc.logger.info("授权小影访问麦克风")
            try:
                el_record.click()
                sc.driver.find_element_by_name("好").click()  # 授权访问麦克风
                time.sleep(1)
            except NoSuchElementException:
                sc.logger.info("已授权")

            sc.logger.info('长按录制5s音频')
            actions = TouchAction(sc.driver)
            actions.long_press(el_record, None, None, 5000).release().perform()
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('添加的配音音频时长超出20s，可选择时长小的音频或者修改等待时长')

        sc.logger.info('点击“右上角”保存')
        sc.driver.find_element_by_name("xiaoying com ok").click()

        sc.logger.info('存草稿并返回创作页首页')
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_edit_sound_03_del(self):
        """剪辑-配音-删除."""
        sc.logger.info('剪辑-配音-删除')
        fun_name = 'test_edit_sound_del'

        time.sleep(1)
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

        sc.logger.info('点击"配音"')
        try:
            sc.driver.find_element_by_name("配音").click()
        except NoSuchElementException:
            sc.logger.info('未找到"配乐"按钮，再向左滑动')
            sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 800)
            sc.driver.find_element_by_name("配音").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"播放"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar play").click()

        sc.logger.info('点击"编辑"按钮')
        try:
            WebDriverWait(sc.driver,30).until(
                lambda el_edit:el_edit.find_element_by_name("vivavideo tool fx edit n"))
            sc.logger.info('点击左侧"暂停"按钮')
            sc.driver.find_element_by_name("vivavideo editor framebar paus").click()

            sc.driver.find_element_by_name("vivavideo tool fx edit n").click()
            sc.capture_screen(fun_name, self.img_path)
            sc.logger.info('点击删除按钮')
            sc.driver.find_element_by_name("vivavideo tool subtitle delete").click()
            sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('点击右上角确认按钮')
            sc.driver.find_element_by_name("xiaoying com ok").click()
        except NoSuchElementException:
            sc.logger.error('未找到编辑按钮，请重试')
            return False

    def test_edit_sound_04_cancel(self):
        """剪辑-配音-放弃."""
        sc.logger.info('剪辑-配音-放弃')
        fun_name = 'test_edit_sound_cancel'

        sc.logger.info('点击"配音"')
        time.sleep(1)
        sc.driver.find_element_by_name("配音").click()

        sc.logger.info('点击右侧预置"配音"图标')
        sc.driver.find_element_by_name("vivavideo tool sound list n").click()

        sc.logger.info('选择一个"音频"试听')
        el_sound_name = sc.driver.find_element_by_xpath("//*/XCUIElementTypeTable/*/XCUIElementTypeButton[2]")
        el_sound_name.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加')
        sc.driver.find_element_by_name("添加").click()
        sc.capture_screen(fun_name, self.img_path)

        try:
            WebDriverWait(sc.driver,20).until(
                lambda el_record:el_record.find_element_by_name("vivavideo tool sound start n"))
            sc.logger.info('录制取消')
            el_record = sc.driver.find_element_by_name("vivavideo tool sound start n")
            actions = TouchAction(sc.driver)
            actions.long_press(el_record, None, None, 10000).move_to(
                sc.driver.find_element_by_name("滑到这里"), None, None).release().perform()
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('添加的配音音频时长超出20s，可选择时长小的音频或者修改等待时长')

        sc.logger.info('点击"左上角X"放弃添加')
        sc.driver.find_element_by_name("xiaoying com cancel").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"确认"放弃添加')
        sc.driver.find_element_by_name("确认").click()

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(3)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()