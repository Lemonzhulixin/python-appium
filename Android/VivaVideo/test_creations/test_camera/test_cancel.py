# -*- coding: utf-8 -*-
"""camera取消操作相关的测试用例."""
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Android import script_ultils as sc


class TestCameraCancel(object):
    """camera取消操作相关的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]
    c_btn = 'com.quvideo.xiaoying:id/img_creation'

    def test_cancel_shot(self):
        """拍摄-拍摄页放弃."""
        sc.logger.info('拍摄-拍摄页放弃')
        fun_name = 'test_cancel_shot'

        sc.logger.info('点击创作中心主按钮')
        sc.first_step(self.c_btn)

        sc.logger.info('点击“拍摄”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()

        el_cp = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 长按拍摄5s
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        cancel_btn = 'com.quvideo.xiaoying:id/cam_btn_cancel'
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda capture: capture.find_element_by_id(cancel_btn))
        except Exception as e:
            sc.logger.error('拍摄完成但未找到返回按钮', e)
            return False
        sc.logger.info('点击左上角取消按钮')
        sc.driver.find_element_by_id(cancel_btn).click()
        sc.logger.info('点击“丢弃”按钮')
        sc.driver.find_element_by_android_uiautomator('text("丢弃")').click()
        sc.logger.info('拍摄-拍摄页放弃测试完成')

    def test_cancel_save(self):
        """拍摄-拍摄页保存."""
        sc.logger.info('拍摄-拍摄页保存')
        fun_name = 'test_cancel_save'

        sc.logger.info('点击创作中心“拍摄”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()

        rec_btn = 'com.quvideo.xiaoying:id/btn_rec'
        el_cp = sc.driver.find_element_by_id(rec_btn)
        # 长按拍摄5s
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        cancel_btn = 'com.quvideo.xiaoying:id/cam_btn_cancel'
        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda capture: capture.find_element_by_id(cancel_btn))
        except Exception as e:
            sc.logger.error('拍摄完成但未找到返回按钮', e)
            return False
        sc.logger.info('点击左上角取消按钮')
        sc.driver.find_element_by_id(cancel_btn).click()
        sc.logger.info('点击“保存”按钮')
        sc.driver.find_element_by_android_uiautomator('text("保存")').click()
        sc.logger.info('点击左上角返回按钮退回主页面')
        sc.driver.find_element_by_id(left_btn).click()
        sc.logger.info('拍摄-拍摄页保存测试完成')

    def test_cancel_preview(self):
        """拍摄-预览页放弃."""
        sc.logger.info('拍摄-预览页放弃)')
        fun_name = 'test_cancel_preview'

        sc.logger.info('点击创作中心“拍摄”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()
        el_cp = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 长按拍摄5s
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        next_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        cancel_btn = 'com.quvideo.xiaoying:id/cam_btn_cancel'
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda el: el.find_element_by_id(next_btn))
        except Exception as e:
            sc.logger.error('拍摄完成但未找到返回按钮', e)
            return False
        sc.logger.info('录制完成后点击确认按钮')
        sc.driver.find_element_by_id(next_btn).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击左上角返回按钮')
        sc.driver.find_element_by_id(left_btn).click()
        sc.logger.info('点击左上角取消按钮')
        sc.driver.find_element_by_id(cancel_btn).click()
        sc.logger.info('点击左上角返回按钮退回主页面')
        sc.driver.find_element_by_id(left_btn).click()
        sc.logger.info('拍摄-预览页放弃测试完成')
