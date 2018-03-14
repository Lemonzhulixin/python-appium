# -*- coding: utf-8 -*-
"""预览页面的music测试用例."""
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
import time

class TestPreviewMusic(TestCase):
    """预览页面的music测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @staticmethod
    def test_music_01_create():
        """导出-创建视频."""
        sc.logger.info('分享-创建视频')

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('点击高清拍摄')
        sc.driver.find_element_by_name("高清拍摄").click()

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

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_music_02_add(self):
        """预览页-配乐."""
        sc.logger.info('预览页-配乐')
        fun_name = 'test_music_add'

        time.sleep(1)
        sc.logger.info('点击第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击“配乐”按钮')
        sc.driver.find_element_by_name("vivavideo tool preview music n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“点击添加配乐”按钮')
        sc.driver.find_element_by_name("点击添加配乐").click()
        time.sleep(2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击第下载按钮')
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

        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_name("vivavideo tool camera pause n").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()
        time.sleep(0.5)
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('关闭视频原声')
        sc.driver.find_element_by_name("vivavideo tool preview sound n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('关闭配乐')
        sc.driver.find_element_by_name("vivavideo tool grid moremusic ").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除配乐')
        sc.driver.find_element_by_name("vivavideo tool preview delete2").click()
        sc.capture_screen(fun_name,self.img_path)

    def test_preview_03_recommend(self):
        """音乐库-推荐音乐下载."""
        sc.logger.info('音乐库-推荐音乐下载')
        fun_name = 'test_preview_recommend'

        sc.logger.info('点击“点击添加配乐”按钮')
        sc.driver.find_element_by_name("点击添加配乐").click()
        time.sleep(1)

        sc.logger.info('点击“推荐”tab')
        sc.driver.find_element_by_name("推荐").click()

        sc.logger.info('向上滑动“推荐”音频列表')
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)

        sc.logger.info('同时下载多个音频')
        el_download = sc.driver.find_elements_by_name('vivavideo material download3 n')
        for i in range(len(el_download)):
            el_download[i].click()
        sc.capture_screen(fun_name, self.img_path)

    def test_preview_04_other(self):
        """音乐库-其他分类音乐下载."""
        sc.logger.info('音乐库-其他分类音乐下载')
        fun_name = 'test_preview_other'

        sc.logger.info('通过滑动屏幕切换到"流行"分类')
        start_x = self.width - self.width // 5
        start_bottom = self.height // 2
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.7, 500)

        sc.logger.info('下载"流行"分类音频')
        time.sleep(1)
        el_download = sc.driver.find_element_by_name('vivavideo material download3 n')
        el_download.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('通过点击分类tab切换到"爵士 & 蓝调"分类')
        sc.driver.find_element_by_name("爵士 & 蓝调").click()

        sc.logger.info('下载"爵士 & 蓝调"分类音频')
        time.sleep(1)
        el_download = sc.driver.find_element_by_name('vivavideo material download3 n')
        el_download.click()
        sc.capture_screen(fun_name, self.img_path)

    def test_preview_05_use(self):
        """音乐库-使用已下载音乐."""
        sc.logger.info('音乐库-使用已下载音乐')
        fun_name = 'test_preview_use'

        sc.logger.info('点击“已下载”tab')
        sc.driver.find_element_by_name("已下载").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('选择一首已下载音频试听')
        el_music_name = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        el_music_name.click()

        sc.logger.info('点击播放/暂停按钮')
        sc.driver.find_element_by_name("vivavideo tool camera pause n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()
        time.sleep(0.5)

        sc.logger.info('再次进入音乐库')
        sc.driver.find_element_by_xpath('//XCUIElementTypeImage[@name="vivavideo_tool_preview_next_n"]').click()
        time.sleep(0.5)

        sc.logger.info('切换到“其它”分类')
        sc.driver.find_element_by_name("其它").click()
        sc.capture_screen(fun_name,self.img_path)

    def test_preview_06_delete(self):
        """音乐库-删除已下载音乐."""
        sc.logger.info('音乐库-删除已下载音乐')
        fun_name = 'test_preview_delete'

        sc.logger.info('点击删除按钮')
        sc.driver.find_element_by_name("vivavideo music delete n").click()
        time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择任意一首音频')
        sc.driver.find_element_by_name("vivavideo music choose n").click()
        time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('再次点击删除按钮')
        sc.driver.find_element_by_name("vivavideo music delete h").click()
        sc.capture_screen(fun_name,self.img_path)

    def test_preview_07_local(self):
        """音乐库-使用本地音乐."""
        sc.logger.info('音乐库-使用本地音乐')
        fun_name = 'test_preview_local'

        sc.logger.info('切换到“本地”分类')
        sc.driver.find_element_by_name("本地").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择一首本地音频试听')
        el_music_name = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeTable//*/XCUIElementTypeButton[2]")
        try:
            el_music_name.click()
            sc.logger.info('点击播放/暂停按钮')
            sc.driver.find_element_by_name("vivavideo tool camera pause n").click()

            sc.logger.info('点击“添加”按钮')
            sc.driver.find_element_by_name('添加').click()
            time.sleep(0.5)
        except NoSuchElementException:
            sc.logger.info('本地音乐不存在,返回预览页！')
            sc.driver.find_element_by_name("xiaoying com back").click()

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(0.5)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()