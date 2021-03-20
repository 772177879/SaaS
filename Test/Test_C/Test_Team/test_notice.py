from Object.myunit import MyTest
from Page.Group.create import CreateGroup
from Page.Group.delete import GroupDelete
from Page.Group.member import Member
from Page.Group.notice import GroupNotice
from Page.login import Login
from Object.static import get_config
from Page.Notice.Notice import Notice
import time
account = get_config('client1')  # 读取账号
account2 = get_config('client2')  # 读取账号
team = get_config('team')


class TestGroupNotice(MyTest, CreateGroup, Login, GroupDelete, Member, GroupNotice, Notice):
    def test_Person_TestGroupNotice_00(self):
        """创建团队之前，先清空所有自己的团队"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)  # 点击团队
        time.sleep(3)
        self.delete_all_group(account['name'])  # 删除所有团队

    def test_Person_TestGroupNotice_01(self):
        """接收团队之前，先清空所有自己的团队"""
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)  # 点击团队
        time.sleep(3)
        self.delete_all_group(account2['name'])  # 删除所有团队

    def test_Person_TestGroupNotice_02(self):
        """验证添加公告，团队和成员都可以查看"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)  # 点击团队
        # self.create_group(team['team_name'], team['team_describe'])  # 创建团队
        self.create_team(team['team_name'])  # 创建
        group_list = self.get_group_list()  # 获取所有团队的字典
        self.assertIn([team['team_name'], '我创建的'], group_list)  # 验证出现了团队，且是我创建的
        self.click_file(team['team_name'])  # 选择该团队
        self.element_click(self.group_user_loc)  # 点击成员管理
        time.sleep(1)
        self.add_group_member(account2['username'])  # 添加client2的账号
        # 创建公告
        self.element_click(self.group_setting_loc)      # 点击团队设置
        self.publish_group_notice(team['team_notice_title'], team['team_notice_content'])     # 发布公告
        self.element_click(self.group_notice_loc)   # 点击团队公告
        time.sleep(2)
        (title, content) = self.check_notice_content()      # 获取到的团队信息
        self.assertIn(team['team_notice_title'], title)      # 验证信息是否正确
        self.assertIn(team['team_notice_content'], content)
        self.element_click(self.group_notice_close_loc)     # 关闭
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.into_person_invite()  # 进入通知的邀请消息中
        self.element_click(self.person_agree_loc)  # 点击同意
        time.sleep(5)
        self.close_notice()  # 关闭界面
        # self.element_click(self.group_loc)  # 点击团队
        self.click_file(team['team_name'])     # 点击团队
        self.element_click(self.group_notice_loc)  # 点击团队公告
        (title, content) = self.check_notice_content()  # 获取到的团队信息
        self.assertIn(team['team_notice_title'], title)
        self.assertIn(team['team_notice_content'], content)

