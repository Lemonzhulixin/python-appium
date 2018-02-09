# -*- coding: utf-8 -*-
"""pytest的资源初始化与销毁相关操作"""
from time import sleep
import pytest
from Android.script_params import driver


@pytest.fixture(scope='session', autouse=True)
def testcase_fixtrue(request):
    """初始化与销毁"""
    print('\nTestcase begin!')

    def testcase_teardown():
        """webdriver 退出前，先等待10秒钟"""
        sleep(10)
        driver.quit()
        print('\nTestcase end!')
    request.addfinalizer(testcase_teardown)
