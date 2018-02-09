# -*- coding: utf-8 -*-
"""封面编辑相关的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException


class TestCoverSticker(TestCase):
    """封面编辑相关的测试用例类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_sticker_01_use(self):
        """更换封面-使用贴纸."""
        sc.logger.info('更换封面-使用贴纸')
        fun_name = 'test_sticker_use'

        time.sleep(5)
        sc.logger.info('进入我的工作室')
        sc.driver.find_element_by_name("更多草稿").click()
        time.sleep(0.5)

        sc.logger.info('保存并上传')
        el_publish = sc.driver.find_element_by_name("保存/上传")
        el_publish.click()

        sc.logger.info('点击"更换封面"')
        sc.driver.find_element_by_name("更换封面").click()
        time.sleep(3)

        sc.logger.info('点击"封面贴纸"图标')
        sc.driver.find_element_by_name("cover tool preview sticker n").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加一个贴纸')
        el_sticker_select = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_sticker_select.click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('切换贴纸分类')
        el_sticker_type = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[1]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_sticker_type.click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('保存已添加的封面贴纸')
        sc.driver.find_element_by_name("xiaoying itembar finish").click()
        time.sleep(0.5)
        sc.driver.find_element_by_name("vivavideo editor common ok").click()
        sc.capture_screen(fun_name, self.img_path)

    def test_sticker_02_download(self):
        """更换封面-下载贴纸."""
        sc.logger.info('更换封面-下载贴纸')
        fun_name = 'test_sticker_download'

        time.sleep(1)
        sc.logger.info('点击"更换封面"')
        sc.driver.find_element_by_name("更换封面").click()
        time.sleep(3)

        sc.logger.info('点击"封面贴纸"图标')
        sc.driver.find_element_by_name("cover tool preview sticker n").click()

        sc.logger.info('点击"GIF"图标')
        sc.driver.find_element_by_name("GIF").click()
        time.sleep(5)
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('下载"GIF"贴纸')
        sc.driver.find_element_by_name("下载").click()
        time.sleep(5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('使用"GIF"贴纸')
        sc.driver.find_element_by_name("使用").click()
        time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"下载更多"动画贴纸')
        sc.driver.find_element_by_name("xiaoying itembar down more").click()
        time.sleep(1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"下载"')
        el_sticker_download= sc.driver.find_element_by_name("vivavideo material download n")
        el_sticker_download.click()
        time.sleep(10)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('使用"动画贴纸"')
        el_sticker_use = sc.driver.find_element_by_name("使用")
        try:
            el_sticker_use.click()
            time.sleep(0.5)
        except NoSuchElementException:
            sc.logger.info('动画贴纸下载未完成，继续等待5s')
            time.sleep(5)
            el_sticker_use.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('保存已添加的封面贴纸')
        sc.driver.find_element_by_name("xiaoying itembar finish").click()
        time.sleep(0.5)
        sc.driver.find_element_by_name("vivavideo editor common ok").click()
        sc.capture_screen(fun_name,self.img_path)

    def test_sticker_03_edit(self):
        """更换封面-编辑添加的贴纸."""
        sc.logger.info('更换封面-编辑添加的贴纸')
        fun_name = 'test_sticker_edit'

        time.sleep(1)
        sc.logger.info('点击"更换封面"')
        sc.driver.find_element_by_name("更换封面").click()
        time.sleep(3)

        sc.logger.info('点击"封面贴纸"图标')
        sc.driver.find_element_by_name("cover tool preview sticker n").click()

        sc.logger.info('添加一个贴纸')
        el_sticker_select = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_sticker_select.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('360度镜像贴纸')
        el_mirror = sc.driver.find_element_by_xpath(
            "//XCUIElementTypeImage[@name='XiaoYingResource.bundle/vivavideo_tool_subtitle_flip_n']")
        for i in range(4):
            el_mirror.click()
            sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('删除刚刚添加的贴纸')
        el_sticker_del = sc.driver.find_element_by_xpath(
            "//XCUIElementTypeImage[@name='XiaoYingResource.bundle/xiaoying_subtitle_delete']")
        el_sticker_del.click()

        sc.logger.info('放弃编辑的封面贴纸')
        sc.driver.find_element_by_name("xiaoying itembar close").click()
        sc.driver.find_element_by_name("vivavideo editor common cancel").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()