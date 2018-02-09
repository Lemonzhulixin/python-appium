# -*- coding: utf-8 -*-
"""camera的基本操作测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Android import script_ultils as sc


class TestCameraNormal(object):
    """camera的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_normal_filter_download(self):
        """拍摄-滤镜下载."""
        sc.logger.info('拍摄-滤镜下载')
        fun_name = 'test_normal_filter_download'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“拍摄”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()
        sc.logger.info('点击滤镜图标')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_filter_effect').click()
        try:
            el_filter_download = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon_filter_download')
            sc.logger.info('点击下载按钮')
            el_filter_download.click()
            try:
                WebDriverWait(sc.driver, 30).until(
                    lambda download_flt: download_flt.find_element_by_id(
                        'com.quvideo.xiaoying:id/item_fitler_child_cover'))
            except Exception as e:
                sc.logger.error('滤镜下载失败', e)
        except NoSuchElementException:
            el_filter_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/item_fitler_parent_cover')
            sc.logger.info('点击第三个滤镜主题')
            el_filter_list[2].click()
        time.sleep(1)
        el_child_filter = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/item_fitler_child_cover')
        sc.logger.info('点击第一个滤镜')
        el_child_filter.click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('退出滤镜选项')
        sc.driver.press_keycode(4)
        sc.logger.info('返回创作中心主界面')
        sc.driver.press_keycode(4)
        sc.logger.info('拍摄-滤镜下载测试完成')

    def test_camera_normal_settings(self):
        """拍摄-设置相关."""
        sc.logger.info('拍摄-设置相关')
        fun_name = 'test_camera_normal_settings'

        sc.logger.info('点击“拍摄”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()
        sc.logger.info('点击设置按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_setting').click()
        sc.find_by_classes('android.widget.ImageView', fun_name, self.img_path)
        sc.logger.info('退出设置选项')
        sc.driver.press_keycode(4)
        sc.logger.info('返回创作中心主界面')
        sc.driver.press_keycode(4)
        sc.logger.info('拍摄-设置相关测试完成')

    def test_camera_normal_shot(self):
        """拍摄-高清相机(全屏)."""
        sc.logger.info('拍摄-高清相机(全屏)')
        fun_name = 'test_camera_normal_shot'

        sc.logger.info('点击“拍摄”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()
        sc.logger.info('点击摄像头切换按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_switch').click()
        time.sleep(2)
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        sc.logger.info('点击录制按钮')
        el_capture.click()
        time.sleep(5)
        sc.logger.info('录制5s后点击录制按钮停止录制')
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)

        # 长按拍摄
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_capture, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击撤销按钮两次')
        sc.driver.find_element_by_android_uiautomator('text("撤销")').click()
        sc.driver.find_element_by_android_uiautomator('text("撤销")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        sc.logger.info('点击左上角返回按钮退回创作中心')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.logger.info('拍摄-高清相机拍摄完成')
