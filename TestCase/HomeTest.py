
from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Home.PageOperate import PageOperate


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeTest(ParametrizedTestCase):
    def testFirstOpen(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Android/home/firstOpen.yaml"),
               "device": self.udid, "platformName":self.platformName, "caseName": sys._getframe().f_code.co_name}

        iOSapp = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/iOS/home/firstOpen.yaml"),
               "device": self.udid, "platformName":self.platformName, "caseName": sys._getframe().f_code.co_name}
        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def testSecondOpen(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/Android/home/secondOpen.yaml"),
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        iOSapp = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../yamls/iOS/home/secondOpen.yaml"),
                  "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()
