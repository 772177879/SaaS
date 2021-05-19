from Object.myunit import MyTest
from Page.login import Login
from Page.AdminManage.admin import Admin
from Object.static import get_config
admin = get_config('zsy')  # 读取注册管理员账号
wdgly = get_config('wdgly')  # 读取文档管理员账号
ptgly = get_config('ptgly')  # 读取普通管理员账号


class TestAdminManage(MyTest, Login, Admin):

    def test_TestAdminManage_01(self):
        """登录并且创建各种管理员"""
        self.login(admin['username'], admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.admin_manage_loc)   # 点击管理员管理
        self.element_click(self.admin_manage_inner_loc)  # 点击管理员管理里的管理员管理
        try:
            self.delete_admin(ptgly['name'])  # 删除普通管理员
            self.delete_admin(wdgly['name'])  # 删除文档管理员
        except:
            pass
        self.new_admin('普通管理员', ptgly['name'])      # 添加普通管理员
        self.new_admin('文档管理员', wdgly['name'])  # 添加普通管理员

    def test_TestAdminManage_02(self):
        """验证普通管理员的权限"""
        self.login(ptgly['username'], ptgly['password'])  # 普通管理员登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.manage_check('ptgly')     # 验证权限

    def test_TestAdminManage_03(self):
        """验证文档管理员的权限"""
        self.login(wdgly['username'], wdgly['password'])  # 普通管理员登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.manage_check('wdgly')     # 验证权限

    def test_TestAdminManage_04(self):
        """验证管理员删除其他管理员"""
        self.login(admin['username'], admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.admin_manage_loc)   # 点击管理员管理
        self.element_click(self.admin_manage_inner_loc)     # 点击管理员管理里的管理员管理
        self.delete_admin(ptgly['name'])    # 删除普通管理员
        self.delete_admin(wdgly['name'])  # 删除文档管理员
        self.close_page()   # 退回到前主页
        self.logout()   # 退出登录
        self.login(wdgly['username'], wdgly['password'])  # 文档管理员登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.setting_loc)  # 点击设置
        self.verify_file_none_exist(self.console_loc)   # 没有进入企业控制台
        self.element_click(self.my_file_loc)    # 点击我的文件
        self.logout()   # 退出
        self.login(ptgly['username'], ptgly['password'])  # 文档管理员登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.setting_loc)  # 点击设置
        self.verify_file_none_exist(self.console_loc)   # 没有进入企业控制台
        self.element_click(self.my_file_loc)    # 点击我的文件
        self.logout()   # 退出
