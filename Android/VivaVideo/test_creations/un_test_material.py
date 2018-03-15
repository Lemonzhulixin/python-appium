# -*- coding: utf-8 -*-
"""创作页面素材中心的测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestCreationTemplate(object):
    """创作页面素材中心测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    @classmethod
    def template_download(cls, type, download_id):
        """素材下载."""
        sc.logger.info('%s下载测试', type)

        """
        sc.logger.info('向下滑动')
        start_x = cls.width // 2
        start_bottom = cls.height - cls.height // 5
        while True:
            try:
                sc.driver.find_element_by_android_uiautomator('text("没有更多了…")').click()
                break
            except NoSuchElementException:
                sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 300)
        sc.logger.info('已经滑动到%s最底部了', type)
        """

        sc.logger.info('开始下载')
        el_template_down = sc.driver.find_element_by_id(download_id)
        try:
            el_template_down.click()
        except NoSuchElementException:
            sc.logger.info('当前页面所有素材已下载完成')
            el_template_use = sc.driver.find_elements_by_android_uiautomator('text("使用")')
            el_template_use.click()
            return True

        sc.logger.info('检查素材下载是否成功')
        try:
            WebDriverWait(sc.driver, 30).until(
                lambda theme_use: theme_use.find_element_by_android_uiautomator('text("使用")'))
        except TimeoutError as t:
            sc.logger.info('素材下载超时', t)
            return False
        except Exception as e:
            sc.logger.info('素材下载失败', e)
            return False

        sc.logger.info('%s下载测试完成', type)

    @classmethod
    def template_use(cls, type):
        """使用素材并进入预览页测试."""
        sc.logger.info('%s使用素材并进入预览页测试', type)
        time.sleep(1)
        fun_name = 'template_use'

        try:
            sc.logger.info('点击“使用”按钮')
            el_template_use = sc.driver.find_element_by_android_uiautomator('text("使用")')
            el_template_use.click()
        except NoSuchElementException:
            sc.logger.info('未找到已下载的素材')
            return False

        sc.capture_screen(fun_name, cls.img_path)
        el_videos = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/img_click_mask')
        for i in range(2):
            time.sleep(1)
            el_videos[i].click()
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_import').click()
            try:
                WebDriverWait(sc.driver, 60).until(
                    lambda V_improt: V_improt.find_element_by_android_uiautomator('text("下一步")'))
            except TimeoutError as t:
                sc.logger.error('导入视频超时', t)
                return False
            except Exception as e:
                sc.logger.error('导入视频出错', e)
                return False
        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()

        sc.logger.info('%s使用并进入预览页测试完成', type)

    @classmethod
    def theme_manager(cls, type, delete_id):
        """主题管理."""
        sc.logger.info('%s删除测试', type)
        fun_name = 'theme_manager'

        sc.capture_screen(fun_name, cls.img_path)
        try:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/text_right').click()
        except NoSuchElementException:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/right_mgr').click()
        sc.capture_screen(fun_name, cls.img_path)

        el_del_template = sc.driver.find_element_by_id(delete_id)
        el_del_template.click()
        try:
            sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        except NoSuchElementException:
            sc.logger.info('%s删除不需要确认', type)
        sc.capture_screen(fun_name, cls.img_path)
        sc.logger.info('返回创作中心页面')
        for i in range(3):
            time.sleep(1)
            sc.driver.press_keycode(4)

        sc.logger.info('%s删除测试完成', type)

    def test_template_theme(self):
        """素材中心-主题."""
        sc.logger.info('进入素材中心-主题')
        fun_name = 'test_template_theme'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“素材中心”')
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        sc.logger.info('点击“主题”')
        sc.driver.find_element_by_android_uiautomator('text("主题")').click()

        try:
            btn_download = 'com.quvideo.xiaoying:id/imgbtn_download'
            sc.driver.find_element_by_id(btn_download)
            self.template_download('主题', btn_download)
        except NoSuchElementException:
            sc.logger.info('此页素材已经下载完毕了')

        time.sleep(1)
        self.template_use('主题')
        time.sleep(5)

        sc.logger.info('点击“存草稿”')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        sc.logger.info('点击左上角返回创作中心主界面')
        time.sleep(2)
        sc.driver.press_keycode(4)
        time.sleep(2)

        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        sc.driver.find_element_by_android_uiautomator('text("主题")').click()

        sc.logger.info('删除刚刚下载的主题')
        sc.capture_screen(fun_name, self.img_path)
        self.theme_manager('主题', 'com.quvideo.xiaoying:id/template_caption_grid_btn_update')

    def test_template_subtitle(self):
        """素材中心-字幕."""
        sc.logger.info('素材中心-字幕')
        fun_name = 'test_template_subtitle'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“素材中心”')
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        sc.logger.info('点击“字幕”')
        sc.driver.find_element_by_android_uiautomator('text("字幕")').click()

        sc.logger.info('下载并使用字幕')
        try:
            btn_down = 'com.quvideo.xiaoying:id/template_pack_download_progress'
            sc.driver.find_element_by_id(btn_down)
            self.template_download('字幕', btn_down)
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger('字幕已经下载完毕了')
        self.template_use('字幕')
        time.sleep(5)

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        time.sleep(1)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        time.sleep(2)
        sc.logger.info('点击“存草稿”')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        time.sleep(2)
        sc.driver.press_keycode(4)

        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        sc.driver.find_element_by_android_uiautomator('text("字幕")').click()

        sc.logger.info('删除刚刚下载的字幕')
        sc.capture_screen(fun_name, self.img_path)
        self.theme_manager('字幕', 'com.quvideo.xiaoying:id/img_delete')

    def test_template_effect(self):
        """素材中心-特效."""
        sc.logger.info('素材中心-特效')
        fun_name = 'test_template_effect'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“素材中心”')
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        sc.logger.info('点击“特效”')
        sc.driver.find_element_by_android_uiautomator('text("特效")').click()

        self.template_download('特效', 'com.quvideo.xiaoying:id/template_pack_download_progress')
        self.template_use('特效')

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        time.sleep(2)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        time.sleep(2)
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        time.sleep(2)
        sc.driver.press_keycode(4)

        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        sc.driver.find_element_by_android_uiautomator('text("特效")').click()

        sc.logger.info('删除刚刚下载的特效')
        sc.capture_screen(fun_name, self.img_path)
        self.theme_manager('特效', 'com.quvideo.xiaoying:id/template_caption_grid_btn_update')

    def test_template_filter(self):
        """素材中心-滤镜."""
        sc.logger.info('素材中心-滤镜')
        fun_name = 'test_template_filter'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 5

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“素材中心”')
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        try:
            sc.logger.info('点击“滤镜”')
            sc.driver.find_element_by_android_uiautomator('text("滤镜")').click()
        except NoSuchElementException:
            sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 300)
            sc.driver.find_element_by_android_uiautomator('text("滤镜")').click()

        sc.logger.info('开始下载滤镜')
        try:
            el_template_down = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/template_filter_download')
            el_template_down.click()
        except NoSuchElementException:
            sc.logger.info('当前页面所有滤镜已下载完成')

        sc.logger.info('检查滤镜下载是否成功')
        try:
            WebDriverWait(sc.driver, 30).until(
                lambda use: use.find_element_by_android_uiautomator('text("使用")'))
        except TimeoutError as t:
            sc.logger.info('滤镜下载超时', t)
            return False
        except Exception as e:
            sc.logger.info('滤镜下载失败', e)
            return False
        sc.logger.info('滤镜下载测试完成')

        self.template_use('滤镜')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        time.sleep(10)
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.press_keycode(4)
        time.sleep(2)

        sc.logger.info('删除刚刚下载的滤镜')
        sc.capture_screen(fun_name, self.img_path)
        self.theme_manager('滤镜', 'com.quvideo.xiaoying:id/img_delete')

    def test_template_sticker(self):
        """素材中心-动画贴纸."""
        sc.logger.info('素材中心-动画贴纸')
        fun_name = 'test_template_sticker'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“素材中心”')
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)
        sc.logger.info('点击“动画贴纸”')
        sc.driver.find_element_by_android_uiautomator('text("动画贴纸")').click()

        self.template_download('动画贴纸', 'com.quvideo.xiaoying:id/template_pack_download_progress')
        self.template_use('动画贴纸')

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        time.sleep(1)
        sc.driver.press_keycode(4)
        time.sleep(1)

        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)
        sc.driver.find_element_by_android_uiautomator('text("动画贴纸")').click()

        sc.logger.info('删除刚刚下载的动画贴纸')
        sc.capture_screen(fun_name, self.img_path)
        self.theme_manager('动画贴纸', 'com.quvideo.xiaoying:id/img_delete')

    # 目前code需要先下载至少一个转场，download控件无法获取到，需要再调试
    def test_template_transition(self):
        """素材中心-转场."""
        sc.logger.info('素材中心-转场')
        fun_name = 'test_template_transition'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“素材中心”')
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)
        time.sleep(1)
        sc.logger.info('点击“转场”')
        sc.driver.find_element_by_android_uiautomator('text("转场")').click()

        time.sleep(1)
        try:
            btn_download = 'com.quvideo.xiaoying:id/imgbtn_download'
            sc.driver.find_element_by_id(btn_download)
            self.template_download('转场', btn_download)
        except NoSuchElementException:
            sc.logger.info('当前页面素材已经全部下载完毕了')

        time.sleep(1)
        self.template_use('转场')

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        time.sleep(1)
        sc.driver.press_keycode(4)

        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)
        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator('text("转场")').click()

        sc.logger.info('删除刚刚下载的转场')
        sc.capture_screen(fun_name, self.img_path)
        self.theme_manager('转场', 'com.quvideo.xiaoying:id/template_caption_grid_btn_update')

    def test_template_font(self):
        """素材中心-字体."""
        sc.logger.info('素材中心-字体')
        fun_name = 'test_template_font'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“素材中心”')
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)
        sc.logger.info('点击“字体”')
        sc.driver.find_element_by_android_uiautomator('text("字体")').click()

        sc.logger.info('开始下载字体')
        el_font_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/btn_download')
        try:
            el_font_list[0].click()
        except Exception:
            sc.logger.info('当前页面所有字体已下载完成')
            el_font_use = sc.driver.find_element_by_android_uiautomator('text("使用")')
            el_font_use.click()
            return True

        sc.logger.info('检查字体下载是否成功')
        try:
            WebDriverWait(sc.driver, 30).until(
                lambda use: use.find_element_by_android_uiautomator('text("使用")'))
        except TimeoutError as t:
            sc.logger.info('字体下载超时', t)
            return False
        except Exception as e:
            sc.logger.info('字体下载失败', e)
            return False
        sc.logger.info('字体下载测试完成')

        time.sleep(1)
        self.template_use('字体')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        time.sleep(1)
        sc.driver.press_keycode(4)

        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)
        sc.driver.find_element_by_android_uiautomator('text("字体")').click()

        sc.logger.info('删除刚刚下载的字体')
        sc.capture_screen(fun_name, self.img_path)
        self.theme_manager('字体', 'com.quvideo.xiaoying:id/img_delete')

    def test_template_giphy(self):
        """GIPHY-下载."""
        sc.logger.info('素材中心-GIPHY')
        fun_name = 'test_template_giphy'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“素材中心”')
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)
        sc.logger.info('点击“动画贴纸”')
        sc.driver.find_element_by_android_uiautomator('text("动画贴纸")').click()
        sc.logger.info('点击“GIPHY”')
        sc.driver.find_element_by_android_uiautomator('text("GIPHY")').click()
        time.sleep(5)

        sc.logger.info('开始下载GIPHY')
        try:
            el_template_down = sc.driver.find_elements_by_android_uiautomator('text("下载")')
            el_template_down.click()
        except Exception:
            sc.logger.info('当前页面所有GIPHY已下载完成')

        sc.logger.info('检查GIPHY下载是否成功')
        try:
            WebDriverWait(sc.driver, 30).until(
                lambda giphy_use: giphy_use.find_element_by_android_uiautomator('text("使用")'))
            el_template_use = sc.driver.find_elements_by_android_uiautomator('text("使用")')
            el_template_use.click()
        except TimeoutError as t:
            sc.logger.info('GIPHY下载超时', t)
            return False
        except Exception as e:
            sc.logger.info('GIPHY下载失败', e)
            return False
        sc.logger.info('GIPHY下载测试完成')

        self.template_use('GIPHY')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_right').click()
        sc.logger.info('点击“存草稿”')
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        time.sleep(1)
        sc.driver.press_keycode(4)

        time.sleep(1)
        sc.driver.find_element_by_android_uiautomator('text("素材中心")').click()
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 300)
        sc.driver.find_element_by_android_uiautomator('text("动画贴纸")').click()
        sc.driver.find_element_by_android_uiautomator('text("GIPHY")').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/right_button').click()
        time.sleep(1)

        sc.logger.info('删除刚刚下载的giphy')
        sc.capture_screen(fun_name, self.img_path)
        self.theme_manager('GIPHY', 'com.quvideo.xiaoying:id/text_delete')
