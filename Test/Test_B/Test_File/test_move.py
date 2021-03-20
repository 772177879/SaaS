from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.File.move_file import Move
from Object.static import get_config
import time
account = get_config('zsy')  # 读取账号


class TestMove(MyTest, Login, New, Delete, Move):
    def test_TestMove_01(self):
        """移动文件到我的文件，没法移动到相同位置"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('pg', 'pg移动到我的文件', '移动')      # 新建文件
        self.move_file('pg移动到我的文件', '我的文件')     # 移动到我的文件中
        self.verify_element_exist(self.move_fail_loc)       # 移动失败
        self.verify_file_exist('pg移动到我的文件.pptx')    # 验证老文件存在

    def test_TestMove_02(self):
        """移动文件到我的文件的文件夹内"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('ss', 'ss移动到我的文件', '移动')  # 新建文件
        self.new_folder('放移动文件的文件夹')    # 新建的文件夹
        self.move_file('ss移动到我的文件', '我的文件', '放移动文件的文件夹')  # 移动到我的文件的文件夹
        self.verify_file_none_exist('ss移动到我的文件')     # 验证老文件不存在
        self.click_file('放移动文件的文件夹')    # 进入文件夹中
        self.verify_file_exist('ss移动到我的文件')  # 验证新文件存在






