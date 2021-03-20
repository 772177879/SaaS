from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class CreateGroup(Action, Loc):
    def create_group(self, group_name, introduce):
        log.info('新建群组:%s,%s' % (group_name, introduce))
        # 新建群组
        self.element_click(self.new_group_loc)  # 点击新建群组
        self.element_input(self.groupName_input_loc, group_name)  # 输入群组名
        self.element_input(self.introduce_input_loc, introduce)  # 输入群组描述
        time.sleep(2)
        self.element_click(self.group_input_submit_loc)  # 点击确定
        time.sleep(2)

    def create_team(self, team_name, team_type=0, team_member=None, limit_select=None):
        log.info('新建团队:%s,%s,%s' % (team_name, team_member, limit_select))
        # 新建团队
        self.element_click(self.new_group_loc)  # 点击新建团队
        self.element_input(self.groupName_input_loc, team_name)     # 输入群组名
        if team_type == 1:
            # 直接邀请人
            self.element_click("//div[@id='show-user-list']")   # 点击添加成员
            time.sleep(1)
            self.element_input(self.group_userInput_loc, team_member)  # 添加成员
            time.sleep(2)
            self.element_click("//div[@class='add-view']")  # 点击添加
            time.sleep(2)
            self.element_click(self.group_userInput_submit_loc)  # 点击确定
            time.sleep(1)
            # 控制权限
            self.element_click("//div[@class='m-hd br-2']")  # 点击权限
            time.sleep(1)
            # 点击权限选择
            if limit_select == '查看':
                self.element_click(self.member_read_loc)  # 分配查看权限
            elif limit_select == '编辑':
                self.element_click(self.member_edit_loc)  # 分配编辑权限
            elif limit_select == '移除':
                self.element_click(self.member_remove_loc)  # 移除成员
        self.element_click(self.group_input_submit_loc)  # 点击确定
        time.sleep(2)








