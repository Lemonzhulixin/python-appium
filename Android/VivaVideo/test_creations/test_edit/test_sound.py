# -*- coding: utf-8 -*-
"""配音的基本操作测试用例."""
import time
from appium.webdriver.common.touch_action import TouchAction
from Android import script_ultils as sc


class TestEditSound(object):
    """配音的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_sound_add(self):
        """剪辑-配音-添加."""
        sc.logger.info('剪辑-配音-添加')
        fun_name = 'test_edit_sound_add'

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
            if el_item.text == '配音':
                sc.logger.info('开始点击配音')
                el_item.click()
                break
        el_record = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/dub_panel_audio_record_btn')
        # 长按录制
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_record, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)
        """
        x = record.location.get('x')
        y = record.location.get('y')
        sc.driver.swipe(x, y, x, y, 5000)
        """
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_ve_imgbtn_add_audio_dub').click()
        time.sleep(2)
        el_audio_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/musiclist_title')
        el_audio_name.click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_add_music').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-配音-添加测试完成')

    def test_edit_sound_del(self):
        """剪辑-配音-删除."""
        sc.logger.info('剪辑-配音-删除')
        fun_name = 'test_edit_sound_del'

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
            if el_item.text == '配音':
                sc.logger.info('开始点击配音')
                el_item.click()
                break

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_speed_close').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_del_dub').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-配音-删除测试完成')

    def test_edit_sound_cancel(self):
        """剪辑-配音-放弃."""
        sc.logger.info('剪辑-配音-放弃')
        fun_name = 'test_edit_sound_cancel'
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
            if el_item.text == '配音':
                sc.logger.info('开始点击配音')
                el_item.click()
                break
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_ve_imgbtn_add_audio_dub').click()
        time.sleep(2)
        el_audio_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/musiclist_title')
        el_audio_name.click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_add_music').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-配音-放弃测试完成')
