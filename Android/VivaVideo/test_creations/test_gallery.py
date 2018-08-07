# -*- coding: utf-8 -*-
"""Gallery页面的测试用例."""
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


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
        start_y = self.height // 3

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sc.logger.info('点击“剪辑”')
        sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()
        time.sleep(1)
        try:
            sc.driver.find_element_by_android_uiautomator('text("跳过")').click()

            first_icon = 'com.quvideo.xiaoying:id/icon1'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(first_icon)).click()
        except NoSuchElementException:
            sc.logger.info('已跳过订阅页面')
        sc.logger.info('点击“其它相册”')
        sc.driver.find_element_by_android_uiautomator('text("其他相册")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator('text("全部")').click()
        time.sleep(1)

        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)
        mask_img = 'com.quvideo.xiaoying:id/img_click_mask'
        WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(mask_img)).click()
        sc.capture_screen(fun_name, self.img_path)

        rotate_btn = 'com.quvideo.xiaoying:id/imgbtn_ratate'
        WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(rotate_btn)).click()

        try:
            crop_btn = 'com.quvideo.xiaoying:id/imgbtn_crop'
            sc.driver.find_element_by_id(crop_btn).click()
        except NoSuchElementException:
            sc.logger.info('视频尺寸1:1，无此选项')

        trip_btn = 'com.quvideo.xiaoying:id/btn_start_trim'
        sc.driver.find_element_by_id(trip_btn).click()

        import_btn = 'com.quvideo.xiaoying:id/imgbtn_import'
        WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(import_btn)).click()
        sc.capture_screen(fun_name, self.img_path)
        try:
            n_btn = 'com.quvideo.xiaoying:id/xiaoying_com_storyboard_next_btn'
            WebDriverWait(sc.driver, 60).until(
                lambda x: x.find_element_by_id(n_btn)).click()
        except TimeoutError as t:
            sc.logger.error('导入视频超时', t)
            return False
        except Exception as e:
            sc.logger.error('导入视频出错', e)
            return False
        sc.capture_screen(fun_name, self.img_path)

        time.sleep(1)
        sc.driver.swipe(start_x, start_y, start_x, start_y, 1000)

        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()
        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(left_btn)).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('相册-视频相关操作测试完成')

    def test_gallery_img(self):
        """相册-图片."""
        sc.logger.info('相册-图片')
        fun_name = 'test_gallery_img'
        start_x = self.width // 2
        start_y = self.height // 3

        first_icon = 'com.quvideo.xiaoying:id/icon1'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(first_icon)).click()

        # sc.driver.find_element_by_id('com.quvideo.xiaoying:id/icon1').click()
        sc.driver.find_element_by_android_uiautomator('text("视频")').click()
        sc.driver.find_element_by_android_uiautomator('text("图片")').click()
        sc.driver.find_element_by_android_uiautomator('text("其他相册")').click()
        sc.capture_screen(fun_name, self.img_path)

        sc.driver.find_element_by_android_uiautomator('text("全部")').click()
        mask_img = 'com.quvideo.xiaoying:id/img_click_mask'
        element_list = sc.driver.find_elements_by_id(mask_img)

        if len(element_list) >= 2:
            element_list = element_list[:2]

        for element_em in element_list:
            element_em.click()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

        sc.driver.find_element_by_android_uiautomator('text("下一步")').click()
        sc.capture_screen(fun_name, self.img_path)

        time.sleep(1)
        sc.driver.swipe(start_x, start_y, start_x, start_y, 1000)

        sc.driver.find_element_by_android_uiautomator('text("存草稿")').click()

        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(left_btn)).click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('相册-图片相关操作测试完成')

    def test_gallery_storyboard(self):
        """相册-storyboard."""
        sc.logger.info('相册-storyboard')
        fun_name = 'test_gallery_storyboard'

        first_icon = 'com.quvideo.xiaoying:id/icon1'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(first_icon)).click()

        mask_img = 'com.quvideo.xiaoying:id/img_click_mask'
        el_video_list = sc.driver.find_elements_by_id(mask_img)

        for i in range(2):
            import_btn = 'com.quvideo.xiaoying:id/imgbtn_import'
            el_video_list[i].click()
            sc.driver.find_element_by_id(import_btn).click()
            try:
                WebDriverWait(sc.driver, 60).until(
                    lambda el: el.find_element_by_android_uiautomator(
                        'text("下一步")'))
            except TimeoutError as t:
                sc.logger.error('导入视频超时', t)
                return False
            except Exception as e:
                sc.logger.error('导入视频出错', e)
                return False
        sc.driver.find_element_by_android_uiautomator('text("视频")').click()
        sc.driver.find_element_by_android_uiautomator('text("图片")').click()

        img_icon = 'com.quvideo.xiaoying:id/img_icon'
        element_list = sc.driver.find_elements_by_id(img_icon)

        if len(element_list) >= 2:
            element_list = element_list[:2]

        for element_em in element_list:
            element_em.click()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

        expand_btn = 'com.quvideo.xiaoying:id/btn_expand'
        sc.driver.find_element_by_id(expand_btn).click()

        del_img = 'com.quvideo.xiaoying:id/img_delete'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(del_img)).click()
        sc.capture_screen(fun_name, self.img_path)

        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        sc.driver.find_element_by_id(left_btn).click()

        sc.driver.find_element_by_android_uiautomator('text("保存")').click()
        sc.capture_screen(fun_name, self.img_path)

        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(left_btn)).click()
        sc.logger.info('相册-storyboard相关操作测试完成')

    def test_gallery_giveup(self):
        """相册-放弃操作."""
        sc.logger.info('相册-放弃操作')
        fun_name = 'test_gallery_giveup'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 4

        first_icon = 'com.quvideo.xiaoying:id/icon1'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda c_btn: c_btn.find_element_by_id(first_icon)).click()

        mask_img = 'com.quvideo.xiaoying:id/img_click_mask'
        WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(mask_img)).click()
        sc.capture_screen(fun_name, self.img_path)

        left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
        sc.driver.find_element_by_id(left_btn).click()

        sc.capture_screen(fun_name, self.img_path)
        sc.driver.find_element_by_android_uiautomator('text("视频")').click()
        sc.driver.find_element_by_android_uiautomator('text("图片")').click()

        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)
        img_icon = 'com.quvideo.xiaoying:id/img_icon'
        element_list = sc.driver.find_elements_by_id(img_icon)

        if len(element_list) >= 2:
            element_list = element_list[:2]

        for element_em in element_list:
            element_em.click()
            time.sleep(1)
            sc.capture_screen(fun_name, self.img_path)

        sc.driver.find_element_by_id(left_btn).click()

        sc.driver.find_element_by_android_uiautomator('text("丢弃")').click()
        sc.capture_screen(fun_name, self.img_path)
        sc.logger.info('相册-放弃操作相关操作测试完成')
