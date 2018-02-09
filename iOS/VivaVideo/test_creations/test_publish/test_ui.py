# -*- coding: utf-8 -*-
"""创作页面内分享相关的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction


class TestPublishUI(TestCase):
    """创作页面内分享相关的测试类.

    1.表情/话题/位置控件获取不到，需要再调"""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @staticmethod
    def test_publish_01_create():
        """分享-创建视频."""
        sc.logger.info('分享-创建视频')

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

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_publish_02_ui(self):
        """分享-UI"""
        sc.logger.info('分享-UI')
        fun_name = 'test_publish_ui'

        time.sleep(1)
        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(0.5)

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()
        time.sleep(0.5)
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击"更换封面"')
        sc.driver.find_element_by_name("更换封面").click()
        time.sleep(3)
        sc.capture_screen(fun_name,self.img_path)
        sc.driver.find_element_by_name("vivavideo editor common cancel").click()

        """表情/话题/位置控件获取不到，需要再调试"""
        # sc.logger.info('点击"表情"')
        # time.sleep(1)
        # sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='vivavideo icon face']")
        # # el_emoji = sc.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeButton'")
        # # for emoji in el_emoji:
        # #     if emoji.text == u'vivavideo icon face':
        # #         emoji.click()
        # #         break
        # sc.capture_screen(fun_name, self.img_path)

        # sc.logger.info('点击屏幕消除贴纸控件')
        # actions = TouchAction(sc.driver)
        # actions.tap(None, 500, 500, 0.5).release().perform()
        # time.sleep(0.5)
        # sc.capture_screen(fun_name, self.img_path)

        # sc.logger.info('点击"添加话题"')
        # time.sleep(1)
        # sc.driver.find_element_by_name(" 添加话题").click()
        # sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name=' 添加话题']")
        # sc.capture_screen(fun_name, self.img_path)
        #
        # sc.logger.info('从"添加话题"页面返回')
        # sc.driver.find_element_by_name("取消").click()
        #
        # sc.logger.info('点击"显示位置"')
        # sc.driver.find_element_by_name(" 显示位置").click()
        # time.sleep(1)
        # sc.capture_screen(fun_name, self.img_path)
        #
        # sc.logger.info('授权小影访问位置')
        # try:
        #     sc.driver.find_element_by_name("允许").click()
        # except NoSuchElementException:
        #     sc.logger.info('已授权')
        #
        # sc.logger.info('从"添加位置"页面返回')
        # sc.driver.find_element_by_name("取消").click()

        sc.logger.info('点击"隐私设置"')
        sc.driver.find_element_by_name("隐私设置").click()
        time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('消除"隐私设置"弹窗')
        sc.driver.find_element_by_name("完成").click()

        sc.logger.info('点击"保存/上传"')
        sc.driver.find_element_by_name("保存/上传").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()