# -*- coding: utf-8 -*-
"""camera美颜趣拍的测试用例."""
import time
from Android import script_ultils as sc


class TestCameraSelf(object):
    """camera美颜趣拍的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_camera_self(self):
        """拍摄-自拍视频(1:1)."""
        sc.logger.info('拍摄-美颜趣拍(1:1)')
        fun_name = 'test_camera_self'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“美颜趣拍”')
        sc.driver.find_element_by_android_uiautomator('text("美颜趣拍")').click()
        sc.logger.info('点击摄像头反转按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_switch').click()
        sc.capture_screen(fun_name, self.img_path)
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍5s
        sc.logger.info('点击录制按钮')
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()
        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        sc.logger.info('美颜趣拍测试完成，点击返回按钮返回主页面')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.logger.info('拍摄-美颜趣拍拍摄完成')
