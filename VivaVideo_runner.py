#coding=utf-8
import os
import time
import unittest
from iOS import script_ultils as sc, HTMLTestRunner


def run_test():
    # 用例路径
    sc_path1 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_ahead")
    sc_path2 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_camera")
    sc_path3 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_edit")
    sc_path4 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_preview")
    sc_path5 = os.path.join(os.getcwd(), "iOS/VivaVideo/test_creations/test_publish")

    suite1 = unittest.TestLoader().discover(sc_path1,pattern="*.py", top_level_dir=None)
    suite2 = unittest.TestLoader().discover(sc_path2, pattern="*.py", top_level_dir=None)
    suite3 = unittest.TestLoader().discover(sc_path3, pattern="*.py", top_level_dir=None)
    suite4 = unittest.TestLoader().discover(sc_path4, pattern="*.py", top_level_dir=None)
    suite5 = unittest.TestLoader().discover(sc_path5, pattern="*.py", top_level_dir=None)

    suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5])
    return suite

if __name__ == '__main__':
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxx Start Test xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    now_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    report_path = sc.path_lists[2]
    filename = report_path + now_time + ".html"
    fp = open(filename, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='VivaVideo UI（iOS） 测试结果',
        description='详细测试报告',
        verbosity = 2
    )
    runner.run(run_test())
    fp.close()

    print('关闭appium')
    time.sleep(1)
    cmd_kill = 'pkill node'
    os.system(cmd_kill)
    print("xxxxxxxxxxxxxxxxxxxxxxxxx Finish Test xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")