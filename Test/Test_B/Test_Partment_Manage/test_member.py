from Object.myunit import MyTest
from Page.PartmentManage.organization import Organization
from Page.login import Login
from Object.static import get_config
import time
account = get_config('zsy')   # 读取账号
new_account = get_config('member_01')   # 读取账号
part_name = get_config('part')['part_name']


class TestMember(MyTest, Login, Organization):
    """组织架构中：
    1，新增成员
    2，禁用成员
    3，删除成员
    """
    def test_TestMember_01(self):
        """新增成员（删除前，先判断成员不存在）"""
        self.login(account['username'], account['password'])    # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()     # 进入控制台
        self.element_click(self.console_department_loc)     # 点击通讯录
        self.element_click(self.organization_loc)   # 点击组织架构
        time.sleep(2)
        self.into_partment(part_name)  # 点击部门
        time.sleep(2)
        # 先尝试删除成员，保证一定不存在
        try:
            self.delete(new_account['name'])    # 尝试删除该账号，再去新增账号
        except:
            pass
        time.sleep(2)
        self.element_click(self.add_member_loc)     # 点击新增成员
        self.add_member(new_account['account'], new_account['password_old'], new_account['name'], new_account['sex'],
                        new_account['telephone'], new_account['email'], new_account['position'],
                        new_account['comment'])     # 新增该账号
        self.close_page()   # 关闭后台，进入前端
        self.logout()       # 退出登录
        """新增成员后查看是否能登录"""
        self.login(new_account['account'], new_account['password_old'], new_member_login=1,
                   new_password=new_account['password_new'])     # 看看新账号重置密码能否登陆
        # self.wait_element(self.my_file_loc)     # 首页的我的文件
        self.guide()    # 新手引导

    def test_TestMember_02(self):
        """新增成员后，禁用"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_department_loc)  # 点击部门管理
        self.element_click(self.organization_loc)  # 点击组织架构
        time.sleep(2)
        self.into_partment(part_name)  # 点击部门
        time.sleep(2)
        # 先尝试删除成员，保证一定不存在
        try:
            self.delete(new_account['name'])  # 尝试删除该账号，再去新增账号
        except:
            pass
        time.sleep(2)
        self.element_click(self.add_member_loc)  # 点击新增成员
        self.add_member(new_account['account'], new_account['password_old'], new_account['name'], new_account['sex'],
                        new_account['telephone'], new_account['email'], new_account['position'],
                        new_account['comment'])  # 新增该账号
        time.sleep(2)
        self.forbid(new_account['name'])    # 禁用账号
        self.close_page()  # 关闭后台，进入前端
        self.logout()  # 退出登录
        """新增成员后查看登录是否被禁"""
        self.login(new_account['account'], new_account['password_old'])  # 看看新账号能否登录
        self.verify_element_exist(self.forbid_err_loc)      # 被禁提示

    def test_TestMember_03(self):
        """新增成员后，删除"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_department_loc)  # 点击部门管理
        self.element_click(self.organization_loc)  # 点击组织架构
        time.sleep(2)
        self.into_partment(part_name)  # 点击部门
        time.sleep(2)
        # 先尝试删除成员，保证一定不存在
        try:
            self.delete(new_account['name'])  # 尝试删除该账号，再去新增账号
        except:
            pass
        time.sleep(2)
        self.element_click(self.add_member_loc)  # 点击新增成员
        self.add_member(new_account['account'], new_account['password_old'], new_account['name'], new_account['sex'],
                        new_account['telephone'], new_account['email'], new_account['position'],
                        new_account['comment'])  # 新增该账号
        time.sleep(2)
        self.delete(new_account['name'])  # 删除账号
        self.close_page()  # 关闭后台，进入前端
        self.logout()  # 退出登录
        """新增成员后查看登录是否被删除"""
        self.login(new_account['account'], new_account['password_old'])  # 看看新账号能否登录
        self.wait_element(self.delete_err_loc)  # 被删除提示






