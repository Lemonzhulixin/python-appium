# -*- coding: utf-8 -*-
"""镜头编辑相关操作的测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestEditClip(object):
    """镜头编辑相关操作的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_clip_edit_function(self):
        """剪辑-镜头编辑-功能遍历."""
        sc.logger.info('剪辑-镜头编辑-功能遍历')
        fun_name = 'test_clip_edit_function'
        video_flag = 0

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_img)).click()

        sc.logger.info('尝试点击“编辑该视频”')
        edit_btn = 'com.quvideo.xiaoying:id/edit_this_video_text'
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(edit_btn)).click()
        except TimeoutException:
            sc.logger.info('该视频已经在编辑页，跳过此步骤')

        sc.logger.info('点击“镜头编辑”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("镜头编辑")')).click()

        confirm_btn = 'com.quvideo.xiaoying:id/terminator_right'

        sc.logger.info('剪辑-镜头编辑-图片时长')
        try:
            sc.logger.info('点击“图片时长”')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda c_btn: c_btn.find_element_by_android_uiautomator(
                    'text("图片时长")')).click()
            sc.logger.info('点击“确认”')
            sc.driver.find_element_by_id(confirm_btn).click()
        except TimeoutException:
            video_flag = 1
            sc.logger.info('当前镜头是视频，不支持时长')

        sc.logger.info('剪辑-镜头编辑-修剪')
        try:
            sc.logger.info('点击“修剪”')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda c_btn: c_btn.find_element_by_android_uiautomator(
                    'text("修剪")')).click()
            sc.logger.info('点击“确认”')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(confirm_btn)).click()
        except NoSuchElementException:
            sc.logger.info('当前镜头是图片，不支持修剪')

        sc.logger.info('剪辑-镜头编辑-分割')
        if video_flag == 1:
            sc.logger.info('点击“分割”')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda c_btn: c_btn.find_element_by_android_uiautomator(
                    'text("分割")')).click()
            sc.logger.info('点击“确认”')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(confirm_btn)).click()

            try:
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda el: el.find_element_by_id(confirm_btn))
                sc.logger.info('时长太短不能分割')
                sc.driver.press_keycode(4)
            except TimeoutException:
                sc.logger.info('分割成功')

        sc.logger.info('剪辑-镜头编辑-复制')
        el_copy = WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("复制")'))
        el_copy.click()

        sc.logger.info('工具栏左滑一些')
        time.sleep(2)
        coord_x = el_copy.location.get('x')
        coord_y = el_copy.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.5, 800)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('剪辑-镜头编辑-变速')
        if video_flag == 1:
            sc.logger.info('点击“变速”')
            sc.driver.find_element_by_android_uiautomator(
                'text("变速")').click()
            sc.logger.info('点击“确认”')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(confirm_btn)).click()

        sc.logger.info('剪辑-镜头编辑-调色')
        sc.logger.info('点击“调色”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("调色")')).click()
        sc.logger.info('点击“确认”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(confirm_btn)).click()

        sc.logger.info('剪辑-镜头编辑-静音')
        sc.logger.info('点击“静音”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("静音")')).click()

        sc.logger.info('剪辑-镜头编辑-倒放镜头')
        sc.logger.info('点击“倒放镜头”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("倒放镜头")')).click()
        try:
            WebDriverWait(sc.driver, 120).until(
                lambda reverse: reverse.find_element_by_android_uiautomator(
                    'text("倒放镜头")'))
        except TimeoutError as t:
            sc.logger.error('倒放镜头超时', t)
            return False

        sc.logger.info('剪辑-镜头编辑-旋转')
        sc.logger.info('点击“旋转”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("旋转")')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-镜头编辑-功能遍历完成')
