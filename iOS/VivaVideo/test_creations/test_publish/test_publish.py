# -*- coding: utf-8 -*-
"""发布页面内分享相关的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class TestPublishEdit(TestCase):
    """发布页面内分享相关的测试类.

    1.表情/话题/位置控件获取不到，需要再调"""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_01_topic(self):
        """发布页-添加话题."""
        sc.logger.info('发布页-添加话题')
        fun_name = 'test_edit_topic'

        time.sleep(5)
        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(0.5)

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()

        # sc.logger.info('点击"添加话题"')
        # el_title = sc.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeButton'")
        # print(len(el_title))
        # for el in el_title:
        #     if el.text == u' 添加话题':
        #         el.click()
        #         break
        # time.sleep(1)
        # sc.capture_screen(fun_name, self.img_path)

        # sc.logger.info('添加一个推荐话题')
        # el_topic = sc.driver.find_element_by_ios_predicate("type == 'XCUIElementTypeCell'")
        # el_topic.click()
        # sc.capture_screen(fun_name,self.img_path)
        #
        # sc.logger.info('再次点击"添加话题"')
        # sc.driver.find_element_by_name("添加话题").click()
        # time.sleep(0.5)
        #
        # sc.logger.info('点击"搜索话题"')
        # el_search_topic = sc.driver.find_element_by_ios_predicate(
        #     "type == 'XCUIElementTypeTextField' AND value == '搜索话题'")
        # el_search_topic.clear()
        # el_search_topic.send_keys("vlog")
        # sc.capture_screen(fun_name,self.img_path)
        #
        # sc.logger.info('选择任意一个搜索结果')
        # el_topic = sc.driver.find_element_by_ios_predicate("type == 'XCUIElementTypeCell'")
        # el_topic.click()
        # sc.capture_screen(fun_name, self.img_path)

    # def test_edit_02_loc(self):
    #     """发布页-显示位置."""
    #     sc.logger.info('发布页-显示位置')
    #     fun_name = 'test_edit_loc'
    #
    #     time.sleep(1)
    #     sc.logger.info('点击"显示位置"')
    #     time.sleep(5)
    #
    #     sc.logger.info('点击"添加自定义位置"')
    #     el_search_loc = sc.driver.find_element_by_ios_predicate(
    #         "type == 'XCUIElementTypeTextField' AND value == '添加自定义位置'")
    #     el_search_loc.clear()
    #     el_search_loc.send_keys("HangZhou")
    #     sc.capture_screen(fun_name, self.img_path)
    #
    #     sc.logger.info('确定使用"添加的自定义位置"')
    #     sc.driver.find_element_by_name("添加").click()
    #     sc.capture_screen(fun_name,self.img_path)
    #
    def test_edit_03_privacy(self):
        """发布页-隐私设置."""
        sc.logger.info('发布页-隐私设置')
        fun_name = 'test_edit_privacy'

        time.sleep(1)
        sc.logger.info('点击"隐私设置"')
        sc.driver.find_element_by_name("隐私设置").click()

        sc.logger.info('设置"隐私设置"')
        el_privacy = sc.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeSwitch'")
        for i in range(len(el_privacy)):
            el_privacy[i].click()
            sc.capture_screen(fun_name,self.img_path)
            try:
                sc.driver.find_element_by_name("我知道了").click()
            except NoSuchElementException:
                sc.logger.info('不是第一次设置，无设置提示')

        sc.logger.info('保存"隐私设置"')
        sc.driver.find_element_by_name("完成").click()

    # def test_edit_04_emoji(self):
    #     """发布页-添加表情."""
    #     sc.logger.info('发布页-添加表情')
    #     fun_name = 'test_edit_emoji'
    #
    #     sc.logger.info('点击"表情"')
    #     try:
    #         sc.driver.find_element_by_name("vivavideo icon face").click()
    #         sc.capture_screen(fun_name, self.img_path)
    #     except NoSuchElementException:
    #         sc.logger.info('已经在"表情"页面')
    #
    #     sc.logger.info('添加第一个"表情"')
    #     sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='😀']").click()
    #
    #     sc.logger.info('添加第二个"表情"')
    #     sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='😁']").click()
    #     sc.capture_screen(fun_name,self.img_path)
    #
    #     sc.logger.info('回删一个"表情"')
    #     sc.driver.find_element_by_name("vivavideo video delete n").click()
    #     sc.capture_screen(fun_name, self.img_path)
    #
    #     sc.logger.info('切回"keyboard"')
    #     sc.driver.find_element_by_name("vivavideo icon keyboard").click()
    #     sc.capture_screen(fun_name, self.img_path)
    #
    def test_edit_05_publish(self):
        """发布页-发布."""
        sc.logger.info('发布页-发布')
        fun_name = 'test_edit_publish'

        sc.logger.info('清空标题')
        el_title_clear = sc.driver.find_element_by_xpath("//*/XCUIElementTypeScrollView/XCUIElementTypeTextView")
        el_title_clear.clear()

        sc.logger.info('空标题发布')
        sc.driver.find_element_by_name("保存/上传").click()
        sc.capture_screen(fun_name,self.img_path)
        time.sleep(0.5)

        sc.logger.info('输入标题')
        el_title = sc.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='请输入标题，你的作品记录了什么？']")
        el_title.clear()
        el_title.send_keys('input video title test')
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('输入描述')
        el_des = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[1]/XCUIElementTypeTextView")
        el_des.clear()
        el_des.send_keys("input description text")
        time.sleep(0.5)
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='Done']").click()
        except NoSuchElementException:
            sc.logger.info("当前键盘为中文键盘")
            sc.driver.find_element_by_xpath("完成").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('发布')
        sc.driver.find_element_by_name("保存/上传").click()

        sc.logger.info('选择480P导出')
        sc.driver.find_element_by_name("清晰 480P").click()

        sc.logger.info('开始导出并上传')
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda V_exprot: V_exprot.find_element_by_name('发现'))
            sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('点击"我"查看发布的视频')
            sc.driver.find_element_by_name("我").click()  # 个人页
            time.sleep(2)
            sc.capture_screen(fun_name,self.img_path)
        except Exception as e:
            sc.logger.error('发布失败',e)
            return False