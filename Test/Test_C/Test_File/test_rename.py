from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.File.rename_file import Rename
from Object.static import get_config
import time
account = get_config('client1')  # 读取账号


class TestRename(MyTest, Login, New, Delete, Rename):
    def test_Person_TestRename_01(self):
        """将文件名重命名"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('ss', 'ss重命名的文件', '关注')  # 新建文件
        self.rename('ss', 'ss重命名的文件', 'ss新的名称')     # 重命名
        self.verify_file_none_exist('ss重命名的文件')     # 老文件名不存在
        self.verify_file_exist('ss新的名称')        # 新文件名存在

    def test_Person_TestRename_02(self):
        """将文件夹名重命名"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_folder('用来重命名的文件夹')  # 新建文件
        self.rename('folder', '用来重命名的文件夹', '文件夹新名称')     # 重命名
        self.verify_file_none_exist('用来重命名的文件夹')     # 老文件名不存在
        self.verify_file_exist('文件夹新名称')        # 新文件名存在
