# -*- coding: utf-8 -*-
"""创作页面素材中心的测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase
from iOS import script_ultils as sc


class TestCreationTemplate(TestCase):
    """创作页面素材中心测试类.
    滤镜-下载："vivavideo material download2 n"
    其他-下载："vivavideo material download n"
    gif-下载："下载"
    其他-删除："vivavideo material delete n"
    gif-删除："删除"
    管理："vivavideo material Management "
    """

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @classmethod
    def template_download(cls, type, el_download):
        """素材下载."""
        sc.logger.info('%s下载测试', type)

        fun_name = 'template_download'

        sc.logger.info('开始下载')
        el_template_down = sc.driver.find_element_by_name(el_download)
        try:
            sc.logger.info('点击“下载”按钮')
            el_template_down.click()
            sc.capture_screen(fun_name, cls.img_path)
        except NoSuchElementException:
            sc.logger.info('当前页面所有素材已下载完成')
            return True

        sc.logger.info('检查素材下载是否成功')
        try:
            WebDriverWait(sc.driver, 30).until(
                lambda theme_use: theme_use.find_element_by_name("使用"))
            sc.capture_screen(fun_name, cls.img_path)
        except TimeoutError as t:
            sc.logger.error('素材下载超时', t)
            return False
        except Exception as e:
            sc.logger.error('素材下载失败', e)
            return False

        sc.logger.info('%s下载测试完成', type)

    @classmethod
    def template_use(cls, type):
        """使用素材并进入预览页测试."""
        sc.logger.info('%s使用素材并进入预览页测试', type)
        time.sleep(1)
        fun_name = 'template_use'

        sc.logger.info('点击“使用”按钮')
        try:
            el_template_use = sc.driver.find_element_by_name("使用")
            el_template_use.click()
        except NoSuchElementException:
            sc.logger.error('未找到已下载的素材')
            return False
        sc.capture_screen(fun_name, cls.img_path)

        sc.logger.info('添加视频')
        time.sleep(2)
        el_video = sc.driver.find_element_by_accessibility_id("vivavideo_tool_gallery_audio_type_video")
        el_video.click()
        sc.driver.find_element_by_name("添加 0").click()

        sc.logger.info('添加多张图片')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()
        el_imgs = sc.driver.find_elements_by_xpath("//*/XCUIElementTypeImage")
        i = 1
        while i < len(el_imgs):
            el_imgs[i].click()
            i = i + 1

        sc.logger.info('点击"下一步"')
        sc.driver.find_element_by_name("下一步").click()

        sc.logger.info('%s使用并进入预览页测试完成', type)

    @classmethod
    def theme_manager(cls, type, el_delete):
        """主题管理."""
        sc.logger.info('%s删除测试', type)
        fun_name = 'theme_manager'

        sc.driver.find_element_by_name("vivavideo material Management ").click()
        sc.capture_screen(fun_name, cls.img_path)

        el_template_del = sc.driver.find_element_by_name(el_delete)
        el_template_del.click()
        try:
            sc.driver.find_element_by_name("确认").click()
        except NoSuchElementException:
            sc.logger.info('%s删除不需要确认', type)
        sc.capture_screen(fun_name, cls.img_path)

        sc.logger.info('删除完成后，返回创作中心页面')
        el_back = sc.driver.find_element_by_name("vivavideo com nav back n")
        for i in range(3):
            time.sleep(1)
            el_back.click()

        sc.logger.info('%s删除测试完成', type)

    def test_template_01_theme(self):
        """素材中心-主题."""
        sc.logger.info('进入素材中心-主题')
        fun_name = 'test_template_theme'

        start_x = self.width - self.width // 5
        start_bottom = self.height // 2

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('点击"素材中心"')
        try:
            sc.driver.find_element_by_name("素材中心").click()
            sc.capture_screen(fun_name,self.img_path)
        except NoSuchElementException:
            sc.logger.info('"素材中心"在第二页，需要向左滑动')
            sc.swipe_by_ratio(start_x, start_bottom, 'left', 0.6, 500)
            sc.driver.find_element_by_name("素材中心").click()
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“主题”')
        time.sleep(0.5)
        sc.driver.find_element_by_name("主题").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载“主题”')
        btn_download = 'vivavideo material download n'
        self.template_download('主题', btn_download)

        sc.logger.info('使用“主题”')
        self.template_use('主题')
        time.sleep(2)

        sc.logger.info('点击“存草稿”按钮')
        sc.driver.find_element_by_name("存草稿").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('点击"主题"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("主题").click()

        sc.logger.info('删除下载的主题')
        btn_del = 'vivavideo material delete n'
        self.theme_manager('主题', btn_del)

    def test_template_02_filter(self):
        """素材中心-滤镜."""
        sc.logger.info('素材中心-滤镜')
        fun_name = 'test_template_filter'

        time.sleep(1)
        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('点击"滤镜"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("滤镜").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('下载“滤镜”')
        btn_download = 'vivavideo material download2 n'
        self.template_download('滤镜', btn_download)

        sc.logger.info('使用“滤镜”')
        self.template_use('滤镜')
        time.sleep(2)

        sc.logger.info('保存使用的滤镜')
        sc.driver.find_element_by_name("xiaoying com ok").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(1)
        sc.driver.find_element_by_name("存草稿").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('点击"滤镜"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("滤镜").click()

        sc.logger.info('删除下载的滤镜')
        btn_del = 'vivavideo material delete n'
        self.theme_manager('滤镜', btn_del)

    def test_template_03_effect(self):
        """素材中心-特效."""
        sc.logger.info('素材中心-特效')
        fun_name = 'test_template_effect'

        time.sleep(1)
        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('点击"特效"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("特效").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载“特效”')
        btn_download = 'vivavideo material download n'
        self.template_download('特效', btn_download)

        sc.logger.info('使用“特效”')
        self.template_use('特效')
        time.sleep(2)

        sc.logger.info('保存使用的特效')
        sc.driver.find_element_by_name("xiaoying com ok").click()
        time.sleep(1)
        sc.driver.find_element_by_name("xiaoying com ok").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(1)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('点击"特效"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("特效").click()

        sc.logger.info('删除下载的特效')
        btn_del = 'vivavideo material delete n'
        self.theme_manager('特效', btn_del)

    def test_template_04_font(self):
        """素材中心-字体."""
        sc.logger.info('素材中心-字体')
        fun_name = 'test_template_font'

        time.sleep(1)
        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('点击"字体"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("字体").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载“字体”')
        btn_download = 'vivavideo material download n'
        self.template_download('字体', btn_download)

        sc.logger.info('使用“字体”')
        self.template_use('字体')
        time.sleep(2)

        sc.logger.info('确认使用该下载的字体')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()
        time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('截取使用该字体的片段')
        try:
            WebDriverWait(sc.driver, 300).until(
                lambda theme_use: theme_use.find_element_by_name("vivavideo editor common ok"))
            sc.capture_screen(fun_name,self.img_path)
            sc.driver.find_element_by_name("vivavideo editor common ok").click()
        except TimeoutError as t:
            sc.logger.error('视频时长超出300s，尚未完成添加字幕，试一试使用时长较短的视频。', t)
            return False

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(1)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('点击"字体"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("字体").click()

        sc.logger.info('删除下载的字体')
        btn_del = 'vivavideo material delete n'
        self.theme_manager('字体', btn_del)

    def test_template_05_text(self):
        """素材中心-字幕."""
        sc.logger.info('素材中心-字幕')
        fun_name = 'test_template_text'

        time.sleep(1)
        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('向上滑动')
        start_x = self.width // 2
        start_bottom = self.height - self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"字幕"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("字幕").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载“字幕”')
        btn_download = 'vivavideo material download n'
        self.template_download('字幕', btn_download)

        sc.logger.info('使用“字幕”')
        self.template_use('字幕')
        time.sleep(2)

        sc.logger.info('确认使用该下载的字幕')
        sc.driver.find_element_by_name("vivavideo editor common ok").click()
        time.sleep(0.5)

        sc.logger.info('截取使用该字体的片段')
        try:
            WebDriverWait(sc.driver, 300).until(
                lambda theme_use: theme_use.find_element_by_name("vivavideo editor common ok"))
            sc.capture_screen(fun_name,self.img_path)
            sc.driver.find_element_by_name("vivavideo editor common ok").click()
        except TimeoutError as t:
            sc.logger.error('视频时长超出300s，尚未完成添加字幕，试一试使用时长较短的视频。', t)
            return False

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(1)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('向上滑动')
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)

        sc.logger.info('点击"字幕"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("字幕").click()

        sc.logger.info('删除下载的字幕')
        btn_del = 'vivavideo material delete n'
        self.theme_manager('字幕', btn_del)

    def test_template_06_sticker(self):
        """素材中心-动画贴纸."""
        sc.logger.info('素材中心-动画贴纸')
        fun_name = 'test_template_sticker'

        time.sleep(1)
        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('向上滑动')
        start_x = self.width // 2
        start_bottom = self.height - self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)

        sc.logger.info('点击"动画贴纸"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("动画贴纸").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载“动画贴纸”')
        btn_download = 'vivavideo material download n'
        self.template_download('动画贴纸', btn_download)

        sc.logger.info('使用“动画贴纸”')
        self.template_use('动画贴纸')
        time.sleep(2)

        sc.logger.info('确认使用该下载的贴纸')
        sc.driver.find_element_by_name("xiaoying com ok").click()
        time.sleep(0.5)
        sc.driver.find_element_by_name("xiaoying com ok").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(1)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('向上滑动')
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)

        sc.logger.info('点击"动画贴纸"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("动画贴纸").click()

        sc.logger.info('删除下载的贴纸')
        btn_del = 'vivavideo material delete n'
        self.theme_manager('动画贴纸', btn_del)

    def test_template_07_giphy(self):
        """GIPHY-下载."""
        sc.logger.info('素材中心-GIPHY')
        fun_name = 'test_template_giphy'

        time.sleep(1)
        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('向上滑动')
        start_x = self.width // 2
        start_bottom = self.height - self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)

        sc.logger.info('点击"动画贴纸"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("动画贴纸").click()

        sc.logger.info('切换到"GIF"分类')
        sc.driver.find_element_by_name("GIF").click()
        time.sleep(3)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载“GIF贴纸”')
        btn_download = '下载'
        self.template_download('GIF贴纸', btn_download)

        sc.logger.info('使用“GIF贴纸”')
        self.template_use('GIF贴纸')
        time.sleep(2)

        sc.logger.info('确认使用该下载的GIF贴纸')
        sc.driver.find_element_by_name("xiaoying com ok").click()
        time.sleep(0.5)
        sc.driver.find_element_by_name("xiaoying com ok").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(1)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('向上滑动')
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)

        sc.logger.info('点击"动画贴纸"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("动画贴纸").click()

        sc.logger.info('切换到"GIF"分类')
        sc.driver.find_element_by_name("GIF").click()
        time.sleep(3)

        sc.logger.info('删除下载的GIF贴纸')
        btn_del = '删除'
        self.theme_manager('GIF贴纸', btn_del)

    #转场下载按钮无法定位，请先至少下载一个转场再进行相关测试
    def test_template_08_transition(self):
        """素材中心-转场."""
        sc.logger.info('素材中心-转场')
        fun_name = 'test_template_transition'

        time.sleep(1)
        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('向上滑动')
        start_x = self.width // 2
        start_bottom = self.height - self.height // 5
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)

        sc.logger.info('点击"转场"')
        time.sleep(0.5)
        try:
            sc.driver.find_element_by_name("转场").click()
        except NoSuchElementException:
            sc.logger.info('仍需要上滑显示转场分类')
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)
            sc.driver.find_element_by_name("转场").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('下载“转场”')
        btn_download = 'vivavideo material download n'
        self.template_download('转场', btn_download)

        sc.logger.info('使用“转场”')
        self.template_use('转场')
        time.sleep(2)

        sc.logger.info('确认使用该下载的转场')
        sc.driver.find_element_by_name("xiaoying com ok").click()
        time.sleep(0.5)
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击“存草稿”按钮')
        time.sleep(1)
        sc.driver.find_element_by_name("存草稿").click()

        sc.logger.info('点击左上角返回按钮退回创作中心')
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

        sc.logger.info('点击"素材中心"')
        sc.driver.find_element_by_name("素材中心").click()

        sc.logger.info('向上滑动')
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)

        sc.logger.info('点击"转场"')
        time.sleep(0.5)
        sc.driver.find_element_by_name("转场").click()

        sc.logger.info('删除下载的转场')
        btn_del = 'vivavideo material delete n'
        self.theme_manager('转场', btn_del)