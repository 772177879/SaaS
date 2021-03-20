from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Object.static import get_config
import time
account = get_config('client1')  # 读取账号


class TestDelete(MyTest, Login, New, Delete):

    def test_Person_TestDelete_01(self):
        """删除文件，验证文件在回收站中，可以恢复"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.element_click(self.recycle_loc)  # 点击回收站
        time.sleep(2)
        self.clean_recycle()    # 清空回收站
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_file('wp', '删除专用wp', 'wp的删除内容')    # 新建文件
        time.sleep(1)
        self.delete_file('删除专用wp')      # 删除文件
        self.verify_file_none_exist('删除专用wp')   # 文件不存在
        self.element_click(self.recycle_loc)    # 进入回收站中
        self.verify_file_exist('删除专用wp')    # 验证文件存在
        self.right_click_filename('删除专用wp')
        self.element_click(self.recover_loc)    # 恢复
        self.verify_element_exist(self.empty_recycle_loc)   # 回收站空了
        self.element_click(self.my_file_loc)    # 点击我的文件
        self.verify_file_exist('删除专用wp')    # 文件恢复了

    def test_Person_TestDelete_02(self):
        """删除文件，验证文件在回收站中，可以永久删除"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.element_click(self.recycle_loc)  # 点击回收站
        time.sleep(2)
        self.clean_recycle()  # 清空回收站
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_file('wp', '删除专用ss', 'ss的删除内容')  # 新建文件
        time.sleep(1)
        self.delete_file('删除专用ss')  # 删除文件
        self.verify_file_none_exist('删除专用wp')  # 文件不存在
        self.element_click(self.recycle_loc)  # 进入回收站中
        self.verify_file_exist('删除专用ss')  # 验证文件存在
        self.right_click_filename('删除专用ss')
        self.element_click(self.forever_delete_loc)  # 永久删除
        self.element_click(self.sure_loc)       # 点击确认
        self.verify_element_exist(self.empty_recycle_loc)  # 回收站空了
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.verify_element_exist(self.empty_loc)   # 我的文件也是空的，文件没恢复

