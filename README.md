# UItest Scripts

## 简介·Description

UItest Scripts，小影app的UI自动化脚本，在UI迭代变化不太迅速的场景下，用于简化测试中部分需要手工反复执行的部分。目前覆盖了测试用例中大约70%的用例条目，覆盖细节见下文。暂时只支持Android平台上的小影app。

## 主要功能·Features

1. 全流程的UI测试，所有脚本可以作为一个全流程遍历完。
2. 分模块测试
  * 每个脚本文件可以作为单独的模块进行测试
  * 每个文件夹可以作为一个大的模块进行测试

## 模块说明

主要模块说明在代码注释头与函数注释内已经标注，详细说明文档待所有功能模块完善与优化后，做出补充。

## 运行环境

UItest Scripts为python3.x编写的脚本，依赖于appium执行相关操作，运行依赖如下所示：
1. Windows 7及以上 / OSX / Linux，其中linux平台上未作完全的功能测试；
2. Android SDK的执行环境；
3. python3.x可执行环境，已在python 3.6.4环境下测试通过，需要以下python模块；
  * pytest
  * pytest-html
  * Appium-Python-Client
4. appium 1.7+，采用了appium中部分新的方法，使用1.7版本以下可能无法正常执行；
5. nodejs；

## 执行方法

### 脚本获取

最新的稳定代码会推送到master分支上，直接clone即可使用。
```
git clone git@192.168.1.33:QAGroup/UItest.git
```

### 在本地环境运行脚本

1. 为了避免端口冲突，为每台设备单独启动一个appium进程，例如：
```
appium -p 4800 -bp 4900 -dc "{\"deviceName\": \"c0d2dc31\", \"noReset\": true}"
```
参数说明：
* -p: 该端口接受webdriver请求，默认开启4723端口，上面示例使用4800；
* -bp: 该端口用于bootstrap接受请求并把命令发给UiAutomator或插桩体系，是和Android通信用的端口，默认开启4724，示例使用4900；
  + -dc：json格式的参数列表
    * deviceName: Android设备id，使用`adb devices`获取
    * noReset: 不重置app数据，默认为false

appium命令行最新参数详见： [Appium server arguments](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/server-args.md)

appium json参数详见：[The --default-capabilities flag，](https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/default-capabilities-arg.md)

注：OSX环境不需要反斜杠'\'转义，linux bash环境下不需要反斜杠'\'转义，zsh环境下需要转义。

2. 进入脚本工程根目录，其中`test_main.py`是用来执行测试的主脚本，修改第11行的`case_path`变量为需要执行的测试模块，例如：
```
case_path = 'Android/VivaVideo/test_video/test_videos.py'
```
这样后续测试就会执行`Android/VivaVideo/test_video/test_videos.py`这个测试脚本。

同理，也可以使用文件夹路径，例如：
```
case_path = 'Android/VivaVideo/test_video/'
```
则会执行`test_video`目录下的所有测试脚本。

3. 进入脚本工程根目录，在shell中输入以下命令，执行需要执行的模块，例如：
```
python3 -m Android.test_main -p 4800 -pl Android -v 5.0.2 -pk com.quvideo.xiaoying -ac .XiaoYingActivity
```

脚本命令行参数解释：
* -m: 需要执行的python模块，目前只支持`Android.test_main`
* -p/--port: 该端口接受webdriver请求，默认开启4723端口，上面示例使用4800，与先前appium的session对应，必填；
* -pl/--platform: 设备操作系统平台，当前仅支持Android，必填；
* -v/--version：设备系统版本，必填；
* -pk/--package：包名，Android平台必填；
* -ac/--activity：启动app的activity，Android平台上必填。

## 目前的遗留问题

- [ ] 登录模块大概率登录失败，问题待定位解决；

- [ ] 全面屏设备支持问题，有些控件在全面屏设备上找不到，待解决；

- [ ] 脚本对用例的覆盖程度，待后续用例完善调整后跟进；

- [ ] 代码风格问题，目前没有统一编程规范，导致代码风格很乱，可读性很差，后续需要统一；

- [ ] 代码健壮性不强，目前代码内考虑情况并未面面俱到，偶尔会复现因脚本代码问题而出现失败的情况，待完善；

- [ ] 用户友好程度不够，执行略为麻烦，待优化。


## 脚本编写中遇到的常见问题

- 用户输入模块问题

  1. 输入后找不到其它控件导致失败，解决方法：输入后使用appium python client的`hide_keyboard`方法先将键盘隐藏，再尝试查找；
  2. 需要提交输入，但是提交无响应，解决方法：暂时未找到完美的解决方案，可更换成能够响应`KEYCODE_ENTER`的输入法，例如”搜狗输入法“；
  3. 混合输入数字、字母或汉字时，注意不要使用输入法的联想功能，可能会输入不正确的结果。

- 等待时长问题，连续的查找点击控件，如果速度过快，设备可能暂时没有完成处理，导致失败。

  目前的等待时间大多依靠手动处理的经验，是的编写脚本效率较低；另一方面，过多的插入等待，也会导致脚本执行时间过长、效率低下。待继续探索更好的解决方案。

- 弹窗问题，需要考虑app内可能出现的弹窗，没有对弹窗加以判断的情况常常导致用例测试失败。

  至于弹窗可能出现的场景与情况，主要靠摸索与经验。

- 测试用例的粒度问题

  1. 粒度细化到足够小，以单个函数对应单个用例步骤，可以尽量减小依赖关系，符合软件工程”高内聚，低耦合“的原则，对单个用例的成功执行而言也会有足够高的保障。

     但是从实际测试场景来看，这样会导致效率过于低下，在完整的测试流程中，每个用例执行前先要初始化，结束后销毁环境，依此类推执行下一个用例，时间开销过大。

  2. 大粒度的情况，以单个脚本对应一个用例的完整流程，可以解决上述测试效率的问题，但是增大了测试失败的风险，因为流程中依赖较多，可能会使得后续流程的执行受到前面模块的影响。而且调试时因为需要一次性包含多个用例，耗费时间更多，使得进度缓慢。

  3. 目前解决方案是：每个用例中的一个主要步骤对应一个测试函数，函数执行完成后退回app主页面，下一个测试函数会从测试主页面进入，开始继续执行。

     这样的做法从效率与风险上均介于1、2之间，但是会造成大量代码冗余，可读性降低，脚本编写时间更长，因此下一步也需要优化这个问题。

