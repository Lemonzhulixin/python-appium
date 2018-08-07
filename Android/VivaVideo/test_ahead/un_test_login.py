# -*- coding: utf-8 -*-
"""用户空间登录的测试用例."""
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestUserLogin(object):
    """用户空间登录测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]
    p_btn = 'com.quvideo.xiaoying:id/img_studio'

    def test_login_origin(self):
        """测试登录页面未登录时的初始状态."""
        sc.logger.info('登录页面初始状态检查测试开始')
        fun_name = 'test_login_origin'

        sc.logger.info('点击个人中心主按钮')
        if sc.first_step(self.p_btn) is True:
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)
            assert True
        else:
            assert False

    @staticmethod
    def login_judge():
        """判断是否已经登录."""
        log_btn = 'com.quvideo.xiaoying:id/btn_v6_login'
        try:
            el_login = WebDriverWait(sc.driver, 5, 1).until(
                                     lambda el: el.find_element_by_id(log_btn))
        except TimeoutException:
            sc.logger.info('未找到“登录/注册”按钮，用户已经登录')
            return True
        else:
            sc.logger.info('找到“登录/注册”按钮，用户未登录')
            return el_login

    @staticmethod
    def qq_login(username, passwd):
        """使用qq登录."""
        sc.logger.info('跳转到QQ登录页面')

        """
        qq_login_id = 'com.tencent.mobileqq:id/name'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(qq_login_id)).click()
        el_qqlogin_list = sc.driver.find_elements_by_id(qq_login_id)

        for el_qq_login in el_qqlogin_list:
            if el_qq_login.text == '添加帐号':
                sc.logger.info('点击“添加帐号”按钮')
                el_qq_login.click()
                break
        """

        # 如果本地QQ未登录，会出现先登录QQ的界面，所以分两种情况处理
        passwd_frame = 'com.tencent.mobileqq:id/password'

        # 本地QQ已经登录的情况
        try:
            """
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_android_uiautomator(
                    'text("添加帐号")')).click()
            """
            qq_login_id = 'com.tencent.mobileqq:id/name'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda c_btn: c_btn.find_element_by_id(qq_login_id)).click()
            el_qqlogin_list = sc.driver.find_elements_by_id(qq_login_id)

            for el_qq_login in el_qqlogin_list:
                if el_qq_login.text == '添加帐号':
                    sc.logger.info('点击“添加帐号”按钮')
                    el_qq_login.click()
                    break

            account_frame = 'com.tencent.mobileqq:id/account'
            el_account = WebDriverWait(sc.driver, 5, 1).until(
                            lambda el: el.find_element_by_id(account_frame))
        # 本地QQ未登录的情况
        except TimeoutException:
            account_frame_n = 'android.widget.EditText'
            el_account = WebDriverWait(sc.driver, 5, 1).until(
                            lambda el: el.find_element_by_class_name(
                                account_frame_n))

        el_account.clear()
        sc.logger.info('输入QQ账号：%s', username)
        el_account.send_keys(username)

        WebDriverWait(sc.driver, 5, 1).until(
            lambda c_btn: c_btn.find_element_by_id(passwd_frame))
        el_passwd = sc.driver.find_element_by_id(passwd_frame)
        sc.logger.info('输入QQ密码：%s', passwd)
        el_passwd.send_keys(passwd)

        qq_log_btn = 'android.widget.Button'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_class_name(qq_log_btn)).click()

        activity_main = 'com.quvideo.xiaoying/.XiaoYingActivity'
        sc.driver.wait_activity(activity_main, 10, 2)

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
            qq_btn = 'com.quvideo.xiaoying:id/tv_login_qq_text'
            WebDriverWait(sc.driver, 5, 1).until(
                          lambda el: el.find_element_by_id(qq_btn)).click()
            return TestUserLogin.qq_login(username, passwd)
        else:
            return False

    def test_login_qq(self):
        """国内用户测试使用qq登录."""
        sc.logger.info('登录页面QQ登录测试开始')
        sc.first_step(self.p_btn)

        login_res = TestUserLogin.login_judge()
        if login_res is True:
            assert True
        else:
            sc.logger.info('点击“注册/登录”按钮')
            login_res.click()
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_android_uiautomator(
                    'text("使用其他账号登录")')).click()
            # username = '1813326733'
            username = '2032083590'
            # passwd = 'qa123456'
            passwd = 'qqqqaaaa'
            login_res = TestUserLogin.login_method('qq', username, passwd)

        assert login_res is not False
