from Object.myunit import MyTest
from Page.Group.create import CreateGroup
from Page.Group.delete import GroupDelete
from Page.Group.member import Member
from Page.login import Login
from Object.static import get_config
from Page.Notice.Notice import Notice
import time
account = get_config('zsy')  # 读取账号
account2 = get_config('sld')  # 读取账号
team = get_config('team')
invite_message = "%s邀请您加入群组%s" % (account['name'], team['team_name'])
delete_message = "您加入的群组%s已被解散" % team['team_name']


class TestCreateGroup(MyTest, CreateGroup, Login, GroupDelete, Member, Notice):
    def test_TestCreateGroup_00(self):
        """创建群组之前，先清空所有自己的群组"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)      # 点击群组
        time.sleep(3)
        self.delete_all_group(account['name'])     # 删除所有群组

    def test_TestCreateGroup_01(self):
        """接收群组之前，先清空所有自己的群组"""
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)      # 点击群组
        time.sleep(3)
        self.delete_all_group(account2['name'])     # 删除所有群组

    def test_TestCreateGroup_02(self):
        """创建群组，并且添加人员"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        group_list = self.get_group_list()  # 获取所有群组的字典
        self.assertIn([team['team_name'], '我创建的'], group_list)  # 验证出现了群组，且是我创建的
        self.click_file(team['team_name'])     # 选择该群组
        self.element_click(self.group_user_loc)  # 点击成员管理
        time.sleep(1)
        self.add_group_member(account2['name'])     # 添加sld账号
        self.logout()   # 退出登录
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_notice_notice()       # 进入通知的通知
        text = self.invite_team_notice()       # 验证邀请的通知存在
        self.assertEqual(invite_message, text)
        self.close_notice()     # 关闭界面
        self.element_click(self.group_loc)  # 点击群组
        group_list = self.get_group_list()  # 获取所有群组的字典
        self.assertIn([team['team_name'], '我加入的'], group_list)  # 验证出现了群组，且是我加入的

    def test_TestCreateGroup_03(self):
        """删除群组，都收到对应通知"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.click_file(team['team_name'])  # 点击群组
        self.element_click(self.group_setting_loc)  # 点击设置
        self.delete_group()  # 删除
        self.into_notice_notice()       # 进入通知的通知
        text = self.team_delete_notice()       # 验证删除群组的通知在
        self.assertEqual(delete_message, text)
        self.close_notice()     # 关闭界面
        self.logout()  # 退出登录
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_notice_notice()  # 进入通知的通知
        text = self.team_delete_notice()  # 验证删除群组的通知在
        self.assertEqual(delete_message, text)
        self.close_notice()  # 关闭界面






