# -*- coding: utf-8 -*-
"""编辑滤镜的基本操作测试用例."""
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from Android_old import script_ultils as sc


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

        sc.logger.info('开始点击滤镜')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("滤镜")')).click()

        sc.logger.info('点击“下载更多”按钮')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("下载更多")')).click()
        sc.capture_screen(fun_name, self.img_path)

        use_btn = 'com.quvideo.xiaoying:id/template_filter_apply'
        try:
            down_btn = 'com.quvideo.xiaoying:id/template_filter_download'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(down_btn)).click()
        except TimeoutException:
            sc.logger.info('当前页面主题都已经下载过了')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(use_btn)).click()

        """
        sc.logger.info('点击“应用”')
        apply_btn = 'com.quvideo.xiaoying:id/btn_filter_apply'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(apply_btn)).click()
        """

        sc.logger.info('点击第二个滤镜')
        filter_cover = ('//android.support.v7.widget.RecyclerView/'
                        'android.widget.RelativeLayout[2]')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_xpath(filter_cover)).click()

        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认按钮')
        right_btn = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(right_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-滤镜测试完成')
