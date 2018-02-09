# -*- coding: utf-8 -*-
"""镜头添加相关操作的测试用例."""
import time
from Android import script_ultils as sc


class TestEditClipsAdd(object):
    """镜头添加相关操作的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_add_clips(self):
        """剪辑-添加镜头-相册添加."""
        sc.logger.info('剪辑-添加镜头-相册添加')
        fun_name = 'test_edit_add_clips'

        start_x = self.width - self.width // 4
        start_bottom = self.height - self.height // 10

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()

        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)
        time.sleep(1)

        el_edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in el_edit_list:
            if el_item.text == '添加镜头':
                sc.logger.info('开始点击“添加镜头”')
                el_item.click()
                break
        sc.logger.info('点击“视频”下拉按钮')
        sc.driver.find_element_by_android_uiautomator('text("视频")').click()
        sc.logger.info('点击“图片”')
        sc.driver.find_element_by_android_uiautomator('text("图片")').click()
        sc.find_by_ids('com.quvideo.xiaoying:id/img_click_mask', fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(3):
            time.sleep(1)
            sc.driver.press_keycode(4)

        sc.logger.info('剪辑-添加镜头-相册添加测试完成')

    def test_edit_clips_shot(self):
        """剪辑-添加镜头-拍摄添加."""
        sc.logger.info('剪辑-添加镜头-拍摄添加')
        fun_name = 'test_edit_clips_shot'

        start_x = self.width - self.width // 4
        start_bottom = self.height - self.height // 10

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)

        el_edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in el_edit_list:
            if el_item.text == '添加镜头':
                sc.logger.info('开始点击“添加镜头”')
                el_item.click()
                break
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_ve_preview_layout_captrue').click()
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        sc.logger.info('点击录制按钮')
        el_capture.click()
        time.sleep(5)
        sc.logger.info('录制5s后点击录制按钮停止录制')
        el_capture.click()
        sc.logger.info('点击确认键')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()

        sc.logger.info('返回创作中心主界面')
        for i in range(3):
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-添加镜头-拍摄添加测试完成')

    def test_edit_clips_cancel(self):
        """剪辑-添加镜头-放弃."""
        sc.logger.info('剪辑-添加镜头-放弃')
        fun_name = 'test_edit_clips_cancel'

        start_x = self.width - self.width // 4
        start_bottom = self.height - self.height // 10

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)

        el_edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in el_edit_list:
            if el_item.text == '添加镜头':
                sc.logger.info('开始点击“添加镜头”')
                el_item.click()
                break
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_ve_preview_layout_captrue').click()
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        el_capture.click()
        time.sleep(5)
        el_capture.click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.driver.find_element_by_android_uiautomator('text("排序")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(3):
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-添加镜头-测试完成')
