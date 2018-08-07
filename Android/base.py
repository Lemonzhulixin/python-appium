# -*- coding: utf-8 -*-
from iOS import script_ultils as sc
import time
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from iOS import iOS_elements
from appium.webdriver.common.touch_action import TouchAction
import random


# 获取屏幕尺寸
width, height = sc.get_size()

def find_element_click(method, timeout, el, duration = 1):
    '''
    等待并点击某一控件.
    :param method: 寻找控件的方法
    :param timeout: timeout时长
    :param el: 控件元素
    :param duration: 单次点击间隔时长
    :return:
    '''
    if method == 'name':
        try:
            WebDriverWait(sc.driver, timeout, duration).until(
                lambda x: x.find_element_by_name(el)).click()
        except TimeoutException:
            return False
    elif method == 'xpath':
        try:
            WebDriverWait(sc.driver, timeout, duration).until(
                lambda x: x.find_element_by_xpath(el)).click()
        except TimeoutException:
            return False
    elif method == 'id':
        try:
            WebDriverWait(sc.driver, timeout, duration).until(
                lambda x: x.find_element_by_accessibility_id(el)).click()
        except TimeoutException:
            return False
    elif method == 'predicate':
        try:
            WebDriverWait(sc.driver, timeout, duration).until(
                lambda x: x.find_element_by_ios_predicate(el)).click()
        except TimeoutException:
            return False
    return True

def home_first_click(el_fun):
    '''
    从创作页面进入各个入口.
    :param fun: 打开的入口
    :param el: 点击的控件
    :return:
    '''
    """
    视频剪辑/高清拍摄/次要功能位置相关/更多草稿等
    """
    sc.logger.info('点击创作中心主按钮')
    try:
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_accessibility_id(iOS_elements.el_home_create)).click()
    except TimeoutException:
        sc.logger.info('当前已经是在创作页面')

    sc.logger.info('点击 %s', el_fun)
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(el_fun)).click()
    except TimeoutException:
        sc.logger.info('向左滑动')
        el_template = sc.driver.find_element_by_name('素材中心')
        coord_x = el_template.location.get('x')
        coord_y = el_template.location.get('y')
        sc.swipe_by_ratio(coord_x, coord_y, 'left', 0.6, 500)  # 从素材中心向左滑动

        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(el_fun)).click()

def open_draft(el_draft):
    '''打开一个草稿工程并进入编辑页面'''
    sc.logger.info('点击一个草稿封面')
    try:
        find_element_click('xpath', 5, el_draft)
        sc.logger.info('尝试点击“编辑该视频”')
        try:
            WebDriverWait(sc.driver, 5, 1).until(
                lambda x: x.find_element_by_name("编辑此视频")).click()
        except TimeoutException:
            sc.logger.info('该视频已经在编辑页，跳过此步骤')
    except TimeoutException:
        sc.logger.info('无草稿工程，请创建一个草稿')

def home_vip_ad():
    """首页-订阅及广告按钮"""
    sc.logger.info('VIP订阅页面展示')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.el_home_vip)).click()

    sc.logger.info('退出VIP订阅页面')
    sc.driver.find_element_by_name(iOS_elements.el_vip_close).click()

    sc.logger.info('首页广告展示及刷新')
    sc.driver.find_element_by_xpath(iOS_elements.el_home_ad).click()

    sc.logger.info('返回首页')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.el_ad_back)).click()

def gallery_clip_add(type_clip, number):
    '''
    Gallery添加镜头（图片/视频）
    :param clip: 添加的素材类型
    :param number: 添加的素材个数
    :return:
    '''
    sc.logger.info('开始添加 %s', type_clip)
    clip_list = WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_elements_by_name(iOS_elements.el_gallery_cho))
    if len(clip_list) >= number:
        clip_list = clip_list[:number]
    for el_clip in clip_list:
        el_clip.click()

def gallery_clip_op():
    '''gallery-图片/视频相关操作'''
    video_flag = 0
    sc.logger.info('勾选一个镜头')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda el: el.find_element_by_name(iOS_elements.el_gallery_cho)).click()

    sc.logger.info('旋转')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda el: el.find_element_by_name(iOS_elements.btn_gallery_rotate)).click()

    try:
        sc.logger.info('点击播放按钮')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.btn_gallery_play)).click()

        video_flag = 1
    except TimeoutException:
        sc.logger.info('当前选择的是图片，不支持播放')

    if video_flag == 1:
        sc.logger.info('点击裁切按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.btn_gallery_trim)).click()

def video_capture(cp_method, btn_rec, duration = 5):
    '''
    默认拍摄5s
    :param cp_method: 点拍/长按拍摄
    :param btn_rec: 拍摄按钮控件
    :param duration: 拍摄视频时长，默认拍摄5s
    :return:
    '''
    """
    美颜自拍：btn_capture = WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(elements.el_cp_self))
            
    高清拍摄：btn_capture = WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(elements.el_cp_normal))
    
    音乐视频：btn_capture = WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(elements.el_cp_music))
    """

    btn_rec = btn_rec
    if cp_method == '点拍':
        # 点拍
        sc.logger.info('开始录制')
        btn_rec.click()

        sc.logger.info('录制 %d 秒后点击录制按钮停止录制', duration)
        time.sleep(duration)
        btn_rec.click()
    elif cp_method == '长按拍摄':
        # 长按拍摄
        sc.logger.info('长按拍摄 %d 秒', duration)
        actions = TouchAction(sc.driver)
        actions.long_press(btn_rec, None, None, duration * 1000).release().perform()

    try:
        sc.logger.info('点击确认按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_cam_next)).click()
    except TimeoutException:
        sc.logger.info('当前是音乐视频拍摄且音乐时长较短，已自动跳转预览页')

def camera_settings():
    """拍摄-设置相关."""
    sc.logger.info('点击设置按钮')
    find_element_click('name', 5, iOS_elements.el_cam_setting)

    sc.logger.info('闪光灯-开')
    try:
        find_element_click('name', 5, iOS_elements.el_cam_flash)
    except NoSuchElementException:
        sc.logger.info('当前为前置拍摄，无闪光灯选项')

    sc.logger.info('网格显示')
    find_element_click('name', 5, iOS_elements.el_cam_grid)

    sc.logger.info('倒计时')
    for i in range(4):
        find_element_click('name', 5, iOS_elements.el_cam_time)

    sc.logger.info('退出设置选项')
    find_element_click('name', 5, iOS_elements.el_cam_setting)

    sc.logger.info('前后置切换')
    find_element_click('name', 5, iOS_elements.el_cam_switch)

    sc.logger.info('视频尺寸,全屏切换到3:4')
    find_element_click('name', 5, iOS_elements.el_ful)

    sc.logger.info('视频尺寸,3:4切换到1:1')
    find_element_click('name', 5, iOS_elements.el_fou)

    sc.logger.info('视频尺寸,1:1切换到全屏')
    find_element_click('name', 5, iOS_elements.el_one)

    sc.logger.info('切换拍摄模式:高清相机->自拍美颜')
    el_self = "自拍美颜"
    el_normal = "高清相机"
    el_music = "音乐视频"
    find_element_click('name', 5, el_self)

    sc.logger.info('切换拍摄模式:自拍美颜->高清相机')
    find_element_click('name', 5, el_normal)

    sc.logger.info('切换拍摄模式:高清相机->音乐视频')
    find_element_click('name', 5, el_music)

    sc.logger.info('返回创作中心主界面')
    find_element_click('name', 5, iOS_elements.el_cam_close)
    sc.logger.info('拍摄-设置相关测试完成')

def screen_tap(fun, x, y):
    '''
    :param fun: 要消除的storyboard控件名称，如贴纸/滤镜等需要点击屏幕消除的
    :param x: 横坐标 eg.200
    :param y: 纵坐标 eg.200
    :return:
    '''
    sc.logger.info('点击屏幕消除 %s 控件', fun)
    actions = TouchAction(sc.driver)
    actions.tap(None, x, y).release().perform()

def swipe_left(el_loc, ratio, duration):
    '''
    以某个元素作为标准点，左滑动
    :param el_loc: 某标准点元素
    :param ratio: 滑动距离与屏幕的比例，范围0到1
    :param duration: 滑动时间，单位ms
    :return:
    '''
    sc.logger.info('向左滑动')
    coord_x = el_loc.location.get('x')
    coord_y = el_loc.location.get('y')
    sc.swipe_by_ratio(coord_x, coord_y, 'left', ratio, duration)  # 从素材中心向左滑动

def more_download(btn_more):
    '''
    :param btn_more: 下载更多控件
    :return:
    '''
    sc.logger.info('下载更多')
    try:
        sc.driver.find_element_by_name(btn_more).click()
    except:
        sc.logger.info('当前页面是vip订阅页面')
        sc.driver.find_element_by_name(iOS_elements.el_vip_close).click()

        sc.logger.info('重新点击下载更多')
        sc.driver.find_element_by_name(btn_more).click()

def material_download(method, type, btn_download):
    '''
    素材下载并使用
    :param method: 控件获取方法
    :param type: 素材类别
    :param btn_download: 下载控件
    :return:
    '''
    sc.logger.info('%s 下载测试', type)

    if method == 'name':
        try:
            sc.logger.info('点击下载按钮')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda x: x.find_element_by_name(btn_download)).click()
        except NoSuchElementException:
            sc.logger.info('当前页面所有素材已下载完成')
    elif method == 'xpath':
        try:
            sc.logger.info('点击下载按钮')
            WebDriverWait(sc.driver, 10, 1).until(
                lambda x: x.find_element_by_xpath(btn_download)).click()
        except NoSuchElementException:
            sc.logger.info('当前页面所有素材已下载完成')

    sc.logger.info('检查素材下载是否成功')
    WebDriverWait(sc.driver, 30, 1).until(
        lambda x: x.find_element_by_name("使用")).click()

def material_manager(type, btn_del):
    '''
    素材中心-管理
    :param type: 素材类别
    :param btn_del: 删除按钮
    :return:
    '''
    sc.logger.info('点击管理按钮')
    sc.driver.find_element_by_name(iOS_elements.btn_manager).click()

    btn_del = sc.driver.find_element_by_name(btn_del)
    btn_del.click()
    try:
        sc.driver.find_element_by_name("确认").click()
    except NoSuchElementException:
        sc.logger.info('%s删除不需要确认', type)

    sc.logger.info('删除完成后，返回素材中心页面')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.el_com_back)).click()

    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.el_com_back)).click()

def material_used(btn_download):
    sc.logger.info('下拉刷新')
    refresh('down', 0.3, 300, 1)

    try:
        sc.logger.info('点击"使用"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("使用")).click()
    except:
        sc.logger.info('无已下载的滤镜，下载后再"使用"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(btn_download)).click()

        WebDriverWait(sc.driver, 20, 1).until(
            lambda x: x.find_element_by_name("使用")).click()

def refresh(direct, ratio, duration, times = 1):
    '''
    刷新
    :param direct: 滑动方向，只支持'up'、'down'两种方向参数
    :param ratio: 滑动距离与屏幕的比例，范围0到1
    :param duration:滑动时间，单位ms
    :param times: 滑动次数，默认1次
    :return:
    '''
    start_x = width // 2
    start_y = height // 8
    start_bottom = height - start_y

    if direct == 'down':
        for i in range(times):
            sc.logger.info('第 %d 次下拉刷新', i)
            sc.swipe_by_ratio(start_x, start_y, 'down', ratio, duration)
            time.sleep(.300)
    elif direct == 'up':
        for i in range(times):
            sc.logger.info('第 %d 次上滑动', i)
            sc.swipe_by_ratio(start_x, start_bottom, 'up', ratio, duration)
            time.sleep(.300)

def music_add():
    '''配乐下载并添加'''
    sc.logger.info('点击第一首已下载音频试听')
    try:
        sc.logger.info('点击下载按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_mus_download)).click()
    except:
        sc.logger.info('当前页面已无未下载音频')

    sc.logger.info('选择一首音频试听')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.el_mus_firstaudio)).click()

    sc.logger.info('点击“添加”按钮')
    sc.driver.find_element_by_name('添加').click()

def preview_music():
    '''预览页添加配乐'''
    sc.logger.info('点击“添加配乐”按钮')
    try:
        sc.driver.find_element_by_name("添加配乐").click()
    except:
        sc.driver.find_element_by_name("更改配乐").click()

    try:
        sc.logger.info('删除配乐')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_music_del)).click()

        sc.logger.info('点击添加配乐')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('点击添加配乐')).click()
    except NoSuchElementException:
        sc.logger.info('未添加过配乐，先添加配乐')

    sc.logger.info('添加配乐')
    music_add()

    sc.logger.info('暂停播放')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_stop)).click()

    sc.logger.info('关闭视频原声')
    try:
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_video_mute)).click()
    except:
        sc.logger.info('当前镜头不是视频')

    sc.logger.info('关闭配乐')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_music_mute)).click()

    sc.logger.info('删除配乐')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_music_del)).click()

    sc.logger.info('确定')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_accessibility_id(iOS_elements.btn_music_confirm)).click()

def back_to_home():
    '''存草稿并返回创作页'''
    sc.logger.info('点击“存草稿”按钮')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda el: el.find_element_by_name("存草稿")).click()

    sc.logger.info('返回创作页')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()

def clip_fun_loop():
    """剪辑-镜头编辑-功能遍历."""
    video_flag = 0

    sc.logger.info('点击“镜头编辑”')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("镜头编辑")).click()

    sc.logger.info('剪辑-镜头编辑-滤镜')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("滤镜")).click()
    sc.logger.info('点击“确认”')
    sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

    sc.logger.info('剪辑-镜头编辑-比例')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("比例")).click()

    sc.logger.info('点击“取消”')
    sc.driver.find_element_by_name(iOS_elements.el_cancel_btn).click()

    sc.logger.info('剪辑-镜头编辑-图片时长')
    try:
        sc.logger.info('点击“图片时长”')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name("图片时长")).click()
        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()
    except TimeoutException:
        video_flag = 1
        sc.logger.info('当前镜头是视频，不支持时长')

    sc.logger.info('剪辑-镜头编辑-修剪')
    if video_flag == 1:
        sc.logger.info('点击“修剪”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("修剪")).click()

        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

    sc.logger.info('剪辑-镜头编辑-分割')
    if video_flag == 1:
        sc.logger.info('点击“分割”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("分割")).click()

        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

    sc.logger.info('剪辑-镜头编辑-复制')
    sc.driver.find_element_by_name("复制").click()

    sc.logger.info('工具栏左滑一些')
    el_loc = sc.driver.find_element_by_name("复制")
    swipe_left(el_loc, 0.5, 500)

    sc.logger.info('剪辑-镜头编辑-变速')
    if video_flag == 1:
        sc.logger.info('点击“变速”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("变速")).click()

        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

    sc.logger.info('剪辑-镜头编辑-调色')
    sc.logger.info('点击“调色”')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("调色")).click()
    sc.logger.info('点击“取消”')
    sc.driver.find_element_by_name(iOS_elements.el_cancel_btn).click()

    sc.logger.info('剪辑-镜头编辑-镜头倒放')
    if video_flag == 1:
        sc.logger.info('点击“镜头倒放”')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("镜头倒放")).click()

        try:
            WebDriverWait(sc.driver, 120, 1).until(
                lambda x: x.find_element_by_name("镜头倒放"))
        except TimeoutError as t:
            sc.logger.error('倒放镜头超时', t)
            return False

    sc.logger.info('剪辑-镜头编辑-静音')
    sc.driver.find_element_by_name("静音").click()

    sc.logger.info('剪辑-镜头编辑-旋转')
    sc.logger.info('点击“旋转”')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("旋转")).click()

    sc.logger.info('工具栏左滑一些')
    time.sleep(0.5)
    el_loc = sc.driver.find_element_by_name("旋转")
    swipe_left(el_loc, 0.5, 500)

    sc.logger.info('剪辑-镜头编辑-转场')
    sc.logger.info('点击“转场”')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("转场")).click()

    try:
        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()
    except NoSuchElementException:
        sc.logger.info('只有一个镜头或者选择的是最后一个镜头，无法应用转场')

    sc.logger.info('剪辑-镜头编辑-图片动画')
    sc.logger.info('点击“图片动画”')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("图片动画")).click()

    sc.logger.info('剪辑-镜头编辑-多选')
    sc.logger.info('点击“多选”')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("多选")).click()

    sc.logger.info('取消相关操作')
    sc.driver.find_element_by_name(iOS_elements.el_multi_reset).click()

def clip_filter():
    '''下载一个滤镜并应用'''
    try:
        sc.logger.info('展开滤镜')
        WebDriverWait(sc.driver, 3, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.btn_filter_cho)).click()
    except:
        sc.logger.info("下载'滤镜'")
        find_element_click('id', 5, iOS_elements.btn_filter_download)

        sc.logger.info('展开滤镜')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.btn_filter_cho)).click()

    sc.logger.info('使用滤镜')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.btn_filter_use)).click()

    sc.logger.info('点击“确认”')
    sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

def clip_proportion(el_proportion):
    '''
    镜头比例
    :param el_proportion: 所要切换的比例控件
    :return:
    '''
    '''
    1:1-->"vivavideo_edit_icon_proportion_1_1"
    2:1-->"vivavideo_edit_icon_proportion_2_1"
    4:5-->"vivavideo_edit_icon_proportion_4_5"
    16:9-->"vivavideo_edit_icon_proportion_16_9"
    9:16-->"vivavideo_edit_icon_proportion_9_16"
    3:4-->"vivavideo_edit_icon_proportion_3_4"
    4:3-->"vivavideo_edit_icon_proportion_4_3"
    2.39:1-->"vivavideo_edit_icon_proportion_239_1"
    '''
    sc.logger.info('切换比例')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_accessibility_id(el_proportion)).click()

    sc.logger.info('背景颜色')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_bg_color)).click()

    sc.logger.info('背景图')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_bg_img)).click()

    sc.logger.info('其他相册并返回')
    WebDriverWait(sc.driver, 10, 1).until(
        lambda x: x.find_element_by_name("其他 相册")).click()

    sc.driver.find_element_by_name(iOS_elements.btn_back).click()

    sc.logger.info('选择一个背景图')
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_bg_img)).click()
    except NoSuchElementException:
        sc.logger.info('当前页面是gif图片')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_bg_gif)).click()

    sc.logger.info('fiti in/out')
    for i in range(2):
        sc.driver.find_element_by_name(iOS_elements.btn_fiti).click()

    sc.logger.info('运用于全部镜头')
    sc.driver.find_element_by_name('运用于全部镜头').click()

    sc.logger.info('点击“确认”')
    sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

    sc.logger.info('取消背景图')
    try:
        sc.logger.info('当前页面是vip订阅页面')
        sc.driver.find_element_by_name(iOS_elements.el_vip_close).click()

        sc.logger.info('选中空取消背景图')
        sc.driver.find_element_by_xpath(iOS_elements.btn_bg_null).click()

        sc.logger.info('点击“确认”')
        sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()
    except:
        sc.logger.info('已经是会员，已保存当前设置')

def clip_speed():
    '''变速'''
    sc.logger.info('点击"变速"')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("变速")).click()

    sc.logger.info('运用于全部镜头')
    sc.driver.find_element_by_name('运用于全部镜头').click()

    sc.logger.info('保持音调不变')
    sc.driver.find_element_by_name('保持音调不变').click()

    sc.logger.info('点击“确认”')
    sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

def clip_reverse():
    '''镜头倒放'''
    sc.logger.info('点击"镜头倒放"')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("镜头倒放")).click()

    try:
        WebDriverWait(sc.driver, 120, 1).until(
            lambda x: x.find_element_by_name("镜头倒放"))
    except TimeoutError as t:
        sc.logger.error('倒放镜头超时', t)
        return False

def clip_transition():
    '''转场'''
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name("应用于全部镜头")).click()
    except TimeoutException:
        sc.logger.info('只有一个镜头，无法添加转场')
        return True

    sc.logger.info('下载更多')
    more_download('下载更多')

    sc.logger.info('选择一个"转场"使用')
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.btn_transition_cho)).click()
    except TimeoutException:
        sc.logger.info('选择一个"转场"下载')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.btn_transition_download)).click()

        sc.logger.info('使用')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.btn_transition_cho)).click()

    sc.logger.info('点击“确认”')
    sc.driver.find_element_by_name(iOS_elements.el_confirm_btn).click()

def clip_mult_select():
    '''多选'''
    sc.logger.info('开始选择镜头')
    clip_list = sc.driver.find_elements_by_name(iOS_elements.el_gallery_cho)
    for el_clip in clip_list:
        el_clip.click()

    sc.logger.info('取消相关操作')
    sc.driver.find_element_by_name(iOS_elements.el_multi_reset).click()

    sc.logger.info('删除镜头')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_clip_del)).click()

    sc.logger.info('确认删除')
    sc.driver.find_element_by_name('确认').click()

def clip_add(clip_from):
    '''
    添加镜头
    :param clip_from: 添加镜头的方式
    :return:
    '''
    sc.logger.info('点击"添加镜头"按钮')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_clip_add)).click()

    if clip_from == '相册':
        sc.logger.info('选择相册')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('相册')).click()

        sc.logger.info('选择一个镜头')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_gallery_cho)).click()

        sc.logger.info('点击下一步')
        find_element_click('predicate', 10, iOS_elements.el_gallery_next)

    elif clip_from == '拍摄':
        sc.logger.info('选择拍摄')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('拍摄')).click()

        btn_rec = WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_cp_normal))

        sc.logger.info('拍摄一段5s的视频')
        video_capture('点拍', btn_rec, 5)

def effect_add_confirm():
    '''添加效果完成'''
    try:
        sc.logger.info('确定')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
    except TimeoutException:
        sc.logger.info('直接点击完成即可')

    sc.logger.info('添加3s的效果')
    time.sleep(3)

    sc.logger.info('点击"完成"')
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('完成')).click()
    except TimeoutException:
        sc.logger.info('直接点击右下角确认按钮即可')

    try:
        sc.logger.info('确定')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
    except TimeoutException:
        sc.logger.info('已经到一级页面')

def effect_add_cancel():
    '''取消添加效果'''
    try:
        sc.logger.info('确定')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()
    except TimeoutException:
        sc.logger.info('直接点击完成即可')

    sc.logger.info('点击"完成"')
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('完成')).click()
    except TimeoutException:
        sc.logger.info('直接点击右下角确认按钮即可')

    try:
        sc.logger.info('取消')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name(iOS_elements.el_cancel_btn)).click()
    except TimeoutException:
        sc.logger.info('已经到一级页面')

    sc.logger.info('确定放弃')
    sc.driver.find_element_by_name('确认').click()

def effects_music():
    '''效果-多段配乐'''
    sc.logger.info('点击"多段配乐"')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name('多段配乐')).click()

    sc.logger.info('点击"添加"')
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('添加')).click()
    except:
        sc.logger.info('当前视频已经有配乐，删除原有音乐')
        sc.driver.find_element_by_name('删除').click()

        sc.logger.info('点击"添加"')
        sc.driver.find_element_by_name('添加').click()

    sc.logger.info('添加配乐')
    music_add()

def text_def_add():
    '''效果-默认动态字幕添加'''
    sc.logger.info('选择添加的"动态字幕"')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.el_text_added)).click()

    sc.logger.info('输入字幕')
    el_text_input = sc.driver.find_element_by_ios_predicate(
        "type == 'XCUIElementTypeTextView' AND value == '请输入动态文字'")
    el_text_input.clear()
    el_text_input.send_keys("input text test")

    sc.logger.info('点击右侧"确认"按钮')
    sc.driver.find_element_by_name("确认").click()

def text_comm_add():
    '''效果-普通字幕添加'''
    sc.logger.info('切换到普通字幕')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_text_comm)).click()

    sc.logger.info('添加一个普通字幕')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.btn_text_cho)).click()

    sc.logger.info('选择添加的"字幕"')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.el_text_added)).click()

    sc.logger.info('输入字幕')
    el_text_input = sc.driver.find_element_by_ios_predicate(iOS_elements.text_input_label)
    el_text_input.clear()
    el_text_input.send_keys("input comm text test")

    sc.logger.info('点击右侧"确认"按钮')
    sc.driver.find_element_by_name("确认").click()

def text_other():
    '''效果-字体其他操作'''
    sc.logger.info('切换到字体')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_text_font)).click()

    sc.logger.info('点击"下载"按钮')
    try:
        sc.driver.find_element_by_accessibility_id(iOS_elements.btn_font_download).click()
    except NoSuchElementException:
        sc.logger.info('当前页面已无为下载字体')

    sc.logger.info('切换到描边页面')
    sc.driver.find_element_by_name(iOS_elements.btn_text_color).click()

    sc.logger.info('切换到字体设置页面')
    sc.driver.find_element_by_name(iOS_elements.btn_text_set).click()

    sc.logger.info('随机对齐方式')
    el_align = [iOS_elements.btn_text_c, iOS_elements.btn_text_l, iOS_elements.btn_text_r]
    sc.driver.find_element_by_name(random.choice(el_align)).click()

    sc.logger.info('点击阴影开关')
    sc.driver.find_element_by_xpath("//*/XCUIElementTypeSwitch[1]").click()

    sc.logger.info('点击字幕动画开关')
    sc.driver.find_element_by_xpath("//*/XCUIElementTypeSwitch[2]").click()

def sticker_comm_add():
    '''效果-普通字幕添加'''
    sc.logger.info('选择一个"贴纸"添加')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.el_sticker_cho)).click()

    sc.logger.info('镜像"贴纸"')
    find_element_click('id', 10, iOS_elements.btn_flip, 1)

def sticker_gif_add():
    '''效果-gif字幕添加'''
    sc.logger.info('点击"GIF"')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name('GIF')).click()

    sc.logger.info('下载并使用"GIF"')
    material_download('name', 'GIF 贴纸', '下载')

def collage_add(type):
    '''画中画'''
    if type == '图片':
        sc.logger.info('点击"图片"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('图片')).click()

        sc.logger.info('选择一个"图片"')
        try:
            sc.driver.find_element_by_xpath(iOS_elements.el_img_cho).click()
        except NoSuchElementException:
            sc.driver.find_element_by_xpath(iOS_elements.el_gif_cho).click()
    elif type == '视频':
        sc.logger.info('点击"视频"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('视频')).click()

        sc.logger.info('选择一个"视频"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_video_cho)).click()
    elif type == 'GIF':
        sc.logger.info('点击"网络"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('网络')).click()

        sc.logger.info('搜索GIF图片')
        el_search = sc.driver.find_element_by_ios_predicate(iOS_elements.el_gif_search)
        el_search.clear()
        el_search.send_keys('a')
        sc.driver.find_element_by_accessibility_id("Search").click()
        time.sleep(3)

        sc.logger.info('下载并使用gif图')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda gif: gif.find_element_by_ios_predicate(iOS_elements.el_gif_download)).click()

        sc.logger.info('使用该下载的GIF图片')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda gif: gif.find_element_by_xpath(iOS_elements.el_gif)).click()

def fx_add():
    '''特效'''
    sc.logger.info('选择一个"特效"使用')
    try:
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_fx_cho)).click()
    except NoSuchElementException:
        sc.logger.info('没有已下载的特效，下载一个"特效"')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_fx_download)).click()

        sc.logger.info('使用"特效"')
        WebDriverWait(sc.driver, 10, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.el_fx_cho)).click()

def sound_rec_add():
    '''配音和音效-录音'''
    sc.logger.info('点击"录制"')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_accessibility_id(iOS_elements.btn_rec_start)).click()

    sc.logger.info('录制3s后停止')
    time.sleep(3)

    sc.logger.info('停止"录制"')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_accessibility_id(iOS_elements.btn_rec_stop)).click()

def sound_audio_add():
    '''配音和音效-音效'''
    sc.logger.info('切换到"音效"')
    sc.driver.find_element_by_name('音效').click()

    sc.logger.info('选择一个"音效"下载')
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath(iOS_elements.btn_audio_download)).click()
    except:
        sc.logger.info('当前页面所有"音效"已下载完成')

    sc.logger.info('使用')
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('众人欢呼')).click()
    except NoSuchElementException:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('小鬼笑')).click()
    sc.driver.find_element_by_name("添加").click()

def export_video(format):
    '''
    视频导出
    :param format: "清晰 480P"/"超清 1080P"/"高清 720P"
    :return:
    '''
    try:
        sc.logger.info('点击 %s ', format)
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name(format)).click()
    except TimeoutException:
        sc.logger.info('该视频已导出，需要确认是否重新导出')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name("重新导出")).click()

        sc.logger.info('点击 %s ', format)
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name(format)).click()

    sc.logger.info('开始导出')
    try:
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('顺便看看使用教程'))
        try:
            WebDriverWait(sc.driver, 120, 1).until(
                lambda x: x.find_element_by_name('我的工作室'))
        except NoSuchElementException:
            sc.driver.find_element_by_name("稍后再说").click()
    except TimeoutException:
        sc.logger.info('不支持 %s 导出，请购买会员后再进行相关操作', format)
        sc.driver.find_element_by_name(iOS_elements.el_vip_close).click()

        sc.logger.info('点击“存草稿”按钮')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name("存草稿")).click()

        sc.logger.info('返回创作页')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda el: el.find_element_by_name(iOS_elements.el_com_back)).click()
        return True

def export_gif(ratio,bitrate):
    '''
    gif导出
    :param ratio: 导出尺寸->480P/320P/240P
    :param bitrate: 导出的比特率->15F/s，10F/s，5F/s
    :return:
    '''
    try:
        sc.logger.info('点击GIF')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('GIF')).click()
    except TimeoutException:
        sc.logger.info('该视频已导出，需要确认是否重新导出')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name("重新导出")).click()

        sc.logger.info('点击GIF')
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('GIF')).click()

    sc.logger.info('选择GIF导出尺寸')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.gif_ratio_cho)).click()
    sc.driver.find_element_by_name(ratio).click()
    time.sleep(0.5)

    sc.logger.info('选择GIF导出帧率')
    sc.driver.find_element_by_xpath(iOS_elements.gif_bitrate_cho).click()
    sc.driver.find_element_by_name(bitrate).click()
    time.sleep(0.5)

    sc.logger.info('点击“确定”按钮')
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('导出5秒')).click()
    except TimeoutException:
        WebDriverWait(sc.driver, 3, 1).until(
            lambda x: x.find_element_by_name('确定')).click()

    sc.logger.info('开始导出')
    try:
        WebDriverWait(sc.driver, 120, 1).until(
            lambda x: x.find_element_by_name('我的工作室'))
    except NoSuchElementException:
        sc.driver.find_element_by_name("稍后再说").click()

def publish_input():
    '''发布-输入相关'''
    sc.logger.info('清空标题')
    el_title_clear = sc.driver.find_element_by_xpath("//*/XCUIElementTypeScrollView/XCUIElementTypeTextView")
    el_title_clear.clear()

    sc.logger.info('输入标题')
    el_title = WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.title_label))
    el_title.clear()
    el_title.send_keys('input video title test')

    sc.logger.info('输入描述')
    el_des = WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.des_label))
    el_des.clear()
    el_des.send_keys("input description text")

    sc.logger.info('保存输入的描述')
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath("//XCUIElementTypeButton[@name='Done']")).click()
    except NoSuchElementException:
        sc.logger.info("当前键盘为中文键盘")
        sc.driver.find_element_by_xpath("完成").click()

def publish_privacy():
    '''发布-隐私设置'''
    sc.logger.info('点击"隐私设置"')
    sc.driver.find_element_by_name("隐私设置").click()

    sc.logger.info('设置"隐私设置"')
    el_privacy = sc.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeSwitch'")
    for i in range(len(el_privacy)):
        el_privacy[i].click()
        try:
            sc.driver.find_element_by_name("我知道了").click()
        except NoSuchElementException:
            sc.logger.info('不是第一次设置，无设置提示')

    sc.logger.info('保存"隐私设置"')
    sc.driver.find_element_by_name("完成").click()

def publish_cover_add():
    '''发布-封面设置'''
    sc.logger.info('点击"更换封面"')
    sc.driver.find_element_by_name("更换封面").click()

    sc.logger.info('点击"动画贴纸"图标')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath("(//XCUIElementTypeImage[@name='cover_tool_preview_bg'])[1]")).click()

    sc.logger.info('选择一个"贴纸"添加')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.el_sticker_cho)).click()

    sc.logger.info('确定')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()

    sc.logger.info('点击"字幕"按钮')
    sc.driver.find_element_by_xpath("(//XCUIElementTypeImage[@name='cover_tool_preview_bg'])[2]").click()

    sc.logger.info('添加一个普通字幕')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath(iOS_elements.btn_text_cho)).click()

    sc.logger.info('点击"字体"按钮')
    sc.driver.find_element_by_name("字体").click()

    sc.logger.info('确定')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.el_confirm_btn)).click()

    sc.logger.info('保存编辑的封面')
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name(iOS_elements.btn_confirm)).click()

def publish_other():
    '''发布-其他设置'''
    sc.logger.info('显示位置')
    try:
        sc.driver.find_element_by_xpath(iOS_elements.el_loc).click()
        try:
            WebDriverWait(sc.driver, 3, 1).until(
                lambda x: x.find_element_by_name('允许')).click()
        except:
            sc.logger.error('已经授权位置获取')

        sc.logger.error('返回分享页面')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name('取消')).click()
    except Exception as e:
        sc.logger.error('获取不到显示位置控件', e)

    sc.logger.info('添加话题')
    try:
        sc.driver.find_element_by_xpath(iOS_elements.el_topic).click()

        sc.logger.info('添加一个推荐话题')
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_ios_predicate("type == 'XCUIElementTypeCell'")).click()
    except Exception as e:
        sc.logger.error('获取不到添加话题控件', e)

def publish():
    '''发布'''
    sc.logger.info('选择480P导出')
    sc.driver.find_element_by_name("清晰 480P").click()

    sc.logger.info('开始导出并上传')
    try:
        WebDriverWait(sc.driver, 120, 1).until(
            lambda x: x.find_element_by_name('发现'))
    except TimeoutException as t:
        sc.logger.error('发布超时', t)

def feedback():
    """设置-意见反馈"""
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_name( "+ 新建反馈")).click()
    except TimeoutException:
        sc.logger.info("第一次反馈")

    sc.logger.info("填写问题")
    el_question = sc.driver.find_element_by_ios_predicate("type == 'XCUIElementTypeTextView'")
    el_question.clear()
    el_question.send_keys("just for ios test")
    try:
        WebDriverWait(sc.driver, 5, 1).until(
            lambda x: x.find_element_by_xpath("//XCUIElementTypeButton[@name='Done']")).click()
    except NoSuchElementException:
        sc.logger.info("当前键盘为中文键盘")
        sc.driver.find_element_by_xpath("完成").click()

    sc.logger.info("选择问题分类")
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("告诉我们该问题属于哪一类(可选)")).click()

    sc.logger.info("滑动选择问题分类")
    start_x = width // 2
    start_bottom = height - height // 10
    sc.swipe_by_ratio(start_x, start_bottom, 'up', 0.2, 500)
    sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='完成']").click()

    sc.logger.info("提供截图")
    sc.driver.find_element_by_xpath("//XCUIElementTypeImage[@name='icon_add_nrm']").click()

    sc.logger.info("取消添加截图")
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_name("取消")).click()

    sc.logger.info("输入联系方式")
    el_contact = sc.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeTextField'")
    for contact in el_contact:
        if contact.text == u'QQ':
            contact.send_keys("245603638")
            break

    for contact in el_contact:
        if contact.text == u'手机号':
            contact.send_keys("15857154810")
            break

    sc.logger.info("保存联系方式")
    WebDriverWait(sc.driver, 5, 1).until(
        lambda x: x.find_element_by_xpath("//XCUIElementTypeButton[@name='Done']")).click()

    sc.logger.info("提交反馈")
    sc.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='提交']").click()



