# -*- coding: utf-8 -*-
"""编辑音乐相关操作测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

class TestEditMusic(TestCase):
    """音乐相关操作测试测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_music_01_add(self):
        """剪辑-多段配乐-添加."""
        sc.logger.info('剪辑-多段配乐-添加')
        fun_name = 'test_edit_music_add'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"多段配乐"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("多段配乐").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('**************添加第一段配乐**************')
        try:
            sc.logger.info('点击添加按钮')
            sc.driver.find_element_by_name("vivavideo tool multimusic add ").click()
        except NoSuchElementException:
            sc.logger.info('当前视频位置已经添加过配乐，删除原配乐')
            sc.driver.find_element_by_name("vivavideo tool fx edit n").click()
            sc.logger.info('点击删除按钮')
            sc.driver.find_element_by_name("vivavideo tool subtitle delete").click()
            sc.logger.info('点击添加按钮')
            sc.driver.find_element_by_name("vivavideo tool multimusic add ").click()

        sc.logger.info('点击下载按钮')
        el_download = sc.driver.find_element_by_name('vivavideo material download3 n')
        el_download.click()
        sc.capture_screen(fun_name, self.img_path)
        time.sleep(10)

        sc.logger.info('点击第一首已下载音频试听')
        el_music_name = sc.driver.find_element_by_xpath("//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        try:
            el_music_name.click()
        except NoSuchElementException:
            sc.logger.error('音频下载未完成，继续等待5s')
            time.sleep(5)
            el_music_name.click()

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()

        sc.logger.info('5s后点击屏幕"暂停"播放')
        time.sleep(5)
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认添加的片段')
        sc.driver.find_element_by_name("vivavideo tool subtitle comple").click()

        sc.logger.info('点击左侧"播放按钮"')
        sc.driver.find_element_by_name("vivavideo editor framebar play").click()

        sc.logger.info('5s后点击屏幕"暂停"播放')
        time.sleep(5)
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('**************添加第二段配乐**************')
        try:
            sc.logger.info('点击添加按钮')
            sc.driver.find_element_by_name("vivavideo tool multimusic add ").click()
        except NoSuchElementException:
            sc.logger.info('当前视频位置已经添加过配乐，删除原配乐')
            sc.driver.find_element_by_name("vivavideo tool fx edit n").click()
            sc.logger.info('点击删除按钮')
            sc.driver.find_element_by_name("vivavideo tool subtitle delete").click()
            sc.logger.info('点击添加按钮')
            sc.driver.find_element_by_name("vivavideo tool multimusic add ").click()

        sc.logger.info('点击第一首音频试听')
        el_music_name = sc.driver.find_element_by_xpath("//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        el_music_name.click()

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()

        sc.logger.info('3s后点击屏幕"暂停"播放')
        time.sleep(3)
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()

        sc.logger.info('确认添加的第二段配乐')
        sc.driver.find_element_by_name("vivavideo tool subtitle comple").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_name("xiaoying com ok").click()

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_edit_music_02_del(self):
        """剪辑-多段配乐-删除."""
        sc.logger.info('剪辑-多段配乐-删除')
        fun_name = 'test_edit_music_del'

        time.sleep(1)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"多段配乐"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("多段配乐").click()

        sc.logger.info('点击"编辑"按钮')
        sc.driver.find_element_by_name("vivavideo tool fx edit n").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击删除按钮')
        sc.driver.find_element_by_name("vivavideo tool subtitle delete").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_name("xiaoying com ok").click()

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_edit_music_03_cancel(self):
        """剪辑-多段配乐-放弃."""
        sc.logger.info('剪辑-多段配乐-放弃')
        fun_name = 'test_edit_music_cancel'

        time.sleep(1)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"多段配乐"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("多段配乐").click()

        sc.logger.info('添加一段配乐')
        try:
            sc.logger.info('点击添加按钮')
            sc.driver.find_element_by_name("vivavideo tool multimusic add ").click()
        except NoSuchElementException:
            sc.logger.info('当前视频位置已经添加过配乐，删除原配乐')
            sc.driver.find_element_by_name("vivavideo tool fx edit n").click()
            sc.logger.info('点击删除按钮')
            sc.driver.find_element_by_name("vivavideo tool subtitle delete").click()
            sc.logger.info('点击添加按钮')
            sc.driver.find_element_by_name("vivavideo tool multimusic add ").click()

        sc.logger.info('点击第一首音频试听')
        el_music_name = sc.driver.find_element_by_xpath("//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        el_music_name.click()

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()

        sc.logger.info('3s后点击屏幕"暂停"播放')
        time.sleep(3)
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()

        sc.logger.info('点击左侧"撤销"按钮')
        sc.driver.find_element_by_name("vivavideo tool subtitle undo n").click()

        sc.logger.info('点击添加按钮')
        sc.driver.find_element_by_name("vivavideo tool multimusic add ").click()

        sc.logger.info('点击第一首音频试听')
        el_music_name = sc.driver.find_element_by_xpath("//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        el_music_name.click()

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()

        sc.logger.info('3s后点击屏幕"暂停"播放')
        time.sleep(3)
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()

        sc.logger.info('确认添加配乐')
        sc.driver.find_element_by_name("vivavideo tool subtitle comple").click()
        sc.capture_screen(fun_name, self.img_path)

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