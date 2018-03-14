# -*- coding: utf-8 -*-
"""镜头编辑相关操作的测试用例."""
import time
from unittest import TestCase
from iOS import script_ultils as sc
from selenium.common.exceptions import NoSuchElementException


class TestEditClip(TestCase):
    """镜头编辑相关操作的测试类."""

    width, height = sc.get_size()
    img_path = sc.path_lists[0]

    def test_clip_edit_01_video(self):
        """剪辑-镜头编辑-视频."""
        sc.logger.info('剪辑-镜头编辑-视频')
        fun_name = 'test_clip_edit_video'

        time.sleep(5)
        sc.logger.info('点击创作中心主按钮')
        try:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_n']").click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='camerta_f']").click()

        sc.logger.info('点击第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        time.sleep(0.5)
        sc.logger.info('点击"镜头编辑"')
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("镜头编辑").click()
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('***************修剪***************')
        time.sleep(1)
        sc.logger.info('点击"修剪"')
        try:
            sc.driver.find_element_by_name("修剪").click()
            # #长按拖动还需要再调试
            # sc.logger.info('滑动左侧trim bar')
            # time.sleep(3)
            # el_left_trim = sc.driver.find_element_by_accessibility_id("vivavideo_tool_clipedit_trim_left_n")
            # actions = TouchAction(sc.driver)
            # actions.long_press(el_left_trim, None, None, 500).move_to(None, 300, None).release().perform()
            # sc.capture_screen(fun_name, self.img_path)
            #
            # sc.logger.info('滑动右侧trim bar')
            # time.sleep(3)
            # el_right_trim = sc.driver.find_element_by_accessibility_id("vivavideo_tool_clipedit_trim_right_n")
            # actions = TouchAction(sc.driver)
            # actions.long_press(el_right_trim, None, None, 500).move_to(None, 500, None).release().perform()
            # sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('点击"确认"，保存修剪')
            sc.driver.find_element_by_name("确认").click()
        # except Exception as e:
        #     sc.logger.info('修剪出错了！',e)
        except NoSuchElementException:
            sc.logger.info('当前镜头为图片，不支持"修剪"')
            return True

        sc.logger.info('***************分割***************')
        sc.logger.info('点击"分割"')
        try:
            sc.driver.find_element_by_name("分割").click()

            sc.logger.info('点击"确认"，保存分割')
            sc.driver.find_element_by_name("确认").click()
        except NoSuchElementException:
            sc.logger.info("当前镜头为图片，不支持'分割'")
            return True

        sc.logger.info('***************复制***************')
        sc.logger.info('点击"复制"')
        sc.driver.find_element_by_name("复制").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('***************变速***************')
        sc.logger.info('点击"变速"')
        try:
            sc.driver.find_element_by_name("变速").click()

            sc.logger.info('勾选"运用于全部视频镜头"')
            sc.driver.find_element_by_name("运用于全部视频镜头").click()

            sc.logger.info('勾选"保持音调不变"')
            sc.driver.find_element_by_name("保持音调不变").click()
            sc.capture_screen(fun_name, self.img_path)

            sc.logger.info('点击"确认"，保存变速')
            sc.driver.find_element_by_name("确认").click()
        except Exception as e:
            sc.logger.info('变速出错了！', e)
        except NoSuchElementException:
            sc.logger.info("当前镜头为图片，不支持'变速'")
            return True

        sc.logger.info('***************调节***************')
        sc.logger.info('点击"调节"')
        el_adjust = sc.driver.find_element_by_name("调节")
        el_adjust.click()

        sc.logger.info('点击"取消"，取消调节')
        sc.driver.find_element_by_name("取消").click()

        sc.logger.info('***************静音***************')
        sc.logger.info('向左滑动')
        time.sleep(0.5)
        coord_x = el_adjust.location.get('x')
        coord_y = el_adjust.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.6, 500) #从调节按钮向左滑动

        sc.logger.info('点击“静音”')
        try:
            sc.driver.find_element_by_name("静音").click()
        except NoSuchElementException:
            sc.logger.info("当前镜头为图片，不支持'静音'")
            return True

        sc.logger.info('***************镜头倒放***************')
        sc.logger.info('点击“镜头倒放”')
        el_reverse = sc.driver.find_element_by_name("镜头倒放")
        el_reverse.click()
        sc.capture_screen(fun_name, self.img_path)
        time.sleep(30)

        # try:
        #     sc.driver.find_element_by_name("镜头倒放").click()
        #     try:
        #         WebDriverWait(sc.driver, 120).until(
        #             lambda reverse: reverse.find_element_by_name("镜头倒放"))
        #     except Exception as e:
        #         sc.logger.error('镜头倒放出错了', e)
        #         return False
        #     except TimeoutError as t:
        #         sc.logger.error('镜头倒放超时', t)
        #         return False
        # except NoSuchElementException:
        #     sc.logger.info("当前镜头为图片，不支持'倒放镜头'")
        #     return True

        sc.logger.info('***************模糊背景***************')
        sc.logger.info('向左滑动')
        time.sleep(0.5)
        coord_x = el_reverse.location.get('x')
        coord_y = el_reverse.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.5, 500)  # 从调节按钮向左滑动

        sc.logger.info('点击“模糊背景”')
        el_bg = sc.driver.find_element_by_name("模糊背景")
        for i in range(2):
            el_bg.click()
            sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('保存编辑')
        sc.driver.find_element_by_name("xiaoying com ok").click()

        sc.logger.info('存草稿并返回创作页首页')
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_clip_edit_02_img(self):
        """剪辑-镜头编辑-图片."""
        sc.logger.info('剪辑-镜头编辑-图片')
        fun_name = 'test_clip_edit_img'

        time.sleep(1)
        sc.logger.info('点击视频剪辑')
        try:
            sc.driver.find_element_by_name("视频剪辑").click()
        except NoSuchElementException:
            sc.driver.find_element_by_name("剪辑").click()

        sc.logger.info('切换到图片')
        sc.driver.find_element_by_name("视频").click()
        sc.driver.find_element_by_name("图片").click()

        sc.logger.info('图片操作-连续多选')
        el_imgs = sc.driver.find_elements_by_xpath("//*/XCUIElementTypeImage")
        i = 1
        while i < len(el_imgs):
            el_imgs[i].click()
            i = i + 1

        sc.logger.info('点击下一步，进入预览页')
        sc.driver.find_element_by_name("下一步").click()
        sc.capture_screen(fun_name, self.img_path)

        time.sleep(0.5)
        sc.logger.info('点击"镜头编辑"')
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("镜头编辑").click()

        sc.logger.info('***************图片时长***************')
        sc.logger.info('点击"图片时长"')
        try:
            sc.driver.find_element_by_name("图片时长").click()

            sc.logger.info('点击"确认"，保存图片时长设置')
            sc.driver.find_element_by_name("确认").click()
        except NoSuchElementException:
            sc.logger.info("当前镜头为视频，不支持'图片时长'")
            return True

        sc.logger.info('***************复制***************')
        sc.logger.info('点击"复制"')
        sc.driver.find_element_by_name("复制").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('***************调节***************')
        sc.logger.info('点击"调节"')
        el_adjust = sc.driver.find_element_by_name("调节")
        el_adjust.click()

        sc.logger.info('点击"取消"，取消调节')
        sc.driver.find_element_by_name("取消").click()

        sc.logger.info('***************模糊背景***************')
        sc.logger.info('向左滑动')
        time.sleep(0.5)
        coord_x = el_adjust.location.get('x')
        coord_y = el_adjust.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.6, 500)  # 从调节按钮向左滑动

        sc.logger.info('点击“模糊背景”')
        el_bg = sc.driver.find_element_by_name("模糊背景")
        for i in range(2):
            el_bg.click()
            sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('保存编辑')
        sc.driver.find_element_by_name("xiaoying com ok").click()

        sc.logger.info('存草稿并返回创作页首页')
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()

    def test_clip_edit_03_other(self):
        """剪辑-镜头编辑-其他编辑."""
        sc.logger.info('剪辑-镜头编辑-其他编辑')
        fun_name = 'test_clip_edit_other'

        time.sleep(5)
        sc.logger.info('点击第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        time.sleep(0.5)
        sc.logger.info('点击"镜头编辑"')
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("镜头编辑").click()
        sc.capture_screen(fun_name,self.img_path)

        # #长按拖动还需要再调试
        # sc.logger.info('调整镜头')
        # el_clip_01 = sc.driver.find_element_by_xpath(
        #     "//*/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeImage[1]")
        # el_clip_02 = sc.driver.find_element_by_xpath(
        #     "//*/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeImage[1]")
        #
        # sc.logger.info('开始把第一个镜头与第二个镜头对调')
        # actions = TouchAction(sc.driver)
        # actions.long_press(el_clip_01,None,None,1500).move_to(el_clip_02,None,None).release().perform()
        # time.sleep(1)
        # sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('删除任一镜头')
        el_clip_del = sc.driver.find_element_by_name("vivavideo edit video close n")
        el_clip_del.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('确认"删除"')
        sc.driver.find_element_by_name("确认").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('多选镜头')
        sc.driver.find_element_by_name("vivavideo tool gallery up n").click()
        time.sleep(0.5)
        sc.driver.find_element_by_name("多选").click()

        sc.logger.info('全选')
        sc.driver.find_element_by_name("全选").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"镜头动态效果"按钮')
        sc.driver.find_element_by_name("vivavideo tool clipedit bgimag").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('多镜头-打开镜头动态效果')
        sc.driver.find_element_by_name("打开镜头动态效果").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('多镜头-关闭镜头动态效果')
        sc.driver.find_element_by_name("vivavideo tool clipedit bgimag").click()
        sc.driver.find_element_by_name("关闭镜头动态效果").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"镜头原音"开关')
        sc.driver.find_element_by_name("vivavideo tool clipedit sound2").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('打开镜头原音')
        sc.driver.find_element_by_name("打开 镜头原音 ").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('关闭镜头原音')
        sc.driver.find_element_by_name("vivavideo tool clipedit sound2").click()
        sc.driver.find_element_by_name("关闭 镜头原音").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"删除"按钮')
        sc.driver.find_element_by_name("vivavideo tool clipedit delete").click()

        sc.logger.info('确认"删除"')
        sc.driver.find_element_by_xpath("(//XCUIElementTypeButton[@name='确认'])[2]").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('保存所有改动')
        sc.driver.find_element_by_name("xiaoying com ok").click()

        sc.logger.info('镜头全部被删除，放弃该工程')
        time.sleep(2)
        sc.driver.find_element_by_name("放弃").click()

    def test_clip_edit_04_add(self):
        """剪辑-镜头编辑-添加镜头."""
        sc.logger.info('剪辑-镜头编辑-添加镜头')
        fun_name = 'test_clip_edit_add'

        start_x = self.width // 2
        start_bottom = self.height - self.height // 10

        time.sleep(1)
        sc.logger.info('点击第一个草稿封面')
        el_draft = sc.driver.find_element_by_xpath("//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton")
        el_draft.click()

        time.sleep(0.5)
        sc.logger.info('点击"镜头编辑"')
        sc.driver.find_element_by_name("剪辑").click()
        sc.driver.find_element_by_name("镜头编辑").click()

        sc.logger.info('点击"添加"按钮')
        sc.driver.find_element_by_name("vivavideo tool gallery up n").click()
        time.sleep(0.5)
        while True:
            try:
                sc.logger.info('点击添加镜头按钮')
                sc.driver.find_element_by_name("vivavideo tool clipedit add n").click()
                sc.capture_screen(fun_name,self.img_path)
                break
            except NoSuchElementException:
                sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.6, 500)

        sc.logger.info('添加视频')
        el_video = sc.driver.find_element_by_accessibility_id("vivavideo_tool_gallery_audio_type_video")
        el_video.click()
        sc.driver.find_element_by_name("添加 0").click()

        sc.logger.info('点击右上角拍摄按钮')
        sc.driver.find_element_by_name("vivavideo gallery create captu").click()
        time.sleep(1)
        sc.capture_screen(fun_name,self.img_path)

        sc.logger.info('开始录制')
        el_capture = sc.driver.find_element_by_xpath(
            "//*/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]")
        el_capture.click()
        time.sleep(5)

        sc.logger.info('录制5s后点击录制按钮停止录制')
        el_capture.click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击确认按钮')
        sc.driver.find_element_by_name("vivavideo camera tool icon nex").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('点击"下一步"')
        sc.driver.find_element_by_name("下一步").click()
        sc.capture_screen(fun_name, self.img_path)

        sc.logger.info('保存编辑')
        sc.driver.find_element_by_name("xiaoying com ok").click()

        sc.logger.info('存草稿并返回创作页首页')
        sc.driver.find_element_by_name("存草稿").click()
        time.sleep(1)
        sc.driver.find_element_by_name("vivavideo com nav back n").click()