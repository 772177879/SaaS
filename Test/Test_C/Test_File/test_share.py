from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.File.share_file import Share
from Object.static import get_config
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
account = get_config('client1')  # 读取账号
account2 = get_config('client2')  # 读取账号
url = get_config('url')['url']


class TestShare(MyTest, Login, New, Delete, Share):
    def test_Person_TestShare_01(self):
        """分享单个文件，并且验证权限是否正确(未登录状态，查看权限，允许下载)"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('ss', 'ss共享文件', '共享(查看权限)')  # 新建文件
        self.open_share('ss共享文件', '查看')       # 开启共享
        # self.element_click(self.set_password_loc)     # 开启密码
        time.sleep(2)
        link = self.get_share_url()     # 获取共享链接
        # password = self.get_password()      # 获取密码
        self.element_click(self.close_loc)      # 关闭共享弹出框
        time.sleep(2)
        self.logout()   # 退出登录
        # 未登录情况下
        self.open_url(link)     # 打开共享链接
        # self.element_input(self.password_input_loc, password)   # 输入密码
        # self.element_click(self.next_sure_loc)   # 确认
        time.sleep(2)
        # 验证界面情况(获取文件名，验证是否一致)
        # self.assertEqual(account['name'], self.find_element(self.share_name_loc).text)   # 验证共享人名称正确
        # self.assertIn('ss共享文件.xlsx', self.get_share_file_list())    # 验证文件能看见
        filename = self.find_element("//span[@title]").text     # 获取文件名
        self.assertEqual("ss共享文件", filename)   # 验证文件名正确
        # 去登录, 登录第二个账号
        self.element_click(self.share_login_loc)    # 点击去登录
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        time.sleep(3)
        # self.element_input(self.password_input_loc, password)  # 输入密码
        # self.element_click(self.next_sure_loc)  # 确认
        time.sleep(2)
        # 验证界面情况
        # self.assertEqual(account['name'], self.find_element(self.share_name_loc).text)  # 验证共享人名称正确
        # self.assertIn('ss共享文件.xlsx', self.get_share_file_list())  # 验证文件能看见
        filename = self.find_element("//span[@title]").text  # 获取文件名
        self.assertEqual("ss共享文件", filename)  # 验证文件名正确
        self.verify_element_exist(self.share_download_loc)     # 验证下载按钮存在
        # 重新访问防止进入自己的主页
        # self.element_click(self.share_setting_loc)  # 点击左上角进入自己的主页
        self.driver.get(url)
        time.sleep(3)
        self.element_click(self.share_file_loc)     # 点击共享文件
        time.sleep(1)
        self.element_click(self.share_me_loc)   # 点击共享给我的
        self.verify_file_exist('ss共享文件.xlsx')       # 验证文件存在
        # 验证右击菜单情况
        limit_list = self.get_file_limit('ss共享文件')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        # self.assertIn('添加标签', limit_list)
        # self.assertIn('复制到', limit_list)
        self.assertIn('创建副本', limit_list)
        self.assertIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        # self.assertIn('移除', limit_list)
        self.assertIn('退出共享', limit_list)
        self.assertNotIn('重命名', limit_list)

    def test_Person_TestShare_02(self):
        """分享单个文件，并且验证权限是否正确(未登录状态，编辑权限，允许下载)"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('ss', 'ss共享文件', '共享(编辑权限)')  # 新建文件
        self.open_share('ss共享文件', '编辑')       # 开启共享
        time.sleep(2)
        link = self.get_share_url()     # 获取共享链接
        self.element_click(self.close_loc)      # 关闭共享弹出框
        time.sleep(2)
        self.logout()   # 退出登录
        # 未登录情况下
        self.open_url(link)     # 打开共享链接
        # self.wait_element(self.share_page_load_loc)     # 等待页面加载完毕
        # 验证界面情况
        # self.assertEqual(account['name'], self.find_element(self.share_name_loc).text)   # 验证共享人名称正确
        # self.assertIn('ss共享文件.xlsx', self.get_share_file_list())    # 验证文件能看见
        # filename = self.find_element("//span[@title]").text  # 获取文件名
        # self.assertEqual("ss共享文件", filename)  # 验证文件名正确
        # self.verify_element_exist(self.share_download_loc)  # 验证下载按钮存在
        # 去登录, 登录第二个账号
        # self.element_click(self.share_login_loc)    # 点击去登录
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        time.sleep(3)
        # 编辑界面，可以点击插入
        # self.assertEqual(account['name'], self.find_element(self.share_name_loc).text)  # 验证共享人名称正确
        # self.assertIn('ss共享文件.xlsx', self.get_share_file_list())  # 验证文件能看见
        # filename = self.find_element("//span[@title]").text  # 获取文件名
        # self.assertEqual("ss共享文件", filename)  # 验证文件名正确
        # self.verify_element_exist(self.share_download_loc)  # 验证下载按钮存在
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.edit_frame_loc)))
        self.element_click(self.view_loc)  # 点击插入
        # 重新访问链接进入主页
        # self.element_click(self.share_setting_loc)  # 点击左上角进入自己的主页
        self.driver.get(url)
        time.sleep(3)
        self.element_click(self.share_file_loc)     # 点击共享文件
        time.sleep(1)
        self.element_click(self.share_me_loc)   # 点击共享给我的
        self.verify_file_exist('ss共享文件.xlsx')       # 验证文件存在
        # 验证右击菜单情况
        limit_list = self.get_file_limit('ss共享文件')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        # self.assertIn('添加标签', limit_list)
        # self.assertIn('复制到', limit_list)
        self.assertIn('创建副本', limit_list)
        self.assertIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        # self.assertIn('移除', limit_list)
        self.assertIn('退出共享', limit_list)
        self.assertIn('重命名', limit_list)
        self.assertNotIn('删除', limit_list)

    # def test_Person_TestShare_03(self):
    #     """分享文件夹，并且验证权限是否正确（登录状态，仅上传权限，不设置密码）"""
    #     self.login(account['username'], account['password'], login_type=1)  # 登录
    #     self.wait_element(self.my_file_loc)
    #     self.element_click(self.my_file_loc)  # 点击我的文件
    #     self.new_folder('清空专用')
    #     self.new_folder('清空专用')
    #     self.delete_all()  # 清空文件
    #     self.new_folder('仅上传权限文件夹')     # 新建文件夹
    #     self.click_file('仅上传权限文件夹')     # 进入文件夹
    #     self.new_file('wp', 'wp共享文件', '共享(仅上传)')  # 新建文件
    #     self.element_click(self.my_file_loc)  # 点击我的文件
    #     self.open_share('仅上传权限文件夹', '仅上传')  # 开启共享
    #     time.sleep(2)
    #     link = self.get_share_url()  # 获取共享链接
    #     self.element_click(self.close_loc)  # 关闭共享弹出框
    #     time.sleep(2)
    #     self.logout()  # 退出登录
    #     # 去登录, 登录第二个账号
    #     self.login(account2['username'], account2['password'], login_type=1)  # 登录
    #     self.wait_element(self.my_file_loc)
    #     # 登录情况下
    #     self.open_url(link)  # 打开共享链接
    #     self.wait_element(self.share_page_load_loc)  # 等待页面加载完毕
    #     # 验证界面情况
    #     self.assertEqual(account['name'], self.find_element(self.share_name_loc).text)  # 验证共享人名称正确
    #     self.assertEqual('仅上传权限文件夹', self.find_element(self.share_folder_name_loc).text)    # 验证文件夹名称正确
    #     self.assertNotIn('wp共享文件.docx', self.get_share_file_list())  # 验证文件不能看见
    #     # 点击左上角进入自己的主页
    #     self.element_click(self.share_setting_loc)  # 点击左上角进入自己的主页
    #     time.sleep(3)
    #     self.element_click(self.share_file_loc)  # 点击共享文件
    #     time.sleep(1)
    #     self.element_click(self.share_me_loc)  # 点击共享给我的
    #     self.verify_file_exist('仅上传权限文件夹')  # 验证文件存在
    #     # 验证右击菜单情况
    #     limit_list = self.get_file_limit('仅上传权限文件夹')  # 获取右击菜单的权限
    #     self.assertIn('共享', limit_list)
    #     self.assertIn('协作', limit_list)
    #     self.assertIn('收藏文件', limit_list)
    #     self.assertNotIn('关注文件', limit_list)
    #     # self.assertIn('添加标签', limit_list)
    #     # self.assertNotIn('复制到', limit_list)
    #     self.assertNotIn('创建副本', limit_list)
    #     self.assertNotIn('下载', limit_list)
    #     self.assertIn('查看详情', limit_list)
    #     # self.assertIn('移除', limit_list)
    #     self.assertIn('退出共享', limit_list)
    #     self.assertNotIn('重命名', limit_list)
    #     self.click_file('仅上传权限文件夹')     # 进入文件夹中
    #     self.verify_file_none_exist('wp共享文件.docx')      # 验证里面的文件看不见

    def test_Person_TestShare_04(self):
        """分享文件夹，并且验证权限是否正确（登录状态，查看权限，不允许下载，不设置密码）"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_folder('查看权限文件夹')  # 新建文件夹
        self.click_file('查看权限文件夹')  # 进入文件夹
        self.new_file('pg', 'pg共享文件', '共享(查看)')  # 新建文件
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.open_share('查看权限文件夹', '查看', forbid_download=1)  # 开启共享,不允许下载
        time.sleep(2)
        link = self.get_share_url()  # 获取共享链接
        self.element_click(self.close_loc)  # 关闭共享弹出框
        time.sleep(2)
        self.logout()  # 退出登录
        # 去登录, 登录第二个账号
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # 登录情况下
        self.open_url(link)  # 打开共享链接
        self.wait_element(self.share_page_load_loc)  # 等待页面加载完毕
        # 验证界面情况
        self.assertEqual(account['name'], self.find_element(self.share_name_loc).text)  # 验证共享人名称正确
        self.assertEqual('查看权限文件夹', self.find_element(self.share_folder_name_loc).text)  # 验证文件夹名称正确
        self.assertIn('pg共享文件.pptx', self.get_share_file_list())  # 验证文件能看见
        # 点击左上角进入自己的主页
        self.element_click(self.share_setting_loc)  # 点击左上角进入自己的主页
        time.sleep(3)
        self.element_click(self.share_file_loc)  # 点击共享文件
        time.sleep(1)
        self.element_click(self.share_me_loc)  # 点击共享给我的
        self.verify_file_exist('查看权限文件夹')  # 验证文件存在
        # 验证右击菜单情况
        limit_list = self.get_file_limit('查看权限文件夹')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertNotIn('关注文件', limit_list)
        # self.assertIn('添加标签', limit_list)
        # self.assertNotIn('复制到', limit_list)
        self.assertNotIn('创建副本', limit_list)
        self.assertNotIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        # self.assertIn('移除', limit_list)
        self.assertIn('退出共享', limit_list)
        self.assertNotIn('重命名', limit_list)
        self.click_file('查看权限文件夹')  # 进入文件夹中
        limit_list = self.get_file_limit('pg共享文件.pptx')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        # self.assertIn('添加标签', limit_list)
        # self.assertNotIn('复制到', limit_list)
        self.assertNotIn('创建副本', limit_list)
        self.assertNotIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        # self.assertNotIn('移除', limit_list)
        self.assertNotIn('退出共享', limit_list)
        self.assertNotIn('重命名', limit_list)

    def test_Person_TestShare_05(self):
        """分享文件夹，并且验证权限是否正确（登录状态，编辑权限，不允许下载，不设置密码）"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_folder('编辑权限文件夹')  # 新建文件夹
        self.click_file('编辑权限文件夹')  # 进入文件夹
        self.new_file('pg', 'pg共享文件', '共享(编辑)')  # 新建文件
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.open_share('编辑权限文件夹', '编辑', forbid_download=1)  # 开启共享,不允许下载
        time.sleep(2)
        link = self.get_share_url()  # 获取共享链接
        self.element_click(self.close_loc)  # 关闭共享弹出框
        time.sleep(2)
        self.logout()  # 退出登录
        # 去登录, 登录第二个账号
        self.login(account2['username'], account2['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        # 登录情况下
        self.open_url(link)  # 打开共享链接
        self.wait_element(self.share_page_load_loc)  # 等待页面加载完毕
        # 验证界面情况
        self.assertEqual(account['name'], self.find_element(self.share_name_loc).text)  # 验证共享人名称正确
        self.assertEqual('编辑权限文件夹', self.find_element(self.share_folder_name_loc).text)  # 验证文件夹名称正确
        self.assertIn('pg共享文件.pptx', self.get_share_file_list())  # 验证文件能看见
        # 点击左上角进入自己的主页
        self.element_click(self.share_setting_loc)  # 点击左上角进入自己的主页
        time.sleep(3)
        self.element_click(self.share_file_loc)  # 点击共享文件
        time.sleep(1)
        self.element_click(self.share_me_loc)  # 点击共享给我的
        self.verify_file_exist('编辑权限文件夹')  # 验证文件存在
        # 验证右击菜单情况
        limit_list = self.get_file_limit('编辑权限文件夹')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertNotIn('关注文件', limit_list)
        # self.assertIn('添加标签', limit_list)
        # self.assertIn('复制到', limit_list)
        self.assertIn('创建副本', limit_list)
        self.assertIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        # self.assertIn('移除', limit_list)
        self.assertIn('退出共享', limit_list)
        self.assertIn('重命名', limit_list)
        self.click_file('编辑权限文件夹')  # 进入文件夹中
        limit_list = self.get_file_limit('pg共享文件.pptx')  # 获取右击菜单的权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('收藏文件', limit_list)
        self.assertIn('关注文件', limit_list)
        # self.assertIn('添加标签', limit_list)
        # self.assertIn('复制到', limit_list)
        self.assertIn('创建副本', limit_list)
        self.assertIn('移动到', limit_list)
        self.assertIn('下载', limit_list)
        self.assertIn('查看详情', limit_list)
        # self.assertNotIn('移除', limit_list)
        self.assertNotIn('退出共享', limit_list)
        self.assertIn('重命名', limit_list)
        self.assertIn('放入回收站', limit_list)




