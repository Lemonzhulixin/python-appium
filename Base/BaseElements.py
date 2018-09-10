
class Element(object):
    # Android
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    find_element_by_class_name = "class_name"
    find_elements_by_class_name = "class_names"
    find_element_by_android_uiautomator = 'text'
    find_elements_by_android_uiautomator = 'texts'
    INDEX = "index"

    # iOS
    find_element_by_accessibility_id = 'ios_id'
    find_elements_by_accessibility_id = 'ios_ids'
    find_element_by_ios_predicate = 'predicate'
    find_elements_by_ios_predicate = 'predicates'
    find_element_by_name = "name"
    find_elements_by_name = "names"

    # Android&iOS
    find_element_by_xpath = "xpath"
    find_elements_by_xpath = "xpaths"

    CLICK = "click"
    TAP = "tap"
    ACCESSIBILITY = "accessibility"
    ADB_TAP = "adb_tap"
    SWIPE_DOWN = "swipe_down"
    SWIPE_UP = "swipe_up"
    SWIPE_LEFT = "swipe_left"
    SWIPE_RIGHT = "swipe_right"


    SCREEN_TAP = 'screen_tap'
    SET_VALUE = "set_value"
    GET_VALUE = "get_value"
    WAIT_TIME = 10
    PRESS_KEY_CODE = "press_keycode"

    GET_CONTENT_DESC = "get_content_desc"

    # 错误日志
    TIME_OUT = "timeout"
    NO_SUCH = "noSuch"
    WEB_DROVER_EXCEPTION = "WebDriverException"
    INDEX_ERROR = "index_error"
    STALE_ELEMENT_REFERENCE_EXCEPTION = "StaleElementReferenceException"
    DEFAULT_ERROR = "default_error"

    # 检查点
    CONTRARY = "contrary"  # 相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    CONTRARY_GETVAL = "contrary_getval"  # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    DEFAULT_CHECK = "default_check"  # 默认检查点，就是查找页面元素
    COMPARE = "compare"  # 历史数据和实际数据对比
    TOAST = "toast"


    RE_CONNECT = 1 # 是否失败后再次运行一次用例

    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    DEVICES_FILE = "devices.pickle"
    REPORT_FILE = "Report.xlsx"


    #启动页

    #首页
    c_btn = 'com.quvideo.xiaoying:id/img_creation'
    el_home_vip = 'com.quvideo.xiaoying:id/btn_vip'
    el_home_ad = 'com.quvideo.xiaoying:id/btn_shuffle'
    el_home_edit = 'com.quvideo.xiaoying:id/icon1'
    el_home_cam = 'com.quvideo.xiaoying:id/icon2'
    'com.quvideo.xiaoying:id/xiaoying_alert_dialog_positive'
    #Gallery

    #Camera

    #工作室
    el_studio_more = 'com.quvideo.xiaoying:id/btn_more'

    #订阅
