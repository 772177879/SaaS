from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.File.cooperate_file import Cooperate
from Object.static import get_config
from Page.Notice.Notice import Notice
import time
account = get_config('zsy')  # 读取账号
account2 = get_config('sld')  # 读取账号


class TestCooperate(MyTest, Login, New, Delete, Cooperate, Notice):
    def test_TestCooperate_01(self):
        """协作单个文件，并且验证权限是否正确(查看权限，允许下载)"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('pg', 'pg协作文件', '协作(查看权限)')  # 新建文件
        self.open_cooperate('pg协作文件', account2['name'], '查看')  # 开启协作，查看权限
        time.sleep(2)
        self.element_click(self.close_loc)  # 关闭协作弹出框
        time.sleep(2)
        self.logout()  # 退出登录
        # 去登录, 登录第二个账号
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_notice_cooperation()      # 进入通知的协作通知中
        text = self.invite_cooperate()      # 获取被协作的通知
        invite_message = "%s 邀请您加入协作【pg协作文件.pptx】" % account['name']
        self.assertEqual(invite_message, text)
        self.close_notice()  # 关闭界面
        self.element_click(self.share_file_loc)  # 点击共享文件
        time.sleep(1)
        self.element_click(self.share_me_loc)  # 点击共享给我的
        self.verify_file_exist('pg协作文件.pptx')  # 验证文件存在
        # 验证右击菜单情况
        limit_list = self.get_file_limit('pg协作文件')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        self.assertIn('添加标签', limit_list)
        self.assertIn('创建副本', limit_list)
        self.assertIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        self.assertIn('退出共享', limit_list)
        self.assertNotIn('重命名', limit_list)

    def test_TestCooperate_02(self):
        """协作单个文件，并且验证权限是否正确(查看权限，不允许下载)"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('pg', 'pg协作文件', '协作(查看权限)')  # 新建文件
        self.open_cooperate('pg协作文件', account2['name'], '查看', forbid_download=1)  # 开启协作，查看权限，但是不允许下载
        time.sleep(2)
        self.element_click(self.close_loc)  # 关闭协作弹出框
        time.sleep(2)
        self.logout()  # 退出登录
        # 去登录, 登录第二个账号
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_notice_cooperation()      # 进入通知的协作通知中
        text = self.invite_cooperate()      # 获取被协作的通知
        invite_message = "%s 邀请您加入协作【pg协作文件.pptx】" % account['name']
        self.assertEqual(invite_message, text)
        self.close_notice()  # 关闭界面
        self.element_click(self.share_file_loc)  # 点击共享文件
        time.sleep(1)
        self.element_click(self.share_me_loc)  # 点击共享给我的
        self.verify_file_exist('pg协作文件.pptx')  # 验证文件存在
        # 验证右击菜单情况
        limit_list = self.get_file_limit('pg协作文件')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        self.assertIn('添加标签', limit_list)
        self.assertNotIn('创建副本', limit_list)
        self.assertNotIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        self.assertIn('退出共享', limit_list)
        self.assertNotIn('重命名', limit_list)

    def test_TestCooperate_03(self):
        """协作单个文件，并且验证权限是否正确(编辑权限，允许添加协作人)"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', 'wp协作文件', '协作(编辑权限)')  # 新建文件
        self.open_cooperate('wp协作文件', account2['name'], '编辑', forbid_download=1)  # 开启协作，编辑权限，
        # 但是不允许下载，允许添加协作人
        time.sleep(2)
        self.element_click(self.close_loc)  # 关闭协作弹出框
        time.sleep(2)
        self.logout()  # 退出登录
        # 去登录, 登录第二个账号
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_notice_cooperation()      # 进入通知的协作通知中
        text = self.invite_cooperate()      # 获取被协作的通知
        invite_message = "%s 邀请您加入协作【wp协作文件.docx】" % account['name']
        self.assertEqual(invite_message, text)
        self.close_notice()  # 关闭界面
        self.element_click(self.share_file_loc)  # 点击共享文件
        time.sleep(1)
        self.element_click(self.share_me_loc)  # 点击共享给我的
        self.verify_file_exist('wp协作文件.docx')  # 验证文件存在
        # 验证右击菜单情况
        limit_list = self.get_file_limit('wp协作文件')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        self.assertIn('添加标签', limit_list)
        self.assertIn('创建副本', limit_list)
        self.assertIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        self.assertIn('退出共享', limit_list)
        self.assertIn('重命名', limit_list)
        self.element_click(self.cooperate_loc)      # 点击协作
        time.sleep(3)
        self.assertTrue(self.find_element(self.cooperate_search_loc).is_displayed())

    def test_TestCooperate_04(self):
        """协作单个文件，并且验证权限是否正确(编辑权限，禁止添加协作人)"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', 'wp协作文件', '协作(编辑权限)')  # 新建文件
        self.open_cooperate('wp协作文件', account2['name'], '编辑', forbid_download=1, forbid_modify=1)  # 开启协作，
        # 查看权限，但是不允许下载，禁止添加协作人
        time.sleep(2)
        self.element_click(self.close_loc)  # 关闭协作弹出框
        time.sleep(2)
        self.logout()  # 退出登录
        # 去登录, 登录第二个账号
        self.login(account2['username'], account2['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_notice_cooperation()      # 进入通知的协作通知中
        text = self.invite_cooperate()      # 获取被协作的通知
        invite_message = "%s 邀请您加入协作【wp协作文件.docx】" % account['name']
        self.assertEqual(invite_message, text)
        self.close_notice()  # 关闭界面
        self.element_click(self.share_file_loc)  # 点击共享文件
        time.sleep(1)
        self.element_click(self.share_me_loc)  # 点击共享给我的
        self.verify_file_exist('wp协作文件.docx')  # 验证文件存在
        # 验证右击菜单情况
        limit_list = self.get_file_limit('wp协作文件')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        self.assertIn('添加标签', limit_list)
        self.assertIn('创建副本', limit_list)
        self.assertIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        self.assertIn('退出共享', limit_list)
        self.assertIn('重命名', limit_list)
        self.element_click(self.cooperate_loc)  # 点击协作
        time.sleep(3)
        self.assertFalse(self.find_element(self.cooperate_search_loc).is_displayed())
