from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.File.tag_file import Tag
from Object.static import get_config
import time
account = get_config('zsy')  # 读取账号


class TestTag(MyTest, Login, New, Delete, Tag):
    def test_TestTag_01(self):
        """为文件添加标签,并且进行标签筛选"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('ss', 'ss添加标签的文件', '标签以及标签搜索')  # 新建文件
        time.sleep(2)
        self.add_tag('ss添加标签的文件', 'zsy自动化标签')   # 添加标签zsy自动化标签
        self.element_click(self.close_loc)  # 点击关闭添加标签界面
        time.sleep(2)
        file_names = self.tag_search('zsy自动化标签')   # 标签筛选
        self.assertIn('ss添加标签的文件.xlsx', file_names)

    def test_TestTag_02(self):
        """为文件夹添加标签，并且进行标签筛选"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_folder('标签的文件夹')  # 新建文件夹
        time.sleep(2)
        self.add_tag('标签的文件夹', 'zsy自动化标签')  # 添加标签zsy自动化标签
        self.element_click(self.close_loc)  # 点击关闭添加标签界面
        time.sleep(2)
        file_names = self.tag_search('zsy自动化标签')  # 标签筛选
        self.assertIn('标签的文件夹', file_names)
