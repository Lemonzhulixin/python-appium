from Base.BaseError import get_error
from Base.BaseOperate import OperateElement
from Base.BaseElements import Element as be
from PageObject.SumResult import statistics_result


class FeedbackPage:
    '''
    滑动删除收藏
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
    '''

    def __init__(self, kwargs):
        self.driver = kwargs["driver"]
        if kwargs.get("launch_app", "0") == "0":  # 若为空，重新打开app
            self.driver.launch_app()
        # self.path = kwargs["path"]
        self.operateElement = OperateElement(self.driver)
        self.isOperate = True
        self.test_msg = kwargs["test_msg"]
        self.testInfo = self.test_msg[1]["testinfo"]
        self.testCase = self.test_msg[1]["testcase"]
        self.testcheck = self.test_msg[1]["check"]
        self.device = kwargs["device"]
        self.logTest = kwargs["logTest"]
        self.caseName = kwargs["caseName"]
        self.platformName = kwargs["platformName"]
        self.get_value = []
        self.is_get = False  # 检查点特殊标志，结合get_value使用。若为真，说明检查点要对比历史数据和实际数据
        self.msg = ""

    '''
     操作步骤
     logTest 日记记录器
    '''

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

    def operate(self):
        m_s_g = self.msg + "\n" if self.msg != "" else ""
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, self.logTest, self.device)
            if not result["result"]:
                msg = "执行过程中失败，请检查元素是否存在" + item["element_info"]
                print(msg)
                self.testInfo[0]["msg"] = msg
                self.msg = m_s_g + msg
                self.isOperate = False
                return False

            if item.get("operate_type", "0") == be.SWIPE_UP:  # 根据元素上滑动
                width, height = self.get_size()
                start_x = width // 2
                start_bottom = height - height // 8
                el_up = self.driver.find_elements_by_id(item["element_info"])
                while True:
                    try:
                        el_up.click()
                        break
                    except:
                        self.swipe_by_ratio(start_x, start_bottom, 'up', 0.5, 500)


            if item.get("operate_type", "0") == be.GET_VALUE:
                self.get_value.append(result["text"])
        return True

    def checkPoint(self, kwargs={}):
        result = self.check(kwargs)
        if self.test_msg[0] is not False:  # 如果用例编写正确
            if result is not True and be.RE_CONNECT:
                self.msg = "用例失败并重连过一次，失败原因:" + self.testInfo[0]["msg"]
                self.logTest.buildStartLine(self.caseName + "_失败重连")  # 记录日志
                # self.operateElement.switchToNative()
                self.driver.launch_app()
                self.isOperate = True
                self.get_value = []
                self.is_get = False
                self.operate()
                result = self.check(kwargs)
                self.testInfo[0]["msg"] = self.msg

        statistics_result(result=result, testInfo=self.testInfo, caseName=self.caseName,
                          driver=self.driver, logTest=self.logTest, devices=self.device,
                          testCase=self.testCase, platformName=self.platformName,
                          testCheck=self.testcheck)

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    contrary：相反检查点，传1表示如果检查元素存在就说明失败
    toast: 表示提示框检查点
    contrary_getval: 相反值检查点，如果对比成功，说明失败
    check_point: 自定义检查结果    
    '''

    def check(self, kwargs):
        result = True
        m_s_g = self.msg + "\n" if self.msg != "" else ""
        # 如果有重跑机制，成功后会默认把日志传进来


        # if kwargs.get("check_point", "0") != "0": 自定义检查点
        #     return kwargs["check_point"]

        if self.isOperate:
            for item in self.testcheck:
                # toast检查，存在则说明成功
                if kwargs.get("check", be.DEFAULT_CHECK) == be.TOAST:
                    result = \
                    self.operateElement.toast(item["element_info"], testInfo=self.testInfo, logTest=self.logTest)[
                        "result"]
                    if result is False:
                        m = get_error(
                            {"type": be.DEFAULT_CHECK, "element_info": item["element_info"], "info": item["info"]})
                        self.msg = m_s_g + m
                        print(m)
                        self.testInfo[0]["msg"] = m
                    break
                else:
                    resp = self.operateElement.operate(item, self.testInfo, self.logTest, self.device)
                    # 默认检查点，就是查找页面元素
                if kwargs.get("check", be.DEFAULT_CHECK) == be.DEFAULT_CHECK and not resp["result"]:
                    m = get_error(
                        {"type": be.DEFAULT_CHECK, "element_info": item["element_info"], "info": item["info"]})
                    self.msg = m_s_g + m
                    print(m)
                    self.testInfo[0]["msg"] = m
                    result = False
                    break
                # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
                if kwargs.get("check", be.DEFAULT_CHECK) == be.CONTRARY and resp["result"]:
                    m = get_error({"type": be.CONTRARY, "element_info": item["element_info"], "info": item["info"]})
                    self.msg = m_s_g + m
                    print(m)
                    self.testInfo[0]["msg"] = self.msg
                    result = False
                    break
                # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
                if kwargs.get("check", be.DEFAULT_CHECK) == be.CONTRARY_GETVAL and self.is_get and resp["result"] \
                        in self.get_value:
                    m = get_error(
                        {"type": be.CONTRARY_GETVAL, "current": item["element_info"], "history": resp["text"]})
                    self.msg = m_s_g + m
                    print(m)
                    self.testInfo[0]["msg"] = m
                    result = False
                    break
                # 历史数据和实际数据对比
                if kwargs.get("check", be.DEFAULT_CHECK) == be.COMPARE and self.is_get and resp["text"] \
                        not in self.get_value:  # 历史数据和实际数据对比
                    result = False
                    m = get_error({"type": be.COMPARE, "current": item["element_info"], "history": resp["text"]})
                    self.msg = m_s_g + m
                    print(m)
                    self.testInfo[0]["msg"] = m
                    break
        else:
            result = False
        return result


if __name__ == "__main__":
    pass
