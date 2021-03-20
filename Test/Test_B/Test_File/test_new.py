from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.search import Search
from Object.static import get_config
import time
account = get_config('zsy')  # 读取账号


class TestNew(MyTest, Login, New, Delete, Search):
    def test_TestNew_00(self):
        """进行操作之前，先保证我的文件是空的"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()       # 清空文件

    def test_TestNew_01(self):
        """新建wp文件，文件名：新建的wp， 文件内容：wp的文本内容"""
        self.login(account['username'], account['password'])    # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)    # 点击我的文件
        time.sleep(5)
        self.new_file('wp', '新建的wp', 'wp的文本内容')
        self.verify_file_exist('新建的wp')     # 验证文件存在
        time.sleep(5)
        self.driver.refresh()       # 刷新
        time.sleep(10)
        self.driver.refresh()  # 刷新
        file_names = self.search_file_content('wp的文本内容')     # 搜索内容后获取显示的文件列表
        print(file_names)
        self.assertIn('新建的wp.docx', file_names)

    def test_TestNew_02(self):
        """新建ss文件，文件名：新建的ss， 文件内容：ss的文本内容"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        time.sleep(5)
        self.new_file('ss', '新建的ss', 'ss的文本内容')
        self.verify_file_exist('新建的ss')     # 验证文件存在
        time.sleep(5)
        self.driver.refresh()  # 刷新
        time.sleep(10)
        self.driver.refresh()  # 刷新
        file_names = self.search_file_content('ss的文本内容')  # 搜索内容后获取显示的文件列表
        print(file_names)
        self.assertIn('新建的ss.xlsx', file_names)

    def test_TestNew_03(self):
        """新建pg文件，文件名：新建的pg， 文件内容：pg的文本内容"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        time.sleep(5)
        self.new_file('pg', '新建的pg', 'pg的文本内容')
        self.verify_file_exist('新建的pg')     # 验证文件存在
        time.sleep(5)
        self.driver.refresh()  # 刷新
        time.sleep(10)
        self.driver.refresh()  # 刷新
        file_names = self.search_file_content('pg的文本内容')  # 搜索内容后获取显示的文件列表
        print(file_names)
        self.assertIn('新建的pg.pptx', file_names)

    def test_TestNew_04(self):
        """新建文件夹，文件名：新建的文件夹"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        time.sleep(5)
        self.new_folder('新建的文件夹')
        time.sleep(5)
        self.verify_file_exist('新建的文件夹')

