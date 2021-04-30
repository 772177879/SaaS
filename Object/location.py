class Loc:
    """
    所有位置的元素定位
    """
    """登录界面的元素定位"""
    company_login_loc = "//span[text()='企业账号']"    # 企业账号登录
    username_loc = "//input[@name='id']"   # 登录界面的用户名输入位置
    password_loc = "//input[@name='pwd']"  # 登录界面的密码输入位置
    submit_loc = "//button[@id='account-login-btn']"   # 登录界面的登录按钮
    new_password_loc = "//input[@placeholder='新密码']"    # 新账号登录的新密码位置
    new_password_confirm_loc = "//input[@placeholder='确认新密码']"      # 新账号密码登录的新密码确认密码位置
    new_password_submit_loc = "//button[@class='btn btn-primary btn-block']"        # 新账号密码登录的新密码确认位置
    forbid_err_loc = "//p[text()='账号已被禁用']"     # 账号被禁提示
    delete_err_loc = "//p[text()='账号不存在']"      # 用户不存在提示
    """优云使用引导"""
    guide_loc = "//h3[text()='优云使用引导']"       # 出现优云使用指导
    guide_start_loc = "//a[text()='开始']"        # 开始指导
    guide_new_file_loc = "//h3[text()='新手引导：创建/上传一份文档']"      # 新建指导
    guide_next_loc = "//a[text()='下一步']"    # 下一步
    guide_manage_file_loc = "//h3[text()='新手引导：管理我的文件']"
    guide_manage_team_loc = "//h3[text()='新手引导：管理我的群组。']"
    guide_manage_group_loc = "//h3[text()='新手引导：我的部门']"
    guide_manage_application_loc = "//h3[text()='新手引导：我的应用']"
    guide_manage_share_loc = "//h3[text()='新手引导：分享文档']"
    guide_done_loc = "//a[text()='完成']"  # 完成

    """首页的元素定位"""
    file_loc = "//span[text()='文件']"    # 文件
    my_file_loc = "//span[text()='我的文件']"     # 首页我的文件
    recent_file_loc = "//span[text()='最近文件']"       # 首页最近文件
    my_collect_loc = "//span[contains(text(), '收藏')]"    # 首页收藏文件
    setting_loc = "//span[@class='setting']"   # 设置的弹出框
    info_loc = "//li[@id='setting']"  # 个人设置
    console_loc = "//li[@id='enterprise']"  # 企业控制台
    logout_loc = "//li[@id='logout']"   # 退出登录
    """新建按钮定位"""
    new_loc = "//button[@class='button done createBtn']"    # 新建按钮
    no_new_loc = "//li[text()='当前目录您无操作权限']"    # 当前目录您无操作权限
    new_wp_loc = "//li[@data-type='newWord']"    # 新建wp
    new_ss_loc = "//li[@data-type='newExcel']"      # 新建ss
    new_pg_loc = "//li[@data-type='newPPT']"    # 新建pg
    new_folder_loc = "//li[@data-type='createFolder']"      # 新建文件夹
    upload_loc = "//button[@data-type='upload']"    # 上传按钮
    upload_file_loc = "//li[@data-type='upload']"        # 上传文件
    upload_folder_loc = "//li[@data-type='uploadFileFolders']"        # 上传文件夹
    filename_input_loc = "//input[@name='filename']"        # 文件名输入框
    folder_input_loc = "//input[@name='folderName']"        # 文件夹名输入框
    rename_input_loc = "//input[@name='fileName']"          # 重命名时输入框
    filename_input_submit_loc = "//footer[@class='window-footer text-right']/button[text()='确定']"    # 文件名处的确认
    """编辑区域定位"""
    edit_frame_loc = "//iframe[@id='bodyIframe']"    # 编辑frame区域
    canvas_loc = "//canvas[@id='myCanvas']"  # 画布
    edit_area_loc = "//input[@id='myInput']"  # 输入区
    view_loc = "//span[text()='插入']"  # 插入
    read_loc = "//span[text()='审阅']"  # 审阅
    new_pg_page_loc = "//div[@id='yozo_PG_createSlide']"    # 新建幻灯片
    """搜索相关定位"""
    search_area_loc = "//input[@class='search-input search-file']"      # 搜索输入区域
    # search_button_loc = "//i[@class='icon icon30 ic-search-input']"        # 搜索按钮
    search_filename_loc = "//span[text()='文件名']"        # 搜索后的文件名筛选
    search_content_loc = "//span[text()='文本内容']"        # 搜索后的文本内容筛选
    filter_loc = "//span[@class='file-text']"       # 搜索结果的筛选
    close_loc = "//header//button[@class='icon closeBtn']"       # 关闭按钮
    """文件总菜单相关定位"""
    # select_all_loc = "/html/body/div[2]/div[2]/div/div[4]/div/div/div[2]/div[4]/header/div/div[1]/div"      # 全选
    select_all_loc = "//div[@class='t-row']//div[@class='chb']"     # 全选
    # select_first_loc = "/html/body/div[2]/div[2]/div/div[4]/div/div/div[2]/div[4]/section/div/div[1]/div[1]" \
    #     #                    "/div/div[1]/div"    # 全选后的第一个位置
    select_first_loc = "//div[@class='row-cells']//div[@class='chb']"   # 全选后的第一个位置
    all_move_loc = "//button[@title='移动']"     # 全选后的移动到
    all_copy_loc = "//button[@title='复制']"     # 全选后的复制到
    all_download_loc = "//button[@title='下载']"      # 全选后的下载
    all_delete_loc = "//button[@title='放入回收站']"        # 全选后的放入回收站
    sure_loc = "//div[@class='m-alert animated']//button[@class='button done']"     # 需要确定框位的确认
    next_sure_loc = "//button[@class='button done']"    # 不需要确认框位的确认
    # empty_loc = "//p[text()='当前文件夹为空']"     # 文件夹为空时的显示
    empty_loc = "//p[contains(text(),'你可以在此')]"     # 文件夹为空时的显示
    move_fail_loc = "//span[text()='移动失败 : 文件没有移动']"        # 文件移动失败
    """单个文件菜单相关定位"""
    share_loc = "//div[text()='共享']"    # 共享
    cooperate_loc = "//div[text()='协作']"  # 协作
    collect_loc = "//div[text()='收藏文件']"  # 收藏文件
    collect_cancel_loc = "//div[text()='取消收藏']"  # 取消收藏
    attention_loc = "//div[text()='关注文件']"  # 关注文件
    attention_cancel_loc = "//div[text()='取消关注']"  # 取消关注
    tag_loc = "//div[text()='添加标签']"  # 添加标签
    copy_loc = "//div[text()='复制到']"  # 复制到
    person_copy_loc = "//div[text()='创建副本']"  # 创建副本
    move_loc = "//div[text()='移动到']"  # 移动到
    rename_loc = "//div[text()='重命名']"  # 重命名
    download_loc = "//div[text()='下载']"  # 下载
    information_loc = "//div[text()='查看详情']"  # 查看详情
    delete_loc = "//div[text()='放入回收站']"  # 加入回收站
    recover_loc = "//div[text()='恢复']"  # 恢复
    forever_delete_loc = "//div[text()='永久删除']"  # 永久删除
    """回收站相关定位"""
    recycle_loc = "//span[text()='回收站']"    # 回收站
    part_recycle_loc = "//a[text()='部门回收站']"    # 部门回收站
    group_recycle_loc = "//a[text()='群组回收站']"  # 群组回收站
    clean_recycle_loc = "//button[@id='clearTrashBtn']"     # 清空回收站
    empty_recycle_loc = "//p[text()='提示 : 您可以清空回收站来释放空间']"      # 回收站为空
    """标签相关定位"""
    tag_input_loc = "//input[@name='tag-name']"     # 标签名称输入
    create_tag_loc = "//span[text()='创建']"      # 创建标签按钮
    add_tag_loc = "//span[text()='添加']"     # 添加标签按钮
    select_tag_loc = "//ul//span[@class='emp']"    # 选择标签
    into_tag_loc = "//button[@id='tagBtn']"     # 进入标签搜索
    tag_search_input_loc = "//input[@class='tag-Input']"        # 标签输入
    tag_search_button_loc = "//button[@class='searchByTag-btn']"    # 标签搜索
    """共享相关定位"""
    share_file_loc = "//span[text()='共享文件']"      # 共享文件
    my_share_loc = "//a[text()='我共享的']"     # 我共享的
    share_me_loc = "//a[text()='共享给我的' and @data-nav='joinshare']"    # 共享给我的
    share_switch_loc = "//div[@class='right']"      # 共享开关
    limit_select_loc = "//div[@class='m-dropdown-menu']"    # 权限选择
    upload_only_limit_loc = "//li[text()='仅上传（投件）']"      # 仅上传权限
    read_only_limit_loc = "//li[text()='查看']"     # 查看权限
    edit_limit_loc = "//li[text()='编辑']"     # 编辑权限
    download_save_print_switch_loc = "//span[text()='允许查看权限者下载、另存、打印']" \
                                     "/..//div[@class='round-switch small tooltipped tooltipped-bc']"   # 允许查看权限开关
    set_password_loc = "//div[@id='share-window']//span[contains(text(),'密码')]"     # 设置密码按钮
    share_link_loc = "//input[@id='link']"      # 链接地址
    share_password_loc = "//input[@class='password']"   # 密码地址
    share_page_load_loc = "//div[text()='大小']"    # 出现这个说明加载完毕
    """被共享的界面定位"""
    password_input_loc = "//input[@id='pwdField']"      # 输入密码的位置
    share_name_loc = "//span[@id='js-name']"    # 共享人的名称
    share_folder_name_loc = "//div[@class='filePaths']/span"    # 共享的文件夹名称
    share_login_loc = "//a[@id='js-login']"     # 共享界面的登录按钮
    share_setting_loc = "//a[@class='setting']"     # 左上角设置返回
    share_download_loc = "//i[@class='icon ic-download']"       # 预览界面的下载按钮
    """协作界面定位"""
    cooperate_search_loc = "//div[@class='input-view']/input"   # 协作人搜索
    limit_choose_loc = "//div[@class='m-dropdown-menu with-no-border']"  # 权限选择
    forbid_add_new_person_loc = "//span[text()='禁止编辑权限的协作者修改权限和添加新的协作人']" \
                                "/..//div[@class='round-switch small tooltipped tooltipped-bc']"    # 禁止添加协作人
    """群组界面的元素定位"""
    group_loc = "//span[text()='群组']"  # 首页群组
    my_first_group_loc = "//div[@class='view-scroll']//li[1]"  # 群组界面的第一个群组
    # new_group_loc = "//i[@aria-label='创建群组']"  # 新建群组按钮
    new_group_loc = "//i[@id='groudAdd']"  # 新建群组按钮
    groupName_input_loc = "//input[@name='groupName']"  # 群组界面的群组名输入位置
    introduce_input_loc = "//textarea[@name='description']"  # 群组界面的群组简介输入位置
    group_input_submit_loc = "//footer[@class='window-footer text-right']/button[text()='确定']"  # 添加群组处的确认
    group_user_loc = "//label[@aria-label='成员管理']"  # 成员管理
    # group_setting_loc = "//label[@aria-label='群组设置']"  # 群组设置
    group_setting_loc = "//i[@class='l-ioc l-ioc-setting']"  # 群组设置
    # group_notice_loc = "//label[@aria-label='群组公告']"  # 群组公告
    group_notice_loc = "//i[@class='l-ioc l-ioc-notice']"    # 群组公告
    group_logo_loc1 = "//em[@class='tip tip-a l-ioc']"  # 群组标识：创建
    group_logo_loc2 = "//em[@class='tip tip-b l-ioc']"  # 群组标识：加入
    group_addUser_loc = "//i[@id='adduser']"  # 添加成员按钮
    group_userInput_loc = "//input[@id='search-input']"  # 添加成员账号的输入位置
    # group_userInput_submit_loc = "//footer/a[2]"  # 添加成员处的确定
    group_userInput_submit_loc = "//a[@id='but-done']"  # 添加成员处的确定
    groupName_input_setting_loc = "//input[@name='grloupName']"  # 群组管理界面的群组名修改位置
    introduce_input_setting_loc = "//textarea[@name='description']"  # 群组管理界面的群组简介修改位置
    group_icon_loc = "//img[@id='logo']"  # 群组图标
    group_addNotice_loc = "//span[@class='add']"  # 发布公告按钮
    group_noticeTitle_input_loc = "//input[@name='noticeTitle']"  # 群组公告界面的公告标题位置
    group_noticeIntroduce_input_loc = "//textarea[@placeholder='请输入公告内容']"  # 群组公告界面的公告内容位置
    group_notice_title_loc = "//h5[@class='notice-title']"  # 群组公告标题
    group_notice_content_loc = "//pre"   # 群组公告内容
    group_notice_close_loc = "//header[@class='window-header']//button[@class='icon closeBtn']"  # 群组公告关闭按钮
    group_delete_loc = "//button[@class='remove']"  # 删除群组
    """群组成员的元素定位"""
    member_read_loc = "//div[@class='dropdowm-select-list  with-shadow isdisplay']/ul/li[text()='成员-查看']"   # 查看
    member_edit_loc = "//div[@class='dropdowm-select-list  with-shadow isdisplay']/ul/li[text()='成员-编辑']"   # 编辑
    member_remove_loc = "//div[@class='dropdowm-select-list  with-shadow isdisplay']/ul/li[text()='移除成员']"  # 移除
    member_quit_loc = "//div[@class='dropdowm-select-list  with-shadow isdisplay']/ul/li[text()='退出群组']"     # 退出
    """部门的元素定位"""
    part_loc = "//span[text()='部门']"  # 首页部门

    """企业控制台的元素定位"""
    console_board_loc = "//span[text()='企业概况']"  # 企业概况
    console_document_loc = "//span[text()='文档管理']"  # 文档管理
    console_group_loc = "//span/span[text()='群组管理']"  # 群组管理
    console_department_loc = "//span[text()='通讯录']"  # 部门管理
    console_setting_loc = "//span[text()='通用设置']"  # 通用设置
    console_security_loc = "//span[text()='安全管理']"  # 安全管理
    console_management_loc = "//span[text()='管理员管理']"  # 管理员管理
    """文档管理的元素定位"""
    document_depart_loc = "//span[text()='部门文档管理']"  # 部门文档管理
    document_group_loc = "//span[text()='群组文档管理']"  # 群组文档管理
    document_sharing_loc = "//span[text()='企业共享文档管理']"  # 企业共享文档管理
    """群组管理的元素定位"""
    group_manage_loc = "//a/span[text()='群组管理']"  # 群组管理
    group_notice_manage_loc = "//a/span[text()='群组公告']"  # 群组公告
    group_manage_name_loc = ""
    group_manage_state_loc = ""
    """组织架构的元素定位"""
    organization_loc = "//a[@href='/epadmin/department/orgStructure']"  # 组织架构
    add_member_loc = "//div[text()='部门人员']/..//span[text()='添 加']"  # 新增成员
    delete_member_loc = "//div[text()='部门人员']/..//span[text()='删 除']"      # 删除成员
    delete_sure_loc = "//button[@class='ant-btn ant-btn-primary']/span"  # 删除成员时的确认
    forbid_member_loc = "//div[text()='部门人员']/..//span[text()='禁 用']"  # 禁用成员
    # add_part_loc = "//span[text()='增加部门']"      # 新增部门
    forbid_sure_loc = "//div[contains(text(),'禁用')]/../..//span[text()='确 定']"  # 禁用成员时的确认
    # add_part_name_loc = "//input[@placeholder='部门名称']"      # 部门名称
    delete_part_loc = "//button[@class='ant-btn ant-btn-danger ant-btn-background-ghost']/span[text()='删 除']"  # 删除部门
    part_sure_loc = "//button[@class='ant-btn ant-btn-primary ant-btn-sm']/span[text()='确 定']"  # 删除部门时的确认

    """新增成员界面元素定位"""
    add_account_loc = "//input[@id='account']"  # 账号输入
    add_password_loc = "//input[@id='password']"  # 密码输入
    add_name_loc = "//div[@class='ant-modal-body']//input[@id='name']"  # 真实姓名输入
    add_sex_man_loc = "//span[text()='男']/preceding-sibling::span"  # 性别男
    add_sex_women_loc = "//span[text()='女']/preceding-sibling::span"  # 性别女
    add_tel_loc = "//div[@class='ant-modal-body']//input[@id='phone']"  # 手机号输入
    add_email_loc = "//div[@class='ant-modal-body']//input[@id='email']"  # 邮箱输入
    add_position_loc = "//div[@class='ant-modal-body']//input[@id='position']"  # 职务输入
    add_jobNo_loc = "//div[@class='ant-modal-body']//input[@id='jobNo']"  # 工号输入
    add_comment_loc = "//div[@class='ant-modal-body']//textarea[@id='comment']"  # 备注输入
    add_submit_loc = "//button[@type='submit']"  # 确定
    """导入成员界面元素定位"""
    bulk_add_loc = "//span[text()='批量导入']"  # 批量导入
    bulk_title_loc = "//div[@class='ant-modal-title']"  # 批量导入title
    add_step_loc = "//span[text()='下一步']"  # 下一步
    add_member_file_loc = "//div[@class='ant-upload-drag-container']"  # 选择文件上传
    btn_member_pwd_loc = "//span[text()='随机密码']"  # 设置随机密码按钮
    member_pwd_loc = "//div[@class='steps-content content___35hvi']/div/input[@class='ant-input']"  # 获取初始密码
    member_bulk_loc = "//span[text()='执行导入']"  # 执行导入按钮

    """部门文档管理"""
    part_doc_manage_loc = "//a[@href='/epadmin/files/department']"     # 部门文档管理
    all_select_checkbox_loc = "//input[@type='checkbox']"       # 全选框
    delete_all_button_loc = "//button[@class='ant-btn ant-btn-primary ant-btn-dangerous']"      # 全选的删除
    delete_doc_sure_loc = "//button[@class='ant-btn ant-btn-primary']/span[text()='确 定']"       # 确认删除
    search_doc_loc = "//input[@id='queryString']"   # 搜索位置
    begin_time_loc = "//input[@id='createTime']"    # 开始日期
    search_doc_button_loc = "//button[@type='submit']"      # 查询按钮
    reset_button_loc = "//button[@class='ant-btn ant-btn-primary ant-btn-background-ghost']/span"   # 重置按钮
    """群组文档管理"""
    group_select_loc = "//input"    # 群组选择
    group_doc_manage_loc = "//a[@href='/epadmin/files/team']"   # 群组文档管理
    """企业共享文档管理"""
    company_share_manage_loc = "//a[@href='/epadmin/files/share']"      # 企业共享文档管理
    """群组管理"""
    console_group_manage_loc = "//a[@href='/epadmin/team/manage']"  # 群组管理
    console_group_notice_loc = "//a[@href='/epadmin/team/bulletins']"   # 群组公告
    """pdf应用相关"""
    pdf_loc = "//label[@title='pdf工具集']/i"      # pdf工具集按钮
    # pdf_to_word_loc = "//h1[text()='PDF转Word']"     # pdf转word
    pdf_select_file_loc = "//button[text()='选择本地文件']"   # 选择本地文件
    pdf_upload_success_loc = "//span[text()=' 上传完成']"   # 文件上传成功标识
    pdf_start_loc = "//button[text()='开始转换']"       # 开始转换
    pdf_work_success_loc = "//span[text()=' 转换成功']"   # 文件转换完成
    application_folder_loc = "//span[text()='应用']"  # 应用文件夹
    pdf_folder_loc = "//span[text()='PDF工具集']"  # pdf工具集文件夹
    app_frame_loc = "//iframe[@id='appFrame']"  # pdf的frame
    """日历应用相关"""
    calendar_loc = "//label[@title='日历']/i"      # 日历按钮
    new_calendar_loc = "//span[text()='新建日程']"    # 新建
    new_date_loc = "//div[text()='日程']"    # 新建日程
    date_title_loc = "//textarea[@id='title']"   # 标题
    new_date_submit_loc = "//span[text()='新 建']"    # 点击新建提交
    date_cancel_loc = "//div[@class='header']/div[@class='class-3e5907bd']/div[2]//*[name()='svg']"  # 取消日程
    date_delete_loc = "//div[@class='header']/div[@class='class-3e5907bd']/div[2]//*[name()='svg']"  # 删除日程
    date_delete_sure_loc = "//span[text()='确 认']"   # 确认删除
    """表单应用相关"""
    form_loc = "//label[@title='表单']/i"      # 表单按钮
    new_form_loc = "//span[text()='新建表单']"      # 新建表单
    form_menu_loc = "//div[@class='table-operate']//div[@class='el-dropdown']"    # 菜单栏
    form_delete_loc = "//li[contains(text(),'删除')]"     # 删除按钮
    form_delete_sure_loc = "//span[contains(text(),'确定')]"      # 删除确定
    new_form_question_loc = "//span[@class='indexNum' and text()='1.']/..//textarea"    # 表单问题输入区
    new_form_submit_loc = "//span[text()='发布']"     # 点击发布
    url_loc = "//input[@class='share-content']"     # 产生的链接
    answer_loc = "//input[@type='text']"        # 回答问题的地方
    answer_submit_loc = "//span[text()='提交']"   # 提交按钮
    answer_submit_success_loc = "//span[text()='提交成功']"     # 提交成功
    first_form_loc = "//pre"    # 点击第一个表单
    collect_answer_loc = "//div[text()='收集结果' and @aria-selected='true']"   # 收集结果
    """通知公告相关"""
    public_loc = "//i[@title='公告']"     # 公告按钮
    notice_loc = "//i[@title='通知']"     # 通知按钮
    person_notice_loc = "//i[@title='消息']"    # 个人版消息
    person_notice_invite_loc = "//span[text()='邀请消息']"    # 个人版消息里的邀请消息
    person_notice_invite_message_loc = "//div[@class='activity-content']/div[2]/div"   # 个人版消息里的邀请消息内容
    person_agree_loc = "//span[contains(text(),'同意')]"  # 个人版点同意
    person_refuse_loc = "//span[contains(text(),'拒绝')]"     # 个人版点拒绝
    notice_cooperation_loc = "//span[text()='协作']"      # 协作通知
    notice_notice_loc = "//span[text()='协作']"  # 通知的通知
    notice_message_loc = "//section/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div"    # 通知的文本固定内容
    cooperate_message_loc = "//section/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div"     # 协作的文本固定内容
    """管理员管理相关"""
    admin_manage_loc = "//li[@class='ant-menu-submenu ant-menu-submenu-inline']//span[text()='管理员管理']"  # 管理员管理
    admin_manage_inner_loc = "//a[@href='/epadmin/admin/manage']"   # 管理员管理里的管理员管理
    add_admin_loc = "//span[text()='添加管理员']"    # 添加管理员
    admin_select_loc = "//div[@class='ant-modal-content']//input[@class='ant-select-selection-search-input']"  # 选择管理员
    admin_search_loc = "//div[@class='ant-modal-body']//input[@class='ant-input']"      # 搜索框
    wd_admin_loc = "//div[@title='文档管理员']"  # 文档管理员
    pt_admin_loc = "//div[@title='普通管理员']"  # 普通管理员
    admin_sure_loc = "//span[text()='确 定']"     # 确定
