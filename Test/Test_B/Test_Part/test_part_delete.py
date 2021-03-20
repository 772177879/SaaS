from Object.myunit import MyTest
from Page.login import Login
from Object.static import get_config
from Page.File.new_file import New
from Page.File.delete_file import Delete
import time
account_admin = get_config('zsy')
account_cdd = get_config('cdd')
account_sld = get_config('sld')
part = get_config('part')['part_name']
part_son = get_config('part_son')['part_son_name']
manager_file = get_config('part_file_manager')
manager_folder = get_config('part_folder_manager')
member_file = get_config('part_file_member')
member_folder = get_config('part_folder_member')


class TestPartDelete(MyTest, Login, New, Delete):

    def test_TestPartDelete_01(self):
        """验证部门经理删除文件后，文件在部门经理的部门回收站中"""
        self.login(account_cdd['username'], account_cdd['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)   # 点击部门
        self.click_file(part)   # 进入自动化部门中
        try:
            self.delete_all(delete_type=1)      # 删除所有文件
        except:
            pass
        self.element_click(self.recycle_loc)  # 点击回收站
        self.element_click(self.part_recycle_loc)  # 点击部门回收站
        time.sleep(2)
        try:
            self.clean_recycle()  # 清空回收站
        except:
            pass
        # 去新建文件
        self.element_click(self.part_loc)  # 点击部门
        self.click_file(part)  # 进入自动化部门中
        self.new_file('wp', manager_file['name'], manager_file['content'])      # 新建经理文件
        self.new_folder(manager_folder['name'])     # 新建经理文件夹
        # 经理删除自己的文件夹和文件，看看回收站的位置
        self.delete_file(manager_file['name'])      # 删除文件
        self.delete_file(manager_folder['name'])    # 删除文件夹
        # 看部门回收站中是否有东西
        self.element_click(self.recycle_loc)  # 点击回收站
        self.element_click(self.part_recycle_loc)  # 点击部门回收站
        time.sleep(2)
        self.verify_file_exist(manager_file['name'])    # 验证存在
        self.verify_file_exist(manager_folder['name'])  # 验证存在
        self.logout()   # 退出登录
        # 验证成员的部门回收站是没有的
        self.login(account_sld['username'], account_sld['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.recycle_loc)  # 点击回收站
        self.element_click(self.part_recycle_loc)  # 点击部门回收站
        time.sleep(2)
        self.verify_file_none_exist(manager_file['name'])  # 验证不存在
        self.verify_file_none_exist(manager_folder['name'])  # 验证不存在

    def test_TestPartDelete_02(self):
        """验证部门成员删除文件后，文件在部门经理的部门回收站中"""
        self.login(account_cdd['username'], account_cdd['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)   # 点击部门
        self.click_file(part)   # 进入自动化部门中
        try:
            self.delete_all(delete_type=1)      # 删除所有文件
        except:
            pass
        self.element_click(self.recycle_loc)  # 点击回收站
        self.element_click(self.part_recycle_loc)  # 点击部门回收站
        time.sleep(2)
        try:
            self.clean_recycle()  # 清空回收站
        except:
            pass
        self.logout()   # 退出登录
        # 成员去新建文件再删除
        self.login(account_sld['username'], account_sld['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)  # 点击部门
        self.click_file(part)  # 进入自动化部门中
        self.new_file('wp', member_file['name'], member_file['content'])      # 新建经理文件
        self.new_folder(member_folder['name'])     # 新建经理文件夹
        # 成员删除自己的文件夹和文件，看看回收站的位置
        self.delete_file(member_file['name'])      # 删除文件
        self.delete_file(member_folder['name'])    # 删除文件夹
        # 看部门回收站中是否有东西
        self.element_click(self.recycle_loc)  # 点击回收站
        self.element_click(self.part_recycle_loc)  # 点击部门回收站
        time.sleep(2)
        self.verify_file_none_exist(member_file['name'])    # 验证不存在
        self.verify_file_none_exist(member_folder['name'])  # 验证不存在
        self.logout()   # 退出登录
        # 验证经理的部门回收站是有的
        self.login(account_cdd['username'], account_cdd['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.recycle_loc)  # 点击回收站
        self.element_click(self.part_recycle_loc)  # 点击部门回收站
        time.sleep(2)
        self.verify_file_exist(member_file['name'])  # 验证存在
        self.verify_file_exist(member_folder['name'])  # 验证存在


