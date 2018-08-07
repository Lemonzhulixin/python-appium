# -*- coding: utf-8 -*-
"""创作页面素材中心的测试用例."""
from iOS import script_ultils as sc
import time
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements,base as ba
from selenium.common.exceptions import NoSuchElementException,TimeoutException


class TestTemplate(TestCase):
    """素材中心测试类."""

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

    def test_template_01_theme(self):
        """素材中心-主题."""
        sc.logger.info('素材中心-主题')
        fun_name = 'test_template_theme'

        ba.home_first_click('素材中心')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击顶部banner')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_accessibility_id(iOS_elements.el_banner)).click()

        sc.logger.info('返回')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda el: el.find_element_by_xpath('//XCUIElementTypeButton[@name="vivavideo com nav back n"]')).click()
        except TimeoutException:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda el: el.find_element_by_xpath('//XCUIElementTypeButton[@name="vivavideo back n"]')).click()

        sc.logger.info('点击“主题”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('主题')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载并使用主题')
        ba.material_used(iOS_elements.el_store_download1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加"视频"')
        ba.gallery_clip_add('视频', 2)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('取消限制弹窗')
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name(iOS_elements.el_cancel)).click()
        except TimeoutException:
            sc.logger.info('限制弹窗已取消')

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('素材中心')).click()

        sc.logger.info('点击“主题”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('主题')).click()

        sc.logger.info('删除下载的主题')
        ba.material_manager('主题', iOS_elements.el_store_del)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('素材中心-主题测试完成')

    def test_template_02_filter(self):
        """素材中心-滤镜."""
        sc.logger.info('素材中心-滤镜')
        fun_name = 'test_template_filter'

        sc.logger.info('点击“滤镜”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('滤镜')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载并使用滤镜')
        ba.material_used(iOS_elements.el_store_download2)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加"视频"')
        ba.gallery_clip_add('视频', 2)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('素材中心')).click()

        sc.logger.info('点击“滤镜”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('滤镜')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除下载的滤镜')
        ba.material_manager('滤镜', iOS_elements.el_store_del)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('素材中心-滤镜测试完成')

    def test_template_03_fx(self):
        """素材中心-特效."""
        sc.logger.info('素材中心-特效')
        fun_name = 'test_template_effect'

        sc.logger.info('点击“特效”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('特效')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载并使用特效')
        ba.material_used(iOS_elements.el_store_download1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加"视频"')
        ba.gallery_clip_add('视频', 2)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“确认”')
        ba.effect_add_confirm()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('素材中心')).click()

        sc.logger.info('点击“特效”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('特效')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除下载的特效')
        ba.material_manager('特效', iOS_elements.el_store_del)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('素材中心-特效测试完成')

    def test_template_04_font(self):
        """素材中心-字体."""
        sc.logger.info('素材中心-字体')
        fun_name = 'test_template_font'

        sc.logger.info('点击“字体”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('字体')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载并使用字体')
        ba.material_used(iOS_elements.el_store_download1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加"视频"')
        ba.gallery_clip_add('视频', 2)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“确认”')
        ba.effect_add_confirm()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('素材中心')).click()

        sc.logger.info('点击“字体”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('字体')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除下载的字体')
        ba.material_manager('字体', iOS_elements.el_store_del)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('素材中心-字体测试完成')

    def test_template_05_text(self):
        """素材中心-字幕."""
        sc.logger.info('素材中心-字幕')
        fun_name = 'test_template_text'

        sc.logger.info('点击“字幕”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('字幕')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载并使用字幕')
        ba.material_used(iOS_elements.el_store_download1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加"视频"')
        ba.gallery_clip_add('视频', 2)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“确认”')
        ba.effect_add_confirm()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('素材中心')).click()

        sc.logger.info('点击“字幕”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('字幕')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除下载的字幕')
        ba.material_manager('字幕', iOS_elements.el_store_del)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('素材中心-字幕测试完成')

    def test_template_06_sticker(self):
        """素材中心-动画贴纸."""
        sc.logger.info('素材中心-动画贴纸')
        fun_name = 'test_template_sticker'

        ba.home_first_click('素材中心')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('向上滑动')
        el_text = sc.driver.find_element_by_name("字幕")
        coord_x = el_text.location.get('x')
        coord_y = el_text.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'up', 0.5, 500)

        sc.logger.info('点击“动画贴纸”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('动画贴纸')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载并使用动画贴纸')
        ba.material_used(iOS_elements.el_store_download1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加"视频"')
        ba.gallery_clip_add('视频', 2)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“确认”')
        ba.effect_add_confirm()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('素材中心')).click()

        sc.logger.info('向上滑动')
        sc.swipe_by_ratio(coord_x, coord_y, 'up', 0.5, 500)

        sc.logger.info('点击“动画贴纸”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('动画贴纸')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除下载的动画贴纸')
        ba.material_manager('动画贴纸', iOS_elements.el_store_del)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('素材中心-动画贴纸测试完成')

    def test_template_07_gif(self):
        """素材中心-GIF."""
        sc.logger.info('素材中心-GIF')
        fun_name = 'test_template_gif'

        sc.logger.info('点击“动画贴纸”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('动画贴纸')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换到“GIF”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("GIF")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载并使用GIF贴纸')
        ba.material_used('下载')
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加"视频"')
        ba.gallery_clip_add('视频', 2)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“确认”')
        ba.effect_add_confirm()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('素材中心')).click()

        sc.logger.info('向上滑动')
        el_text = sc.driver.find_element_by_name("字幕")
        coord_x = el_text.location.get('x')
        coord_y = el_text.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'up', 0.7, 300)

        sc.logger.info('点击“动画贴纸”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('动画贴纸')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('切换到“GIF”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("GIF")).click()

        sc.logger.info('删除下载的GIF贴纸')
        ba.material_manager('GIF贴纸', '删除')
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('素材中心-GIF贴纸测试完成')

    def test_template_08_transition(self):
        """素材中心-转场."""
        sc.logger.info('素材中心-转场')
        fun_name = 'test_template_transition'
        start_x = self.width // 2
        start_y = self.height // 8
        start_bottom = self.height - start_y

        sc.logger.info('点击“转场”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('转场')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('向上滑动直到最底部')
        while True:
            try:
                sc.driver.find_element_by_name("没有更多了…").click()
                break
            except NoSuchElementException:
                sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 300)

        sc.logger.info('下载并使用转场')
        ba.material_used(iOS_elements.el_store_download1)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('添加"视频"')
        ba.gallery_clip_add('视频', 2)

        sc.logger.info('点击下一步进入预览页')
        ba.find_element_click('predicate', 10, iOS_elements.el_gallery_next)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('返回创作页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('素材中心')).click()

        sc.logger.info('向上滑动')
        el_text = sc.driver.find_element_by_name("字幕")
        coord_x = el_text.location.get('x')
        coord_y = el_text.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'up', 0.7, 500)

        sc.logger.info('点击“转场”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('转场')).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除下载的转场')
        ba.material_manager('转场', iOS_elements.el_store_del)
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('素材中心-动画贴纸测试完成')