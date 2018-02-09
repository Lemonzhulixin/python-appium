# -*- coding: utf-8 -*-
"""预览页面的theme测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestPreviewTheme(object):
    """预览页面的theme测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_theme_ui(self):
        """预览页-切换到主题页面."""
        sc.logger.info('预览页-切换到主题页面')
        fun_name = 'test_theme_ui'

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()
        el_video = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_click_mask')
        el_video.click()
        sc.logger.info('点击“添加”')
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
        sc.logger.info('点击“下一步”')
        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()
        sc.logger.info('点击“主题”按钮')
        sc.driver.find_element_by_android_uiautomator('text("主题")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('预览页-切换到主题页面')

    def test_theme_download(self):
        """预览页-主题下载."""
        sc.logger.info('预览页-主题下载')
        start_x = self.width // 4
        start_bottom = self.height - self.height // 10

        sc.swipe_by_ratio(start_x, start_bottom, 'right', 0.5, 500)
        sc.logger.info('点击“下载更多”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgview_get_more_thumbnail_bg').click()
        time.sleep(1)
        try:
            el_theme_use = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/template_caption_grid_btn_update')
            sc.logger.info('点击“使用”按钮')
            el_theme_use.click()
        except NoSuchElementException:
            el_download_template = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_download')
            sc.logger.info('点击下载按钮')
            el_download_template.click()
            try:
                WebDriverWait(sc.driver, 30).until(
                    lambda download_theme: download_theme.find_element_by_android_uiautomator('text("使用")'))
                sc.driver.find_element_by_android_uiautomator('text("使用")').click()
            except TimeoutError as t:
                sc.logger.error('素材下载超时', t)
                sc.logger.info('返回创作中心主界面')
                for i in range(4):
                    sc.driver.press_keycode(4)
                return False
            except Exception as e:
                sc.logger.info('返回创作中心主界面')
                for i in range(4):
                    sc.driver.press_keycode(4)
                sc.logger.error('素材下载失败', e)
                return False

        sc.logger.info('返回创作中心主界面')
        for i in range(3):
            sc.driver.press_keycode(4)
        sc.logger.info('预览页-主题测试完成')
