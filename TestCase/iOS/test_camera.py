from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Operate.PageOperate import PageOperate
from Base.BaseReplace import ReplaceYaml


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

tc_temp = PATH("../yamls/temp.yaml")
el_android = PATH("../yamls/el_android.yaml")
el_iOS = PATH("../yamls/el_iOS.yaml")

class CameraTest(ParametrizedTestCase):

    def repalce(self, tc, tc_temp):
        if self.platformName == 'android':
            ReplaceYaml(tc, tc_temp, el_android)
        elif self.platformName == 'iOS':
            ReplaceYaml(tc, tc_temp, el_iOS)

    def test_autodyne(self):
        tc = PATH("../yamls/iOS/test_camera/test_autodyne.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_music_change(self):
        tc = PATH("../yamls/iOS/test_camera/test_music_change.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_music_redo(self):
        tc = PATH("../yamls/iOS/test_camera/test_music_redo.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_normal_cancel(self):
        tc = PATH("../yamls/iOS/test_camera/test_normal_cancel.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_normal_filter(self):
        tc = PATH("../yamls/iOS/test_camera/test_normal_filter.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_normal_save(self):
        tc = PATH("../yamls/iOS/test_camera/test_normal_save.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_normal_settings(self):
        tc = PATH("../yamls/iOS/test_camera/test_normal_settings.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_normal_shot(self):
        tc = PATH("../yamls/iOS/test_camera/test_normal_shot.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(CameraTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CameraTest, cls).tearDownClass()
