from Object.myunit import MyTest
from Page.GroupManage.GroupManage import GroupManage
from Page.Group.create import CreateGroup
from Page.Group.delete import GroupDelete
from Page.login import Login
from Object.static import get_config
import time
account_admin = get_config('zsy')   # 读取账号
account_sld = get_config('sld')   # 读取账号
team = get_config('team')


class TestGroupManage(MyTest, Login, GroupDelete, CreateGroup, GroupManage):
    def test_TestGroupManage_01(self):
        """前端新增了群组后，后端显示群组，且为正常状态"""
        self.login(account_sld['username'], account_sld['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account_sld['name'])  # 删除所有群组
        self.element_click(self.group_loc)  # 点击群组
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        self.logout()   # 退出登录
        """进入后端查看时，发现群组为新增状态"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_group_loc)  # 点击群组管理
        time.sleep(2)
        self.element_click(self.console_group_manage_loc)   # 进入群组管理
        status = self.get_group_status(team['team_name'])       # 获取群组状态
        self.assertEqual('正常', status)      # 验证状态是正常

    def test_TestGroupManage_02(self):
        """前端新增了群组后，再去删除群组，后端显示群组，且为已解散状态"""
        self.login(account_sld['username'], account_sld['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account_sld['name'])  # 删除所有群组
        self.element_click(self.group_loc)  # 点击群组
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        self.click_file(team['team_name'])  # 点击群组
        self.element_click(self.group_setting_loc)  # 点击设置
        self.delete_group()    # 删除群组
        self.logout()  # 退出登录
        """进入后端查看时，发现群组为新增状态"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_group_loc)  # 点击群组管理
        time.sleep(2)
        self.element_click(self.console_group_manage_loc)  # 进入群组管理
        status = self.get_group_status(team['team_name'])  # 获取群组状态
        self.assertEqual('已解散', status)  # 验证状态是正常

