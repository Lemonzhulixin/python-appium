# -*- coding: utf-8 -*-
"""所有控件集"""

"""首页"""
#创作页按钮
el_home_create = "camerta_n"
#剪辑
el_home_edit = '//XCUIElementTypeStaticText[@name="视频剪辑"]'
#拍摄
el_home_camera = '//XCUIElementTypeStaticText[@name="高清拍摄"]'
#草稿
el_home_draft = "//*/XCUIElementTypeOther[2]/*/XCUIElementTypeButton"
el_studio_draft = '//*/XCUIElementTypeCollectionView//*/XCUIElementTypeOther[2]/XCUIElementTypeImage[1]'
btn_listview = "vivavideo tool studio list n"
btn_gridview = "vivavideo tool studio list2 n"
btn_studio_del2 = 'vivavideo tool studio delete2 '
btn_studio_del1 = 'vivavideo tool studio delete n'
btn_ad_clo  = 'vivavideo purchase close n'

#VIP
el_home_vip ="//*/XCUIElementTypeOther/XCUIElementTypeButton[1]"
#订阅页面
el_vip_close = "icon close n"
el_try_close = 'vivavideo popup close'
#广告
el_home_ad = "//*/XCUIElementTypeOther/XCUIElementTypeButton[2]"
el_ad_back = "vivavideo common back n"
el_ad_clo = 'vivavideo com nav cancel n'
#次要功能位置图标
sub_icon_btn = '//*XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/*/XCUIElementTypeOther/XCUIElementTypeImage'


#我
btn_me = "//*/XCUIElementTypeTabBar/XCUIElementTypeButton[3]"

#拍摄按钮
el_cp_normal = "//*/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[1]"
el_cp_self = "//*/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther[1]"
el_cp_music = "//*/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther[1]"
#人脸贴纸/滤镜
el_sticker_icon = "vivavideo camera tool icon sti"
el_sticker_download = "(//XCUIElementTypeImage[@name='vivavideo_camera_tool_icon_sticker_download_nrm'])[1]"
el_sticker_used = "//*/XCUIElementTypeCollectionView[1]//*/XCUIElementTypeCell[2]/XCUIElementTypeOther/XCUIElementTypeImage"
el_sticker_null = "//XCUIElementTypeImage[@name='vivavideo_camera_tool_icon_null_nrm']"
el_filter_icon = 'vivavideo camera tool icon fil'
el_filter_download ='//*/XCUIElementTypeOther[3]//*/XCUIElementTypeOther/XCUIElementTypeImage[2]'
el_filter_more = 'vivavideo_camera_bg_filter_store'

#camera设置
el_ful = "vivavideo camera tool icon ful" #全屏
el_fou = "vivavideo camera tool icon fou" #3:4
el_one = "vivavideo camera tool icon one" #1:1
el_cam_setting = "vivavideo camera tool icon set"
el_cam_flash = "vivavideo camera tool icon fla"
el_cam_grid = "vivavideo camera tool icon gri"
el_cam_time = "vivavideo camera tool icon tim"
el_cam_switch = "vivavideo camera tool icon cha"
#配乐
el_mus_download = "music select download n"
el_mus_title = '//*/XCUIElementTypeOther[4]//*/XCUIElementTypeButton'
el_mus_play = "//*/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeButton[2]"

el_mus_del = "music select delete n"
el_mus_del2 = "music select delete h"
el_mus_cho = "music select music choose n"

#左上角X
el_cam_close = "vivavideo camera tool icon clo"

#其他
el_cam_next = "vivavideo camera tool icon nex"
el_com_back = "vivavideo com nav back n"
el_preview_back = "vivavideo playerview fullscree"
btn_back = 'vivavideo gallery back n'
el_cancel = "取消"
el_discard = '丢弃'
el_save = '保存'
el_studio_back = '//XCUIElementTypeButton[@name="vivavideo com nav back n"]'

#Gallery
el_gallery_cho = "vivavideo edit gallery icon ch"
el_gallery_next = "type == 'XCUIElementTypeButton' AND label CONTAINS '下一步'"
btn_gallery_trim = "vivavideo edit gallery icon tr"
btn_gallery_rotate = "vivavideo edit gallery icon ro"
btn_gallery_play = "vivavideo playerview small whi"
el_gallery_back = "vivavideo popup icon cancel nr"


"""高级剪辑"""
el_confirm_btn = "xiaoying itembar finish"
el_cancel_btn = "xiaoying itembar close"
el_multi_reset = "vivavideo_editor_framebar_undo"

#素材中心
btn_manager = "vivavideo material Management "

#预览页
btn_stop = 'vivavideo playerview small whi'
btn_video_mute = 'theme change music left n'
btn_music_mute ='theme change music right n'
btn_music_added = 'theme_change_music_add_arrow'
btn_music_del = "theme change music add delete"
btn_music_confirm = 'vivavideo_green_tick'
btn_img_time = '//*/XCUIElementTypeWindow[1]//*/XCUIElementTypeOther/XCUIElementTypeButton'
el_theme_download = '(//XCUIElementTypeImage[@name="vivavideo_camera_tool_icon_download_nrm"])[1]'
el_theme_use = '//*/XCUIElementTypeOther[3]//*/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage'
el_watermark = "vivavideo watermark edit cn n"
el_pre_clo = '//XCUIElementTypeButton[@name="vivavideo editor common cancel"]'

#编辑
btn_filter_download = 'vivavideo_camera_tool_icon_download_nrm'
btn_filter_cho = '//*/XCUIElementTypeOther[2]/*/XCUIElementTypeOther[2]//*/XCUIElementTypeImage'
btn_filter_use = '//*/XCUIElementTypeOther[1]//*/XCUIElementTypeOther/XCUIElementTypeImage'

#比例
btn_one = 'vivavideo_edit_icon_proportion_1_1'
btn_bg_pro = "vivavideo edit icon vague nrm"
btn_bg_color = "vivavideo edit icon color nrm"
btn_bg_img = "vivavideo edit icon background"
el_bg_gif = '(//XCUIElementTypeImage[@name="vivavideo_edit_gallery_icon_gif_nrm"])[1]'
el_bg_img = '//*/XCUIElementTypeCollectionView[1]/*/XCUIElementTypeOther/XCUIElementTypeImage'
btn_bg_null = '//*/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther'
btn_fiti = "vivavideo edit ratio icon fiti"

#转场
btn_transition_download  = "vivavideo material download n"
btn_transition_cho = '(//XCUIElementTypeButton[@name="使用"])[1]'
btn_transition_icon = 'vivavideo transfer icon transf'
btn_clip_del ='vivavideo edit video close n'


#添加镜头
btn_clip_add = "vivavideo edit add clip n"

#字幕
btn_text_default = "xiaoying caption bar text t h"
btn_text_comm = "xiaoying caption bar text n"
btn_text_font = "xiaoying caption bar aa n"
btn_text_color = "xiaoying caption bar font n"
btn_text_set = "xiaoying caption bar set n"

btn_text_cho = "//*/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeOther/XCUIElementTypeImage"
el_text_added = "//*/XCUIElementTypeOther/XCUIElementTypeImage[1]"
btn_flip = 'vivavideo_edit_icon_flip_n'
btn_font_download = "vivavideo_camera_tool_icon_sticker_download_nrm"
text_input_label1 = "type == 'XCUIElementTypeTextView' AND value CONTAINS '请输入字幕...'"
text_input_label2 = "type == 'XCUIElementTypeTextView' AND value CONTAINS '点击输入字幕'"

btn_text_r = "xiaoying caption bar set btn r"
btn_text_c = "xiaoying caption bar set btn c"
btn_text_l = "xiaoying caption bar set btn l"
btn_text_switch = "type == 'XCUIElementTypeSwitch'"

#贴纸
el_sticker_cho = "//*/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeOther/XCUIElementTypeImage"

#画中画
el_img_cho = "//*/XCUIElementTypeCollectionView[1]//*/XCUIElementTypeImage[1]"
el_gif_cho = "//*/XCUIElementTypeCollectionView[1]//*/XCUIElementTypeImage"
el_video_cho = "//*/XCUIElementTypeCollectionView[2]//*/XCUIElementTypeImage"
el_gif_search = "type == 'XCUIElementTypeTextField' AND value == '搜索Gif'"
el_gif_download = "type == 'XCUIElementTypeImage' AND name == 'vivavideo_tool_collage_download_n'"
el_gif = "//*/XCUIElementTypeCollectionView[3]/*/XCUIElementTypeOther/XCUIElementTypeImage"

#特效
el_fx_download = '(//XCUIElementTypeImage[@name="vivavideo_camera_tool_icon_sticker_download_nrm"])[1]'
el_fx_cho = "//*/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeCollectionView[2]/*/XCUIElementTypeImage"

#配音和音效
btn_rec_start = 'vivavideo_edit_dub_play_nrm'
btn_rec_stop = "vivavideo_edit_dub_stop_nrm"
btn_audio_download = '(//XCUIElementTypeImage[@name="vivavideoedit_dub_download"])[1]'
btn_audio_cho1 = '/XCUIElementTypeOther[2]/XCUIElementTypeScrollView//*/XCUIElementTypeCell[2]/XCUIElementTypeOther[1]'
btn_audio_cho2 = '/XCUIElementTypeOther[2]/XCUIElementTypeScrollView//*/XCUIElementTypeCell[20]/XCUIElementTypeOther[2]'

#导出
gif_ratio_cho = "(//XCUIElementTypeImage[@name='vivavideo_gif_icon_arrow_n'])[1]"
gif_bitrate_cho = "(//XCUIElementTypeImage[@name='vivavideo_gif_icon_arrow_n'])[2]"

#发布
title_label = '//XCUIElementTypeStaticText[@name="请输入标题，你的作品记录了什么？"]'
des_label = "//*/XCUIElementTypeOther[1]/XCUIElementTypeTextView"
el_loc_clo = '//XCUIElementTypeButton[@name="icon not box n"]'
btn_confirm = 'vivavideo editor common ok'
el_loc = '//XCUIElementTypeButton[@name=" 显示位置"]'
el_topic = '//XCUIElementTypeButton[@name=" 添加话题"]'


#素材中心
el_banner = 'XiaoYingResource.bundle/xiaoying_template_no_banner'
el_store_download1 = "vivavideo material download n" #主题/特效/字体/字幕/贴纸/转场
el_store_download2 = "vivavideo material download2 n" #滤镜
el_store_del = 'vivavideo material delete n' #主题/滤镜/特效/字体/字幕/贴纸/转场
el_banner_back = 'vivavideo back n'
#个人页
btn_settings = 'vivavideo me setting n'
el_push_message = "type == 'XCUIElementTypeImage'"
btn_privacy = "//*/XCUIElementTypeOther[3]/XCUIElementTypeImage"
el_abouts = "type == 'XCUIElementTypeImage' AND name == 'vivavideo_com_disclosure_indicator_n'"
about_clo = 'xiaoying about cross'
about_back = "vivavideo aboutxiaoying back n"


