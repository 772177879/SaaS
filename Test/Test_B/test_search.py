from Object.myunit import MyTest
from Page.login import Login
from Page.File.new_file import New
from Page.File.delete_file import Delete
from Page.search import Search
from Object.static import get_config
import time
account = get_config('zsy')  # 读取账号


class TestSearch(MyTest, Login, New, Delete, Search):

    def test_TestSearch_01(self):
        """通过文件名搜索"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', '搜索专用wp', 'wp的文本内容')
        time.sleep(1)
        self.new_file('ss', '搜索专用ss', 'ss的文本内容')
        time.sleep(1)
        self.new_file('pg', '搜索专用pg', 'pg的文本内容')
        time.sleep(1)
        self.new_folder('搜索专用的文件夹')
        time.sleep(5)
        self.driver.refresh()
        time.sleep(10)
        self.driver.refresh()
        file_names = self.search_filename('搜索专用')    # 通过文件名搜索
        time.sleep(2)
        self.assertIn('搜索专用wp.docx', file_names)     # 搜索结果有wp
        time.sleep(1)
        self.assertIn('搜索专用ss.xlsx', file_names)     # 搜索结果有ss
        time.sleep(1)
        self.assertIn('搜索专用pg.pptx', file_names)     # 搜索结果有pg
        time.sleep(1)
        self.assertIn('搜索专用的文件夹', file_names)    # 搜索结果有文件夹

    def test_TestSearch_02(self):
        """通过文件内容搜索"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', '搜索专用wp', 'wp的搜索专用文本内容')
        time.sleep(1)
        self.new_file('ss', '搜索专用ss', 'ss的搜索专用文本内容')
        time.sleep(1)
        self.new_file('pg', '搜索专用pg', 'pg的搜索专用文本内容')
        time.sleep(1)
        self.new_folder('搜索专用的文件夹')
        time.sleep(5)
        self.driver.refresh()
        time.sleep(10)
        self.driver.refresh()
        file_names = self.search_file_content('搜索专用文本内容')  # 通过文件内容搜索
        self.assertIn('搜索专用wp.docx', file_names)  # 搜索结果有wp
        self.assertIn('搜索专用ss.xlsx', file_names)  # 搜索结果有ss
        self.assertIn('搜索专用pg.pptx', file_names)  # 搜索结果有pg
        self.assertNotIn('搜索专用的文件夹', file_names)  # 搜索结果没有文件夹

    def test_TestSearch_03(self):
        """搜索结果进行筛选"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', '搜索专用wp', 'wp的搜索专用文本内容')
        time.sleep(1)
        self.new_file('ss', '搜索专用ss', 'ss的搜索专用文本内容')
        time.sleep(1)
        self.new_file('pg', '搜索专用pg', 'pg的搜索专用文本内容')
        time.sleep(1)
        self.new_folder('搜索专用的文件夹')
        time.sleep(5)
        self.driver.refresh()
        time.sleep(10)
        self.driver.refresh()
        file_names = self.search_filter_type('搜索专用', 1)  # 通过文件名的搜索后，wp筛选
        self.assertIn('搜索专用wp.docx', file_names)     # 验证wp出现
        self.assertEqual(1, len(file_names))        # 且只有wp出现
        self.element_click(self.close_loc)   # 关闭搜索界面
        time.sleep(2)
        file_names = self.search_filter_type('搜索专用', 3)  # 通过文件名的搜索后，ss筛选
        self.assertIn('搜索专用ss.xlsx', file_names)  # 验证ss出现
        self.assertEqual(1, len(file_names))  # 且只有ss出现
        self.element_click(self.close_loc)  # 关闭搜索界面
        time.sleep(2)
        file_names = self.search_filter_type('搜索专用', 2)  # 通过文件名的搜索后，pg筛选
        self.assertIn('搜索专用pg.pptx', file_names)  # 验证pg出现
        self.assertEqual(1, len(file_names))  # 且只有pg出现
        self.element_click(self.close_loc)  # 关闭搜索界面
        time.sleep(2)
        file_names = self.search_filter_type('搜索专用', 4)  # 通过文件名的搜索后，其他筛选
        self.assertIn('搜索专用的文件夹', file_names)  # 验证文件夹出现
        self.assertEqual(1, len(file_names))  # 且只有文件夹出现
        self.element_click(self.close_loc)  # 关闭搜索界面









