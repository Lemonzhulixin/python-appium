# -*- coding: utf-8 -*-
"""edit创建视频的测试用例."""
import time

from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestEditCreate(object):
    """edit创建视频的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_create_craft(self):
        """创建一个草稿视频."""
        sc.logger.info('创建一个草稿视频')
        fun_name = 'test_create_craft'
        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“剪辑”按钮')
        editor_btn = 'com.quvideo.xiaoying:id/btn1'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(editor_btn)).click()

        mask_img = 'com.quvideo.xiaoying:id/btn_item_status'
        el_video_list = sc.driver.find_elements_by_id(mask_img)
        if len(el_video_list) >= 2:
            el_video_list = el_video_list[:2]
        for i in range(2):
            el_video_list[i].click()

        sc.logger.info('点击“视频”按钮')
        type_btn = 'com.quvideo.xiaoying:id/gallery_type'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(type_btn)).click()
        sc.logger.info('点击“图片”按钮')
        img_type_btn = 'com.quvideo.xiaoying:id/xiaoying_gallery_photo_tab'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(img_type_btn)).click()

        el_img_list = sc.driver.find_elements_by_id(mask_img)
        if len(el_img_list) >= 2:
            el_img_list = el_img_list[:2]

        for el_img_list in el_img_list:
            el_img_list.click()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“下一步”按钮')
        import_n_btn = 'com.quvideo.xiaoying:id/tv_next'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(import_n_btn)).click()

        sc.logger.info('点击“存草稿”按钮')
        draft_btn = 'com.quvideo.xiaoying:id/editor_draft'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_btn)).click()

        sc.logger.info('返回创作中心主界面')
        sc.driver.press_keycode(4)
        sc.logger.info('创建一个草稿视频完成')
