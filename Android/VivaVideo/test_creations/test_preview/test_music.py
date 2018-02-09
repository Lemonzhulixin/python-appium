# -*- coding: utf-8 -*-
"""预览页面的music测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from Android import script_ultils as sc


class TestPreviewMusic(object):
    """预览页面的music测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @staticmethod
    def test_music_create():
        """导出-创建视频."""
        sc.logger.info('分享-创建视频')
        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“拍摄”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon2').click()
        el_capture = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_rec')
        # 点拍
        el_capture.click()
        time.sleep(5)
        el_capture.click()
        time.sleep(1)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/cam_btn_next').click()
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        sc.logger.info('分享-创建视频完成')

    def test_music_add(self):
        """预览页-配乐."""
        sc.logger.info('预览页-配乐')
        fun_name = 'test_music_add'

        sc.logger.info('点击第一个草稿封面')
        el_draft = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb')
        el_draft.click()
        sc.logger.info('点击“配乐”')
        sc.driver.find_element_by_android_uiautomator('text("配乐")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击添加配乐')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/txtview_bgm_name').click()

        el_download = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_download')
        el_music_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_name')
        sc.logger.info('下载音乐')
        el_download.click()

        sc.logger.info('添加音乐')
        el_music_name.click()

        while True:
            try:
                sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_play_state').click()
                sc.logger.info('点击播放状态')
                break
            except NoSuchElementException:
                time.sleep(5)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('使用音乐')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_use').click()
        # sc.driver.tap([(start_x, start_bottom), (start_x, start_bottom)], 100)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/preview_layout_fake').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击声音按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgview_icon_video').click()
        sc.logger.info('点击音乐按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgview_icon_bgm').click()
        sc.logger.info('点击删除音乐按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_del_music').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('预览页-配乐测试完成')

    def test_preview_recommend(self):
        """音乐库-推荐音乐下载."""
        sc.logger.info('音乐库-推荐音乐下载')
        fun_name = 'test_preview_recommend'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        sc.logger.info('点击添加配乐')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/txtview_bgm_name').click()
        sc.logger.info('点击“推荐”tab')
        sc.driver.find_element_by_android_uiautomator('text("推荐")').click()

        # 推荐音乐下载
        while True:
            try:
                sc.driver.find_element_by_android_uiautomator('text("没有更多了…")').click()
                break
            except NoSuchElementException:
                sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)

        el_download = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_download')
        el_download.click()
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
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.7, 500)
        sc.logger.info('点击第一个可下载按钮')
        el_download = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_download')
        el_download.click()
        time.sleep(5)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-其他分类音乐下载测试完成')

    def test_preview_use(self):
        """音乐库-使用已下载音乐."""
        sc.logger.info('音乐库-使用已下载音乐')
        fun_name = 'test_preview_use'

        sc.logger.info('点击“已下载”tab')
        sc.driver.find_element_by_android_uiautomator('text("已下载")').click()
        sc.capture_screen(fun_name, self.img_path)
        el_music_name = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_name')
        el_music_name.click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_play_state').click()
        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_android_uiautomator('text("添加")').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/preview_layout_fake').click()
        sc.capture_screen(fun_name, self.img_path)
        time.sleep(1)
        sc.logger.info('音乐库-使用已下载音乐测试完成')

    def test_preview_delete(self):
        """音乐库-删除已下载音乐."""
        sc.logger.info('音乐库-删除已下载音乐')
        fun_name = 'test_preview_delete'

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/txtview_bgm_name').click()
        sc.logger.info('点击删除按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_rubbish_icon').click()
        sc.logger.info('依次选择已下载音乐')
        sc.find_by_ids('com.quvideo.xiaoying:id/music_item_check_box', fun_name, self.img_path)
        sc.logger.info('再次点击删除按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_rubbish_icon').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-删除已下载音乐测试完成')

    def test_preview_local(self):
        """音乐库-使用本地音乐."""
        sc.logger.info('音乐库-使用本地音乐')
        fun_name = 'test_preview_local'
        sc.driver.find_element_by_android_uiautomator('text("本地")').click()
        sc.capture_screen(fun_name, self.img_path)
        m_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/music_item_name')
        try:
            m_list[0].click()
        except Exception:
            sc.logger.info('本地音乐不存在！返回创作中心主界面。')
            for i in range(4):
                time.sleep(1)
                sc.driver.press_keycode(4)
            return True
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/music_item_play_state').click()
        sc.driver.find_element_by_android_uiautomator('text("添加")').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/preview_layout_fake').click()
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.logger.info('音乐库-使用本地音乐测试完成')

    def test_preview_time(self):
        """预览页-时长."""
        sc.logger.info('预览页-时长')
        fun_name = 'test_preview_time'

        sc.logger.info('点击“相册MV')
        sc.driver.find_element_by_android_uiautomator('text("相册MV")').click()
        sc.logger.info('添加图片')
        sc.find_by_ids('com.quvideo.xiaoying:id/img_click_mask', fun_name, self.img_path)
        sc.logger.info('点击“下一步”')
        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/preview_layout_fake').click()
        sc.logger.info('点击“时长”')
        sc.driver.find_element_by_android_uiautomator('text("时长")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('点击“存草稿”')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        sc.logger.info('点击左上角返回创作中心主界面')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('预览页-时长测试完成')
