# -*- coding: utf-8 -*-
"""用户空间登录的测试用例."""
import time
import inspect
from selenium.common.exceptions import NoSuchElementException
from Android import script_ultils as sc


class TestUserLogin(object):
    """用户空间登录测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_login_origin(self):
        """测试登录页面未登录时的初始状态."""
        sc.logger.info('登录页面初始状态检查测试开始')
        fun_name = 'test_login_origin'

        time.sleep(2)
        btn_home = 'com.quvideo.xiaoying:id/img_studio'
        el_home = sc.driver.find_element_by_id(btn_home)
        el_home.click()
        time.sleep(.500)
        sc.capture_screen(fun_name, self.img_path)
        assert el_home is not None

    @staticmethod
    def login_judge():
        """判断是否已经登录."""
        btn_login = 'com.quvideo.xiaoying:id/btn_v6_login'
        try:
            el_login_btn = sc.driver.find_element_by_id(btn_login)
        except NoSuchElementException:
            sc.logger.info('未找到“立即登录”按钮，用户已经登录')
            return True
        else:
            sc.logger.info('找到“立即登录”按钮，用户未登录')
            return el_login_btn

    @staticmethod
    def qq_login(username, passwd):
        """使用qq登录."""
        sc.logger.info('跳转到QQ登录页面')
        btn_qq = 'com.quvideo.xiaoying:id/btn_login_qq'
        el_btn_qq = sc.driver.find_element_by_id(btn_qq)
        el_btn_qq.click()
        time.sleep(5)

        qq_login_id = 'com.tencent.mobileqq:id/name'
        el_qqlogin_list = sc.driver.find_elements_by_id(qq_login_id)

        for el_qq_login in el_qqlogin_list:
            if el_qq_login.text == '添加帐号':
                sc.logger.info('点击“添加帐号”按钮')
                el_qq_login.click()
                break

        account_frame = 'com.tencent.mobileqq:id/account'
        passwd_frame = 'com.tencent.mobileqq:id/password'
        time.sleep(5)
        el_account = sc.driver.find_element_by_id(account_frame)
        el_account.click()
        sc.logger.info('输入QQ账号：%s', username)
        el_account.send_keys(username)

        el_passwd = sc.driver.find_element_by_id(passwd_frame)
        el_passwd.click()
        sc.logger.info('输入QQ密码：%s', passwd)
        el_passwd.send_keys(passwd)

        el_qqlogin_list = sc.driver.find_elements_by_id(qq_login_id)

        for el_qq_login in el_qqlogin_list:
            if el_qq_login.text == '登录':
                sc.logger.info('点击“登录”按钮')
                time.sleep(1)
                el_qq_login.click()
                activity_main = 'com.quvideo.xiaoying/.XiaoYingActivity'
                sc.driver.wait_activity(activity_main, 10)
                break
        time.sleep(10)

        if TestUserLogin.login_judge() is True:
            return True
        return False

    @staticmethod
    def login_method(req_method, username, passwd):
        """定义带登录方法的登录方式，目前国内只支持三种."""
        method_list = ['weibo', 'wechat', 'qq']
        if req_method not in method_list:
            sc.logger.error('不支持的登录方式： %s', req_method)
            return False

        if req_method == 'qq':
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
            login_res = TestUserLogin.login_method('qq', username, passwd)

        assert login_res is not False
