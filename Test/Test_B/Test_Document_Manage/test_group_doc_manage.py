from Object.myunit import MyTest
from Page.DocumentManage.part_doc_manage import PartDocumentManage
from Page.DocumentManage.group_doc_manage import GroupDocumentManage
from Page.Group.create import CreateGroup
from Page.Group.delete import GroupDelete
from Page.login import Login
from Object.static import get_config
from Page.File.new_file import New
import time
from Page.File.delete_file import Delete
account_admin = get_config('zsy')   # 读取账号
account_ynzf = get_config('cdd')   # 读取账号
team = get_config('team')
team_doc = get_config('team_doc')
team_folder_name = get_config('team_folder')['team_folder_name']


class TestGroupDocManage(MyTest, Login, PartDocumentManage, New, GroupDocumentManage, CreateGroup, GroupDelete):
    def test_TestGroupDocManage_01(self):
        """前端删除所有群组，创建群组后新建文件，后端验证前端新建的文件在这里是正常状态显示"""
        self.login(account_ynzf['username'], account_ynzf['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)      # 点击群组
        time.sleep(3)
        self.delete_all_group(account_ynzf['name'])     # 删除所有群组
        self.element_click(self.group_loc)  # 点击群组
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        self.click_file(team['team_name'])  # 选择该群组
        """前端开始新建文件"""
        self.new_folder(team_folder_name)   # 新建配置的文件夹
        self.new_file('ss', team_doc['team_doc_name'], team_doc['team_doc_content'])    # 新建配置的文件
        self.logout()   # 退出登录
        """后端再进入查看是否有文件，且是否是正常状态"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.group_doc_manage_loc)  # 点击群组文档管理
        time.sleep(2)
        self.select_group(team['team_name'])    # 选择群组
        time.sleep(2)
        """查看文件"""
        doc_status = self.get_file_status('ss', team_doc['team_doc_name'])   # 获取文件状态
        self.assertEqual('正常', doc_status)      # 验证是文件是正常
        time.sleep(1)
        folder_status = self.get_file_status('folder', team_folder_name)    # 获取文件状态
        self.assertEqual('正常', folder_status)  # 验证是文件是正常

    def test_TestGroupDocManage_02(self):
        """前端删除所有群组，创建群组后，新建文件删除，后端验证前端新建的文件在这里是已删除状态显示"""
        self.login(account_ynzf['username'], account_ynzf['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account_ynzf['name'])  # 删除所有群组
        self.element_click(self.group_loc)  # 点击群组
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        self.click_file(team['team_name'])  # 选择该群组
        """前端开始新建文件"""
        self.new_folder(team_folder_name)  # 新建配置的文件夹
        self.new_file('ss', team_doc['team_doc_name'], team_doc['team_doc_content'])  # 新建配置的文件
        """前端删除文件"""
        Delete(self.driver).delete_all()  # 删除所有文件
        self.logout()  # 退出登录
        """后端再进入查看是否有文件，且是否是正常状态"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.group_doc_manage_loc)  # 点击群组文档管理
        time.sleep(2)
        self.select_group(team['team_name'])  # 选择群组
        time.sleep(2)
        """查看文件"""
        doc_status = self.get_file_status('ss', team_doc['team_doc_name'])  # 获取文件状态
        self.assertEqual('已删除', doc_status)  # 验证是文件是已删除
        time.sleep(1)
        folder_status = self.get_file_status('folder', team_folder_name)  # 获取文件状态
        self.assertEqual('已删除', folder_status)  # 验证是文件是已删除

    def test_TestGroupDocManage_03(self):
        """前端删除所有群组，创建群组后，新建文件删除并清空回收站，后端验证前端新建的文件在这里是彻底删除状态显示"""
        self.login(account_ynzf['username'], account_ynzf['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(3)
        self.delete_all_group(account_ynzf['name'])  # 删除所有群组
        self.element_click(self.group_loc)  # 点击群组
        time.sleep(1)
        self.create_group(team['team_name'], team['team_describe'])  # 创建群组
        self.click_file(team['team_name'])  # 选择该群组
        """前端开始新建文件"""
        self.new_folder(team_folder_name)  # 新建配置的文件夹
        self.new_file('ss', team_doc['team_doc_name'], team_doc['team_doc_content'])  # 新建配置的文件
        """前端删除文件"""
        Delete(self.driver).delete_all()  # 删除所有文件
        self.element_click(self.recycle_loc)  # 点击回收站
        self.element_click(self.group_recycle_loc)  # 点击群组回收站
        time.sleep(2)
        Delete(self.driver).clean_recycle()  # 清空回收站
        self.logout()  # 退出登录
        """后端再进入查看是否有文件，且是否是正常状态"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.group_doc_manage_loc)  # 点击群组文档管理
        time.sleep(2)
        self.select_group(team['team_name'])  # 选择群组
        time.sleep(2)
        """查看文件"""
        doc_status = self.get_file_status('ss', team_doc['team_doc_name'])  # 获取文件状态
        self.assertEqual('彻底删除', doc_status)  # 验证是文件是彻底删除
        time.sleep(1)
        folder_status = self.get_file_status('folder', team_folder_name)  # 获取文件状态
        self.assertEqual('彻底删除', folder_status)  # 验证是文件是彻底删除
