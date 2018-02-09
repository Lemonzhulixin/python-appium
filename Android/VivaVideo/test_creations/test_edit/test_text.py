# -*- coding: utf-8 -*-
"""添加字幕的基本操作测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from Android import script_ultils as sc


class TestEditText(object):
    """添加字幕的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_text(self):
        """剪辑-字幕-添加."""
        sc.logger.info('剪辑-字幕-添加')
        fun_name = 'test_edit_text'

        start_x = self.width // 2
        start_bottom = self.height // 2
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
        el_edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in el_edit_list:
            if el_item.text == '字幕':
                sc.logger.info('开始点击字幕')
                el_item.click()
                break
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_add_subtitle').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 100)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-字幕-添加测试完成')

    def test_edit_text_cancel(self):
        """剪辑-字幕-放弃."""
        sc.logger.info('剪辑-字幕-放弃')
        fun_name = 'test_edit_text_cancel'

        start_x = self.width // 2
        start_bottom = self.height // 2
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
        el_edit_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in el_edit_list:
            if el_item.text == '字幕':
                sc.logger.info('开始点击字幕')
                el_item.click()
                break

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_add_subtitle').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 100)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-字幕-放弃测试完成')
