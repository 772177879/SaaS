from Object.myunit import MyTest
from Page.login import Login
from Page.File.delete_file import Delete
from Page.File.new_file import New
from Page.Application.calendar import Calendar
from Object.static import get_config
import time
account = get_config('yy')  # 读取账号
date_name = get_config('calendar')['date_name']


class TestCalendar(MyTest, Login, Delete, Calendar, New):

    def test_TestCalendar_01(self):
        """新建日程并且删除日程"""
        self.login(account['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.calendar_loc)        # 进入日历
        self.into_calendar()    # 进入日历中
        while True:
            try:
                self.delete_all_date(date_name)
            except:
                pass
                break
        time.sleep(5)
        self.new_date(date_name)    # 新建一个日程
        self.element_click("//span[text()='%s']" % date_name)  # 点击该日程
        self.cancel_date(date_name)  # 取消日程
        time.sleep(2)
        self.element_click("//span[text()='%s']" % date_name)  # 点击该日程
        self.delete_date(date_name)     # 删除日程
        time.sleep(2)
        self.verify_file_none_exist(date_name)      # 验证日程不存在
