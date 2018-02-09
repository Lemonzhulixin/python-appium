# -*- coding: utf-8 -*-
"""镜头编辑相关操作的测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Android import script_ultils as sc


class TestEditClip(object):
    """镜头编辑相关操作的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_clip_edit_function(self):
        """剪辑-镜头编辑-功能遍历."""
        sc.logger.info('剪辑-镜头编辑-功能遍历')
        fun_name = 'test_clip_edit_function'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()
        sc.logger.info('点击第一个草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()
        sc.logger.info('点击“镜头编辑”')
        sc.driver.find_element_by_android_uiautomator('text("镜头编辑")').click()

        sc.logger.info('剪辑-镜头编辑-时长')
        try:
            sc.logger.info('点击“时长”')
            sc.driver.find_element_by_android_uiautomator('text("时长")').click()
            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        except NoSuchElementException:
            sc.logger.info('当前镜头是视频，不支持时长')

        sc.logger.info('剪辑-镜头编辑-修剪')
        try:
            sc.logger.info('点击“修剪”')
            sc.driver.find_element_by_android_uiautomator('text("修剪")').click()
            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        except NoSuchElementException:
            sc.logger.info('当前镜头是图片，不支持修剪')

        sc.logger.info('剪辑-镜头编辑-分割')
        try:
            sc.logger.info('点击“分割”')
            sc.driver.find_element_by_android_uiautomator('text("分割")').click()
            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        except NoSuchElementException:
            sc.logger.info('当前镜头是图片，不支持分割')

        sc.logger.info('剪辑-镜头编辑-复制')
        sc.driver.find_element_by_android_uiautomator('text("复制")').click()

        sc.logger.info('剪辑-镜头编辑-调节速度')
        try:
            sc.logger.info('点击“调节速度”')
            sc.driver.find_element_by_android_uiautomator('text("调节速度")').click()
            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        except NoSuchElementException:
            sc.logger.info('当前镜头是图片，不支持调节速度')

        sc.logger.info('剪辑-镜头编辑-调节')
        el_adjust = sc.driver.find_element_by_android_uiautomator('text("调节")')
        sc.logger.info('点击“调节”')
        el_adjust.click()
        sc.logger.info('点击“取消”')
        sc.driver.find_element_by_android_uiautomator('text("取消")').click()

        sc.logger.info('剪辑-镜头编辑-静音')
        time.sleep(1)
        coord_x = el_adjust.location.get('x')
        coord_y = el_adjust.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.6, 500)
        sc.logger.info('点击“静音”')
        sc.driver.find_element_by_android_uiautomator('text("静音")').click()

        sc.logger.info('剪辑-镜头编辑-倒放镜头')
        sc.logger.info('点击“倒放镜头”')
        sc.driver.find_element_by_android_uiautomator('text("倒放镜头")').click()
        try:
            WebDriverWait(sc.driver, 120).until(
                lambda reverse: reverse.find_element_by_android_uiautomator('text("倒放镜头")'))
        except TimeoutError as t:
            sc.logger.error('倒放镜头超时', t)
            return False

        sc.logger.info('剪辑-镜头编辑-动态效果')
        sc.logger.info('点击“动态效果”')
        sc.driver.find_element_by_android_uiautomator('text("动态效果")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        sc.driver.press_keycode(4)
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        for i in range(3):
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-镜头编辑-功能遍历完成')

    def test_clip_edit_add(self):
        """剪辑-镜头编辑-添加镜头."""
        sc.logger.info('剪辑-镜头编辑-添加镜头')
        fun_name = 'test_clip_edit_add'

        start_x = self.width // 2
        start_bottom = self.height - self.height // 10

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()
        sc.logger.info('点击第一个草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()
        sc.logger.info('点击“镜头编辑”')
        sc.driver.find_element_by_android_uiautomator('text("镜头编辑")').click()

        while True:
            try:
                sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_ve_storyboard_item_add_btn').click()
                sc.logger.info('点击添加镜头按钮')
                break
            except NoSuchElementException:
                sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.25, 500)

        sc.logger.info('点击拍摄按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_ve_preview_layout_captrue').click()
        sc.logger.info('点击录像按钮')
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 长按拍摄
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_capture, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_storyboard_next_btn').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('镜头编辑-删除镜头')
        el_del_clip = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_delete')
        el_del_clip.click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/buttonDefaultPositive').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        sc.driver.press_keycode(4)
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        for i in range(3):
            sc.driver.press_keycode(4)

        sc.logger.info('剪辑-镜头编辑-添加镜头测试完成')
