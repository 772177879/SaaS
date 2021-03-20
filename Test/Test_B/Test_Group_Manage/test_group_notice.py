from Object.myunit import MyTest
from Page.DocumentManage.part_doc_manage import PartDocumentManage
from Page.GroupManage.GroupNotice import GroupNoticeConsole
from Page.Group.notice import GroupNotice
from Page.Group.create import CreateGroup
from Page.Group.delete import GroupDelete
from Page.login import Login
from Object.static import get_config
import time
account_admin = get_config('zsy')   # 读取账号
account_sld= get_config('sld')   # 读取账号
team = get_config('team')


class TestGroupNotice(MyTest, Login, GroupDelete, CreateGroup, PartDocumentManage, GroupNotice, GroupNoticeConsole):
    def test_TestGroupNotice_01(self):
        """后端删除所有公告后，在前端新建群组后公告后，能有对应信息，且正确"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_group_loc)  # 点击群组管理
        time.sleep(2)
        self.element_click(self.console_group_notice_loc)   # 点击群组公告
        try:
            self.delete_all()   # 删除所有文件
        except:
            pass
        self.close_page()  # 关闭后台，进入前端
        self.logout()  # 退出登录
        """前端登录后新建群组公告"""
        self.login(account_sld['username'], account_sld['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account_sld['name'])  # 删除所有群组
        self.element_click(self.group_loc)  # 点击群组
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        self.click_file(team['team_name'])      # 点击群组
        self.element_click(self.group_setting_loc)  # 点击群组设置
        time.sleep(2)
        self.publish_group_notice(team['team_notice_title'], team['team_notice_content'])  # 发布公告
        self.logout()  # 退出登录
        """后台校验出现了该公告"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_group_loc)  # 点击群组管理
        time.sleep(2)
        self.element_click(self.console_group_notice_loc)  # 点击群组公告
        group, creator = self.get_notice_status(team['team_notice_title'])      # 获取群组名，和创建者
        content = self.get_notice_content(team['team_notice_title'])        # 获取内容
        self.assertEqual(group, team['team_name'])      # 验证名称一致
        self.assertEqual(creator, account_sld['name'])     # 验证创建人一致
        self.assertEqual(content, team['team_notice_content'])      # 验证内容一致

