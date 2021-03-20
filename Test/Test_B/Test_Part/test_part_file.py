from Object.myunit import MyTest
from Page.login import Login
from Object.static import get_config
from Page.File.new_file import New
from Page.File.delete_file import Delete
account_admin = get_config('zsy')
account_cdd = get_config('cdd')
account_sld = get_config('sld')
part = get_config('part')['part_name']
part_son = get_config('part_son')['part_son_name']
manager_file = get_config('part_file_manager')
manager_folder = get_config('part_folder_manager')
member_file = get_config('part_file_member')
member_folder = get_config('part_folder_member')


class TestPartFile(MyTest, Login, New, Delete):

    def test_TestPartFile_01(self):
        """验证部门经理在里面新建了文件，经理和成员的权限区别"""
        self.login(account_cdd['username'], account_cdd['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)   # 点击部门
        self.click_file(part)   # 进入自动化部门中
        try:
            self.delete_all(delete_type=1)      # 删除所有文件
        except:
            pass
        self.new_file('wp', manager_file['name'], manager_file['content'])      # 新建经理文件
        self.new_folder(manager_folder['name'])     # 新建经理文件夹
        # 经理验证对于自己新建文件的权限
        manager_folder_limit_list = self.get_file_limit(manager_folder['name'])  # 获取右击菜单的权限
        self.assertIn('共享', manager_folder_limit_list)
        self.assertIn('协作', manager_folder_limit_list)
        self.assertIn('收藏文件', manager_folder_limit_list)
        self.assertIn('添加标签', manager_folder_limit_list)
        self.assertIn('创建副本', manager_folder_limit_list)
        self.assertIn('移动到', manager_folder_limit_list)
        self.assertIn('重命名', manager_folder_limit_list)
        self.assertIn('下载', manager_folder_limit_list)
        self.assertIn('增设权限', manager_folder_limit_list)
        self.assertIn('查看详情', manager_folder_limit_list)
        self.assertIn('放入回收站', manager_folder_limit_list)
        self.assertEqual(11, len(manager_folder_limit_list))
        self.driver.refresh()   # 刷新一下界面
        manager_file_limit_list = self.get_file_limit(manager_file['name'])   # 获取右击菜单的权限
        self.assertIn('共享', manager_file_limit_list)
        self.assertIn('协作', manager_file_limit_list)
        self.assertIn('收藏文件', manager_file_limit_list)
        self.assertIn('关注文件', manager_file_limit_list)
        self.assertIn('添加标签', manager_file_limit_list)
        self.assertIn('创建副本', manager_file_limit_list)
        self.assertIn('移动到', manager_file_limit_list)
        self.assertIn('重命名', manager_file_limit_list)
        self.assertIn('下载', manager_file_limit_list)
        self.assertIn('增设权限', manager_file_limit_list)
        self.assertIn('锁定文件', manager_file_limit_list)
        self.assertIn('查看详情', manager_file_limit_list)
        self.assertIn('放入回收站', manager_file_limit_list)
        self.assertEqual(13, len(manager_file_limit_list))
        self.logout()   # 退出登录
        # 成员对于经理的文件的权限判断
        self.login(account_sld['username'], account_sld['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)  # 点击部门
        self.click_file(part)  # 进入自动化部门中
        member_folder_limit_list = self.get_file_limit(manager_folder['name'])  # 获取右击菜单的权限
        self.assertIn('共享', member_folder_limit_list)
        self.assertIn('协作', member_folder_limit_list)
        self.assertIn('收藏文件', member_folder_limit_list)
        self.assertIn('添加标签', member_folder_limit_list)
        self.assertIn('创建副本', member_folder_limit_list)
        self.assertIn('重命名', member_folder_limit_list)
        self.assertIn('下载', member_folder_limit_list)
        self.assertIn('查看详情', member_folder_limit_list)
        self.assertEqual(8, len(member_folder_limit_list))
        self.driver.refresh()  # 刷新一下界面
        member_file_limit_list = self.get_file_limit(manager_file['name'])  # 获取右击菜单的权限
        self.assertIn('共享', member_file_limit_list)
        self.assertIn('协作', member_file_limit_list)
        self.assertIn('收藏文件', member_file_limit_list)
        self.assertIn('关注文件', member_file_limit_list)
        self.assertIn('添加标签', member_file_limit_list)
        self.assertIn('创建副本', member_file_limit_list)
        self.assertIn('重命名', member_file_limit_list)
        self.assertIn('下载', member_file_limit_list)
        self.assertIn('锁定文件', member_file_limit_list)
        self.assertIn('查看详情', member_file_limit_list)
        self.assertEqual(10, len(member_file_limit_list))

    def test_TestPartFile_02(self):
        """验证部门成员在里面新建了文件，经理和成员的权限区别"""
        self.login(account_sld['username'], account_sld['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)  # 点击部门
        self.click_file(part)  # 进入自动化部门中
        self.new_file('wp', member_file['name'], member_file['content'])  # 新建成员文件
        self.new_folder(member_folder['name'])  # 新建成员文件夹
        # 成员验证对于自己新建文件的权限
        member_folder_limit_list = self.get_file_limit(member_folder['name'])  # 获取右击菜单的权限
        self.assertIn('共享', member_folder_limit_list)
        self.assertIn('协作', member_folder_limit_list)
        self.assertIn('收藏文件', member_folder_limit_list)
        self.assertIn('添加标签', member_folder_limit_list)
        self.assertIn('创建副本', member_folder_limit_list)
        self.assertIn('重命名', member_folder_limit_list)
        self.assertIn('下载', member_folder_limit_list)
        self.assertIn('查看详情', member_folder_limit_list)
        self.assertIn('放入回收站', member_folder_limit_list)
        self.assertEqual(9, len(member_folder_limit_list))
        self.driver.refresh()  # 刷新一下界面
        member_file_limit_list = self.get_file_limit(member_file['name'])  # 获取右击菜单的权限
        self.assertIn('共享', member_file_limit_list)
        self.assertIn('协作', member_file_limit_list)
        self.assertIn('收藏文件', member_file_limit_list)
        self.assertIn('关注文件', member_file_limit_list)
        self.assertIn('添加标签', member_file_limit_list)
        self.assertIn('创建副本', member_file_limit_list)
        self.assertIn('重命名', member_file_limit_list)
        self.assertIn('下载', member_file_limit_list)
        self.assertIn('锁定文件', member_file_limit_list)
        self.assertIn('查看详情', member_file_limit_list)
        self.assertIn('放入回收站', member_file_limit_list)
        self.assertEqual(11, len(member_file_limit_list))
        self.logout()  # 退出登录
        # 经理对于成员的文件的权限判断
        self.login(account_cdd['username'], account_cdd['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)  # 点击部门
        self.click_file(part)  # 进入自动化部门中
        manager_folder_limit_list = self.get_file_limit(member_folder['name'])  # 获取右击菜单的权限
        self.assertIn('共享', manager_folder_limit_list)
        self.assertIn('协作', manager_folder_limit_list)
        self.assertIn('收藏文件', manager_folder_limit_list)
        self.assertIn('添加标签', manager_folder_limit_list)
        self.assertIn('创建副本', manager_folder_limit_list)
        self.assertIn('移动到', manager_folder_limit_list)
        self.assertIn('重命名', manager_folder_limit_list)
        self.assertIn('下载', manager_folder_limit_list)
        self.assertIn('增设权限', manager_folder_limit_list)
        self.assertIn('查看详情', manager_folder_limit_list)
        self.assertIn('放入回收站', manager_folder_limit_list)
        self.assertEqual(11, len(manager_folder_limit_list))
        self.driver.refresh()  # 刷新一下界面
        manager_file_limit_list = self.get_file_limit(member_file['name'])  # 获取右击菜单的权限
        self.assertIn('共享', manager_file_limit_list)
        self.assertIn('协作', manager_file_limit_list)
        self.assertIn('收藏文件', manager_file_limit_list)
        self.assertIn('关注文件', manager_file_limit_list)
        self.assertIn('添加标签', manager_file_limit_list)
        self.assertIn('创建副本', manager_file_limit_list)
        self.assertIn('移动到', manager_file_limit_list)
        self.assertIn('重命名', manager_file_limit_list)
        self.assertIn('下载', manager_file_limit_list)
        self.assertIn('增设权限', manager_file_limit_list)
        self.assertIn('锁定文件', manager_file_limit_list)
        self.assertIn('查看详情', manager_file_limit_list)
        self.assertIn('放入回收站', manager_file_limit_list)
        self.assertEqual(13, len(manager_file_limit_list))
