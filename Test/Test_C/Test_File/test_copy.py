from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.File.copy_file import Copy
from Object.static import get_config
import time
account = get_config('client1')  # 读取账号


class TestCopy(MyTest, Login, New, Delete, Copy):
    def test_Person_TestCopy_01(self):
        """复制文件到我的文件"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('pg', 'pg复制到我的文件', '复制')      # 新建文件
        self.copy_file('pg复制到我的文件', '我的文件')     # 复制到我的文件中
        self.verify_file_exist('pg复制到我的文件.pptx')    # 验证老文件存在
        self.verify_file_exist('pg复制到我的文件(1).pptx')     # 验证出现新的重复文件

    def test_Person_TestCopy_02(self):
        """复制文件到我的文件的文件夹内"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('ss', 'ss复制到我的文件的文件夹', '复制')  # 新建文件
        self.new_folder('放复制文件的文件夹')    # 新建的文件夹
        self.copy_file('ss复制到我的文件的文件夹', '我的文件', '放复制文件的文件夹')
        self.verify_file_exist('ss复制到我的文件的文件夹')     # 验证老文件存在
        self.click_file('放复制文件的文件夹')    # 进入文件夹中
        self.verify_file_exist('ss复制到我的文件的文件夹')  # 验证新文件存在






