# -*- coding: utf-8 -*-
"""脚本里用到的一些方法."""
import os
import logging
import logging.config
from iOS.script_params import driver
import time


def mkdir(path):
    """自定义的创建文件夹方法."""
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip('\\')
    path = path.rstrip('/')

    # 判断路径是否存在
    if os.path.exists(path):
        # 如果目录存在则不创建，并提示目录已存在
        logging.debug(u'%s目录已存在', path)
    else:
        # 如果不存在则创建目录
        os.makedirs(path)

        logging.info(u'%s创建成功', path)
        return True
    return False

def test_init():
    """测试初始化."""
    print('Test init begin!!!')
    local_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
    #path_list = ['./Report/', local_time, '/']
    path_list = ['/Users/zhulixin/Desktop/UItest/iOS/Report/', local_time, '/']

    capture_list = path_list + ['screenshots/']
    log_list = path_list + ['logs/']
    report_list = path_list + ['reports/']

    capture_dir = ''.join(capture_list)
    log_dir = ''.join(log_list)
    report_dir = ''.join(report_list)

    mkdir(capture_dir)
    mkdir(log_dir)
    mkdir(report_dir)

    return capture_dir, log_dir, report_dir

# 日志格式
def logger_init():
    """logger初始化方法."""
    log_config = {
        'version': 1,
        'formatters': {
            'simple': {
                'format': u'%(asctime)s-%(levelname)s: %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'simple'
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': path_lists[1] + 'logging.log',
                'level': 'DEBUG',
                'formatter': 'simple',
                'encoding': 'utf-8'
            },
        },
        'loggers': {
            'root': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
            'simple': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
            }
        }
    }
    logging.config.dictConfig(log_config)
    loggers = logging.getLogger('simple')
    return loggers

def capture_screen(fun, path):
    """用appium client截屏."""
    if path.endswith('/') or path.endswith('\\'):
        # 考虑到截图操作可能很多，为了效率，所以使用列表拼接字符串
        mkdir(path)
        local_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime())
        name_list = [local_time, fun, '.png']

        capture_name = '_'.join(name_list)
        path_name = path + capture_name

        driver.get_screenshot_as_file(path_name)
        logger.info(u'保存截图%s', capture_name)
    else:
        logger.error(u'截图路径请使用"\\"或者"/"结尾')
        return False
    return True

def get_size():
    """获取屏幕分辨率."""
    rect = driver.get_window_size()
    return rect['width'], rect['height']

def swipe_by_ratio(start_x, start_y, direction, ratio, duration=None):
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
        logger.error(u'滑动方向%s不支持', direction)

    width, height = get_size()

    def swipe_up():
        """上滑."""
        end_y = start_y - ratio * height
        if end_y < 0:
            logger.warning(u'上滑距离过大')
            return False
        else:
            driver.swipe(start_x, start_y, start_x, end_y, duration)
        return True

    def swipe_down():
        """下滑."""
        end_y = start_y + ratio * height
        if end_y > height:
            logger.warning(u'下滑距离过大')
            return False
        else:
            driver.swipe(start_x, start_y, start_x, end_y, duration)
        return True

    def swipe_left():
        """左滑."""
        end_x = start_x - ratio * width
        if end_x < 0:
            logger.warning(u'左滑距离过大')
            return False
        else:
            driver.swipe(start_x, start_y, end_x, start_y, duration)
        return True

    def swipe_right():
        """右滑."""
        end_x = start_x + ratio * width
        if end_x > width:
            logger.warning(u'右滑距离过大')
            return False
        else:
            driver.swipe(start_x, start_y, end_x, start_y, duration)
        return True

    swipe_dict = {'up': swipe_up, 'down': swipe_down, 'left': swipe_left,
                  'right': swipe_right}
    return swipe_dict[direction]()

path_lists = test_init()
logger = logger_init()

