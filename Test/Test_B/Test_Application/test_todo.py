from Object.myunit import MyTest
from Page.login import Login
from Page.File.delete_file import Delete
from Page.File.new_file import New
from Page.Application.todo import Todo
from Object.static import get_config
import time
account = get_config('yy')  # 读取账号
date_name = get_config('todo')['date_name']


class TestCalendar(MyTest, Login, Delete, Todo, New):

    def test_TestTodo_01(self):
        """新建待办并且完成待办"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.todo_loc)        # 进入待办
        self.into_todo()    # 进入待办中
        while True:
            try:
                self.delete_all_date(date_name)
            except:
                pass
                break
        time.sleep(5)
        self.new_todo(date_name)    # 新建一个待办
        self.element_click("//div[text()='%s']" % date_name)  # 点击该待办
        self.submit_date(date_name)     # 删除待办
        time.sleep(2)
        self.verify_todo_none_exist(date_name)      # 验证待办已完成不存在
