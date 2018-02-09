# -*- coding: utf-8 -*-
from unittest import TestCase
from iOS import script_ultils as sc
import time
from selenium.common.exceptions import NoSuchElementException


class Settings(TestCase):
    # 获取屏幕尺寸
    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_settings_01_net(self):
        """设置-网络设置"""
        fun_name = 'test_settings_net'

        time.sleep(5)
        sc.logger.info("进入设置页面")
        sc.driver.find_element_by_name("我").click()  # 个人页
        sc.driver.find_element_by_name("vivavideo setting p").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info("网络设置")
        sc.driver.find_element_by_name("只在WIFI网络上传/下载视频").click()

        sc.logger.info("自动播放设置")
        sc.driver.find_element_by_name("自动播放设置").click()
        sc.driver.find_element_by_name("不自动播放").click()
        sc.driver.find_element_by_name("仅在wifi环境下").click()
        sc.driver.find_element_by_name("在wifi和移动网络环境下").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("返回设置页面")
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info("接收通知推送")
        sc.driver.find_element_by_name("接收通知推送").click()
        el_push_message = sc.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeImage'")
        for el in el_push_message:
            el.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("返回设置页面")
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_settings_02_privacy(self):
        """设置-隐私设置"""
        fun_name = 'test_settings_privacy'

        sc.logger.info("设置私信权限")
        sc.driver.find_element_by_name("私信权限").click()
        sc.driver.find_element_by_name("所有人").click()
        sc.driver.find_element_by_name("我关注的人").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("返回设置页面")
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info("查看黑名单")
        sc.driver.find_element_by_name("黑名单").click()
        time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("返回设置页面")
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info("隐私账号设置")
        try:
            sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[3]/XCUIElementTypeImage").click()
        except NoSuchElementException:
            sc.logger.info("隐私账号设置已开启")
        sc.capture_screen(fun_name,self.img_path)

    def test_settings_03_feedback(self):
        """设置-意见反馈"""
        fun_name = 'test_settings_feedback'

        sc.logger.info("意见反馈")
        # width = sp.get_window_size()['width']
        # heightt = sp.get_window_size()['heightt']
        # sp.swipe(width / 2, heightt * 9 / 10, width / 2, heightt * 1 / 10, 500)

        start_x = self.width // 2
        start_bottom = self.height - self.height // 10
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.8, 500)

        sc.logger.info("进入反馈页面")
        sc.driver.find_element_by_name("意见反馈").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("新建反馈")
        sc.driver.find_element_by_name("+ 新建反馈").click()
        time.sleep(2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("填写问题")
        el_question = sc.driver.find_element_by_ios_predicate("type == 'XCUIElementTypeTextView'")
        el_question.clear()
        el_question.send_keys("just for ios test")
        time.sleep(1)
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Done']").click()
        except NoSuchElementException:
            sc.logger.info("当前键盘为中文键盘")
            sc.driver.find_element_by_xpath("完成").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("选择问题分类")
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo_common_pulldown_n").click()
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.2, 500)
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='完成']").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("提供截图")
        sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='icon_add_nrm']").click()
        time.sleep(1)
        sc.driver.find_element_by_name("取消").click()

        sc.logger.info("输入联系方式")
        el_contact = sc.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeTextField'")
        for contact in el_contact:
            if contact.text == u'QQ':
                contact.send_keys("245603638")
                break

        for contact in el_contact:
            if contact.text == u'手机号':
                contact.send_keys("15857154810")
                break

        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info("提交反馈")
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Done']").click()
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='提交']").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_settings_04_other(self):
        """设置-其他设置"""
        fun_name = 'test_settings_other'

        sc.logger.info("其他设置")
        start_x = self.width // 2
        start_bottom = self.height - self.height // 10
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.8, 500)

        sc.logger.info('关于小影')
        sc.driver.find_element_by_name("关于小影").click()
        sc.driver.find_element_by_name("vivavideo aboutxiaoying back n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('赏个好评')
        sc.driver.find_element_by_name("赏个好评，支持我们").click()
        time.sleep(2)
        sc.capture_screen(fun_name, self.img_path)
        try:
            sc.driver.find_element_by_name("以后").click()
        except NoSuchElementException:
            sc.logger.info("非正式版本，无法跳转苹果商店")

        sc.logger.info('成为VIP会员')
        sc.driver.find_element_by_name("成为VIP会员").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("icon close n").click()

        sc.logger.info('恢复购买')
        sc.driver.find_element_by_name("恢复购买").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("取消").click()

        sc.logger.info('推荐小影给好友')
        sc.driver.find_element_by_name("推荐小影给好友").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='xiaoying sns icon small qq nor']").click()
        time.sleep(2)
        sc.driver.find_element_by_name("我的电脑").click()
        sc.driver.find_element_by_name("发送").click()
        time.sleep(2)
        sc.driver.find_element_by_name("返回小影").click()

        sc.logger.info('清除缓存')
        sc.driver.find_element_by_name("清除缓存").click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_name("取消").click()

        sc.driver.find_element_by_name("清除缓存").click()
        sc.driver.find_element_by_name("清除缓存").click()