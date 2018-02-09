# -*- coding: utf-8 -*-
"""编辑页面画中画的基本操作测试用例."""
import time
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestEditCollage(object):
    """编辑页面画中画的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_collage(self):
        """剪辑-画中画-图片添加."""
        sc.logger.info('剪辑-画中画-图片添加')
        fun_name = 'test_edit_collage'

        start_x = self.width // 2
        start_bottom = self.height // 3

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
            if el_item.text == '画中画':
                sc.logger.info('开始点击画中画')
                el_item.click()
                break
        sc.logger.info('开始添加图片')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_editor_btn_gif_add').click()
        el_pic = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/collage_pic_item_cover')
        sc.logger.info('添加一张图片')
        el_pic.click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 100)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()
        sc.logger.info('再次点击确认按钮回到预览页')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-画中画-图片添加测试完成')

    def test_edit_collage_add(self):
        """剪辑-画中画-GIF添加."""
        sc.logger.info('剪辑-画中画-GIF添加')
        fun_name = 'test_edit_collage_add'

        start_x = self.width // 2
        start_bottom = self.height // 3

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
            if el_item.text == '画中画':
                sc.logger.info('开始点击画中画')
                el_item.click()
                break
        sc.logger.info('开始添加图片')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_editor_btn_gif_add').click()
        sc.logger.info('点击上方"gif" tab')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_editor_title_gif_choose_gif').click()
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda gif: gif.find_element_by_id('com.quvideo.xiaoying:id/collage_gif_item_cover'))
            el_gif = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/collage_gif_item_cover')
            el_gif.click()
            time.sleep(5)
            el_gif.click()
        except Exception as e:
            sc.logger.error('GIF图片加载异常', e)
            return False
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 1000)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()
        sc.logger.info('再次点击确认按钮回到预览页')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-画中画-GIF添加测试完成')

    def test_edit_collage_search(self):
        """剪辑-画中画-GIF搜索."""
        sc.logger.info('剪辑-画中画-GIF搜索')
        fun_name = 'test_edit_collage_search'
        start_x = self.width // 2
        start_bottom = self.height // 3

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
            if el_item.text == '画中画':
                sc.logger.info('开始点击画中画')
                el_item.click()
                break
        sc.logger.info('开始添加图片')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_editor_btn_gif_add').click()
        sc.logger.info('点击上方"gif" tab')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_editor_title_gif_choose_gif').click()
        el_gif_search = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_search_gif')
        el_gif_search.clear()
        el_gif_search.send_keys('a')
        sc.logger.info('用字符"a"搜索gif')
        sc.driver.press_keycode(66)
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda gif: gif.find_element_by_id('com.quvideo.xiaoying:id/collage_gif_item_cover'))
            el_gif = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/collage_gif_item_cover')
            sc.logger.info('下载gif')
            el_gif.click()
            time.sleep(5)
            el_gif.click()
            sc.capture_screen(fun_name, self.img_path)
        except Exception as e:
            sc.logger.error('GIF图片加载异常', e)
            sc.capture_screen(fun_name, self.img_path)
            return False
        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 1000)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()
        sc.logger.info('再次点击确认按钮回到预览页')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-画中画-GIF搜索测试完成')

    def test_edit_collage_cancel(self):
        """剪辑-画中画-放弃."""
        sc.logger.info('剪辑-画中画-放弃')
        fun_name = 'test_edit_collage_cancel'

        start_x = self.width // 2
        start_bottom = self.height // 3

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
            if el_item.text == '画中画':
                sc.logger.info('开始点击画中画')
                el_item.click()
                break
        sc.logger.info('开始添加图片')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_editor_btn_gif_add').click()
        el_pic = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/collage_pic_item_cover')
        sc.logger.info('添加一张图片')
        el_pic.click()

        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_right_button').click()
        sc.driver.swipe(start_x, start_bottom, start_x, start_bottom, 1000)
        sc.logger.info('放弃所有操作')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_left_button').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/video_title_left_button').click()
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()

        sc.logger.info('返回创作中心主界面')
        for i in range(4):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-画中画-放弃测试完成')
