# -*- coding: utf-8 -*-
"""小影创作主页面的测试用例."""
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from Android_old import script_ultils as sc


class TestHome(object):
    """小影主页面的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_home_minor(self):
        """首页-次要功能位检查."""
        sc.logger.info('首页-次要功能位检查')
        fun_name = 'test_home_minor'

        sc.logger.info('点击创作中心主按钮')
        c_btn = 'com.quvideo.xiaoying:id/img_creation'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(c_btn)).click()

        sub_icon_btn = 'com.quvideo.xiaoying:id/sub_btn_icon'
        element_list = sc.driver.find_elements_by_id(sub_icon_btn)
        element_list.pop(0)

        for element_em in element_list:
            element_em.click()
            time.sleep(2)
            sc.driver.press_keycode(4)
            sc.capture_screen(fun_name, self.img_path)

        coord_x = element_list[-1].location.get('x')
        coord_y = element_list[-1].location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.7, 500)

        sec_list = sc.driver.find_elements_by_id(sub_icon_btn)

        for sec_em in sec_list:
            sec_em.click()
            time.sleep(2)
            sc.driver.press_keycode(4)
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('首页-次要功能位检查完毕')

    def test_home_other(self):
        """首页-小影百宝箱及其他."""
        sc.logger.info('首页-推荐位-小影百宝箱及其他')
        fun_name = 'test_home_other'
        start_x = self.width // 2
        start_bottom = self.height - self.height // 5

        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.7, 500)

        vip_btn = 'com.quvideo.xiaoying:id/btn_vip'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(vip_btn)).click()

        back_img = 'com.quvideo.xiaoying:id/vip_home_close'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(back_img)).click()

        shuffle_btn = 'com.quvideo.xiaoying:id/btn_shuffle'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(shuffle_btn)).click()

        sc.driver.press_keycode(4)
        img_item = 'com.quvideo.xiaoying:id/creation_item_img'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(img_item)).click()
        sc.capture_screen(fun_name, self.img_path)

        time.sleep(3)
        sc.driver.press_keycode(4)
        sc.logger.info('首页-推荐位-小影百宝箱及其他检查完毕')

    def test_home_studio(self):
        """首页-我的工作室."""
        sc.logger.info('首页-我的工作室')
        fun_name = 'test_home_studio'
        start_x = self.width // 2
        start_bottom = self.height // 5

        sc.logger.info('下滑一点')
        time.sleep(1)
        sc.swipe_by_ratio(start_x, start_bottom, 'down', 0.7, 700)

        sc.capture_screen(fun_name, self.img_path)
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_android_uiautomator(
                'text("更多草稿")')).click()

        sc.logger.info('点击第一个草稿封面')
        draft_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_project_thumb'
        sc.driver.find_element_by_id(draft_img).click()

        time.sleep(1)
        try:
            sc.logger.info('点击左上角返回')
            left_btn = 'com.quvideo.xiaoying:id/xiaoying_com_btn_left'
            WebDriverWait(sc.driver, 10, 1).until(
                lambda el: el.find_element_by_id(left_btn)).click()
            sc.capture_screen(fun_name, self.img_path)
        except NoSuchElementException:
            sc.logger.info('此草稿视频为拍摄视频，返回的是拍摄页面')
            cancel_btn = 'com.quvideo.xiaoying:id/cam_btn_cancel'
            sc.driver.find_element_by_id(cancel_btn).click()
            sc.capture_screen(fun_name, self.img_path)

        sc.driver.press_keycode(4)

        sc.logger.info('点击“保存/上传”')
        publish_btn = 'com.quvideo.xiaoying:id/xiaoying_studio_publish_btn'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(publish_btn)).click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击左上角返回')
        back_img = 'com.quvideo.xiaoying:id/img_back'
        WebDriverWait(sc.driver, 10, 1).until(
            lambda el: el.find_element_by_id(back_img)).click()

        sc.logger.info('删除一个草稿')
        del_img = 'com.quvideo.xiaoying:id/xiaoying_studio_img_delete'
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_id(del_img)).click()

        sc.driver.find_element_by_android_uiautomator('text("确认")').click()
        sc.driver.press_keycode(4)
        sc.logger.info('首页-我的工作室完成')
