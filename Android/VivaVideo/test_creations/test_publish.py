# -*- coding: utf-8 -*-
"""创作页面内分享相关的测试用例."""
import time
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestCreationShare(object):
    """创作页面内分享相关的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_share_create(self):
        """分享-创建视频."""
        sc.logger.info('分享-创建视频')
        fun_name = 'test_share_create'
        time.sleep(1)

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        el_capture.click()
        time.sleep(5)
        el_capture.click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        sc.driver.find_element_by_android_uiautomator('text("保存/上传")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('分享-创建视频完成')

    def test_share_edit(self):
        """分享-编辑视频标题/话题相关."""
        sc.logger.info('分享-编辑视频标题/话题相关')
        fun_name = 'test_share_edit'

        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        sc.logger.info('添加标题')
        el_title = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/share_video_title_text')
        el_title.clear()
        el_title.send_keys('video title test')

        sc.logger.info('添加话题')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/share_btn_add_topic').click()
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)
        el_tag = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/txtview_tag_name')
        el_tag.click()
        sc.capture_screen(fun_name, self.img_path)

        # 显示位置有点问题，后续再优化
        """ sc.logger.info("显示位置")
        sc.driver.find_element_by_id("com.quvideo.xiaoying:id/txt_locating_tips").click()
        try:
            element = WebDriverWait(dr, 60).until(
                lambda local: local.find_element_by_id("com.quvideo.xiaoying:id/img_back"))
            sc.capture_screen(fun_name, self.img_path)
            loc_list = sc.driver.find_elements_by_id("com.quvideo.xiaoying:id/map_list_item_txt_title")
            for loc in loc_list:
                if loc.text == u'不显示位置':
                    loc.click()
        except TimeoutError as t:
            sc.loggererror("加载位置超时", t)
            return False
        sc.capture_screen(fun_name, self.img_path)
        """

        sc.logger.info('隐私设置')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/share_btn_privacy').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/private_setting_visible_btn').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/private_setting_candnload_btn').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/buttonDefaultPositive').click()
        sc.logger.info('导出-导出页编辑测试完成')

    def test_share_upload(self):
        """导出-分享上传."""
        sc.logger.info('导出-分享上传')
        fun_name = 'test_share_upload'

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/share_btn_share').click()
        # sc.driver.find_element_by_id('com.quvideo.xiaoying:id/purchase_duration_limit_title').click()
        try:
            WebDriverWait(sc.driver, 300).until(
                lambda V_exprot: V_exprot.find_element_by_id('com.quvideo.xiaoying:id/textview_id_sns_qqspace'))
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/textview_id_sns_qqspace').click()
            time.sleep(5)
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.press_keycode(4)
        except TimeoutError as t:
            sc.logger.error('导出视频超时', t)
            sc.driver.press_keycode(4)
            return False
        sc.logger.info('导出-分享上传完成')
