from Object.myunit import MyTest
from Page.Group.create import CreateGroup
from Page.Group.delete import GroupDelete
from Page.Group.member import Member
from Page.login import Login
from Object.static import get_config
from Page.Notice.Notice import Notice
import time
account = get_config('client1')  # 读取账号
account2 = get_config('client2')  # 读取账号
team = get_config('team')
invite_message = "邀请您加入团队【%s】" % team['team_name']
# delete_message = "您加入的团队%s已被解散" % team['team_name']


class TestCreateGroup(MyTest, CreateGroup, Login, GroupDelete, Member, Notice):
    def test_Person_TestCreateGroup_00(self):
        """创建团队之前，先清空所有自己的团队"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)      # 点击团队
        time.sleep(3)
        self.delete_all_group(account['name'])     # 删除所有团队

    def test_Person_TestCreateGroup_01(self):
        """接收团队之前，先清空所有自己的团队"""
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)      # 点击团队
        time.sleep(3)
        self.delete_all_group(account2['name'])     # 删除所有团队

    def test_Person_TestCreateGroup_02(self):
        """创建团队后，再去添加人员"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)  # 点击团队
        # self.create_group(team['team_name'], team['team_describe'])  # 创建团队
        self.create_team(team['team_name'])     # 创建
        group_list = self.get_group_list()  # 获取所有团队的字典
        self.assertIn([team['team_name'], '我创建的'], group_list)  # 验证出现了团队，且是我创建的
        self.click_file(team['team_name'])     # 选择该团队
        self.element_click(self.group_user_loc)  # 点击成员管理
        time.sleep(1)
        self.add_group_member(account2['username'])     # 添加client2账号
        self.logout()   # 退出登录
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.into_notice_notice()       # 进入通知的通知
        self.into_person_invite()   # 进入通知的邀请消息中
        # text = self.invite_team_notice()       # 验证邀请的通知存在
        text = self.person_invite()    # 验证邀请加入团队的通知存在
        # self.assertEqual(invite_message, text)
        self.assertIn(invite_message, text)
        self.element_click(self.person_agree_loc)   # 点击同意
        time.sleep(5)
        self.close_notice()     # 关闭界面
        # self.element_click(self.group_loc)  # 点击团队
        group_list = self.get_group_list()  # 获取所有团队的字典
        self.assertIn([team['team_name'], '我加入的'], group_list)  # 验证出现了团队，且是我加入的

    def test_Person_TestCreateGroup_03(self):
        """删除团队，团队消失"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)  # 点击团队
        time.sleep(3)
        self.click_file(team['team_name'])  # 点击团队
        self.element_click(self.group_setting_loc)  # 点击设置
        self.delete_group()  # 删除
        # self.into_notice_notice()       # 进入通知的通知
        # text = self.team_delete_notice()       # 验证删除团队的通知在
        # self.assertEqual(delete_message, text)
        # self.close_notice()     # 关闭界面
        self.logout()  # 退出登录
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.into_notice_notice()  # 进入通知的通知
        # text = self.team_delete_notice()  # 验证删除团队的通知在
        # self.assertEqual(delete_message, text)
        # self.close_notice()  # 关闭界面
        self.verify_file_none_exist(team['team_name'])  # 验证团队不存在

    def test_Person_TestCreateGroup_04(self):
        """创建团队时就直接添加成员，查看权限"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)      # 点击团队
        time.sleep(3)
        self.delete_all_group(account['name'])  # 删除所有团队
        self.create_team(team['team_name'], team_type=1, team_member=account2['username'], limit_select='查看')  # 创建
        group_list = self.get_group_list()  # 获取所有团队的字典
        self.assertIn([team['team_name'], '我创建的'], group_list)  # 验证出现了团队，且是我创建的
        self.logout()  # 退出登录
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.into_person_invite()  # 进入通知的邀请消息中
        text = self.person_invite()  # 验证邀请加入团队的通知存在
        self.assertIn(invite_message, text)
        self.element_click(self.person_agree_loc)  # 点击同意
        self.close_notice()  # 关闭界面
        group_list = self.get_group_list()  # 获取所有团队的字典
        self.assertIn([team['team_name'], '我加入的'], group_list)  # 验证出现了团队，且是我加入的
        self.click_file(team['team_name'])  # 点击团队
        self.element_click(self.new_loc)    # 点击新建
        self.verify_element_exist(self.no_new_loc)  # 显示无操作权限，查看权限

    def test_Person_TestCreateGroup_05(self):
        """创建团队时就直接添加成员，编辑权限"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)      # 点击团队
        time.sleep(3)
        self.delete_all_group(account['name'])  # 删除所有团队
        self.create_team(team['team_name'], team_type=1, team_member=account2['username'], limit_select='编辑')  # 创建
        group_list = self.get_group_list()  # 获取所有团队的字典
        self.assertIn([team['team_name'], '我创建的'], group_list)  # 验证出现了团队，且是我创建的
        self.logout()  # 退出登录
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.into_person_invite()  # 进入通知的邀请消息中
        text = self.person_invite()  # 验证邀请加入团队的通知存在
        self.assertIn(invite_message, text)
        self.element_click(self.person_agree_loc)  # 点击同意
        self.close_notice()  # 关闭界面
        group_list = self.get_group_list()  # 获取所有团队的字典
        self.assertIn([team['team_name'], '我加入的'], group_list)  # 验证出现了团队，且是我加入的
        self.click_file(team['team_name'])  # 点击团队
        self.element_click(self.new_loc)    # 点击新建
        self.verify_element_exist(self.new_wp_loc)  # 显示出新建wp

    def test_Person_TestCreateGroup_06(self):
        """创建团队时邀请成员，成员拒绝"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # self.element_click(self.group_loc)      # 点击团队
        time.sleep(3)
        self.delete_all_group(account['name'])  # 删除所有团队
        self.create_team(team['team_name'], team_type=1, team_member=account2['username'], limit_select='编辑')  # 创建
        group_list = self.get_group_list()  # 获取所有团队的字典
        self.assertIn([team['team_name'], '我创建的'], group_list)  # 验证出现了团队，且是我创建的
        self.logout()  # 退出登录
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.into_person_invite()  # 进入通知的邀请消息中
        text = self.person_invite()  # 验证邀请加入团队的通知存在
        self.assertIn(invite_message, text)
        self.element_click(self.person_refuse_loc)  # 点击拒绝
        self.close_notice()  # 关闭界面
        group_list = self.get_group_list()  # 获取所有团队的字典
        self.assertNotIn([team['team_name'], '我加入的'], group_list)  # 验证没有出现该团队
        # self.click_file(team['team_name'])  # 点击团队
        # self.element_click(self.new_loc)    # 点击新建
        # self.verify_element_exist(self.new_wp_loc)  # 显示出新建wp
        self.logout()  # 退出登录
        # 发起人登录后查看用户，没有该用户
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.click_file(team['team_name'])  # 选择该团队
        self.element_click(self.group_user_loc)  # 点击成员管理
        self.verify_file_exist(account['name'])   # 自己存在
        self.verify_file_none_exist(account2['name'])   # 被邀请的人不在










