# -*- coding: utf-8 -*-
"""编辑滤镜的基本操作测试用例."""
import time
from Android import script_ultils as sc


class TestEditFilter(object):
    """编辑滤镜的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_filter(self):
        """剪辑-滤镜."""
        sc.logger.info('剪辑-滤镜')
        fun_name = 'test_edit_filter'

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
            if el_item.text == '滤镜':
                sc.logger.info('开始点击“滤镜”按钮')
                el_item.click()
                break
        sc.logger.info('点击“下载更多”按钮')
        el_filter_use = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/ImageView_Content_Thumbnail')
        el_filter_use.click()
        time.sleep(1)
        sc.logger.info('点击左上角返回按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_back').click()
        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-滤镜测试完成')
