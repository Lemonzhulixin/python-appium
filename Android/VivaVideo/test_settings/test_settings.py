# -*- coding: utf-8 -*-
"""设置页面的测试用例."""
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestSettings(object):
    """设置页面的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_settings_ui(self):
        """设置：默认值UI遍."""
        sc.logger.info('设置：默认UI遍历')
        fun_name = 'test_settings_ui'

        sc.logger.info('点击个人中心主按钮')
        p_btn = 'com.quvideo.xiaoying:id/img_studio'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda c_btn: c_btn.find_element_by_id(p_btn)).click()

        sc.logger.info('开始进入个人空间截图')
        sc.capture_screen(fun_name, self.img_path)

        setting_btn = 'com.quvideo.xiaoying:id/btn_setting'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(setting_btn)).click()

        el_set_list = sc.driver.find_elements_by_class_name(
            'android.widget.TextView')

        for el_set_content in el_set_list:
            el_set_content.click()
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.press_keycode(4)
            time.sleep(1)
            """
            try:
                sc.driver.find_element_by_id(
                    'com.quvideo.xiaoying:id/btn_setting').click()
            except NoSuchElementException:
                sc.logger.info('[%s]: 未找到设置按钮', fun_name)
            """
        sc.logger.info('设置选项UI第一页遍历完成')

    def test_settings_net(self):
        """设置：自动播放/网络/推送/分享设置."""
        sc.logger.info('设置：自动播放/网络/推送/分享设置遍历测试')
        fun_name = 'test_settings_net'

        try:
            sc.driver.find_element_by_id(
                'com.quvideo.xiaoying:id/btn_setting').click()
        except NoSuchElementException:
            sc.logger.info('已经在设置页面了，直接进行下一步')

        el_net_wifi = WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("只在WIFI网络上传/下载视频")'))

        sc.logger.info('点击网络设置选项')
        el_net_wifi.click()
        sc.logger.info('开始网络设置选项截图')
        sc.capture_screen(fun_name, self.img_path)
        try:
            sc.driver.find_element_by_id(
                'com.quvideo.xiaoying:id/buttonDefaultPositive').click()
        except NoSuchElementException:
            el_net_wifi.click()
            sc.driver.find_element_by_id(
                'com.quvideo.xiaoying:id/buttonDefaultPositive').click()
        el_net_wifi.click()

        sc.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("接收通知推送")').click()
        sc.find_by_classes('android.widget.TextView',
                           fun_name, self.img_path)
        sc.logger.info('通知推送设置遍历完成')

        sc.driver.press_keycode(4)
        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("分享帐号设置")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/img_back').click()
        sc.logger.info('网络设置相关测试完成')

    def test_settings_privacy(self):
        """设置：隐私设置."""
        sc.logger.info('设置：隐私设置')
        fun_name = 'test_settings_privacy'

        start_x = self.width // 2
        start_bottom = self.height - self.height // 10

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("私信权限")')).click()

        sc.find_by_classes('android.widget.TextView', fun_name, self.img_path)
        sc.logger.info('隐私权限设置遍历完成')

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(
                'com.quvideo.xiaoying:id/img_back')).click()

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'new UiSelector().text("隐私帐号")')).click()
        time.sleep(1)

        try:
            sc.driver.find_element_by_android_uiautomator(
                'new UiSelector().text("水印显示昵称")').click()
        except NoSuchElementException:
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.3, 500)
            sc.driver.find_element_by_android_uiautomator(
                'new UiSelector().text("水印显示昵称")').click()
        sc.logger.info('设置：隐私设置测试完成')

    def test_settings_live(self):
        """设置：摄像头校正."""
        sc.logger.info('设置：摄像头校正')
        fun_name = 'test_settings_live'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 10

        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.3, 500)

        sc.capture_screen(fun_name, self.img_path)
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'new UiSelector().text("摄像头校正")')).click()

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'new UiSelector().text("校正前置摄像头")')).click()

        time.sleep(3)
        sc.logger.info('校正前置摄像头时截图')
        sc.capture_screen(fun_name, self.img_path)

        left_btn = 'com.quvideo.xiaoying:id/cam_adjust_dialog_btn_rotate_left'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(left_btn)).click()

        r_btn = 'com.quvideo.xiaoying:id/cam_adjust_dialog_btn_rotate_right'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(r_btn)).click()

        h_btn = 'com.quvideo.xiaoying:id/cam_adjust_dialog_btn_flip_horizontal'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(h_btn)).click()

        v_btn = 'com.quvideo.xiaoying:id/cam_adjust_dialog_btn_flip_vertical'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(v_btn)).click()

        sc.driver.press_keycode(4)
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("摄像头校正")')).click()
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("校正后置摄像头")')).click()

        time.sleep(2)
        sc.logger.info('校正后置摄像头时截图')
        sc.capture_screen(fun_name, self.img_path)

        left_btn = 'com.quvideo.xiaoying:id/cam_adjust_dialog_btn_rotate_left'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(left_btn)).click()

        r_btn = 'com.quvideo.xiaoying:id/cam_adjust_dialog_btn_rotate_right'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(r_btn)).click()

        h_btn = 'com.quvideo.xiaoying:id/cam_adjust_dialog_btn_flip_horizontal'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(h_btn)).click()

        v_btn = 'com.quvideo.xiaoying:id/cam_adjust_dialog_btn_flip_vertical'
        WebDriverWait(sc.driver, 10, 1).until(
                      lambda el: el.find_element_by_id(v_btn)).click()

        sc.driver.press_keycode(4)
        sc.logger.info('设置：摄像头校正测试完成')

    def test_settings_feedback(self):
        """设置：意见反馈."""
        sc.logger.info('设置：意见反馈')
        fun_name = 'test_settings_feedback'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 10

        time.sleep(2)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("意见反馈")')).click()
        try:
            sc.driver.find_element_by_id(
                'com.quvideo.xiaoying:id/feedback_btn_issue_create').click()
        except NoSuchElementException:
            sc.logger.info('当前是第一次反馈')
        el_question_msg = sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/feedback_question_msg')
        el_question_msg.send_keys('QA test feedback')

        sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/feedback_question_type').click()

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("完成")')).click()
        sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/feedback_layout_sh_').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.press_keycode(4)

        time.sleep(1)
        el_qq_contact = sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/feedback_contact_edit_1')
        el_qq_contact.send_keys('245603638')

        el_ph_contact = sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/feedback_contact_edit_2')
        el_ph_contact.send_keys('15857154810')

        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("提交")').click()
        time.sleep(2)
        sc.capture_screen(fun_name, self.img_path)

        """
        sc.logger.info('查看反馈')
        el_feedback = sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/feedback_layout_history_item')
        el_feedback.click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.press_keycode(4)
        """

        left_icon = 'com.quvideo.xiaoying:id/feedback_left_icon'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(left_icon)).click()
        sc.logger.info('意见反馈测试完成')

    def test_settings_senior(self):
        """设置：高级设置和其他."""
        sc.logger.info('设置：高级设置和其他')
        fun_name = 'test_settings_senior'

        hardware_btn = WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'new UiSelector().text("视频处理硬件加速")'))
        hardware_btn.click()
        sc.capture_screen(fun_name, self.img_path)
        hardware_btn.click()

        sc.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("视频保存位置")').click()
        sc.driver.press_keycode(4)

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'new UiSelector().text("关于小影")')).click()

        sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/img_back').click()

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'new UiSelector().text("评价小影")')).click()

        sc.capture_screen(fun_name, self.img_path)
        sc.driver.press_keycode(4)

        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator(
            'new UiSelector().text("成为VIP会员")').click()
        sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/vip_home_close').click()

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'new UiSelector().text("恢复购买")')).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('设置：高级设置和其他测试完成')
