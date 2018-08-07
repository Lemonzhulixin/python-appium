# -*- coding: utf-8 -*-
"""预览页面的music测试用例."""
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from Android_old import script_ultils as sc


class TestPreviewMusic(object):
    """预览页面的music测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_music_create(self):
        """导出-创建视频."""
        sc.logger.info('分享-创建视频')
        fun_name = 'test_music_create'

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“拍摄”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()

        el_cp = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')

        # 长按拍摄
        sc.logger.info('长按拍摄5s')
        actions = TouchAction(sc.driver)
        actions.long_press(el_cp, None, None, 5000).release().perform()
        sc.capture_screen(fun_name, self.img_path)

        next_btn = 'com.quvideo.xiaoying:id/cam_btn_next'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(next_btn)).click()

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("存草稿")')).click()

        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('分享-创建视频完成')

    def test_music_add(self):
        """预览页-配乐."""
        sc.logger.info('预览页-配乐')
        start_x = self.width // 2
        start_y = self.height // 3
        fun_name = 'test_music_add'

        sc.logger.info('点击草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        sc.driver.find_element_by_id(draft_img).click()

        sc.logger.info('点击“配乐”')
        sc.driver.find_element_by_android_uiautomator('text("配乐")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击添加配乐')
        try:
            del_icon = 'com.quvideo.xiaoying:id/imgbtn_del_music'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(del_icon)).click()
            sc.capture_screen(fun_name, self.img_path)
        except TimeoutException:
            bgm_row = 'com.quvideo.xiaoying:id/txtview_bgm_name'
            sc.driver.find_element_by_id(bgm_row).click()

        sc.logger.info('下载音乐')
        music_item_download = 'com.quvideo.xiaoying:id/music_item_download'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(music_item_download)).click()

        sc.logger.info('添加音乐')
        time.sleep(5)
        music_item_name = 'com.quvideo.xiaoying:id/music_item_name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(music_item_name)).click()

        while True:
            try:
                state_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
                WebDriverWait(sc.driver, 10, 1).until(
                    lambda el: el.find_element_by_id(state_btn)).click()
                sc.logger.info('点击播放状态')
                break
            except TimeoutException:
                WebDriverWait(sc.driver, 10, 1).until(
                    lambda el: el.find_element_by_id(music_item_name)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('使用音乐')
        use_btn = 'com.quvideo.xiaoying:id/music_item_use'
        sc.driver.find_element_by_id(use_btn).click()

        time.sleep(1)
        sc.driver.swipe(start_x, start_y, start_x, start_y, 1000)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击声音按钮')
        video_icon = 'com.quvideo.xiaoying:id/imgview_icon_video'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(video_icon)).click()

        sc.logger.info('点击音乐按钮')
        bgm_icon = 'com.quvideo.xiaoying:id/imgview_icon_bgm'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(bgm_icon)).click()

        sc.logger.info('点击删除音乐按钮')
        del_icon = 'com.quvideo.xiaoying:id/imgbtn_del_music'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(del_icon)).click()

        time.sleep(1)
        sc.driver.swipe(start_x, start_y, start_x, start_y, 1000)

        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('预览页-配乐测试完成')

    def test_preview_recommend(self):
        """音乐库-推荐音乐下载."""
        sc.logger.info('音乐库-推荐音乐下载')
        fun_name = 'test_preview_recommend'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        sc.logger.info('点击添加配乐')
        b_btn = 'com.quvideo.xiaoying:id/txtview_bgm_name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(b_btn)).click()

        # 推荐音乐下载
        while True:
            try:
                sc.driver.find_element_by_android_uiautomator(
                    'text("没有更多了…")').click()
                break
            except NoSuchElementException:
                sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 600)

        sc.logger.info('下载音乐')
        music_item_download = 'com.quvideo.xiaoying:id/music_item_download'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(music_item_download)).click()

        time.sleep(5)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-推荐音乐下载测试完成')

    def test_preview_other(self):
        """音乐库-其他分类音乐下载."""
        sc.logger.info('音乐库-其他分类音乐下载')
        fun_name = 'test_preview_other'
        start_x = self.width - self.width // 5
        start_bottom = self.height // 2

        # 切换到流行分类
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.7, 500)
        sc.logger.info('点击第一个可下载按钮')
        sc.logger.info('下载音乐')
        music_item_download = 'com.quvideo.xiaoying:id/music_item_download'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(music_item_download)).click()

        time.sleep(5)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-其他分类音乐下载测试完成')

    def test_preview_use(self):
        """音乐库-使用已下载音乐."""
        sc.logger.info('音乐库-使用已下载音乐')
        start_x = self.width // 2
        start_y = self.height // 3
        fun_name = 'test_preview_use'

        sc.logger.info('点击“已下载”tab')
        sc.driver.find_element_by_android_uiautomator('text("已下载")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加音乐')
        music_item_name = 'com.quvideo.xiaoying:id/music_item_name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(music_item_name)).click()

        state_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(state_btn)).click()

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_android_uiautomator(
            'text("添加")').click()

        time.sleep(1)
        sc.driver.swipe(start_x, start_y, start_x, start_y, 1000)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-使用已下载音乐测试完成')

    def test_preview_delete(self):
        """音乐库-删除已下载音乐."""
        sc.logger.info('音乐库-删除已下载音乐')
        fun_name = 'test_preview_delete'

        b_btn = 'com.quvideo.xiaoying:id/txtview_bgm_name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(b_btn)).click()

        sc.logger.info('点击删除按钮')
        rubbish_icon = 'com.quvideo.xiaoying:id/music_rubbish_icon'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(rubbish_icon)).click()

        sc.logger.info('依次选择已下载音乐')
        check_item = 'com.quvideo.xiaoying:id/music_item_check_box'
        sc.find_by_ids(check_item, fun_name, self.img_path)

        sc.logger.info('再次点击删除按钮')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(rubbish_icon)).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-删除已下载音乐测试完成')

    def test_preview_local(self):
        """音乐库-使用本地音乐."""
        sc.logger.info('音乐库-使用本地音乐')
        start_x = self.width // 2
        start_y = self.height // 3
        fun_name = 'test_preview_local'

        sc.driver.find_element_by_android_uiautomator('text("本地")').click()
        sc.capture_screen(fun_name, self.img_path)

        music_item_name = 'com.quvideo.xiaoying:id/music_item_name'
        m_list = sc.driver.find_elements_by_id(music_item_name)
        try:
            m_list[0].click()
        except Exception:
            sc.logger.info('本地音乐不存在！返回创作中心主界面。')
            for i in range(4):
                time.sleep(1)
                sc.driver.press_keycode(4)
            return True

        state_btn = 'com.quvideo.xiaoying:id/music_item_play_state'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(state_btn)).click()

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_android_uiautomator(
            'text("添加")').click()

        time.sleep(1)
        sc.driver.swipe(start_x, start_y, start_x, start_y, 1000)

        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()

        left_icon = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(left_icon)).click()
        sc.logger.info('音乐库-使用本地音乐测试完成')

    def test_preview_time(self):
        """预览页-时长."""
        sc.logger.info('预览页-时长')
        fun_name = 'test_preview_time'
        start_x = self.width // 2
        start_y = self.height // 3

        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“相册MV')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("相册MV")')).click()

        sc.logger.info('添加图片')
        click_mask = 'com.quvideo.xiaoying:id/img_click_mask'
        element_list = sc.driver.find_elements_by_id(click_mask)

        if len(element_list) >= 2:
            element_list = element_list[:2]

        for element_em in element_list:
            element_em.click()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“下一步”')
        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()

        time.sleep(1)
        sc.driver.swipe(start_x, start_y, start_x, start_y, 1000)

        sc.logger.info('点击“时长”')
        sc.driver.find_element_by_android_uiautomator('text("时长")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()

        sc.logger.info('点击左上角返回创作中心主界面')
        left_icon = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(left_icon)).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('预览页-时长测试完成')
