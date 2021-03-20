from Object.myunit import MyTest
from Page.login import Login
from Object.static import get_config
import time
account = get_config('client1')   # 读取账号


class TestLogin(MyTest, Login):
    def test_Person_TestLogin_01(self):
        """登录和退出登录测试"""
        self.login(account['username'], account['password'], login_type=1)    # 登录
        self.wait_element(self.my_file_loc)
        self.logout()   # 退出
        self.wait_element(self.username_loc)    # 验证回到了登录界面
