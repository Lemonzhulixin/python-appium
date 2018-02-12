# -*- coding: utf-8 -*-
"""动画贴纸的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException


class TestEditSticker(TestCase):
    """动画贴纸的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_sticker_add(self):
        """剪辑-动画贴纸-添加."""
        sc.logger.info('剪辑-动画贴纸-添加')
        fun_name = 'test_edit_sticker_add'

        time.sleep(5)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"剪辑"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()

        sc.logger.info('向左滑动')
        el_collage = sc.driver.find_element_by_name("画中画")
        coord_x = el_collage.location.get('x')
        coord_y = el_collage.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.6, 800)  # 从转场向左滑动

        sc.logger.info('点击"动画贴纸"')
        sc.driver.find_element_by_name("动画贴纸").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"添加"按钮')
        sc.driver.find_element_by_name("vivavideo tool sticker add n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('选择一个"贴纸"添加')
        el_sticker = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_sticker.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('镜像"贴纸"')
        sc.driver.find_element_by_accessibility_id(
            "XiaoYingResource.bundle/vivavideo_tool_subtitle_flip_n").click()

        sc.logger.info('切换"贴纸"分类')
        el_sticker_type = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[1]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_sticker_type.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载该分类"贴纸"')
        try:
            sc.driver.find_element_by_name("免费下载").click()
        except NoSuchElementException:
            sc.logger.info('该分类"贴纸"已下载')

        sc.logger.info('点击GIF图标')
        sc.driver.find_element_by_name("GIF").click()
        time.sleep(3)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回贴纸添加页面')
        sc.driver.find_element_by_name('vivavideo com nav back n').click()

        sc.logger.info('点击下载更多')
        sc.driver.find_element_by_name("xiaoying itembar down more").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回贴纸添加页面')
        sc.driver.find_element_by_name('vivavideo com nav back n').click()

        sc.logger.info('点击右上角保存')
        el_ok_btn = sc.driver.find_element_by_name("xiaoying com ok")
        for i in range(2):
            el_ok_btn.click()
            sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_edit_sticker_cancel(self):
        """剪辑-动画贴纸-放弃."""
        sc.logger.info('剪辑-动画贴纸-放弃')
        fun_name = 'test_edit_sticker_cancel'

        time.sleep(1)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"剪辑"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()

        sc.logger.info('向左滑动')
        el_collage = sc.driver.find_element_by_name("画中画")
        coord_x = el_collage.location.get('x')
        coord_y = el_collage.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.6, 800)  # 从转场向左滑动

        sc.logger.info('点击"动画贴纸"')
        sc.driver.find_element_by_name("动画贴纸").click()

        sc.logger.info('点击"添加"按钮')
        sc.driver.find_element_by_name("vivavideo tool sticker add n").click()

        sc.logger.info('点击右上角保存')
        sc.driver.find_element_by_name("xiaoying com ok").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('放弃编辑')
        sc.driver.find_element_by_name("xiaoying com cancel").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"确认"放弃添加')
        sc.driver.find_element_by_name("确认").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(3)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()