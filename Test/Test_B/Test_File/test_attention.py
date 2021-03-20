from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.File.attention_file import Attention
from Object.static import get_config
import time
account = get_config('zsy')  # 读取账号


class TestAttention(MyTest, Login, New, Delete, Attention):
    def test_TestAttention_01(self):
        """关注我的文件的文件，再取消关注"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', 'wp关注的文件', '关注')  # 新建文件
        # 关注文件
        self.attention_file('wp关注的文件')      # 关注文件
        file_list = self.attention_file_list()      # 获取关注文件列表
        self.assertIn('wp关注的文件.docx', file_list)       # 验证关注文件列表出现该文件
        # 取消关注
        self.attention_cancel_file('wp关注的文件')       # 取消关注
        time.sleep(2)
        file_list = self.attention_file_list()  # 获取关注文件列表
        self.assertNotIn('wp关注的文件.docx', file_list)  # 验证关注文件列表出现该文件



