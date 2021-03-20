from Object.myunit import MyTest
from Page.Group.create import CreateGroup
from Page.Group.delete import GroupDelete
from Page.Group.member import Member
from Page.login import Login
from Page.File.new_file import New
from Object.static import get_config
import time
team = get_config('team')
account = get_config('zsy')  # 读取账号
account2 = get_config('sld')  # 读取账号


class TestGroupLimit(MyTest, CreateGroup, Login, GroupDelete, Member, New):
    def test_TestGroupLimit_00(self):
        """创建群组之前，先清空所有自己的群组"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account['name'])  # 删除所有群组

    def test_TestGroupLimit_01(self):
        """接收群组之前，先清空所有自己的群组"""
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account2['name'])  # 删除所有群组

    def test_TestGroupLimit_02(self):
        """验证成员编辑权限，对文件的权限判断"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        group_list = self.get_group_list()  # 获取所有群组的字典
        self.assertIn([team['team_name'], '我创建的'], group_list)  # 验证出现了群组，且是我创建的
        self.click_file(team['team_name'])  # 选择该群组
        self.new_file('wp', '群组内文件编辑权限', '群组内权限判断')
        self.element_click(self.group_user_loc)  # 点击成员管理
        time.sleep(1)
        self.add_group_member(account2['name'])  # 添加sld账号
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        self.click_file(team['team_name'])  # 点击群组
        limit_list = self.get_file_limit('群组内文件编辑权限')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        self.assertIn('添加标签', limit_list)
        self.assertIn('创建副本', limit_list)
        self.assertIn('移动到', limit_list)
        self.assertIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        self.assertIn('重命名', limit_list)
        self.assertIn('放入回收站', limit_list)

    def test_TestGroupLimit_03(self):
        """创建群组之前，先清空所有自己的群组"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account['name'])  # 删除所有群组

    def test_TestGroupLimit_04(self):
        """验证成员查看权限，对文件的权限判断"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        group_list = self.get_group_list()  # 获取所有群组的字典
        self.assertIn([team['team_name'], '我创建的'], group_list)  # 验证出现了群组，且是我创建的
        self.click_file(team['team_name'])  # 选择该群组
        self.new_file('wp', '群组内文件查看权限', '群组内权限判断')
        self.element_click(self.group_user_loc)  # 点击成员管理
        time.sleep(1)
        self.add_group_member(account2['name'])  # 添加sld账号
        time.sleep(2)
        self.def_member_options(account2['name'], '查看')
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        self.click_file(team['team_name'])  # 点击群组
        limit_list = self.get_file_limit('群组内文件查看权限')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        self.assertIn('添加标签', limit_list)
        self.assertNotIn('创建副本', limit_list)
        self.assertNotIn('移动到', limit_list)
        self.assertNotIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        self.assertNotIn('重命名', limit_list)
        self.assertNotIn('删除', limit_list)
