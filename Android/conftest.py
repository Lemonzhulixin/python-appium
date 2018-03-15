# -*- coding: utf-8 -*-
"""pytest的资源初始化与销毁相关操作"""
from time import sleep
import pytest
from Android.script_params import driver


@pytest.fixture(scope='module', autouse=True)
def testcase_fixtrue(request):
    """初始化与销毁"""
    sleep(1)
    print('\nTestcase begin!')
    # driver.launch_app()
    driver.start_activity('com.quvideo.xiaoying', '.XiaoYingActivity')
    sleep(5)

    def testcase_teardown():
        """关闭app前，先等待2秒钟"""
        sleep(2)
        # driver.quit()
        driver.close_app()

        print('\nTestcase end!')
    request.addfinalizer(testcase_teardown)
