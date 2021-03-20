from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
from time import sleep


class Login(Action, Loc):

    def login(self, username, password, new_member_login=0, login_type=0, new_password=None):
        # 登录
        log.info('以下为登录操作:%s,%s' % (username, password))
        if login_type == 0:     # 0企业版登录，1个人版登录
            self.element_click(self.company_login_loc)      # 点击企业账号登录
        self.element_input(self.username_loc, username)     # 输入用户名
        self.element_input(self.password_loc, password)     # 输入密码
        self.element_click(self.submit_loc)     # 点击登录
        if new_member_login == 1:
            self.element_input(self.new_password_loc, new_password)     # 新密码输入
            self.element_input(self.new_password_confirm_loc, new_password)     # 新密码输入
            self.element_click(self.new_password_submit_loc)        # 点击确认
        # sleep(5)
        # self.wait_element(self.my_file_loc)     # 等待我的文件出现

    def logout(self):
        log.info('以下为退出登录操作')
        # 退出
        self.element_click(self.setting_loc)        # 点击设置弹出框
        self.element_click(self.logout_loc)         # 点击退出登录
        self.wait_element(self.username_loc)  # 验证回到了登录界面

    def guide(self):
        log.info('以下为进入优云指导')
        self.wait_element(self.guide_loc)      # 出现优云指导
        self.element_click(self.guide_start_loc)    # 点击开始指导
        self.wait_element(self.guide_new_file_loc)  # 出现新建指导
        self.element_click(self.guide_next_loc)     # 下一步
        self.wait_element(self.guide_manage_file_loc)  # 出现管理我的文件
        self.element_click(self.guide_next_loc)  # 下一步
        self.wait_element(self.guide_manage_team_loc)  # 出现管理我的群组
        self.element_click(self.guide_next_loc)  # 下一步
        self.wait_element(self.guide_manage_group_loc)  # 出现管理我的部门
        self.element_click(self.guide_next_loc)  # 下一步
        self.wait_element(self.guide_manage_application_loc)  # 出现管理我的应用
        self.element_click(self.guide_next_loc)  # 下一步
        self.wait_element(self.guide_manage_share_loc)  # 出现管理我的共享
        self.element_click(self.guide_done_loc)     # 完成





