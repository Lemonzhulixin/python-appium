# -*- coding: utf-8 -*-
"""特效的基本操作测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.webdriver.support.ui import WebDriverWait


class TestEditFX(TestCase):
    """特效的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_fx_01_add(self):
        """剪辑-特效-添加."""
        sc.logger.info('剪辑-特效-添加')
        fun_name = 'test_edit_fx_add'

        time.sleep(5)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"剪辑"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()

        sc.logger.info('向左滑动')
        start_x = self.width - self.width // 10
        start_bottom = self.height - self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 800)

        # sc.logger.info('点击"特效"')
        # try:
        #     sc.driver.find_element_by_name("特效").click()
        # except NoSuchElementException:
        #     sc.logger.info('未找到"特效"按钮，再向左滑动')
        #     sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 800)
        #     sc.driver.find_element_by_name("特效").click()
        # sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"特效"')
        el_sound = sc.driver.find_element_by_name('配音')
        coord_x = el_sound.location.get('x')
        coord_y = el_sound.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.8, 800)
        sc.driver.find_element_by_name("特效").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"添加"按钮')
        sc.driver.find_element_by_name("vivavideo tool fx add n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择一个"特效"下载')
        el_fx_down = sc.driver.find_element_by_accessibility_id("vivavideo_tool_camera_download_n")
        el_fx_down.click()

        sc.logger.info('选择一个"特效"使用')
        try:
            WebDriverWait(sc.driver,20).until(
                lambda el_fx_use:el_fx_use.find_element_by_xpath(
                    "//*/XCUIElementTypeOther[5]//*/XCUIElementTypeOther/XCUIElementTypeImage"))
            el_fx = sc.driver.find_element_by_xpath(
                "//*/XCUIElementTypeOther[5]//*/XCUIElementTypeOther/XCUIElementTypeImage")
            el_fx.click()
            sc.capture_screen(fun_name, self.img_path)
        except Exception as e:
            sc.logger.info('下载"贴纸"失败', e)
            return False

        sc.logger.info('点击下载更多')
        sc.driver.find_element_by_name("vivavideo tool subtitle store ").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回贴纸添加页面')
        sc.driver.find_element_by_name('vivavideo com nav back n').click()

        sc.logger.info('点击右上角保存')
        el_ok_btn = sc.driver.find_element_by_name("xiaoying com ok")
        for i in range(2):
            el_ok_btn.click()
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_edit_fx_02_del(self):
        """剪辑-特效-删除."""
        sc.logger.info('剪辑-特效-删除')
        fun_name = 'test_edit_fx_del'

        time.sleep(5)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"剪辑"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()

        sc.logger.info('向左滑动')
        start_x = self.width - self.width // 10
        start_bottom = self.height - self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.8, 800)

        sc.logger.info('点击"特效"')
        el_sound = sc.driver.find_element_by_name('配音')
        coord_x = el_sound.location.get('x')
        coord_y = el_sound.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.8, 800)
        sc.driver.find_element_by_name("特效").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('向左滑动到添加fx片段位置')
        fx_edit_x = self.width - self.width // 4
        fx_edit_y = self.height - self.height // 4
        sc.swipe_by_ratio(fx_edit_x, fx_edit_y, 'left', 0.1, 500)

        sc.logger.info('点击编辑按钮')
        sc.driver.find_element_by_name("vivavideo tool fx edit n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击删除按钮')
        sc.driver.find_element_by_name("vivavideo tool subtitle delete").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_name("xiaoying com ok").click()

    def test_edit_fx_03_cancel(self):
        """剪辑-特效-放弃."""
        sc.logger.info('剪辑-特效-放弃')
        fun_name = 'test_edit_fx_cancel'

        sc.logger.info('点击“特效”')
        time.sleep(1)
        sc.driver.find_element_by_name("特效").click()

        sc.logger.info('点击"添加"按钮')
        sc.driver.find_element_by_name("vivavideo tool fx add n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择一个"特效"使用')
        el_fx = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[5]//*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_fx.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角保存')
        sc.driver.find_element_by_name("xiaoying com ok").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“左上角X”取消')
        sc.driver.find_element_by_name("xiaoying com cancel").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认取消')
        sc.driver.find_element_by_name("确认").click()
        time.sleep(3)

        sc.logger.info('存草稿并返回创作页首页')
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()