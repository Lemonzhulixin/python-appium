# -*- coding: utf-8 -*-
"""camera美颜趣拍的测试用例."""
from appium.webdriver.common.touch_action import TouchAction
from Android_old import script_ultils as sc


class TestCameraSelf(object):
    """camera美颜趣拍的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]
    c_btn = 'com.quvideo.xiaoying:id/img_creation'

    def test_camera_self(self):
        """拍摄-自拍视频(1:1)."""
        sc.logger.info('拍摄-美颜趣拍(1:1)')
        fun_name = 'test_camera_self'

        sc.logger.info('点击创作中心主按钮')
        sc.first_step(self.c_btn)

        sc.logger.info('点击“美颜趣拍”')
        sc.driver.find_element_by_android_uiautomator('text("美颜趣拍")').click()
        sc.logger.info('点击摄像头反转按钮')

        switch_btn = 'com.quvideo.xiaoying:id/img_switch'
        sc.driver.find_element_by_id(switch_btn).click()
        sc.capture_screen(fun_name, self.img_path)
        el_cp = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')

        # 长按拍摄5s
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认按钮')
        next_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
        sc.driver.find_element_by_id(next_btn).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()

        sc.logger.info('美颜趣拍测试完成，点击返回按钮返回主页面')
        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        sc.driver.find_element_by_id(left_btn).click()
        sc.logger.info('拍摄-美颜趣拍拍摄完成')
