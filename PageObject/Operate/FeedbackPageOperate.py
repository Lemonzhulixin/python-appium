from Base.BaseYaml import getYam
from PageObject.Pages import SettingsFeedbackPage


class FeedbackPageOperate:
    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYam(kwargs["path"]), "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "platformName": kwargs["platformName"],"caseName": kwargs["caseName"]}
        self.page = SettingsFeedbackPage.FeedbackPage(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()


if __name__ == "__main__":
    pass
