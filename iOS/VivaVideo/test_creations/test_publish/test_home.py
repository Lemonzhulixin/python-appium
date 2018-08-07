# -*- coding: utf-8 -*-
"""小影创作主页面的测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import TimeoutException,NoSuchElementException

class TestHome(TestCase):
    """小影主页面的测试类."""

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

    def test_home(self):
        """首页."""
        sc.logger.info('首页')
        fun_name = 'test_home'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('VIP订阅页面展示')
        sc.driver.find_element_by_xpath(iOS_elements.el_home_vip).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.driver.find_element_by_name(iOS_elements.el_vip_close).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('首页广告展示及刷新')
        try:
            sc.driver.find_element_by_xpath(iOS_elements.el_home_ad).click()
            sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('刷新广告')
            time.sleep(5)
            sc.driver.find_element_by_name(iOS_elements.el_ad_back).click()

            sc.logger.info('退出广告')
            try:
                WebDriverWait(sc.driver, 10, 1).until(
                    lambda x: x.find_element_by_name(iOS_elements.el_ad_clo)).click()
            except TimeoutException:
                sc.logger.info('已经退出广告页面了')
        except NoSuchElementException:
            sc.logger.error('首页加载出错了')
            pass

        sc.logger.info('点击"更多草稿"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('更多草稿')).click()

        sc.logger.info('切换展示方式')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.btn_gridview)).click()
        except TimeoutException:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.btn_listview)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击删除按钮')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.btn_studio_del1)).click()
        except TimeoutException:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.btn_studio_del2)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确定删除')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name('是')).click()
        except TimeoutException:
            sc.logger.info('视频正在上传，无法删除')
            return True
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('首页-我的工作室完成')