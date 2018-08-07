# -*- coding: utf-8 -*-
"""创作页面内导出视频相关的测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException,NoSuchElementException

class TestCreationExport(TestCase):
    """
    创作页面内导出视频相关的测试类.

    1.执行导出用例时，请确认当前app未进行过导出操作
    2.使用已购买会员账号登录
    """

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

    def test_export_01_480P(self):
        """导出-保存到相册-480P-首次导出."""
        sc.logger.info('导出-保存到相册-480P-首次导出')
        fun_name = 'test_export_first'

        sc.logger.info('点击创作中心主按钮')
        ba.home_enter()

        sc.logger.info('点击“保存到相册”')
        ba.export_to_album()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“480P 清晰”')
        ba.export_video("清晰 480P")
        sc.logger.info('导出-保存到相册-480P-首次导出测试完成')

    def test_export_02_720P(self):
        """导出-保存到相册-720P-二次导出."""
        sc.logger.info('导出-保存到相册-720P-二次导出')
        fun_name = 'test_export_second'

        try:
            sc.logger.info('消除评论弹窗')
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name('稍后再说')).click()
        except TimeoutException:
            sc.logger.info('评论弹窗未弹出')

        sc.logger.info('点击“保存到相册”')
        ba.export_to_album()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“高清 720P”')
        ba.export_video("高清 720P")
        sc.logger.info('导出-保存到相册-720P-二次导出测试完成')

    def test_export_03_1080P(self):
        """导出-保存到相册-1080P-三次导出."""
        sc.logger.info('导出-保存到相册-1080P')
        fun_name = 'test_export_third'

        sc.logger.info('点击“保存到相册”')
        ba.export_to_album()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“超清 1080P”')
        ba.export_video("超清 1080P")
        sc.logger.info('导出-保存到相册-1080P测试完成')

    def test_export_04_gif(self):
        """导出-保存到相册-GIF."""
        sc.logger.info('导出-保存到相册-GIF')
        fun_name = 'test_export_gif'

        sc.logger.info('点击“保存到相册”')
        ba.export_to_album()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“GIF”')
        ba.export_gif('320P','10F/s')
        sc.logger.info('导出-保存到相册-GIF测试完成')
