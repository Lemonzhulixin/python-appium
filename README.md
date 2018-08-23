# UI自动化框架（支持Android&iOS）

## 简介·Description

UI AutoTest，采用python3+appium1.8，基于PageObject框架的UI自动化测试持续集成。
* unittest参数化
* PageObject分层管理
* 用例编写基于yaml配置多关键字驱动
* 自动生成excel测试报告
* 同时支持Android/iOS
* 支持多设备执行
* 支持Windows/Mac OS （iOS必须使用Mac OS）

## 目录结构

###1.app
```
 待测apk/ipa 安装包路径
 uiautomator2等安装包路径
```

###2.Base
 ```
Android 测试相关：
BaseAdb.py
BaseAndroidPhone.py
BaseApk.py
BaseLog.py
BaseLogcat.py

iOS 测试相关：
BaseIosPhone.py
BaseIpa.py
BaseIosLog.py

数据处理相关：
BaseConfig.py
BaseExcel.py
BaseFile.py
BasePickle.py
BaseYaml.py
BaseOperate.py

测试执行相关：
BaseAppiumServer.py
BaseInit.py
BaseRunner.py
BaseElements.py

报告相关：
BaseStatisics.py
BaseError.py
BaseEmail.py
```

###3.Log
```
设备日志及持久化数据
操作日志，失败截图
crash解析结果
```

###4.PageObject
```
操作的封装及测试结果统计
测试用例模块分级
```

###5.其他
```
../Report       =====测试报告
../Runner       =====执行文件
../TestCase     =====测试用例集
../yamls        =====用例管理
```

##主要功能

###1.基础测试类及方法
  * 获取apk/ipa安装包信息
  * 获取Android/iOS设备信息
  * 自动分配端口并启动appiumserver
  * 设备日志及crashlog分析
  * 失败重试
  * 失败截图
  * 报告统计及输出
  * 邮件发送
  * case管理
  * 常用操作封装
  * 其他

###2.ymal用例demo
```buildoutcfg
测试用例yaml编写的说明文档

testinfo: 表示用例介绍
    - id: 用例id
    - title: 用例标题
    - info: 前置条件
testcase: 用例的执行步骤
    - element_info: //XCUIElementTypeStaticText[@name="剪辑"] 元素
    -  find_type: id  元素类型
        - id
        - xpath
        - name
        - text
        - ids 需要增加index
        - index 和ids/xpaths/texts等配合 
        - class_name
        - ios_id
        - predicate

    - operate_type: click4 操作
        - click
        - swipe_down
        - swipe_up
        - get_value
        - set_value
        - screen_tap
        - swipe_left
        - swipe_right
        - msg 传给set_value关键字
        - adb_tab 使用adb中的tab命令点击元素,元素必须可识别，应用于悬浮层场景
        -  get_content_desc 无法切换到webview时，用此关键字
        - press_key_code 键盘触发事件，需要传code
        - code 传给press_key_code关键字
        - is_webview:1 为1表示切换到webview,为2表示切换到原生
        - 其他关键字 用于定制一些特殊业务
    - is_time: 3 自定义暂停3秒
    - info: 点击动态列表第一条数据 操作步骤介绍
    
- check: 检查点,支持多检查点
  - element_info: //XCUIElementTypeStaticText[@name="剪辑"]
  - find_type: ids
  - index: 0
  - operate_type:
    - contrary"  相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    - contrary_getval  检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    - default_check  默认检查点，就是查找页面元素
    - compare 历史数据和实际数据对比
    - toast  toast检查
  - info: 查找是否存在历史记录

```
###3.yaml实例

```buildoutcfg

==========================================================
testinfo:
    - id: home_test_001
      title: 启动app并进入gallery
      info: 打开app并点击高级编辑
testcase:
    - element_info: camerta_n
      find_type: ios_id
      operate_type: click　
      info: 点击创作中心主按钮

    - element_info: //XCUIElementTypeStaticText[@name="剪辑"]
      find_type: xpath
      operate_type: click
      info: 点击剪辑按钮

    - element_info: 跳过
      find_type: name
      operate_type: click
      info: 跳过升级页面

    - element_info: //XCUIElementTypeStaticText[@name="剪辑"]
      find_type: xpath
      operate_type: click
      info: 点击剪辑按钮

    - element_info: 好
      find_type: name
      operate_type: click
      info: 授权存储

    - element_info: 好
      find_type: name
      operate_type: click
      info: 授权相册

check:
    - element_info: //XCUIElementTypeButton[@name="下一步"]
      find_type: xpath
      check: default_check
      info: 进入'Gallery'页面成功
```

###4.某个用例的page层

```buildoutcfg
from PageObject import Pages

class PageOperate:
    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYam(kwargs["path"]), "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "platformName": kwargs["platformName"],"caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()
```

###5.testcase层调用page层

```buildoutcfg
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
```

###6.Case入口
```buildoutcfg
def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices)) #加入测试类
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")
```

###7.实时日志展示

```buildoutcfg
testFirstOpen (TestCase.HomeTest.HomeTest) ... ==操作步骤：com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive_click  ==
==操作步骤：com.android.packageinstaller:id/permission_allow_button_click  ==
==操作步骤：com.android.packageinstaller:id/permission_allow_button_click  ==
==操作步骤：com.quvideo.xiaoying:id/wel_skip_click  ==
==操作步骤：com.quvideo.xiaoying:id/layout_fragment_creation_click  ==
==操作步骤：com.quvideo.xiaoying:id/icon1_click  ==
==操作步骤：text("跳过")_click  ==
==操作步骤：com.quvideo.xiaoying:id/icon1_click  ==
==操作步骤：text("其他相册")_   ==
Platform: android
Device: 4ed397ac
==用例_启动app并进入gallery检查点成功==
ok
```

###8.操作日志输出展示

```buildoutcfg
2018-08-23 11:51:08,390  - INFO - ----  home_test_001_启动app并进入gallery_com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive_click          ----
2018-08-23 11:51:09,711  - INFO - ----  home_test_001_启动app并进入gallery_com.android.packageinstaller:id/permission_allow_button_click          ----
2018-08-23 11:51:10,583  - INFO - ----  home_test_001_启动app并进入gallery_com.android.packageinstaller:id/permission_allow_button_click          ----
2018-08-23 11:51:19,866  - INFO - ----  home_test_001_启动app并进入gallery_com.quvideo.xiaoying:id/wel_skip_click          ----
2018-08-23 11:51:23,644  - INFO - ----  home_test_001_启动app并进入gallery_com.quvideo.xiaoying:id/layout_fragment_creation_click          ----
2018-08-23 11:51:29,023  - INFO - ----  home_test_001_启动app并进入gallery_com.quvideo.xiaoying:id/icon1_click          ----
2018-08-23 11:51:30,361  - INFO - ----  home_test_001_启动app并进入gallery_text("跳过")_click          ----
2018-08-23 11:51:33,660  - INFO - ----  home_test_001_启动app并进入gallery_com.quvideo.xiaoying:id/icon1_click          ----
2018-08-23 11:51:35,636  - INFO - ----  home_test_001_启动app并进入gallery_text("其他相册")_           ----
2018-08-23 11:51:35,698  - INFO - [CheckPoint_1]: testFirstOpen_ : OK
2018-08-23 11:51:52,341  - INFO - ----  home_test_002_进入拍摄页面_com.quvideo.xiaoying:id/img_creation_click          ----
2018-08-23 11:51:54,148  - INFO - ----  home_test_002_进入拍摄页面_com.quvideo.xiaoying:id/icon2_click          ----
2018-08-23 11:51:55,116  - INFO - ----  home_test_002_进入拍摄页面_text("允许")_click          ----
2018-08-23 11:51:56,704  - INFO - ----  home_test_002_进入拍摄页面_text("总是允许")_click          ----
2018-08-23 11:51:57,834  - INFO - ----  home_test_002_进入拍摄页面_text("总是允许")_click          ----
2018-08-23 11:52:01,559  - INFO - ----  home_test_002_进入拍摄页面_text("高清相机")_           ----
2018-08-23 11:52:01,647  - INFO - [CheckPoint_2]: testSecondOpen_ : OK

```

###9.crash解析-android

```

=========================crash================================
06-20 13:41:06.165  7638  7638 E AndroidRuntime: Process: com.quvideo.xiaoying, PID: 7638
06-20 13:41:06.165  7638  7638 E AndroidRuntime: java.lang.NullPointerException: Attempt to read from field 'int com.quvideo.xiaoying.datacenter.social.publish.PublishTaskInfo.step' on a null object reference
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.d.a.aI(SourceFile:67)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.d.a.aK(SourceFile:123)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.d.a.a(SourceFile:151)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.SocialPublishBaseActivity.da(SourceFile:1531)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.SocialPublishBaseActivity.aaM(SourceFile:1565)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.c.b$1.acg(SourceFile:312)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.videoeditor.j.a.a$4.m(SourceFile:650)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.ui.dialog.c.onClick(SourceFile:165)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.view.View.performClick(View.java:6291)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.view.View$PerformClick.run(View.java:24931)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.os.Handler.handleCallback(Handler.java:808)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.os.Handler.dispatchMessage(Handler.java:101)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.os.Looper.loop(Looper.java:166)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.app.ActivityThread.main(ActivityThread.java:7425)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at java.lang.reflect.Method.invoke(Native Method)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:245)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:921)
06-20 13:41:06.367   732   732 E wificond: Failed to get NL80211_RATE_INFO_NOISE
06-20 13:41:06.367   732   732 E wificond: Failed to get NL80211_RATE_INFO_SNR
06-20 13:41:06.367   732   732 E wificond: Failed to get NL80211_STA_INFO_CNAHLOAD
06-20 13:41:07.841  1157  1174 I chatty  : uid=1000(system) android.ui expire 3 lines
06-20 13:41:07.851  1448  1780 I HwNetworkPolicyManager: getHwUidPolicy uid = 10063 policy = 0
06-20 13:41:07.878  1157  2823 I chatty  : uid=1000(system) Binder:1157_F expire 1 line
06-20 13:41:07.879  1157  1350 I chatty  : uid=1000(system) ConnectivitySer expire 14 lines
06-20 13:41:07.879  1157  8282 I chatty  : uid=1000(system) Binder:1157_1B expire 10 lines
06-20 13:41:07.893  1157  8281 I chatty  : uid=1000(system) Binder:1157_1A expire 12 lines
06-20 13:41:07.900 17940 17940 I ActivityThread: Removing dead content provider:android.content.ContentProviderProxy@b3b0cdb
06-20 13:41:07.911  1157 14597 I chatty  : uid=1000(system) Binder:1157_1F expire 9 lines
06-20 13:41:07.936  1157  1167 I chatty  : uid=1000(system) Binder:1157_1 expire 14 lines
=========================crash=========================
06-20 13:41:06.165  7638  7638 E AndroidRuntime: Process: com.quvideo.xiaoying, PID: 7638
06-20 13:41:06.165  7638  7638 E AndroidRuntime: java.lang.NullPointerException: Attempt to read from field 'int com.quvideo.xiaoying.datacenter.social.publish.PublishTaskInfo.step' on a null object reference
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.d.a.aI(SourceFile:67)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.d.a.aK(SourceFile:123)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.d.a.a(SourceFile:151)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.SocialPublishBaseActivity.da(SourceFile:1531)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.SocialPublishBaseActivity.aaM(SourceFile:1565)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.app.publish.c.b$1.acg(SourceFile:312)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.videoeditor.j.a.a$4.m(SourceFile:650)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.quvideo.xiaoying.ui.dialog.c.onClick(SourceFile:165)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.view.View.performClick(View.java:6291)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.view.View$PerformClick.run(View.java:24931)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.os.Handler.handleCallback(Handler.java:808)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.os.Handler.dispatchMessage(Handler.java:101)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.os.Looper.loop(Looper.java:166)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at android.app.ActivityThread.main(ActivityThread.java:7425)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at java.lang.reflect.Method.invoke(Native Method)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.android.internal.os.Zygote$MethodAndArgsCaller.run(Zygote.java:245)
06-20 13:41:06.165  7638  7638 E AndroidRuntime:  at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:921)
06-20 13:41:06.367   732   732 E wificond: Failed to get NL80211_RATE_INFO_NOISE
06-20 13:41:06.367   732   732 E wificond: Failed to get NL80211_RATE_INFO_SNR
06-20 13:41:06.367   732   732 E wificond: Failed to get NL80211_STA_INFO_CNAHLOAD
06-20 13:41:07.841  1157  1174 I chatty  : uid=1000(system) android.ui expire 3 lines
06-20 13:41:07.851  1448  1780 I HwNetworkPolicyManager: getHwUidPolicy uid = 10063 policy = 0
06-20 13:41:07.878  1157  2823 I chatty  : uid=1000(system) Binder:1157_F expire 1 line
06-20 13:41:07.879  1157  1350 I chatty  : uid=1000(system) ConnectivitySer expire 14 lines
06-20 13:41:07.879  1157  8282 I chatty  : uid=1000(system) Binder:1157_1B expire 10 lines
06-20 13:41:07.893  1157  8281 I chatty  : uid=1000(system) Binder:1157_1A expire 12 lines
06-20 13:41:07.900 17940 17940 I ActivityThread: Removing dead content provider:android.content.ContentProviderProxy@b3b0cdb
06-20 13:41:07.911  1157 14597 I chatty  : uid=1000(system) Binder:1157_1F expire 9 lines
06-20 13:41:07.936  1157  1167 I chatty  : uid=1000(system) Binder:1157_1 expire 14 lines
06-20 13:41:07.942  1157  1367 I chatty  : uid=1000(system) CallbackHandler expire 2 lines
06-20 13:41:07.958  1157  1182 I chatty  : uid=1000(system) android.display expire 1 line

```

###10.报告输出
```
路径：../Report
```

##运行环境

1. Windows 7及以上 / OSX
2. Android SDK的执行环境
3. python3.x
4. Appium 1.7.x及以上

##代码获取

最新的稳定代码会推送到lemon分支上，直接clone即可使用。
```
git clone git@192.168.1.33:QAGroup/UItest.git
```

##执行注意事项
1.安装包路径指定：Base.BaseInit
```
apkPath = PATH("../app/VivaVideo_7.2.5.apk")  # 测试的app路径
ipaPath = PATH("../app/xiaoying.ipa")  # 测试的app路径
```

2.为了避免同一台PC上同时连接android和iOS设备时，获取设备问题，将runner文件
两个平台分开处理
```
Android执行: python3 runner.py

iOS执:python3 runner_iOS.py
```

##目前的遗留问题

- 因为初始化log路径的问题，暂时未解决crashlog路径获取
- email邮件发送尚未调试
- iOS crashlog分析
- 控件集参数化
- 多设备执行还有点问题
- 当遇到有些用例比较麻烦，必须单独写page层

##后续计划

- 测试数据DB存储
- 结果集分析

