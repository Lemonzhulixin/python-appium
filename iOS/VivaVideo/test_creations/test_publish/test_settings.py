# -*- coding: utf-8 -*-
"""设置页面的测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import TimeoutException,NoSuchElementException


class TestSettings(TestCase):
    """设置页面的测试类."""

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

    def test_settings_01_ui(self):
        """设置：默认值UI遍."""
        sc.logger.info('设置：默认UI遍历')
        fun_name = 'test_settings_ui'
        start_x = self.width // 2
        start_y = self.height // 8
        start_bottom = self.height - start_y

        sc.logger.info("进入我页面")
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name('我')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("点击设置按钮")
        sc.driver.find_element_by_name(iOS_elements.btn_settings).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("已选择语言")
        sc.driver.find_element_by_name('已选择语言').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择"Enlish"')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('English')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("切回简体中文")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('Language already selected')).click()

        time.sleep(0.5)

        sc.logger.info('向上滑动并切换回简体中文')
        for i in range(2):
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)

        sc.driver.find_element_by_name('简体中文').click()

        sc.logger.info("接收通知推送")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('接收通知推送')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下拉刷新')
        sc.swipe_by_ratio(start_x, start_y, 'down', 0.5, 300)

        checkbox_list = WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_elements_by_ios_predicate("type == 'XCUIElementTypeImage'"))
        for el_checkbox in checkbox_list:
            el_checkbox.click()
            time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("返回设置页")
        sc.driver.find_element_by_name(iOS_elements.el_com_back).click()

        sc.logger.info("隐私权限")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath('//XCUIElementTypeStaticText[@name="私信权限"]')).click()

        sc.logger.info("我关注的人")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath('//XCUIElementTypeStaticText[@name="我关注的人"]')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("返回设置页")
        sc.driver.find_element_by_name(iOS_elements.el_com_back).click()

        sc.logger.info("黑名单")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath('//XCUIElementTypeStaticText[@name="黑名单"]')).click()
        sc.capture_screen(fun_name, self.img_path)

        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name('移除')).click()
        except TimeoutException:
            sc.logger.info("黑名单列表为空")
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("返回设置页")
        sc.driver.find_element_by_name(iOS_elements.el_com_back).click()

        sc.logger.info("隐私账号")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.btn_privacy)).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('设置选项UI第一页遍历完成')

    def test_settings_02_feedback(self):
        """设置：意见反馈."""
        sc.logger.info('设置：意见反馈')
        fun_name = 'test_settings_feedback'
        start_x = self.width // 2
        start_y = self.height // 8
        start_bottom = self.height - start_y

        sc.logger.info('向上滑动')
        for i in range(2):
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)

        sc.logger.info("意见反馈")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda el: el.find_element_by_name('意见反馈')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("填写意见反馈")
        ba.feedback()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("返回设置页")
        sc.driver.find_element_by_name(iOS_elements.el_com_back).click()
        sc.logger.info('意见反馈测试完成')

    def test_settings_03_senior(self):
        """设置：高级设置和其他."""
        sc.logger.info('设置：高级设置和其他')
        fun_name = 'test_settings_senior'
        start_x = self.width // 2
        start_y = self.height // 8
        start_bottom = self.height - start_y

        sc.logger.info('向上滑动')
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)

        sc.logger.info("关于小影")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('关于小影')).click()
        sc.capture_screen(fun_name, self.img_path)

        about_list= sc.driver.find_elements_by_ios_predicate(iOS_elements.el_abouts)
        for el in about_list:
            el.click()
            sc.capture_screen(fun_name, self.img_path)
            try:
                sc.driver.find_element_by_name(iOS_elements.about_clo).click()
            except NoSuchElementException:
                WebDriverWait(sc.driver, 3, 1).until(
                    lambda x: x.find_element_by_name(iOS_elements.el_ad_back)).click()

        sc.logger.info("返回设置页")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.about_back)).click()

        sc.logger.info("成为VIP会员")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('成为VIP会员')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回设置页')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_vip_close)).click()

        sc.logger.info('向上滑动')
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)

        sc.logger.info("清除缓存")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('清除缓存')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("清除缓存")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath('//XCUIElementTypeButton[@name="清除缓存"]')).click()

        sc.logger.info("退出账号")
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('退出当前账号')).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('设置：高级设置和其他测试完成')