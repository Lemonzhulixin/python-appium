# -*- coding: utf-8 -*-
"""Gallery页面的测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android import script_ultils as sc


class TestGallery(object):
    """Gallery的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_gallery_video(self):
        """相册-视频."""
        sc.logger.info('相册-视频')
        fun_name = 'test_gallery_video'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        time.sleep(1)
        sc.logger.info('点击创作中心主按钮')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_creation').click()
        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()
        time.sleep(1)
        try:
            sc.driver.find_element_by_android_uiautomator('text("跳过")').click()
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()
        except NoSuchElementException:
            sc.logger.info('已跳过订阅页面')
        sc.logger.info('点击“其它相册”')
        sc.driver.find_element_by_android_uiautomator('text("其他相册")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator('text("全部")').click()
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)
        el_video = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_click_mask')
        el_video.click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_ratate').click()
        try:
            sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_crop').click()
        except NoSuchElementException:
            sc.logger.info('视频尺寸1:1，无此选项')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_start_trim').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/imgbtn_import').click()
        sc.capture_screen(fun_name, self.img_path)
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
        sc.capture_screen(fun_name, self.img_path)

        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('相册-视频相关操作测试完成')

    def test_gallery_img(self):
        """相册-图片."""
        sc.logger.info('相册-图片')
        fun_name = 'test_gallery_img'

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()
        sc.driver.find_element_by_android_uiautomator('text("视频")').click()
        sc.driver.find_element_by_android_uiautomator('text("图片")').click()
        sc.driver.find_element_by_android_uiautomator('text("其他相册")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator('text("全部")').click()
        sc.find_by_ids('com.quvideo.xiaoying:id/img_click_mask', fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/preview_layout_fake').click()
        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('相册-图片相关操作测试完成')

    def test_gallery_storyboard(self):
        """相册-storyboard."""
        sc.logger.info('相册-storyboard')
        fun_name = 'test_gallery_storyboard'

        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()
        el_video_list = sc.driver.find_elements_by_id('com.quvideo.xiaoying:id/img_click_mask')

        for i in range(3):
            el_video_list[i].click()
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
        sc.driver.find_element_by_android_uiautomator('text("视频")').click()
        sc.driver.find_element_by_android_uiautomator('text("图片")').click()
        sc.find_by_ids('com.quvideo.xiaoying:id/img_icon', fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/btn_expand').click()
        el_storyboard_del = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_delete')
        el_storyboard_del.click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.driver.find_element_by_android_uiautomator('text("保存")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.logger.info('相册-storyboard相关操作测试完成')

    def test_gallery_giveup(self):
        """相册-放弃操作."""
        sc.logger.info('相册-放弃操作')
        fun_name = 'test_gallery_giveup'

        start_x = self.width // 2
        start_bottom = self.height - self.height // 4
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()
        el_video = sc.driver.find_element_by_id('com.quvideo.xiaoying:id/img_click_mask')
        el_video.click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator('text("视频")').click()
        sc.driver.find_element_by_android_uiautomator('text("图片")').click()
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)
        sc.find_by_ids('com.quvideo.xiaoying:id/img_icon', fun_name, self.img_path)
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/xiaoying_com_btn_left').click()
        sc.driver.find_element_by_android_uiautomator('text("丢弃")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('相册-放弃操作相关操作测试完成')
