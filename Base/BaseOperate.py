# -*- coding: utf-8 -*-
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException, StaleElementReferenceException
from Base.BaseElements import Element as be
import os
from appium.webdriver.common.touch_action import TouchAction

'''
# 此脚本主要用于查找元素是否存在，操作页面元素
'''

class OperateElement:
    def __init__(self, driver=""):
        self.driver = driver

    def findElement(self, mOperate):
        '''
        查找元素.mOperate,dict|list
        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            if type(mOperate) == list:  # 多检查点
                for item in mOperate:
                    # if item.get("is_webview", "0") == 1:  # 1表示切换到webview
                    #     self.switchToWebview()
                    # elif item.get("is_webview", "0") == 2:
                    #     self.switchToNative()
                    if item.get("element_info", "0") == "0":   # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                        return {"result": True}
                    t = item["check_time"] if item.get("check_time", "0") != "0" else be.WAIT_TIME
                    WebDriverWait(self.driver, t).until(lambda x: self.elements_by(item))
                return {"result": True}
            if type(mOperate) == dict:  # 单检查点
                # if mOperate.get("is_webview", "0") == 1 and self.switchToWebview() is False:  # 1表示切换到webview
                #     print("切换到webview失败，请确定是否在webview页面")
                #     return {"result": False, "webview": False}
                # elif mOperate.get("is_webview", "0") == 2:
                #     self.switchToNative()
                if mOperate.get("element_info", "0") == "0":  # 如果没有页面元素，就不检测是页面元素，可能是滑动等操作
                    return {"result": True}
                t = mOperate["check_time"] if mOperate.get("check_time", "0") != "0" else be.WAIT_TIME  # 如果自定义检测时间为空，就用默认的检测等待时间
                WebDriverWait(self.driver, t).until(lambda x: self.elements_by(mOperate))  # 操作元素是否存在
                return {"result": True}
        except TimeoutException:
            # print("==查找元素超时==")
            return {"result": False, "type": be.TIME_OUT}
        except NoSuchElementException:
            # print("==查找元素不存在==")
            return {"result": False, "type": be.NO_SUCH}
        except WebDriverException:
            # print("WebDriver出现问题了")
            return {"result": False, "type": be.WEB_DROVER_EXCEPTION}

    '''
    查找元素.mOperate是字典
    operate_type：对应的操作
    element_info：元素详情
    find_type: find类型
    testInfo: 用例介绍
    logTest: 记录日志
    device: 设备名
    '''

    def operate(self, mOperate, testInfo, logTest, device):
        res = self.findElement(mOperate)
        if res["result"]:
            return self.operate_by(mOperate, testInfo, logTest, device)
        else:
            return res

    def operate_by(self, operate, testInfo, logTest, device):
        try:
            info = operate.get("element_info", " ") + "_" + operate.get("operate_type", " ") + str(operate.get(
                "code", " ")) + operate.get("msg", " ")
            logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + info)  # 记录日志
            print("==操作步骤：%s==" % info)

            # if operate.get("operate_type", "0") == "0":  # 如果没有此字段，说明没有相应操作，一般是检查点，直接判定为成功
            #     return {"result": True}

            # threading._start_new_thread(self.click_windows(device),())
            elements = {
                be.SWIPE_DOWN: lambda: self.swipeToDown(operate),
                be.SWIPE_UP: lambda: self.swipeToUp(operate),
                be.SWIPE_RIGHT: lambda: self.swipeToRight(operate),
                be.SWIPE_LEFT: lambda: self.swipeToLeft(operate),
                be.CLICK: lambda: self.click(operate),
                be.IGNORE: lambda: self.ignore(operate),
                be.REPEAT: lambda: self.repeat(operate),
                be.SCREEN_TAP:lambda: self.screen_tap(200,200),
                # be.GET_VALUE: lambda: self.get_value(operate),
                be.SET_VALUE: lambda: self.set_value(operate),
                be.ADB_TAP: lambda: self.adb_tap(operate, device),
                be.GET_CONTENT_DESC: lambda: self.get_content_desc(operate),
                be.PRESS_KEY_CODE: lambda: self.press_keycode(operate)
            }
            return elements[operate.get("operate_type")]()
        except IndexError:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate["element_info"] + "索引错误")  # 记录日志
            # print(operate["element_info"] + "索引错误")
            return {"result": False, "type": be.INDEX_ERROR}
        except NoSuchElementException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素不存在或没加载完成")  # 记录日志
            # print(operate["element_info"] + "页面元素不存在或没有加载完成")
            return {"result": False, "type": be.NO_SUCH}
        except StaleElementReferenceException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素已经变化")  # 记录日志
            # print(operate["element_info"] + "页面元素已经变化")
            return {"result": False, "type": be.STALE_ELEMENT_REFERENCE_EXCEPTION}
        except KeyError:
            # 如果key不存在，一般都是在自定义的page页面去处理了，这里直接返回为真
            return {"result": True}

    # 获取到元素到坐标点击，主要解决浮动层遮档无法触发driver.click的问题
    def adb_tap(self, mOperate, device):

        bounds = self.elements_by(mOperate).location
        x = str(bounds["x"])
        y = str(bounds["y"])

        cmd = "adb -s " + device + " shell input tap " + x + " " + y
        print(cmd)
        os.system(cmd)

        return {"result": True}

    def toast(self, xpath, logTest, testInfo):
        logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + "查找弹窗元素_" + xpath)  # 记录日志
        try:
            WebDriverWait(self.driver, 10, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
            return {"result": True}
        except TimeoutException:
            return {"result": False}
        except NoSuchElementException:
            return {"result": False}

    # 点击事件
    def click(self, mOperate):
        # print(self.driver.page_source)
        if mOperate["find_type"] == be.find_element_by_id or mOperate["find_type"] == be.find_element_by_xpath or mOperate["find_type"] == be.find_element_by_android_uiautomator or \
                mOperate["find_type"] == be.find_element_by_accessibility_id or mOperate["find_type"] == be.find_element_by_name:
            self.elements_by(mOperate).click()
        elif mOperate["find_type"] == be.find_elements_by_id or mOperate["find_type"] == be.find_elements_by_xpath:
            self.elements_by(mOperate)[mOperate["index"]].click()
        return {"result": True}

    # 忽略不存在的元素
    def ignore(self, mOperate):
        if self.click(mOperate):
            pass
        else:
            pass
        return {"result": True}

    # 重复执行多次操作，默认三次
    def repeat(self, mOperate):
        try:
            for i in range(3):
                self.click(mOperate)
            return {"result": True}
        except:
            print('操作失败了，请重试该操作')
            return {"result": False}

    # code 事件
    def press_keycode(self, mOperate):
        self.driver.press_keycode(mOperate.get("code", 0))
        return {"result": True}

    def get_content_desc(self, mOperate):
        result = self.elements_by(mOperate).get_attribute("contentDescription")
        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}

    # '''
    # 切换native
    #
    # '''
    #
    # def switchToNative(self):
    #     self.driver.switch_to.context("NATIVE_APP")  # 切换到native
    #
    # '''
    # 切换webview
    # '''
    #
    # def switchToWebview(self):
    #     try:
    #         n = 1
    #         while n < 10:
    #             time.sleep(3)
    #             n = n + 1
    #             print(self.driver.contexts)
    #             for cons in self.driver.contexts:
    #                 if cons.lower().startswith("webview"):
    #                     self.driver.switch_to.context(cons)
    #                     # print(self.driver.page_source)
    #                     self.driver.execute_script('document.querySelectorAll("html")[0].style.display="block"')
    #                     self.driver.execute_script('document.querySelectorAll("head")[0].style.display="block"')
    #                     self.driver.execute_script('document.querySelectorAll("title")[0].style.display="block"')
    #                     print("切换webview成功")
    #                     return {"result": True}
    #         return {"result": False}
    #     except appium.common.exceptions.NoSuchContextException:
    #         print("切换webview失败")
    #         return {"result": False, "text": "appium.common.exceptions.NoSuchContextException异常"}

    def get_size(self):
        """获取屏幕分辨率."""
        rect = self.driver.get_window_size()
        return rect['width'], rect['height']

    def swipe_by_ratio(self, start_x, start_y, direction, ratio, duration=None):
        """
        按照屏幕比例的滑动.

        :param start_x: 起始横坐标
        :param start_y: 起始纵坐标
        :param direction: 滑动方向，只支持'up'、'down'、'left'、'right'四种方向参数
        :param ratio: 滑动距离与屏幕的比例，范围0到1
        :param duration: 滑动时间，单位ms
        :return:
        """
        direction_list = ['up', 'down', 'left', 'right']
        if direction not in direction_list:
            print('滑动方向%s不支持', direction)

        width, height = self.get_size()

        def swipe_up():
            """上滑."""
            end_y = start_y - ratio * height
            if end_y < 0:
                print('上滑距离过大')
                return False
            else:
                self.driver.swipe(start_x, start_y, start_x, end_y, duration)
            return True

        def swipe_down():
            """下滑."""
            end_y = start_y + ratio * height
            if end_y > height:
                print('下滑距离过大')
                return False
            else:
                self.driver.swipe(start_x, start_y, start_x, end_y, duration)
            return True

        def swipe_left():
            """左滑."""
            end_x = start_x - ratio * width
            if end_x < 0:
                print('左滑距离过大')
                return False
            else:
                self.driver.swipe(start_x, start_y, end_x, start_y, duration)
            return True

        def swipe_right():
            """右滑."""
            end_x = start_x + ratio * width
            if end_x > width:
                print('右滑距离过大')
                return False
            else:
                self.driver.swipe(start_x, start_y, end_x, start_y, duration)
            return True

        swipe_dict = {'up': swipe_up, 'down': swipe_down, 'left': swipe_left,
                      'right': swipe_right}
        return swipe_dict[direction]()

    # 左滑动
    def swipeToLeft(self, mOperate):
        '''
        以某个元素作为标准点，左滑动
        :param element_info: 某标准点元素
        :return:
        '''
        print('向左滑动')
        coord_x = self.elements_by(mOperate).location.get('x')
        coord_y = self.elements_by(mOperate).location.get('y')
        self.swipe_by_ratio(coord_x, coord_y, 'left', 0.5, 300)  # 从某一元素向左滑动
        return {"result": True}

    def swipeToRight(self, mOperate):
        '''
        以某个元素作为标准点，右滑动
        :param element_info: 某标准点元素
        :return:
        '''
        print('向右滑动')
        coord_x = self.elements_by(mOperate).location.get('x')
        coord_y = self.elements_by(mOperate).location.get('y')
        self.swipe_by_ratio(coord_x, coord_y, 'right', 0.5, 300)  # 从某一元素向右滑动
        return {"result": True}

    def swipeToUp(self, mOperate):
        '''
        以某个元素作为标准点，上滑动
        :param element_info: 某标准点元素
        :return:
        '''
        print('向上滑动')
        coord_x = self.elements_by(mOperate).location.get('x')
        coord_y = self.elements_by(mOperate).location.get('y')
        self.swipe_by_ratio(coord_x, coord_y, 'up', 0.5, 300)  # 从某一元素向上滑动
        return {"result": True}

    def swipeToDown(self, mOperate):
        '''
        以某个元素作为标准点，下滑动
        :param element_info: 某标准点元素
        :return:
        '''
        print('向下滑动')
        coord_x = self.elements_by(mOperate).location.get('x')
        coord_y = self.elements_by(mOperate).location.get('y')
        self.swipe_by_ratio(coord_x, coord_y, 'down', 0.5, 300)  # 从某一元素向下滑动
        return {"result": True}

    # def swipeToDown(self):
    #     width, height = self.get_size()
    #     start_x = width // 2
    #     start_y = height // 8
    #     start_bottom = height - start_y
    #
    #     print("向下滑动")
    #     self.swipe_by_ratio(start_x, start_bottom, 'down', 0.5, 500)
    #     return {"result": True}

    # def swipeToUp(self):
    #     width, height = self.get_size()
    #     start_x = width // 2
    #     start_bottom = height - height // 8
    #     print("向上滑动")
    #     self.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)
    #     return {"result": True}

    # def swipeToRight(self):
    #     width, height = self.get_size()
    #     start_x = width // 8
    #     start_bottom = height // 2
    #     print("向右滑动")
    #     self.swipe_by_ratio(start_x, start_bottom, 'right', 0.5, 500)
    #     return {"result": True}

    def screen_tap(self, x, y):
        '''
        :param fun: 要消除的storyboard控件名称，如贴纸/滤镜等需要点击屏幕消除的
        :param x: 横坐标 eg.200
        :param y: 纵坐标 eg.200
        :return:
        '''
        print('点击屏幕消除弹窗控件')
        actions = TouchAction(self.driver)
        actions.tap(None, x, y).release().perform()

    def set_value(self, mOperate):
        """
        输入值，代替过时的send_keys
        :param mOperate:
        :return:
        """
        self.elements_by(mOperate).clear()
        self.elements_by(mOperate).send_keys(mOperate["msg"])
        return {"result": True}

    # def get_value(self, mOperate):
    #     '''
    #     读取element的值,支持webview下获取值
    #     :param mOperate:
    #     :return:
    #     '''
    #
    #     if mOperate.get("find_type") == be.find_elements_by_id:
    #         element_info = self.elements_by(mOperate)[mOperate["index"]]
    #         if mOperate.get("is_webview", "0") == 1:
    #             result = element_info.text
    #         else:
    #             result = element_info.get_attribute("text")
    #         re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
    #         return {"result": True, "text": "".join(re_reulst)}
    #
    #     element_info = self.elements_by(mOperate)
    #     if mOperate.get("is_webview", "0") == 1:
    #         result = element_info.text
    #     else:
    #         result = element_info.get_attribute("text")
    #
    #     re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
    #     return {"result": True, "text": "".join(re_reulst)}

    # 封装常用的标签
    def elements_by(self, mOperate):

        elements = {
            be.find_element_by_id: lambda: self.driver.find_element_by_id(mOperate["element_info"]),
            be.find_elements_by_id: lambda: self.driver.find_elements_by_id(mOperate["element_info"])[mOperate['index']],
            be.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(mOperate["element_info"]),
            be.find_elements_by_xpath: lambda: self.driver.find_elements_by_xpath(mOperate["element_info"])[mOperate['index']],
            be.find_element_by_name: lambda: self.driver.find_element_by_name(mOperate['element_info']),
            be.find_elements_by_name: lambda: self.driver.find_elements_by_name(mOperate['element_info'])[mOperate['index']],
            be.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(mOperate['element_info']),
            be.find_elements_by_class_name: lambda: self.driver.find_elements_by_class_name(mOperate['element_info'])[
                mOperate['index']],
            be.find_element_by_accessibility_id: lambda: self.driver.find_element_by_accessibility_id(
                mOperate["element_info"]),
            be.find_elements_by_accessibility_id: lambda: self.driver.find_elements_by_accessibility_id(
                mOperate["element_info"])[mOperate['index']],
            be.find_element_by_ios_predicate: lambda: self.driver.find_element_by_ios_predicate(mOperate["element_info"]),
            be.find_elements_by_ios_predicate: lambda: self.driver.find_elements_by_ios_predicate(mOperate["element_info"])[mOperate['index']],
            be.find_element_by_android_uiautomator: lambda: self.driver.find_element_by_android_uiautomator(
                mOperate["element_info"])
        }
        return elements[mOperate["find_type"]]