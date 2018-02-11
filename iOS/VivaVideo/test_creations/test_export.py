# -*- coding: utf-8 -*-
"""创作页面内导出视频相关的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction


class TestCreationExport(TestCase):
    """
    创作页面内导出视频相关的测试类.
    使用已购买会员账号登录
    """

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @staticmethod
    def test_export_01_create():
        """导出-创建视频."""
        sc.logger.info('导出-创建视频')

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

    def test_export_02_first(self):
        """导出-保存到相册-480P."""
        sc.logger.info('导出-保存到相册-480P-首次导出')
        fun_name = 'test_export_first'

        time.sleep(1)
        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(0.5)

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()
        time.sleep(0.5)

        sc.logger.info('点击屏幕消除软键盘')
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()

        sc.logger.info('点击“保存到相册”')
        sc.driver.find_element_by_name('保存到相册').click()
        time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“清晰 480P”')
        try:
            sc.driver.find_element_by_name("清晰 480P").click()
            time.sleep(0.5)
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('该视频已导出，需要确认是否重新导出')
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_name("重新导出").click()
            time.sleep(0.5)
            sc.driver.find_element_by_name("清晰 480P").click()
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('开始导出')
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_exprot: V_exprot.find_element_by_name('我的工作室'))
            sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(0.5)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("感觉如何")
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_name("稍后再说").click()

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(0.5)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
        except Exception as e:
            sc.logger.error('导出失败', e)
            return False

    def test_export_03_second(self):
        """导出-保存到相册-720P."""
        sc.logger.info('导出-保存到相册-720P-二次导出')
        fun_name = 'test_export_second'

        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(0.5)

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()
        time.sleep(0.5)

        sc.logger.info('点击屏幕消除软键盘')
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()

        sc.logger.info('点击“保存到相册”')
        sc.driver.find_element_by_name('保存到相册').click()
        time.sleep(0.5)

        sc.logger.info('点击“高清 720P”')
        try:
            sc.driver.find_element_by_name("高清 720P").click()
            time.sleep(0.5)
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('该视频已导出，需要确认是否重新导出')
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_name("重新导出").click()
            time.sleep(0.5)
            sc.driver.find_element_by_name("高清 720P").click()
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('开始导出')
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_exprot: V_exprot.find_element_by_name('我的工作室'))

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(0.5)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("感觉如何")
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_name("稍后再说").click()

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(0.5)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
        except Exception as e:
            sc.logger.error('导出失败', e)
            return False

    def test_export_04_third(self):
        """导出-保存到相册-1080P."""
        sc.logger.info('导出-保存到相册-1080P')
        fun_name = 'test_export_third'

        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(0.5)

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()
        time.sleep(0.5)

        sc.logger.info('点击屏幕消除软键盘')
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()

        sc.logger.info('点击“保存到相册”')
        sc.driver.find_element_by_name('保存到相册').click()
        time.sleep(0.5)

        sc.logger.info('确认视频是否已导出')
        try:
            sc.driver.find_element_by_name("重新导出").click()
            time.sleep(0.5)
        except NoSuchElementException:
            sc.logger.info('该视频未导出过，直接选择要导出的尺寸')

        sc.logger.info('点击“超清 1080P”')
        try:
            sc.driver.find_element_by_name("超清 1080P").click()
            time.sleep(0.5)
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('当前设备不支持1080P导出，点击屏幕消除选项框')
            actions = TouchAction(sc.driver)
            actions.tap(None, 500, 300, 1).release().perform()

            sc.logger.info('点击“存草稿”按钮')
            sc.driver.find_element_by_name("存草稿").click()

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(1)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
            return True

        sc.logger.info('开始导出')
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_exprot: V_exprot.find_element_by_name('我的工作室'))

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(0.5)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("感觉如何")
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_name("稍后再说").click()

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(0.5)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
        except Exception as e:
            sc.logger.error('导出失败', e)
            return False

    def test_export_05_gif(self):
        """导出-保存到相册-GIF."""
        sc.logger.info('导出-保存到相册-GIF')
        fun_name = 'test_export_gif'

        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(0.5)

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()
        time.sleep(0.5)

        sc.logger.info('点击屏幕消除软键盘')
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()

        sc.logger.info('点击“保存到相册”')
        sc.driver.find_element_by_name('保存到相册').click()
        time.sleep(0.5)

        sc.logger.info('确认视频是否已导出')
        try:
            sc.driver.find_element_by_name("重新导出").click()
            time.sleep(0.5)
        except NoSuchElementException:
            sc.logger.info('该视频未导出过，直接选择要导出的尺寸')

        sc.logger.info('点击“GIF”')
        try:
            sc.driver.find_element_by_name("GIF").click()
            time.sleep(0.5)
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('当前设备不支持GIF导出，点击屏幕消除选项框')
            actions = TouchAction(sc.driver)
            actions.tap(None, 500, 300, 1).release().perform()

            sc.logger.info('点击“存草稿”按钮')
            sc.driver.find_element_by_name("存草稿").click()

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(1)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
            return True

        sc.logger.info('选择GIF导出尺寸')
        sc.driver.find_element_by_xpath(
            "(//XCUIElementTypeImage[@name='vivavideo_gif_icon_arrow_n'])[1]").click()
        sc.capture_screen(fun_name,self.img_path)
        sc.driver.find_element_by_name("320P").click()
        time.sleep(0.5)

        sc.logger.info('选择GIF导出帧率')
        sc.driver.find_element_by_xpath(
            "(//XCUIElementTypeImage[@name='vivavideo_gif_icon_arrow_n'])[2]").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("15F/s").click()
        time.sleep(0.5)

        sc.logger.info('点击“确定”按钮')
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("确定").click()

        sc.logger.info('开始导出')
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_exprot: V_exprot.find_element_by_name('我的工作室'))

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(0.5)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("感觉如何")
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_name("稍后再说").click()

            sc.logger.info('点击左上角返回按钮退回创作中心')
            time.sleep(0.5)
            sc.driver.find_element_by_name("vivavideo com nav back n").click()
        except Exception as e:
            sc.logger.error('导出失败', e)
            return False

    def test_export_06_giveup(self):
        """导出-保存到相册-导出取消."""
        sc.logger.info('导出-保存到相册-导出取消')
        fun_name = 'test_export_giveup'

        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(0.5)

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()
        time.sleep(0.5)

        sc.logger.info('点击屏幕消除软键盘')
        actions = TouchAction(sc.driver)
        actions.tap(None, 500, 500, 1).release().perform()

        sc.logger.info('点击“保存到相册”')
        sc.driver.find_element_by_name('保存到相册').click()
        time.sleep(0.5)

        sc.logger.info('确认视频是否已导出')
        try:
            sc.driver.find_element_by_name("重新导出").click()
            time.sleep(0.5)
        except NoSuchElementException:
            sc.logger.info('该视频未导出过，直接选择要导出的尺寸')

        sc.logger.info('点击“高清 720P”')
        sc.driver.find_element_by_name("高清 720P").click()
        time.sleep(1)

        sc.logger.info('放弃导出')
        sc.driver.find_element_by_name('icon exit close n').click()
        sc.capture_screen(fun_name,self.img_path)
        sc.driver.find_element_by_name("不等了").click()

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()