# -*- coding: utf-8 -*-
"""创作页面内导出视频相关的测试用例."""
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Android_old import script_ultils as sc


class TestCreationExport(object):
    """
    创作页面内导出视频相关的测试类.

    1.执行导出用例时，请确认当前app未进行过导出操作
    2.使用已购买会员账号登录
    """

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @classmethod
    def hardware_acceleration(cls):
        """硬件加速设置."""
        try:
            sc.logger.info('尝试开启硬件加速')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_android_uiautomator(
                    'text("视频处理硬件加速")')).click()
        except TimeoutException:
            sc.logger.info('未找到硬件加速选项，上滑半屏尝试')
            start_x = cls.width // 2
            start_y = cls.height // 8
            start_bottom = cls.height - start_y

            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.4, 600)
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_android_uiautomator(
                    'text("视频处理硬件加速")')).click()
        time.sleep(1)
        sc.driver.press_keycode(4)

    @classmethod
    def restore_purchase(cls):
        """用来处理恢复购买."""
        try:
            sc.logger.info('尝试恢复购买')

            vip_btn = 'com.quvideo.xiaoying:id/privilege_to_be_vip'
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(vip_btn)).click()

            restore_btn = 'com.quvideo.xiaoying:id/vip_home_restore_button'
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(restore_btn)).click()

            close_btn = 'com.quvideo.xiaoying:id/vip_home_close'
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(close_btn)).click()
        except TimeoutException:
            sc.logger.info('无需设置恢复购买')

    def test_export_create(self):
        """导出-创建视频."""
        sc.logger.info('导出-创建视频')
        fun_name = 'test_export_create'
        start_x = self.width // 2
        start_bottom = self.height // 3

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“拍摄”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()

        sc.logger.info('点击录制按钮')
        el_cp = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')

        # 长按拍摄
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认按钮')
        time.sleep(1)
        next_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
        sc.driver.find_element_by_id(next_btn).click()
        sc.capture_screen(fun_name, self.img_path)

        time.sleep(1)
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 1000)

        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()
        sc.logger.info('导出-创建视频完成')

    def test_export_first(self):
        """导出-保存到相册-480P-首次导出."""
        sc.logger.info('导出-保存到相册-480P-首次导出')
        fun_name = 'test_export_first'

        sc.logger.info('点击“保存到相册”')
        export_btn = 'com.quvideo.xiaoying:id/btn_export'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(export_btn)).click()
        # sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_export').click()

        try:
            pos_btn = 'com.quvideo.xiaoying:id/buttonDefaultPositive'
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(pos_btn)).click()
            TestCreationExport.hardware_acceleration()

            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(export_btn)).click()
        except TimeoutException:
            sc.logger.info('无需设置硬件加速')

        sc.logger.info('点击“480P 清晰”')
        limit_btn = 'com.quvideo.xiaoying:id/normal_layout'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(limit_btn)).click()
        try:
            WebDriverWait(sc.driver, 20).until(
                lambda x: x.find_element_by_android_uiautomator('text("工作室")'))
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            sc.driver.press_keycode(4)
        time.sleep(1)
        sc.driver.press_keycode(4)
        sc.logger.info('导出-保存到相册-480P-首次导出测试完成')

    def test_export_second(self):
        """导出-保存到相册-720P-二次导出."""
        sc.logger.info('导出-保存到相册-720P-二次导出')
        fun_name = 'test_export_second'

        sc.logger.info('点击“更多草稿”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("更多草稿")')).click()
        # sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()
        sc.logger.info('点击第一个草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_img)).click()

        sc.logger.info('点击“保存/上传”')
        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()

        sc.logger.info('点击“保存到相册”')
        export_btn = 'com.quvideo.xiaoying:id/btn_export'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(export_btn)).click()
        try:
            hd_title = 'com.quvideo.xiaoying:id/purchase_hd_title'
            sc.driver.find_element_by_id(hd_title).click()
            TestCreationExport.restore_purchase()

            WebDriverWait(sc.driver, 10, 1).until(
                lambda c_btn: c_btn.find_element_by_id(export_btn)).click()
            sc.driver.find_element_by_id(hd_title).click()
        except NoSuchElementException:
            sc.logger.info('当前设备不支持720P导出')
            sc.logger.info('返回创作中心主界面')
            for i in range(5):
                time.sleep(1)
                sc.driver.press_keycode(4)
            return True

        try:
            WebDriverWait(sc.driver, 60).until(
                lambda x: x.find_element_by_android_uiautomator('text("工作室")'))
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

        sc.logger.info('点击“更多草稿”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("更多草稿")')).click()

        sc.logger.info('点击第一个草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_img)).click()

        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()

        export_btn = 'com.quvideo.xiaoying:id/btn_export'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(export_btn)).click()
        try:
            fhd_title = 'com.quvideo.xiaoying:id/purchase_hd_1080_title'
            sc.driver.find_element_by_id(fhd_title).click()
        except NoSuchElementException:
            sc.logger.info('当前设备不支持1080P导出')
            sc.logger.info('返回创作中心主界面')
            for i in range(5):
                time.sleep(1)
                sc.driver.press_keycode(4)
            return True
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda x: x.find_element_by_android_uiautomator('text("工作室")'))
            sc.capture_screen(fun_name, self.img_path)

            left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
            sc.driver.find_element_by_id(left_btn).click()
        except TimeoutError as t:
            sc.logger.error('导出视频超时', t)
            return False
        sc.logger.info('导出-保存到相册-1080P测试完成')

    def test_export_gif(self):
        """导出-保存到相册-GIF."""
        sc.logger.info('导出-保存到相册-GIF')
        fun_name = 'test_export_gif'

        sc.logger.info('点击“更多草稿”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("更多草稿")')).click()

        sc.logger.info('点击第一个草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_img)).click()

        sc.logger.info('点击“保存/上传”')
        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()

        sc.logger.info('点击“保存到相册”')
        export_btn = 'com.quvideo.xiaoying:id/btn_export'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(export_btn)).click()

        try:
            sc.logger.info('点击“GIF”')
            gif_title = 'com.quvideo.xiaoying:id/gif_layout'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(gif_title)).click()
        except NoSuchElementException:
            sc.logger.info('当前版本不支持GIF导出')
            return True

        sc.logger.info('点击“导出”按钮')
        share_btn = 'com.quvideo.xiaoying:id/share_btn_share'
        WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(share_btn)).click()
        try:
            WebDriverWait(sc.driver, 20).until(
                lambda x: x.find_element_by_android_uiautomator('text("工作室")'))
            sc.capture_screen(fun_name, self.img_path)

            left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(left_btn)).click()
        except TimeoutError as t:
            sc.logger.error('导出GIF超时', t)
            sc.driver.press_keycode(4)
            sc.capture_screen(fun_name, self.img_path)

            pos_btn = 'com.quvideo.xiaoying:id/buttonDefaultPositive'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(pos_btn)).click()
            sc.logger.info('返回创作中心主界面')
            for i in range(4):
                time.sleep(1)
                sc.driver.press_keycode(4)
            return False
        sc.logger.info('导出-保存到相册-GIF测试完成')
