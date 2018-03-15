# -*- coding: utf-8 -*-
"""编辑滤镜的基本操作测试用例."""
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from Android import script_ultils as sc


class TestEditFilter(object):
    """编辑滤镜的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_filter(self):
        """剪辑-滤镜."""
        sc.logger.info('剪辑-滤镜')
        fun_name = 'test_edit_filter'

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        el_draft = sc.driver.find_element_by_id(draft_img)
        el_draft.click()
        sc.logger.info('点击“剪辑”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("剪辑")')).click()

        t_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in t_list:
            if el_item.text == '滤镜':
                sc.logger.info('开始点击“滤镜”按钮')
                el_item.click()
                break

        sc.logger.info('点击“下载更多”按钮')
        more_btn = 'com.quvideo.xiaoying:id/item_fitler_parent_cover'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(more_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        use_btn = 'com.quvideo.xiaoying:id/template_filter_apply'
        try:
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(use_btn)).click()
        except NoSuchElementException:
            down_btn = 'com.quvideo.xiaoying:id/template_filter_download'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(down_btn)).click()
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(use_btn)).click()

        filter_cover = 'com.quvideo.xiaoying:id/item_fitler_child_cover'

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(filter_cover)).click()
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角确认按钮')
        right_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_right'
        sc.driver.find_element_by_id(right_btn).click()
        sc.capture_screen(fun_name, self.img_path)

        draft_btn = 'com.quvideo.xiaoying:id/xiaoying_txtview_draft_btn'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(draft_btn)).click()

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-滤镜测试完成')
