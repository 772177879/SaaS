from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Object.myunit import MyTest
from Page.login import Login
from Page.File.upload_file import Upload
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.search import Search
from Object.static import get_config
import time
account = get_config('client1')  # 读取账号


class TestUpload(MyTest, Login, Upload, New, Delete, Search):
    def test_Person_TestUpload_00(self):
        """进行操作之前，先保证我的文件是空的"""
        self.login(account['username'], account['password'], login_type=1)  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()       # 清空文件

    def test_Person_TestUpload_01(self):
        """上传wp文件，验证文件内容是有的"""
        self.login(account['username'], account['password'], login_type=1)    # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)    # 点击我的文件
        time.sleep(5)
        self.upload_file('全文检索文档.doc')
        self.verify_file_exist('全文检索文档')     # 验证文件存在
        # time.sleep(5)
        # self.driver.refresh()       # 刷新
        # time.sleep(10)
        # self.driver.refresh()  # 刷新
        # file_names = self.search_file_content('全文检索文档')     # 搜索内容后获取显示的文件列表
        # print(file_names)
        # self.assertIn('全文检索文档.doc', file_names)

    def test_Person_TestUpload_02(self):
        """上传ss文件，验证文件内容是有的"""
        self.login(account['username'], account['password'], login_type=1)    # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)    # 点击我的文件
        time.sleep(5)
        self.upload_file('全文检索表格.xls')
        self.verify_file_exist('全文检索表格')     # 验证文件存在
        # time.sleep(5)
        # self.driver.refresh()       # 刷新
        # time.sleep(10)
        # self.driver.refresh()  # 刷新
        # file_names = self.search_file_content('全文检索表格')     # 搜索内容后获取显示的文件列表
        # print(file_names)
        # self.assertIn('全文检索表格.xls', file_names)

    def test_Person_TestUpload_03(self):
        """上传pg文件，验证文件内容是有的"""
        self.login(account['username'], account['password'], login_type=1)    # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)    # 点击我的文件
        time.sleep(5)
        self.upload_file('全文检索简报.ppt')
        self.verify_file_exist('全文检索简报')     # 验证文件存在
        # time.sleep(5)
        # self.driver.refresh()       # 刷新
        # time.sleep(10)
        # self.driver.refresh()  # 刷新
        # file_names = self.search_file_content('全文检索简报')     # 搜索内容后获取显示的文件列表
        # print(file_names)
        # self.assertIn('全文检索简报.ppt', file_names)

    # def test_TestUpload_04(self):
    #     """上传文件夹，验证文件夹的内容是有的"""
    #     self.login(account['username'], account['password'])  # 登录
    #     self.wait_element(self.my_file_loc)
    #     self.element_click(self.my_file_loc)  # 点击我的文件
    #     time.sleep(5)
    #     self.upload_folder('上传文件夹')
    #     # WebDriverWait(self.driver, 20).until(EC.alert_is_present())
    #     # self.driver.switch_to.default_content()
    #     # alert = self.driver.switch_to.alert
    #     # print(alert.text)
    #     # alert.accept()
    #     time.sleep(5)
    #     ActionChains(self.driver).send_keys(Keys.LEFT).perform()
    #     time.sleep(5)
    #     ActionChains(self.driver).send_keys(Keys.ENTER).perform()
    #     time.sleep(5)
    #     ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
    #
    #
    #     self.verify_file_exist('上传文件夹')  # 验证文件存在




