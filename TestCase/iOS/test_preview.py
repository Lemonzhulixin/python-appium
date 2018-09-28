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

class PreviewTest(ParametrizedTestCase):

    def repalce(self, tc, tc_temp):
        if self.platformName == 'android':
            ReplaceYaml(tc, tc_temp, el_android)
        elif self.platformName == 'iOS':
            ReplaceYaml(tc, tc_temp, el_iOS)

    def test_pre_album(self):
        tc = PATH("../yamls/iOS/test_preview/test_pre_album.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_pre_music(self):
        tc = PATH("../yamls/iOS/test_preview/test_pre_music.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_pre_music_del(self):
        tc = PATH("../yamls/iOS/test_preview/test_pre_music_del.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    def test_pre_theme(self):
        tc = PATH("../yamls/iOS/test_preview/test_pre_theme.yaml")
        self.repalce(tc, tc_temp)
        app = {"logTest": self.logTest, "driver": self.driver, "path": tc_temp,
               "device": self.udid, "platformName": self.platformName, "caseName": sys._getframe().f_code.co_name}

        page = PageOperate(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(PreviewTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(PreviewTest, cls).tearDownClass()
