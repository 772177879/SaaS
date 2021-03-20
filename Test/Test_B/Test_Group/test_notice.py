from Object.myunit import MyTest
from Page.Group.create import CreateGroup
from Page.Group.delete import GroupDelete
from Page.Group.member import Member
from Page.Group.notice import GroupNotice
from Page.login import Login
from Object.static import get_config
import time
account = get_config('zsy')  # 读取账号
account2 = get_config('sld')  # 读取账号
team = get_config('team')


class TestGroupNotice(MyTest, CreateGroup, Login, GroupDelete, Member, GroupNotice):
    def test_TestGroupNotice_00(self):
        """创建群组之前，先清空所有自己的群组"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account['name'])  # 删除所有群组

    def test_TestGroupNotice_01(self):
        """接收群组之前，先清空所有自己的群组"""
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account2['name'])  # 删除所有群组

    def test_TestGroupNotice_02(self):
        """验证添加公告，群组和成员都可以查看"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        group_list = self.get_group_list()  # 获取所有群组的字典
        self.assertIn([team['team_name'], '我创建的'], group_list)  # 验证出现了群组，且是我创建的
        self.click_file(team['team_name'])  # 选择该群组
        self.element_click(self.group_user_loc)  # 点击成员管理
        time.sleep(1)
        self.add_group_member(account2['name'])  # 添加sld账号
        # 创建公告
        self.element_click(self.group_setting_loc)      # 点击群组设置
        self.publish_group_notice(team['team_notice_title'], team['team_notice_content'])     # 发布公告
        self.element_click(self.group_notice_loc)   # 点击群组公告
        time.sleep(2)
        (title, content) = self.check_notice_content()      # 获取到的群组信息
        self.assertIn(team['team_notice_title'], title)      # 验证信息是否正确
        self.assertIn(team['team_notice_content'], content)
        self.element_click(self.group_notice_close_loc)     # 关闭
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        self.click_file(team['team_name'])     # 点击群组
        self.element_click(self.group_notice_loc)  # 点击群组公告
        (title, content) = self.check_notice_content()  # 获取到的群组信息
        self.assertIn(team['team_notice_title'], title)
        self.assertIn(team['team_notice_content'], content)

