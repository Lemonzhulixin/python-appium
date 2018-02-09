# -*- coding: utf-8 -*-
"""创作页面内导出视频相关的测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestCreationExport(object):
    """
    创作页面内导出视频相关的测试类.

    1.执行导出用例时，请确认当前app未进行过导出操作
    2.使用已购买会员账号登录
    """

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_export_create(self):
        """导出-创建视频."""
        sc.logger.info('导出-创建视频')
        fun_name = 'test_export_create'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“拍摄”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()
        sc.logger.info('点击录制按钮')
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        el_capture.click()
        time.sleep(5)
        el_capture.click()
        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()
        sc.logger.info('导出-创建视频完成')

    def test_export_first(self):
        """导出-保存到相册-480P-首次导出."""
        sc.logger.info('导出-保存到相册-480P-首次导出')
        fun_name = 'test_export_first'

        sc.logger.info('点击“保存到相册”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_export').click()
        sc.logger.info('点击“标清(480P)”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/purchase_duration_limit_title').click()
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_exprot: V_exprot.find_element_by_android_uiautomator('text("工作室")'))
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.press_keycode(4)

            # 等待不要删除视频提示消息消失
            time.sleep(10)
            sc.driver.press_keycode(4)
        except NoSuchElementException:
            sc.driver.find_element_by_android_uiautomator('text("感觉如何")')
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.press_keycode(4)
        except TimeoutError as t:
            sc.logger.error('导出视频超时', t)
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.press_keycode(4)
            return False
        sc.logger.info('导出-保存到相册-480P-首次导出测试完成')

    def test_export_second(self):
        """导出-保存到相册-720P-二次导出."""
        sc.logger.info('导出-保存到相册-720P-二次导出')
        fun_name = 'test_export_second'

        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()
        sc.logger.info('点击第一个草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()

        sc.logger.info('点击“保存/上传”')
        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()
        sc.logger.info('点击“保存到相册”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_export').click()
        try:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/purchase_hd_title').click()
        except NoSuchElementException:
            sc.logger.info('当前设备不支持720P导出')
            sc.logger.info('返回创作中心主界面')
            for i in range(5):
                time.sleep(1)
                sc.driver.press_keycode(4)
            return True

        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_exprot: V_exprot.find_element_by_android_uiautomator('text("工作室")'))
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.press_keycode(4)
            time.sleep(1)
            sc.driver.press_keycode(4)
        except NoSuchElementException:
            sc.driver.find_element_by_android_uiautomator('text("分享小影")')
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.press_keycode(4)
        except TimeoutError as t:
            sc.logger.error('导出视频超时', t)
            return False
        sc.logger.info('导出-保存到相册-720P-二次导出测试完成')

    def test_export_third(self):
        """导出-保存到相册-1080P-三次导出."""
        sc.logger.info('导出-保存到相册-1080P')
        fun_name = 'test_export_third'

        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_export').click()
        try:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/purchase_hd_1080_title').click()
        except NoSuchElementException:
            sc.logger.info('当前设备不支持1080P导出')
            sc.logger.info('返回创作中心主界面')
            for i in range(5):
                time.sleep(1)
                sc.driver.press_keycode(4)
            return True
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_exprot: V_exprot.find_element_by_android_uiautomator('text("工作室")'))
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        except TimeoutError as t:
            sc.logger.error('导出视频超时', t)
            return False
        sc.logger.info('导出-保存到相册-1080P测试完成')

    def test_export_gif(self):
        """导出-保存到相册-GIF."""
        sc.logger.info('导出-保存到相册-GIF')
        fun_name = 'test_export_gif'

        time.sleep(1)
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()
        sc.logger.info('点击第一个草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“保存/上传”')
        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()
        sc.logger.info('点击“保存到相册”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_export').click()
        try:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/gif_title').click()
            sc.logger.info('点击“GIF”')
        except NoSuchElementException:
            sc.logger.info('当前版本不支持GIF导出')
            return True
        time.sleep(1)
        sc.logger.info('点击“确认”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/share_btn_share').click()
        try:
            WebDriverWait(sc.driver, 120).until(
                lambda V_exprot: V_exprot.find_element_by_android_uiautomator('text("工作室")'))
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        except TimeoutError as t:
            sc.logger.error('导出视频超时', t)
            sc.driver.press_keycode(4)
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/buttonDefaultPositive').click()
            sc.logger.info('返回创作中心主界面')
            for i in range(4):
                time.sleep(1)
                sc.driver.press_keycode(4)
            return False
        sc.logger.info('导出-保存到相册-GIF测试完成')
