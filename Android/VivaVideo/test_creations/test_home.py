# -*- coding: utf-8 -*-
"""小影创作主页面的测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from Android import script_ultils as sc


class TestHome(object):
    """小影主页面的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_home_minor(self):
        """首页-次要功能位检查."""
        sc.logger.info('首页-次要功能位检查')
        fun_name = 'test_home_minor'

        time.sleep(5)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.view_by_ids('com.quvideo.xiaoying:id/sub_btn_icon', fun_name, self.img_path)
        time.sleep(2)
        start_x = self.width - self.width // 10
        start_bottom = self.height // 2
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 500)
        sc.view_by_ids('com.quvideo.xiaoying:id/sub_btn_icon', fun_name, self.img_path)
        sc.logger.info('首页-次要功能位检查完毕')

    def test_home_other(self):
        """首页-小影百宝箱及其他."""
        sc.logger.info('首页-推荐位-小影百宝箱及其他')
        fun_name = 'test_home_other'

        time.sleep(3)
        start_x = self.width // 2
        start_bottom = self.height - self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 500)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_vip').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_back').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_shuffle').click()
        sc.driver.press_keycode(4)
        el_ads_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/creation_item_img')

        # 跳转小影记广告位
        for el_ad in el_ads_list:
            el_ad.click()
            time.sleep(3)
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.press_keycode(4)
        sc.logger.info('首页-推荐位-小影百宝箱及其他检查完毕')

    def test_home_studio(self):
        """首页-我的工作室."""
        sc.logger.info('首页-我的工作室')
        fun_name = 'test_home_studio'

        time.sleep(3)
        start_x = self.width // 2
        start_bottom = self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'down', 0.6, 500)
        sc.driver.find_element_by_android_uiautomator('text("更多草稿")').click()
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        time.sleep(1)
        try:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        except NoSuchElementException:
            sc.logger.info('此草稿视频为拍摄视频，返回的是拍摄页面')
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_cancel').click()
        el_publish = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_publish_btn')
        el_publish.click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_back').click()
        el_del_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_delete')
        el_del_draft.click()
        sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        sc.driver.press_keycode(4)
        sc.logger.info('首页-我的工作室完成')
