from Object.myunit import MyTest
from Page.PartmentManage.organization import Organization
from Page.login import Login
from Object.static import get_config
import time
from Page.File.upload_file import Upload
account = get_config('zsy')   # 读取账号
new_account = get_config('member_01')   # 读取账号
part_name = get_config('part')['part_name']


class TestMember(MyTest, Login, Organization, Upload):
    """组织架构中：
    1，新增成员
    2，禁用成员
    3，删除成员
    4. 导入成员
    """
    def test_TestMember_01(self):
        """新增成员（删除前，先判断成员不存在）"""
        self.login(account['username'], account['password'])    # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()     # 进入控制台
        self.element_click(self.console_department_loc)  # 点击部门管理
        self.element_click(self.organization_loc)  # 点击组织架构
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

    def test_TestMember_04(self):
        """导入成员前先清空导入记录"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_department_loc)  # 点击部门管理
        self.element_click(self.organization_loc)  # 点击组织架构
        time.sleep(2)
        # 先尝试删除成员，保证一定不存在
        try:
            self.into_partment('测试部')  # 点击部门
            time.sleep(2)
            self.delete('落荧')  # 尝试删除该账号，再去新增账号
        except:
            pass
        time.sleep(2)
        # 再尝试删除导入部门，保证一定不存在
        try:
            self.into_partment('永中软件')  # 点击导入部门的上级部门
            time.sleep(1)
            self.delete_part('测试部')  # 尝试删除该账号，再去新增账号
        except:
            pass
        time.sleep(2)
        self.element_click(self.bulk_add_loc)  # 点击批量导入
        time.sleep(1)
        self.element_click(self.add_step_loc)  # 点击下一步
        time.sleep(1)
        self.element_click(self.add_member_file_loc)  # 点击选择文件上传
        time.sleep(1)
        self.upload_model_file('yozo_import.xlsx')  # 选择模板上传
        time.sleep(1)
        self.verify_file_exist('yozo_import.xlsx')  # 验证文件上传成功
        self.element_click(self.add_step_loc)  # 点击下一步
        time.sleep(1)
        self.element_click(self.btn_member_pwd_loc)  # 点击设置随机密码
        get_casual = self.get_member_pwd()  # 获取随机密码
        time.sleep(2)
        self.element_click(self.add_step_loc)  # 点击下一步
        self.element_click(self.member_bulk_loc)  # 点击执行导入
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.driver.refresh()
        self.verify_file_exist('测试部', file_type=1)  # 验证部门导入成功
        self.close_page()   # 关闭后台，进入前端
        self.logout()  # 退出登录
        """新增成员后查看是否能登录"""
        self.login('13943225354', get_casual, new_member_login=1,
                   new_password=new_account['password_new'])  # 看看新账号重置密码能否登陆
        # self.wait_element(self.my_file_loc)     # 首页的我的文件
        self.guide()  # 新手引导
