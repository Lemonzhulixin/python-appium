# -*- coding: utf-8 -*-
"""预览页面的music测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from iOS import iOS_elements,base as ba

class TestPreviewMusic(TestCase):
    """预览页面的music测试类."""

    # 获取屏幕尺寸
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @classmethod
    def setUpClass(cls):
        sc.driver.launch_app()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        sc.driver.close_app()

    def test_music_01_add(self):
        """预览页-配乐."""
        sc.logger.info('配乐操作相关')
        fun_name = 'test_music_add'

        sc.logger.info('打开一个草稿视频')
        ba.home_first_click('更多草稿')

        sc.logger.info('点击草稿封面')
        ba.open_draft(iOS_elements.el_studio_draft)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“主题”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("主题")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('配乐相关操作')
        ba.preview_music()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('预览页-配乐测试完成')

    def test_music_02_recommend(self):
        """音乐库-推荐音乐下载."""
        sc.logger.info('音乐库-推荐音乐下载')
        fun_name = 'test_preview_recommend'

        sc.logger.info('点击“添加配乐”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("添加配乐")).click()

        # 推荐音乐下载
        sc.logger.info('向上滑动')
        start_x = self.width // 2
        start_y = self.height // 8
        start_bottom = self.height - start_y
        for i in range(2):
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)

        sc.logger.info('下载音乐')
        music_list = sc.driver.find_elements_by_name(iOS_elements.el_mus_download)
        if len(music_list) >= 3:
            music_list = music_list[:3]
        for el_music in music_list:
            el_music.click()

        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-推荐音乐下载测试完成')

    def test_music_03_other(self):
        """音乐库-其他分类音乐下载."""
        sc.logger.info('音乐库-其他分类音乐下载')
        fun_name = 'test_preview_other'

        # 切换到其他分类
        sc.logger.info('点击“中国风”分类')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('中国风')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载音乐')
        music_list = sc.driver.find_elements_by_name(iOS_elements.el_mus_download)
        if len(music_list) >= 3:
            music_list = music_list[:3]
        for el_music in music_list:
            el_music.click()

        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-其他分类音乐下载测试完成')

    def test_music_04_use(self):
        """音乐库-使用已下载音乐."""
        sc.logger.info('音乐库-使用已下载音乐')
        fun_name = 'test_preview_use'

        sc.logger.info('点击“已下载”tab')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('已下载')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加音乐')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_mus_play)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()

        sc.logger.info('暂停播放')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_stop)).click()

        sc.logger.info('删除配乐')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_music_del)).click()

        sc.logger.info('点击添加配乐')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('点击添加配乐')).click()

        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-使用已下载音乐测试完成')

    def test_music_05_delete(self):
        """音乐库-删除已下载音乐."""
        sc.logger.info('音乐库-删除已下载音乐')
        fun_name = 'test_preview_delete'

        sc.logger.info('点击删除按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_mus_del)).click()

        sc.logger.info('选择一首已下载音乐')
        el_check = sc.driver.find_elements_by_name(iOS_elements.el_mus_cho)
        el_check[0].click()

        sc.logger.info('再次点击删除按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_mus_del2)).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('音乐库-删除已下载音乐测试完成')

    def test_music_06_local(self):
        """音乐库-使用本地音乐."""
        sc.logger.info('音乐库-使用本地音乐')
        fun_name = 'test_preview_local'

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('本地')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加音乐')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_xpath(iOS_elements.el_mus_play)).click()
        except TimeoutException:
            sc.logger.info('本地音乐不存在！')
            return True

        sc.logger.info('点击“添加”按钮')
        sc.driver.find_element_by_name('添加').click()

        sc.logger.info('暂停播放')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_stop)).click()

        sc.logger.info('确定')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_accessibility_id(iOS_elements.btn_music_confirm)).click()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.logger.info('音乐库-使用本地音乐测试完成')
