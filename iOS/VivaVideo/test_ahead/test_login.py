# -*- coding: utf-8 -*-
"""用户空间登录的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from iOS import iOS_elements


class TestUserLogin(TestCase):
    """用户登录测试类."""

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

    def test_login_01_start(self):
        """测试登录页面未登录时的初始状态
        """
        sc.logger.info('登录页面初始状态检查测试开始')
        fun_name = 'test_login_origin'

        sc.logger.info('授权小影发送通知')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name("允许")).click()
        except TimeoutException:
            sc.logger.info('已授权小影发送通知')

        sc.logger.info('执行引导操作')
        try:
            time.sleep(2)
            sc.driver.find_element_by_name("下一步").click()
            sc.driver.find_element_by_name("下一步").click()
            sc.driver.find_element_by_name("完成").click()
        except NoSuchElementException:
            sc.logger.info('已经执行过操作引导页面')

        sc.logger.info('小影圈页面-关闭活动弹窗')
        try:
            sc.driver.find_element_by_name("vivavideo purchase close n").click()
        except NoSuchElementException:
            sc.logger.info('当前无或者已关闭活动弹窗')

        sc.logger.info('切换到"我"')
        sc.driver.find_element_by_xpath(iOS_elements.btn_me).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('小影圈页面-关闭活动弹窗')
        try:
            sc.driver.find_element_by_name("vivavideo purchase close n").click()
        except NoSuchElementException:
            sc.logger.info('当前无或者已关闭活动弹窗')

    @staticmethod
    def login_judge():
        """判断是否已经登录."""
        btn_login = "注册/登录"
        try:
            el_login_btn = sc.driver.find_element_by_name(btn_login)
        except NoSuchElementException:
            sc.logger.info('未找到"注册/登录"按钮，用户已经成功登录')
            return True
        else:
            sc.logger.info('找到"注册/登录"按钮，用户未登录')
            return el_login_btn

    @staticmethod
    def qq_login(username, password):
        """使用qq登录."""

        sc.logger.info('点击"QQ账号"')
        try:
            sc.driver.find_element_by_name("QQ帐号").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("使用此账号登录").click()

        try:
            try:
                WebDriverWait(sc.driver, 10).until(
                    lambda x: x.find_element_by_name("登录")).click()
            except TimeoutException:
                sc.driver.find_element_by_name("授权并登录").click()
            sc.logger.info('QQ账号已登录，直接点击"授权并登录"')
        except NoSuchElementException:
            # 授权页面的登录有时显示"授权并登录"，有时显示"登录"，所以此处输入账号登录的判断需要再优化
            sc.logger.info('QQ账号未登录，请输入QQ账号及密码登录')
            sc.logger.info('输入QQ账号')
            el_account = sc.driver.find_element_by_accessibility_id('帐号')
            el_account.click()
            el_account.send_keys(username)

            sc.logger.info()
            el_passwd = sc.driver.find_element_by_accessibility_id('输入QQ密码')
            el_passwd.click()
            el_passwd.send_keys(password)

            sc.logger.info('点击“登录”按钮')
            sc.driver.find_element_by_name('登录').click()

        sc.logger.info('检查QQ授权登录是否成功')
        try:
            WebDriverWait(sc.driver, 10).until(
                lambda el_settings:el_settings.find_element_by_name(iOS_elements.btn_settings))
            sc.logger.info('授权登录成功')
            try:
                sc.driver.find_element_by_name("icon dj close").click()
            except NoSuchElementException:
                sc.logger.info('非首次登录，已跳过领取特权')
        except TimeoutException:
            sc.logger.info('QQ授权登录超时')

        if TestUserLogin.login_judge() is True:
            return True
        return False

    @staticmethod
    def login_method(req_method, username, passwd):
        """定义带登录方法的登录方式，目前国内只支持三种."""
        method_list = ['weibo', 'wechat', 'QQ']
        if req_method not in method_list:
            sc.logger.error('不支持的登录方式： %s', req_method)
            return False

        if req_method == 'QQ':
            return TestUserLogin.qq_login(username, passwd)
        else:
            return False

    @staticmethod
    def test_login_02_qq():
        """国内用户测试使用qq登录."""
        sc.logger.info('登录页面QQ登录测试开始')
        login_res = TestUserLogin.login_judge()
        if login_res is True:
            assert True
        else:
            sc.logger.info('点击"注册/登录"按钮')
            login_res.click()
            username = '1813326733'
            passwd = 'qa123456'
            login_res = TestUserLogin.login_method('QQ', username, passwd)

        assert login_res is not False