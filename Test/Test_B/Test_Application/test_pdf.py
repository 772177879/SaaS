from Object.myunit import MyTest
from Page.login import Login
from Page.File.delete_file import Delete
from Page.File.new_file import New
from Page.Application.pdf import PDF
from Object.static import get_config
from time import sleep
account = get_config('yy')  # 读取账号
pdf_file = get_config('pdf')['pdf_name']
word_file = get_config('pdf')['pdf_word']
pdf_to_word = get_config('pdf')['PDF转Word']


class TestPDF(MyTest, Login, Delete, PDF, New):

    def test_TestPDF_01(self):
        """上传pdf转为word"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.element_click(self.application_folder_loc)     # 点击应用文件夹
        self.element_click(self.pdf_folder_loc)     # 点击PDF工具集
        try:
            self.delete_file(word_file)
        except:
            pass
        self.element_click(self.pdf_loc)        # pdf工具集按钮
        sleep(5)
        self.into_pdf_type(pdf_to_word)     # 进入pdf转word
        self.pdf_upload_file(pdf_file)      # 上传文件进行pdf转换
        self.driver.switch_to.default_content()     # 切换到默认位置
        self.element_click(self.file_loc)   # 点击文件
        self.element_click(self.my_file_loc)    # 点击我的文件
        self.element_click(self.application_folder_loc)  # 点击应用文件夹
        self.element_click(self.pdf_folder_loc)  # 点击PDF工具集
        self.verify_file_exist(word_file)       # 文件出现









