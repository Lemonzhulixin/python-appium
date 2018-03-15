# -*- coding: utf-8 -*-
"""视频详情页里视频相关的测试用例.

为了不干扰正常用户，下面对于视频的操作均为自己用户空间的视频
"""
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestUserVideos(object):
    """个人视频详情页的测试类，分步截图."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]
    p_btn = 'com.quvideo.xiaoying:id/img_studio'

    def test_video_origin(self):
        """video详情页面的初始状态."""
        sc.logger.info('video详情页初始状态检查开始')
        fun_name = 'test_video_origin'

        sc.logger.info('点击个人中心主按钮')
        sc.first_step(self.p_btn)

        el_video_til = 'com.quvideo.xiaoying:id/xiaoying_com_video_card_title'
        el_video = sc.driver.find_element_by_id(el_video_til)
        sc.logger.info('点击第一个视频标题')
        el_video.click()
        time.sleep(1)
        sc.logger.info('video详情页面初始状态截图开始')
        sc.capture_screen(fun_name, self.img_path)

    def test_video_play(self):
        """测试视频的播放."""
        sc.logger.info('测试视频的暂停/播放/进度条')
        fun_name = 'test_video_play'

        time.sleep(1)
        el_video = sc.driver.find_element_by_id(
            'com.quvideo.xiaoying:id/xiaoying_com_activity_videoview')
        el_video.click()

        sc.capture_screen(fun_name, self.img_path)
        assert el_video is not None

    def test_video_reply(self):
        """测试视频的评论功能."""
        sc.logger.info('开始测试视频的评论功能.')
        fun_name = 'test_video_reply'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        time.sleep(1)
        # 先上滑半屏，便于处理全屏视频
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)

        # 查找评论框并输入'QA Reply Test'
        el_reply_frame = 'com.quvideo.xiaoying:id/comment_editor_view'
        el_reply = sc.driver.find_element_by_id(el_reply_frame)
        sc.logger.info('评论框输入“QA Reply Test”并发送')
        el_reply.send_keys('QA Reply Test')
        btn_reply = 'com.quvideo.xiaoying:id/comment_send_btn'
        sc.driver.find_element_by_id(btn_reply).click()
        sc.capture_screen(fun_name, self.img_path)

    def test_video_like(self):
        """测试视频的点赞功能."""
        sc.logger.info('开始测试视频的点赞功能.')
        fun_name = 'test_video_like'

        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)
        btn_like = 'com.quvideo.xiaoying:id/like_btn'
        sc.driver.find_element_by_id(btn_like).click()
        sc.capture_screen(fun_name, self.img_path)

    def test_video_download(self):
        """测试视频的下载功能."""
        sc.logger.info('开始测试视频的下载功能.')
        fun_name = 'test_video_download'

        sc.capture_screen(fun_name, self.img_path)
        down_btn = 'com.quvideo.xiaoying:id/video_detail_download_icon'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(down_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        try:
            pos_btn = 'com.quvideo.xiaoying:id/buttonDefaultPositive'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(pos_btn)).click()
            sc.driver.press_keycode(4)
        except TimeoutException:
            sc.logger.info('视频下载完成')

    def test_video_share(self):
        """测试视频的分享功能."""
        sc.logger.info('开始测试视频的分享功能.')
        fun_name = 'test_video_share'

        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)
        btn_share = 'com.quvideo.xiaoying:id/btn_share'
        sc.driver.find_element_by_id(btn_share).click()
        sc.capture_screen(fun_name, self.img_path)
