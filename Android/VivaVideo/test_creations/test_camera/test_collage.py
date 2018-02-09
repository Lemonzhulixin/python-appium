# -*- coding: utf-8 -*-
"""camera的画中画功能测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestCameraCollage(object):
    """camera的画中画功能测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_collage_settings(self):
        """拍摄-画中画拍摄-设置."""
        sc.logger.info('拍摄-画中画拍摄-设置')
        fun_name = 'test_collage_settings'
        start_x = self.width - self.width // 10
        start_bottom = self.height // 2

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()

        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 500)
        sc.logger.info('点击"画中画拍摄"')
        sc.driver.find_element_by_android_uiautomator('text("画中画拍摄")').click()

        sc.logger.info('切换样式')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_effect').click()
        el_wheel = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/wheel_img_content')
        sc.logger.info('点击第一个样式效果')
        el_wheel.click()
        sc.driver.press_keycode(4)
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('摄像位置互换')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_mode').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换前后置')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_switch').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('camera设置')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_setting').click()
        try:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/v4_img_flash').click()
        except NoSuchElementException:
            sc.logger.info('前置摄像头不支持闪光灯')

        sc.logger.info('点击倒计时按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/v4_img_timer').click()
        sc.logger.info('点击曝光锁定按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/v4_img_aelock').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.press_keycode(4)
        time.sleep(2)
        sc.logger.info('点击返回按钮返回创作中心主页面')
        sc.driver.press_keycode(4)

        sc.logger.info('拍摄-画中画拍摄-设置完成')

    def test_collage_shot(self):
        """拍摄-画中画拍摄-拍摄."""
        sc.logger.info('拍摄-画中画拍摄-拍摄')
        fun_name = 'test_collage_shot'

        sc.logger.info('点击"画中画拍摄"')
        sc.driver.find_element_by_android_uiautomator('text("画中画拍摄")').click()
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        sc.logger.info('点击录制按钮')
        el_capture.click()
        time.sleep(5)
        sc.logger.info('拍摄5s后点击录制按钮停止拍摄')
        el_capture.click()

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_cam_img_pip_add').click()
        sc.logger.info('添加第二段视频')
        el_capture.click()
        try:
            WebDriverWait(sc.driver, 300).until(
                lambda capture: capture.find_element_by_android_uiautomator('text("存草稿")'))
            sc.logger.info('点击“存草稿”按钮')
            sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
            sc.capture_screen(fun_name, self.img_path)
            sc.logger.info('点击左上角返回按钮返回创作中心主页')
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
            sc.logger.info('拍摄-音乐视频拍摄完成')
        except Exception as e:
            sc.logger.error('拍摄完成跳转预览页异常', e)
            sc.driver.press_keycode(4)
            return False

        sc.logger.info('拍摄-画中画拍摄-拍摄完成')

    def test_collage_album(self):
        """拍摄-画中画拍摄-拍摄."""
        sc.logger.info('拍摄-画中画拍摄-相册视频')
        fun_name = 'test_collage_album'

        sc.logger.info('点击"画中画拍摄"')
        sc.driver.find_element_by_android_uiautomator('text("画中画拍摄")').click()
        sc.logger.info('从相册选择视频')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_cam_btn_pip_gallery').click()
        sc.logger.info('点击相册第一个视频')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_click_mask').click()
        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_import').click()

        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_improt: V_improt.find_element_by_id('com.quvideo.xiaoying:id/btn_rec'))
        except TimeoutError as t:
            sc.logger.error('导入视频超时', t)
            return False
        except Exception as e:
            sc.logger.error('导入视频出错', e)
            return False

        sc.logger.info('添加第二段视频')
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        el_capture.click()
        time.sleep(5)
        el_capture.click()
        try:
            WebDriverWait(sc.driver, 300).until(
                lambda capture: capture.find_element_by_android_uiautomator('text("存草稿")'))
            sc.logger.info('点击"存草稿"按钮')
            sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
            sc.logger.info('点击左上角返回按钮返回创作中心主页面')
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
            sc.capture_screen(fun_name, self.img_path)
            sc.logger.info('拍摄-音乐视频拍摄完成')
        except Exception as e:
            sc.logger.error('拍摄完成跳转预览页异常', e)
            sc.driver.press_keycode(4)
            return False

        sc.logger.info('拍摄-画中画拍摄-相册视频完成')

    def test_collage_edit(self):
        """拍摄-画中画编辑."""
        sc.logger.info('拍摄-画中画编辑')
        fun_name = 'test_collage_edit'

        sc.logger.info('点击"画中画编辑"')
        sc.driver.find_element_by_android_uiautomator('text("画中画编辑")').click()
        sc.logger.info('选择第2个样式')
        el_style_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/xiaoying_imagebtn_style_thumb')
        el_style_list[1].click()
        sc.driver.press_keycode(4)
        sc.capture_screen(fun_name, self.img_path)
