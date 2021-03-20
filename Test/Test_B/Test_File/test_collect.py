from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.File.collect_file import Collect
from Object.static import get_config
import time
account = get_config('zsy')  # 读取账号


class TestCollect(MyTest, Login, New, Delete, Collect):
    def test_TestCollect_01(self):
        """收藏我的文件里的文件后，再去取消收藏"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', 'wp收藏的文件', '收藏')      # 新建文件
        # 收藏文件
        self.collect_file('wp收藏的文件')    # 收藏文件
        self.element_click(self.my_collect_loc)     # 点击我的收藏
        self.verify_file_exist('wp收藏的文件')       # 文件被收藏
        # 取消收藏
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.collect_cancel_file('wp收藏的文件')     # 取消收藏
        self.element_click(self.my_collect_loc)  # 点击我的收藏
        self.verify_file_none_exist('wp收藏的文件')  # 文件没被收藏

    def test_TestCollect_02(self):
        """收藏我的文件里的文件夹（带文件）"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_folder('收藏的文件夹')   # 新建文件夹
        self.click_file('收藏的文件夹')   # 进入文件夹里面
        self.new_file('ss', '文件夹里的ss', '收藏')       # 新建文件
        self.element_click(self.my_file_loc)  # 点击我的文件
        # 收藏
        self.collect_file('收藏的文件夹')     # 收藏文件夹
        self.element_click(self.my_collect_loc)     # 点击我的收藏
        self.verify_file_exist('收藏的文件夹')    # 出现文件夹
        self.verify_file_none_exist('文件夹里的ss')     # 文件没出现
        self.click_file('收藏的文件夹')       # 进入文件夹
        self.verify_file_exist('文件夹里的ss')  # 文件出现
        # 取消收藏
        self.element_click(self.my_collect_loc)     # 点击我的收藏
        self.collect_cancel_file('收藏的文件夹')      # 取消收藏文件夹
        self.verify_file_none_exist('收藏的文件夹')       # 文件夹不存在
        self.verify_file_none_exist('文件夹里的ss')  # 文件不存在

    def test_TestCollect_03(self):
        """收藏我的文件里的文件夹（带文件）和内部文件"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_folder('收藏的文件夹')  # 新建文件夹
        self.click_file('收藏的文件夹')  # 进入文件夹里面
        self.new_file('ss', '文件夹里的ss', '收藏')  # 新建文件
        self.element_click(self.my_file_loc)  # 点击我的文件
        # 收藏
        self.collect_file('收藏的文件夹')  # 收藏文件夹
        self.click_file('收藏的文件夹')  # 进入文件夹里面
        self.collect_file('文件夹里的ss')  # 收藏内部文件
        self.element_click(self.my_collect_loc)  # 点击我的收藏
        self.verify_file_exist('收藏的文件夹')  # 出现文件夹
        self.verify_file_exist('文件夹里的ss')  # 出现文件
        self.click_file('收藏的文件夹')  # 进入文件夹
        self.verify_file_exist('文件夹里的ss')  # 文件出现
        # 取消收藏
        self.element_click(self.my_collect_loc)  # 点击我的收藏
        self.collect_cancel_file('收藏的文件夹')      # 取消收藏文件夹
        self.verify_file_none_exist('收藏的文件夹')       # 文件夹消失
        self.verify_file_exist('文件夹里的ss')  # 但是文件出现



