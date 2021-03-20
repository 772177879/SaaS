from Object.myunit import MyTest
from Page.login import Login
from Page.File.delete_file import Delete
from Page.File.new_file import New
from Page.Application.form import Form
from Object.static import get_config
import time
account = get_config('yy')  # 读取账号
form_question = get_config('form')['form_question']
form_answer = get_config('form')['form_answer']
url = ''


class TestForm(MyTest, Login, Delete, Form, New):

    def test_TestForm_01(self):
        """先删除所有表单，再去新建表单"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.form_loc)        # 进入表单
        self.into_form()    # 进入表单中
        self.delete_all_forms()     # 删除所有表单
        self.new_form(form_question)     # 创建表单
        self.wait_element(self.url_loc)     # 发布后等待出现url
        global url
        url = self.get_form_url()
        print(url)

    def test_TestForm_02(self):
        """直接打开该URL，填写答案"""
        self.open_url(url)
        self.answer_form(form_answer)

    def test_TestForm_03(self):
        """去查看答案是否显示"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.form_loc)  # 进入表单
        self.into_form()  # 进入表单中
        self.check_answer(form_answer)      # 收集结果出现答案












