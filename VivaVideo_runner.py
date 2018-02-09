#coding=utf-8
import time
import unittest
from Base import HTMLTestRunner, Log
from TestCase import Settings,Export,Gallery,Home,Login,Share,Template
from TestCase.Camera import Camera_music,Camera_collage,Camera_self,Camera_normal,Camera_cancel
from TestCase.Edit import Edit_create,Edit_add_clips,Edit_clip_edit,Edit_collage,Edit_filter,Edit_fx,Edit_multi_music,Edit_sound,Edit_sticker,Edit_text,Edit_transition
from TestCase.Preview import Preview_music,Preview_theme


def All_TestCases():
    #设置每个类中case的执行顺序
    """suite = unittest.TestSuite()
    suite.addTest(Home.Home("test_home_001"))
    suite.addTest(Home.Home("test_home_002"))
    suite.addTest(Home.Home("test_home_003"))
    ...
    return suite

    #一次执行多个py文件，顺序随机执行
    # 用例路径
    TestCase_path = os.path.join(os.getcwd(), "TestCase")
    # 报告存放路径
    Report_path = os.path.join(os.getcwd(), "Report")

    def TestCase_All():
        Discover = unittest.defaultTestLoader.discover(TestCase_path, pattern="*.py", top_level_dir=None)
        return Discover
    """

    #设置每个py文件中类的执行顺序
    #suite0 = unittest.TestLoader().loadTestsFromTestCase(Login.Login)
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Settings.Settings)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Gallery.Gallery)
    suite3 = unittest.TestLoader().loadTestsFromTestCase([Camera_normal.Normal,Camera_self.Self,Camera_collage.Collage,Camera_music.Music,Camera_cancel.Cancel])
    suite4 = unittest.TestLoader().loadTestsFromTestCase(Home.Home)
    suite5 = unittest.TestLoader().loadTestsFromTestCase([Preview_theme.Theme,Preview_music.Music])
    suite6 = unittest.TestLoader().loadTestsFromTestCase([Edit_create.Create,Edit_clip_edit.Clip_edit,Edit_filter.Filter,Edit_multi_music.Multi_Music,Edit_text.Text,
                                                          Edit_collage.Collage,Edit_sticker.Sticker,Edit_transition.Transition,Edit_sound.Sound,Edit_fx.FX,Edit_add_clips.Add_Clips])
    suite7 = unittest.TestLoader().loadTestsFromTestCase(Export.Export)
    suite8 = unittest.TestLoader().loadTestsFromTestCase(Share.Share)
    suite9 = unittest.TestLoader().loadTestsFromTestCase(Template.Template)
    suite = unittest.TestSuite([suite1,suite2,suite3,suite4,suite5,suite6,suite7,suite8,suite9])

    return suite

if __name__ == '__main__':
    print("开始测试")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    log = Log.get_logcat()
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    filename = "/Users/zhulixin/Desktop/UI_VivaVideo/Report/" + now_time + ".html"
    fp = open(filename, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='VivaVideo UI 测试结果',
        description='详细测试报告',
        verbosity = 2
        #retry = 0 失败case重试次数
    )
    runner.run(All_TestCases())
    fp.close()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("测试结束")