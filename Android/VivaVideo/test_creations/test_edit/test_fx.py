# -*- coding: utf-8 -*-
"""特效的基本操作测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestEditFX(object):
    """特效的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_fx(self):
        """剪辑-特效-添加."""
        sc.logger.info('剪辑-特效-添加')
        fun_name = 'test_edit_fx'

        start_x = self.width - self.width // 4
        start_bottom = self.height - self.height // 10

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“更多草稿”')
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()

        sc.logger.info('点击草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        sc.driver.find_element_by_id(draft_img).click()

        sc.logger.info('点击“剪辑”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("剪辑")')).click()
        # sc.driver.find_element_by_android_uiautomator('text("剪辑")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)

        t_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in t_list:
            if el_item.text == '特效':
                sc.logger.info('开始点击“特效”按钮')
                el_item.click()
                break
        time.sleep(1)
        while True:
            try:
                sc.logger.info('开始点击“FX”按钮')
                sub_add_btn = 'com.quvideo.xiaoying:id/imgbtn_add_subtitle'
                sc.driver.find_element_by_id(sub_add_btn).click()
                break
            except NoSuchElementException:
                sc.logger.info('该视频已经有特效，先删除特效')
                sc.logger.info('开始点击特效编辑按钮')
                speed_close_btn = 'com.quvideo.xiaoying:id/imgbtn_speed_close'
                sc.driver.find_element_by_id(speed_close_btn).click()
                sc.capture_screen(fun_name, self.img_path)

                sc.logger.info('点击删除特效按钮')
                sub_del_btn = 'com.quvideo.xiaoying:id/imgbtn_del_subtitle'
                sc.driver.find_element_by_id(sub_del_btn).click()

        sc.capture_screen(fun_name, self.img_path)
        right_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_right'
        sc.driver.find_element_by_id(right_btn).click()
        sc.driver.find_element_by_id(right_btn).click()

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-特效-添加测试完成')

    def test_edit_fx_del(self):
        """剪辑-特效-删除."""
        sc.logger.info('剪辑-特效-删除')
        fun_name = 'test_edit_fx_del'
        start_x = self.width - self.width // 4
        start_bottom = self.height - self.height // 10

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

        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)

        t_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for item in t_list:
            if item.text == '特效':
                sc.logger.info('开始点击“特效”按钮')
                item.click()
                break
        sc.logger.info('开始点击特效编辑按钮')
        speed_close_btn = 'com.quvideo.xiaoying:id/imgbtn_speed_close'
        sc.driver.find_element_by_id(speed_close_btn).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击删除特效按钮')
        sub_del_btn = 'com.quvideo.xiaoying:id/imgbtn_del_subtitle'
        sc.driver.find_element_by_id(sub_del_btn).click()

        sc.logger.info('点击右上角确认按钮')
        right_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_right'
        sc.driver.find_element_by_id(right_btn).click()

        for i in range(3):
            time.sleep(2)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-特效-删除测试完成')

    def test_edit_fx_cancel(self):
        """剪辑-特效-放弃."""
        sc.logger.info('剪辑-特效-放弃')
        fun_name = 'test_edit_fx_cancel'
        start_x = self.width - self.width // 4
        start_bottom = self.height - self.height // 10

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

        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)

        t_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/title')
        for el_item in t_list:
            if el_item.text == '特效':
                sc.logger.info('开始点击“特效”按钮')
                el_item.click()
                break

        sc.logger.info('开始点击“FX”按钮')
        sub_add_btn = 'com.quvideo.xiaoying:id/imgbtn_add_subtitle'
        sc.driver.find_element_by_id(sub_add_btn).click()
        x_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/icon')
        try:
            x_list[1].click()
            sc.logger.info('点击第二个特效')
        except Exception:
            flag_img = 'com.quvideo.xiaoying:id/img_lock_flag'
            fx_down_list = sc.driver.find_elements_by_id(flag_img)
            fx_down_list[0].click()
            time.sleep(5)
            x_list[1].click()

        sc.logger.info('点击右上角确认按钮')
        right_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_right'
        sc.driver.find_element_by_id(right_btn).click()

        sc.logger.info('点击左上角放弃按钮')
        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        sc.driver.find_element_by_id(left_btn).click()
        sc.logger.info('确认放弃操作')
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        sc.capture_screen(fun_name, self.img_path)

        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-特效-放弃测试完成')
