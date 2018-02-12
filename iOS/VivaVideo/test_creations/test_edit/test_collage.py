# -*- coding: utf-8 -*-
"""编辑页面画中画的基本操作测试用例."""
import time
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException


class TestEditCollage(TestCase):
    """编辑页面画中画的基本操作测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_edit_collage_01_img(self):
        """剪辑-画中画-图片添加."""
        sc.logger.info('剪辑-画中画-图片添加')
        fun_name = 'test_edit_collage_img'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"画中画"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("画中画").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('**************添加第一张图片**************')
        sc.logger.info('点击添加按钮')
        sc.driver.find_element_by_name("vivavideo editor collage add n").click()

        sc.logger.info('点击"其他相册"')
        sc.driver.find_element_by_name("其他相册").click()

        sc.logger.info('返回画中画')
        sc.driver.find_element_by_name("vivavideo gallery back n").click()

        sc.logger.info('选择一个"图片"添加')
        el_comm = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[1]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_comm.click()

        sc.logger.info('镜像"图片"')
        sc.driver.find_element_by_accessibility_id(
            "XiaoYingResource.bundle/vivavideo_tool_subtitle_flip_n").click()

        sc.logger.info('点击右上角保存')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()

        sc.logger.info('点击左侧"暂停"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar paus").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击底部"确认"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar comp").click()
        sc.capture_screen(fun_name, self.img_path)

    def test_edit_collage_02_gif(self):
        """剪辑-画中画-gif图片添加."""
        sc.logger.info('剪辑-画中画-gif图片添加')
        fun_name = 'test_edit_collage_gif'

        time.sleep(1)
        sc.logger.info('**************添加第二张图片**************')
        sc.logger.info('点击添加按钮')
        sc.driver.find_element_by_name("vivavideo editor collage add n").click()

        sc.logger.info('切换到GIF')
        sc.driver.find_element_by_name("GIF").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('搜索GIF图片')
        el_search = sc.driver.find_element_by_ios_predicate(
            "type == 'XCUIElementTypeTextField' AND value == '搜索Gif'")
        el_search.clear()
        el_search.send_keys('a')
        sc.driver.find_element_by_accessibility_id("Search").click()
        time.sleep(5)
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('检查GIF图片下载是否成功')
        try:
            WebDriverWait(sc.driver, 60).until(
                lambda gif: gif.find_element_by_accessibility_id("vivavideo_tool_collage_download_n"))
            el_gif_download = sc.driver.find_element_by_accessibility_id("vivavideo_tool_collage_download_n")
            el_gif_download.click()
            time.sleep(10)
            sc.capture_screen(fun_name, self.img_path)
        except Exception as e:
            sc.logger.error('GIF图片加载异常', e)
            sc.capture_screen(fun_name, self.img_path)
            return False

        sc.logger.info('使用该下载的GIF图片')
        el_gif_use = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_gif_use.click()
        time.sleep(5)

        sc.logger.info('镜像"GIF图片"')
        sc.driver.find_element_by_accessibility_id(
            "XiaoYingResource.bundle/vivavideo_tool_subtitle_flip_n").click()

        sc.logger.info('点击右上角保存')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()

        sc.logger.info('点击左侧"暂停"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar paus").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击底部"确认"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar comp").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_edit_collage_03_del(self):
        """剪辑-画中画-删除."""
        sc.logger.info('剪辑-画中画-删除')
        fun_name = 'test_edit_text_del'

        time.sleep(1)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"画中画"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("画中画").click()

        sc.logger.info('点击已添加的"图片"')
        time.sleep(1)
        sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击删除按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar dele").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击右上角确认按钮')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_edit_collage_04_cancel(self):
        """剪辑-画中画-放弃."""
        sc.logger.info('剪辑-画中画-放弃')
        fun_name = 'test_edit_collage_cancel'

        time.sleep(1)
        sc.logger.info('点击首页第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        sc.logger.info('点击"画中画"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("画中画").click()

        sc.logger.info('点击添加按钮')
        sc.driver.find_element_by_name("vivavideo editor collage add n").click()

        sc.logger.info('选择一个"图片"添加')
        el_comm = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeCollectionView[1]/*/XCUIElementTypeOther/XCUIElementTypeImage")
        el_comm.click()

        sc.logger.info('点击右上角保存')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()

        sc.logger.info('点击左侧"暂停"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar paus").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左侧"撤销"按钮')
        sc.driver.find_element_by_name("vivavideo editor framebar undo").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('放弃编辑')
        sc.driver.find_element_by_name("vivavideo editor common cancel").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"确认"放弃添加')
        sc.driver.find_element_by_name("确认").click()

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(3)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('返回创作中心主界面')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()