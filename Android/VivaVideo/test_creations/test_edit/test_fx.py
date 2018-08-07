# -*- coding: utf-8 -*-
"""特效的基本操作测试用例."""
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestEditFX(object):
    """特效的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_fx(self):
        """剪辑-特效-添加."""
        sc.logger.info('剪辑-特效-添加')
        fun_name = 'test_edit_fx'

        startx = self.width // 2
        starty = self.height // 3

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

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("效果")')).click()

        sc.logger.info('开始点击特效')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("特效")')).click()

        fx_op_btn = 'com.quvideo.xiaoying:id/ve_music_op_btn'
        try:
            sc.logger.info('查找下载更多')
            fx_down_btn = 'com.quvideo.xiaoying:id/iv_download_more'
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(fx_down_btn))
        except TimeoutException:
            sc.logger.info('当前时间点已有fx，先删除')
            sc.driver.swipe(startx, starty, startx, starty, 500)
            try:
                icon_btn = 'com.quvideo.xiaoying:id/select_item'
                icon_list = sc.driver.find_elements_by_id(icon_btn)
                for icon_el in icon_list:
                    icon_el.click()
                    try:
                        WebDriverWait(sc.driver, 5, 1).until(
                            lambda x: x.find_element_by_id(fx_op_btn)).click()
                        break
                    except TimeoutException:
                        sc.driver.press_keycode(4)
                        time.sleep(1)
                        sc.driver.press_keycode(4)
                        time.sleep(1)
                        sc.driver.swipe(startx, starty, startx, starty, 500)
            except TimeoutException:
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda x: x.find_element_by_id(fx_op_btn)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id(fx_op_btn)).click()

        sc.logger.info('点击第二个特效')
        fx_cover = ('//android.support.v7.widget.RecyclerView/'
                    'android.widget.RelativeLayout[2]')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_xpath(fx_cover)).click()
        sc.capture_screen(fun_name, self.img_path)

        right_btn = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id(right_btn)).click()
        time.sleep(1)
        sc.driver.swipe(startx, starty, startx, starty, 1000)
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id(right_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作中心主界面')
        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-特效-添加测试完成')

    def test_edit_fx_del(self):
        """剪辑-特效-删除."""
        sc.logger.info('剪辑-特效-删除')
        fun_name = 'test_edit_fx_del'
        startx = self.width // 2
        starty = self.height // 3

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

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("效果")')).click()

        sc.logger.info('开始点击特效')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("特效")')).click()

        fx_op_btn = 'com.quvideo.xiaoying:id/ve_music_op_btn'
        try:
            sc.logger.info('查找下载更多')
            fx_down_btn = 'com.quvideo.xiaoying:id/iv_download_more'
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(fx_down_btn))
        except TimeoutException:
            sc.logger.info('当前时间点已有fx，先删除')
            sc.driver.swipe(startx, starty, startx, starty, 500)
            try:
                icon_btn = 'com.quvideo.xiaoying:id/select_item'
                icon_list = sc.driver.find_elements_by_id(icon_btn)
                for icon_el in icon_list:
                    icon_el.click()
                    try:
                        WebDriverWait(sc.driver, 5, 1).until(
                            lambda x: x.find_element_by_id(fx_op_btn)).click()
                        break
                    except TimeoutException:
                        sc.driver.press_keycode(4)
                        time.sleep(1)
                        sc.driver.press_keycode(4)
                        time.sleep(1)
                        sc.driver.swipe(startx, starty, startx, starty, 500)
            except TimeoutException:
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda x: x.find_element_by_id(fx_op_btn)).click()

        right_btn = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id(right_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-特效-删除测试完成')

    def test_edit_fx_cancel(self):
        """剪辑-特效-放弃."""
        sc.logger.info('剪辑-特效-放弃')
        fun_name = 'test_edit_fx_cancel'
        startx = self.width // 2
        starty = self.height // 3

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

        sc.logger.info('点击“效果”')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("效果")')).click()

        sc.logger.info('开始点击特效')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_android_uiautomator(
                'text("特效")')).click()

        fx_op_btn = 'com.quvideo.xiaoying:id/ve_music_op_btn'
        try:
            sc.logger.info('查找下载更多')
            fx_down_btn = 'com.quvideo.xiaoying:id/iv_download_more'
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_id(fx_down_btn))
        except TimeoutException:
            sc.logger.info('当前时间点已有fx，先删除')
            sc.driver.swipe(startx, starty, startx, starty, 500)
            try:
                icon_btn = 'com.quvideo.xiaoying:id/select_item'
                icon_list = sc.driver.find_elements_by_id(icon_btn)
                for icon_el in icon_list:
                    icon_el.click()
                    try:
                        WebDriverWait(sc.driver, 5, 1).until(
                            lambda x: x.find_element_by_id(fx_op_btn)).click()
                        break
                    except TimeoutException:
                        sc.driver.press_keycode(4)
                        time.sleep(1)
                        sc.driver.press_keycode(4)
                        time.sleep(1)
                        sc.driver.swipe(startx, starty, startx, starty, 500)
            except TimeoutException:
                WebDriverWait(sc.driver, 5, 1).until(
                    lambda x: x.find_element_by_id(fx_op_btn)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id(fx_op_btn)).click()

        sc.logger.info('点击第二个特效')
        fx_cover = ('//android.support.v7.widget.RecyclerView/'
                    'android.widget.RelativeLayout[2]')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_xpath(fx_cover)).click()
        sc.capture_screen(fun_name, self.img_path)

        right_btn = 'com.quvideo.xiaoying:id/terminator_right'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id(right_btn)).click()
        time.sleep(1)
        sc.driver.swipe(startx, starty, startx, starty, 1000)

        sc.logger.info('放弃之前的操作')
        left_btn = 'com.quvideo.xiaoying:id/terminator_left'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id(left_btn)).click()

        sc.logger.info('确认放弃')
        confirm_btn = 'com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_id(confirm_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        for i in range(2):
            time.sleep(1)
            sc.driver.press_keycode(4)
        sc.logger.info('剪辑-特效-放弃测试完成')
