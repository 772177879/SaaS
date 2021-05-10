from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.File.download_file import Download
from Object.static import get_config
import time
from Object.static import del_download_file, download_file_success, un_zip
account = get_config('zsy')  # 读取账号


class TestDownload(MyTest, Login, New, Delete, Download):

    def test_TestDownload_01(self):
        """下载文件"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        del_download_file()  # 删除下载目录
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('ss', 'ss下载的文件', '下载')  # 新建文件
        self.download_file('ss下载的文件')   # 下载
        time.sleep(10)
        self.assertTrue(download_file_success('ss下载的文件.xlsx'))      # 验证下载成功了

    def test_TestDownload_02(self):
        """下载文件夹"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        del_download_file()  # 删除下载目录
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_folder('被下载的文件夹')
        self.click_file('被下载的文件夹')      # 进入文件夹中
        self.new_file('ss', 'ss下载的文件', '下载')  # 新建文件
        self.new_file('wp', 'wp下载的文件', '下载')  # 新建文件
        self.new_file('pg', 'pg下载的文件', '下载')  # 新建文件
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.download_file('被下载的文件夹')  # 下载
        time.sleep(10)
        self.assertTrue(download_file_success('被下载的文件夹等1个文件.zip'))  # 验证下载成功了
        self.assertIn('被下载的文件夹/ss下载的文件.xlsx', un_zip('被下载的文件夹.zip'))    # 验证文件在
        self.assertIn('被下载的文件夹/wp下载的文件.docx', un_zip('被下载的文件夹.zip'))  # 验证文件在
        self.assertIn('被下载的文件夹/pg下载的文件.pptx', un_zip('被下载的文件夹.zip'))  # 验证文件在
        self.assertIn('被下载的文件夹/', un_zip('被下载的文件夹.zip'))  # 验证文件在

    def test_TestDownload_03(self):
        """下载组合"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        del_download_file()  # 删除下载目录
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_folder('被下载的文件夹')
        self.new_file('ss', 'ss下载的文件', '下载')  # 新建文件
        self.new_file('wp', 'wp下载的文件', '下载')  # 新建文件
        self.new_file('pg', 'pg下载的文件', '下载')  # 新建文件
        self.click_file('被下载的文件夹')      # 进入文件夹
        self.new_file('ss', 'ss文件夹内部的文件', '下载')  # 新建文件
        self.element_click(self.my_file_loc)  # 点击我的文件
        time.sleep(2)
        self.element_click(self.select_all_loc)     # 全选
        self.element_click(self.all_download_loc)     # 下载
        time.sleep(10)
        self.assertTrue(download_file_success('被下载的文件夹等4个文件.zip'))  # 验证下载成功了
        self.assertIn('ss下载的文件.xlsx', un_zip('被下载的文件夹等4个文件.zip'))  # 验证文件在
        self.assertIn('wp下载的文件.docx', un_zip('被下载的文件夹等4个文件.zip'))  # 验证文件在
        self.assertIn('pg下载的文件.pptx', un_zip('被下载的文件夹等4个文件.zip'))  # 验证文件在
        self.assertIn('被下载的文件夹/', un_zip('被下载的文件夹等4个文件.zip'))  # 验证文件在
        self.assertIn('被下载的文件夹/ss文件夹内部的文件.xlsx', un_zip('被下载的文件夹等4个文件.zip'))  # 验证文件在
