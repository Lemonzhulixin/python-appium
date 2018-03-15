# -*- coding: utf-8 -*-
from unittest import TestCase
from iOS import script_ultils as sc
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class TestHome(TestCase):
    # 获取屏幕尺寸
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_home_01_top(self):
        """首页-VIP&广告"""
        fun_name = 'test_home_top'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_accessibility_id("camerta_n").click()
        except NoSuchElementException:
            sc.driver.find_element_by_accessibility_id("camerta_f").click()

        sc.logger.info('下拉刷新')
        start_x = self.width // 2
        start_bottom = self.height // 8
        sc.swipe_by_ratio(start_x, start_bottom, 'down', 0.5, 500)

        sc.logger.info('VIP订阅页面展示')
        sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther/XCUIElementTypeButton[1]").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='icon close n']").click()

        sc.logger.info('首页广告展示及刷新')
        sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther/XCUIElementTypeButton[2]").click()
        try:
            WebDriverWait(sc.driver, 15).until(
                lambda AD_refresh: AD_refresh.find_element_by_name("xiaoying shuffle change AD btn"))
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_name("xiaoying shuffle change AD btn").click()
        except TimeoutError as t:
            sc.logger.error('广告加载超时',t)
            return False

        sc.logger.info('关闭广告')
        sc.driver.find_element_by_name("xiaoying shuffle ad close btn").click()

    def test_home_02_minor(self):
        """首页-次要功能位"""
        fun_name = 'test_home_minor'

        sc.logger.info('slideplus广告位')
        sc.driver.find_element_by_name("一键大片").click()
        try:
            WebDriverWait(sc.driver, 15).until(
                lambda SlidePlus: SlidePlus.find_element_by_name("完成"))
            sc.capture_screen(fun_name, self.img_path)
            sc.driver.find_element_by_name("完成").click()
        except TimeoutError as t:
            sc.logger.error('跳转AppStore超时',t)
            return False

        sc.logger.info('相册MV')
        sc.driver.find_element_by_name("相册MV").click()

        sc.logger.info("授权小影访问相册和媒体资料")
        try:
            sc.driver.find_element_by_name("好").click()  # 授权相册
            time.sleep(2)
            sc.driver.find_element_by_name("好").click()  # 授权媒体资料库
        except NoSuchElementException:
            sc.logger.info("已授权")

        el_imgs = sc.driver.find_elements_by_xpath("//*/XCUIElementTypeImage")
        i = 1  #第0个为顶部的下拉框
        while i < len(el_imgs):
            el_imgs[i].click()
            i = i + 1
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='vivavideo gallery back n']").click()
        sc.driver.find_element_by_name("保存").click()
        time.sleep(2)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('美颜趣拍')
        sc.driver.find_element_by_name("美颜趣拍").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("授权小影访问相机和麦克风")
        try:
            sc.driver.find_element_by_name("好").click()  # 授权访问相机
            time.sleep(1)
            sc.driver.find_element_by_name("好").click()  # 授权访问麦克风
            time.sleep(1)
        except NoSuchElementException:
            sc.logger.info("已授权")
        sc.driver.find_element_by_name("vivavideo camera tool icon clo").click()

        sc.logger.info('向左滑动')
        start_x = self.width - self.width // 5
        start_bottom = self.height // 2
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)

        sc.logger.info('素材中心')
        sc.driver.find_element_by_name("素材中心").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('音乐视频')
        sc.driver.find_element_by_name("音乐视频").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("vivavideo camera tool icon clo").click()

        sc.logger.info('向左滑动')
        start_x = self.width - self.width // 5
        start_bottom = self.height // 2
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.4, 500)

        sc.logger.info('使用教程')
        sc.driver.find_element_by_name("使用教程").click()
        time.sleep(2)
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("vivavideo common back n").click()

    def test_home_03_studio(self):
        """首页-我的工作室."""
        fun_name = 'test_home_studio'

        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('打开草稿工程')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeImage[1]")
        el_draft.click()
        sc.driver.find_element_by_name("xiaoying com back").click()
        time.sleep(0.5)
        try:
            sc.driver.find_element_by_name("vivavideo gallery back n").click()
        except NoSuchElementException:
            sc.logger.info('此草稿视频为拍摄视频，返回的是拍摄页面')
            sc.driver.find_element_by_name("vivavideo camera tool icon clo").click()

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('删除草稿-否')
        el_del_draft =sc.driver.find_element_by_name("vivavideo tool studio delete n")
        el_del_draft.click()
        sc.driver.find_element_by_name("否").click()

        sc.logger.info('删除草稿-是')
        el_del_draft.click()
        sc.driver.find_element_by_name("是").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('Guide view')
        try:
            sc.driver.find_element_by_name("vivavideo tool studio list n").click()
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('当前已是Guide view')

        sc.logger.info('List view')
        time.sleep(0.5)
        try:
            sc.driver.find_element_by_name("vivavideo tool studio list2 n").click()
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('当前已是List view')

        sc.logger.info('返回创作中心')
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_home_04_other(self):
        """首页-小影百宝箱及其他."""
        fun_name = 'test_home_other'

        sc.logger.info('向上滑动')
        start_x = self.width // 2
        start_bottom = self.height - self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 1000)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('小影百宝箱-浪漫满屋')
        el_box1 = sc.driver.find_elements_by_xpath("//*/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeImage")
        while True:
            try:
                el_box1[1].click()
                sc.capture_screen(fun_name, self.img_path)
                break
            except:
                sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 1000)

        try:
            sc.driver.find_element_by_name("已下载").click()
        except:
            sc.logger.info('点击一键下载')
            sc.driver.find_element_by_name("一键下载").click()
            sc.capture_screen(fun_name, self.img_path)
            try:
                WebDriverWait(sc.driver, 60).until(
                    lambda download: download.find_element_by_name("已下载"))
            except TimeoutError as t:
                sc.logger.error("下载超时", t)
                return False

        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 1000)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('小影百宝箱-老友记')
        el_box2 = sc.driver.find_elements_by_xpath("//*/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeImage")
        el_box2[1].click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        # sc.logger.info('首页活动')
        # sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 800)
        # sc.driver.find_element_by_xpath("//*/XCUIElementTypeCell[5]/XCUIElementTypeOther/XCUIElementTypeButton").click()
        # time.sleep(3)
        # sc.capture_screen(fun_name, self.img_path)
        # sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 1000)
        # sc.driver.find_element_by_name("vivavideo common back n").click()

        sc.logger.info('向下滑动，恢复创作页初始状态')
        x_down = self.width // 2
        y_down = self.height // 5
        sc.swipe_by_ratio(x_down, y_down, 'down', 0.7, 800)
        sc.capture_screen(fun_name, self.img_path)





