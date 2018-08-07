# -*- coding: utf-8 -*-
"""转场的基本操作测试用例."""
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from Android_old import script_ultils as sc


class TestEditTransition(object):
    """转场的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_transition(self):
        """剪辑-转场-添加."""
        sc.logger.info('剪辑-转场-添加')
        fun_name = 'test_edit_transition'

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

        sc.logger.info('开始点击复制')
        el_copy = WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("复制")'))
        el_copy.click()

        time.sleep(1)
        coord_x = el_copy.location.get('x')
        coord_y = el_copy.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.6, 600)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击转场')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda c_btn: c_btn.find_element_by_android_uiautomator(
                    'text("转场")')).click()
        except TimeoutException:
            sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.6, 600)
            sc.capture_screen(fun_name, self.img_path)
            WebDriverWait(sc.driver, 5, 1).until(
                lambda c_btn: c_btn.find_element_by_android_uiautomator(
                    'text("转场")')).click()

        sc.logger.info('点击最后一个转场')
        tr_cover = 'com.quvideo.xiaoying:id/item_cover'
        tr_list = sc.driver.find_elements_by_id(tr_cover)
        tr_list[-1].click()
        sc.capture_screen(fun_name, self.img_path)

        time.sleep(6)
        right_btn = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id(right_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-转场-添加测试完成')
