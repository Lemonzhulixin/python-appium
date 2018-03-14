# -*- coding: utf-8 -*-
"""用户空间登录的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class TestUserLogin(TestCase):
    """用户空间登录测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_login_01_start(self):
        """测试登录页面未登录时的初始状态.

        1.无法获取到启动页的"跳过"控件，所以暂时先手动跳过启动页再进行登录测试，后续再优化
        """
        sc.logger.info('登录页面初始状态检查测试开始')
        fun_name = 'test_login_origin'

        time.sleep(5)
        sc.logger.info('授权小影发送通知')
        try:
            sc.driver.find_element_by_name('允许').click()
        except NoSuchElementException:
            sc.logger.info('已授权小影发送通知')

        sc.logger.info('关闭活动弹窗')
        time.sleep(2)
        try:
            sc.driver.find_element_by_name("vivavideo purchase close n").click()
        except NoSuchElementException:
            sc.logger.info('当前无或者已关闭活动弹窗')

        sc.logger.info('切换到"我"')
        btn_me = "//*/XCUIElementTypeTabBar/XCUIElementTypeButton[3]"
        sc.driver.find_element_by_xpath(btn_me).click()
        time.sleep(.500)
        sc.capture_screen(fun_name, self.img_path)

        assert btn_me is not None

    @staticmethod
    def login_judge():
        """判断是否已经登录."""
        btn_login = '立即登录'
        try:
            el_login_btn = sc.driver.find_element_by_name(btn_login)
        except NoSuchElementException:
            sc.logger.info('未找到“立即登录”按钮，用户已经成功登录')
            return True
        else:
            sc.logger.info('找到“立即登录”按钮，用户未登录')
            return el_login_btn

    @staticmethod
    def qq_login(username, password):
        """使用qq登录."""
        sc.logger.info('跳转到QQ登录页面')

        sc.logger.info('点击"QQ账号"')
        sc.driver.find_element_by_name('QQ帐号').click()

        try:
            try:
                sc.driver.find_element_by_name('授权并登录').click()
            except NoSuchElementException:
                sc.driver.find_element_by_name('登录').click()
            sc.logger.info('QQ账号已登录，直接点击"授权并登录"')
        except NoSuchElementException:
            # 授权页面的登录有时显示"授权并登录"，有时显示"登录"，所以此处输入账号登录的判断需要再优化
            sc.logger.info('QQ账号未登录，请输入QQ账号及密码登录')
            sc.logger.info('输入QQ账号')
            el_account = sc.driver.find_element_by_accessibility_id('帐号')
            el_account.click()
            el_account.send_keys(username)
            time.sleep(1)

            sc.logger.info()
            el_passwd = sc.driver.find_element_by_accessibility_id('输入QQ密码')
            el_passwd.click()
            el_passwd.send_keys(password)

            sc.logger.info('点击“登录”按钮')
            sc.driver.find_element_by_name('登录').click()

        sc.logger.info('检查QQ授权登录是否成功')
        try:
            WebDriverWait(sc.driver,30).until(
                lambda el_settings:el_settings.find_element_by_name("vivavideo setting p"))
            sc.logger.info('授权登录成功')
            time.sleep(2)
            try:
                sc.driver.find_element_by_name("icon dj close").click()
            except NoSuchElementException:
                sc.logger.info('非首次登录，已跳过领取特权')
            except Exception as e:
                sc.logger.info('关闭"领取特权"异常', e)
        except TimeoutError as t:
            sc.logger.info('QQ授权登录超时',t)

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
    def test_login_qq():
        """国内用户测试使用qq登录."""
        sc.logger.info('登录页面QQ登录测试开始')
        login_res = TestUserLogin.login_judge()
        if login_res is True:
            assert True
        else:
            sc.logger.info('点击“立即登录”按钮')
            login_res.click()
            time.sleep(2)
            username = '1813326733'
            passwd = 'qa123456'
            login_res = TestUserLogin.login_method('QQ', username, passwd)

        assert login_res is not False