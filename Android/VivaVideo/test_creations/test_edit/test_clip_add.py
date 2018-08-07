# -*- coding: utf-8 -*-
"""镜头添加相关操作的测试用例."""
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from Android_old import script_ultils as sc


class TestEditClipsAdd(object):
    """镜头添加相关操作的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_add_clips(self):
        """剪辑-添加镜头-相册添加."""
        sc.logger.info('剪辑-添加镜头-相册添加')
        fun_name = 'test_edit_add_clips'

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

        sc.logger.info('点击添加镜头的加号标识')
        clip_add_btn = 'com.quvideo.xiaoying:id/clipedit_add_btn'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(clip_add_btn)).click()

        sc.logger.info('点击相册图标')
        gallary_btn = 'com.quvideo.xiaoying:id/layout_move_gallery'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(gallary_btn)).click()

        sc.logger.info('点击“视频”下拉按钮')
        sc.driver.find_element_by_android_uiautomator('text("视频")').click()
        sc.logger.info('点击“图片”')
        sc.driver.find_element_by_android_uiautomator('text("图片")').click()

        mask_img = 'com.quvideo.xiaoying:id/img_click_mask'
        element_list = sc.driver.find_elements_by_id(mask_img)

        if len(element_list) >= 2:
            element_list = element_list[:2]

        for element_em in element_list:
            element_em.click()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)

        sc.logger.info('剪辑-添加镜头-相册添加测试完成')

    def test_edit_clips_shot(self):
        """剪辑-添加镜头-拍摄添加."""
        sc.logger.info('剪辑-添加镜头-拍摄添加')
        fun_name = 'test_edit_clips_shot'

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

        sc.logger.info('点击添加镜头的加号标识')
        clip_add_btn = 'com.quvideo.xiaoying:id/clipedit_add_btn'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(clip_add_btn)).click()

        camera_btn = 'com.quvideo.xiaoying:id/layout_move_camera'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(camera_btn)).click()

        rec_btn = 'com.quvideo.xiaoying:id/btn_rec'
        el_cp = WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(rec_btn))
        # 长按拍摄
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认键')
        next_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
        sc.driver.find_element_by_id(next_btn).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-添加镜头-拍摄添加测试完成')

    def test_edit_clips_cancel(self):
        """剪辑-添加镜头-放弃."""
        sc.logger.info('剪辑-添加镜头-放弃')
        fun_name = 'test_edit_clips_cancel'

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

        sc.logger.info('点击添加镜头的加号标识')
        clip_add_btn = 'com.quvideo.xiaoying:id/clipedit_add_btn'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(clip_add_btn)).click()

        camera_btn = 'com.quvideo.xiaoying:id/layout_move_camera'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(camera_btn)).click()

        rec_btn = 'com.quvideo.xiaoying:id/btn_rec'
        el_cp = WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(rec_btn))
        # 长按拍摄
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        next_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(next_btn)).click()

        left_btn = 'com.quvideo.xiaoying:id/editor_back_btn'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(left_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('剪辑-添加镜头-测试完成')
