from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
from Object.static import get_project_path
from time import sleep
import win32gui
import win32con
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Calendar(Action, Loc):

    def into_calendar(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.app_frame_loc)))
        # self.element_click("//h1[text()='%s']" % pdf_type)

    def new_date(self, date_name):  # 新建日程
        log.info('新建日程:%s' % date_name)
        self.element_click(self.new_calendar_loc)   # 点击新建
        self.wait_element(self.new_date_loc)    # 等待
        self.element_click(self.new_date_loc)   # 点击新建日程
        self.wait_element(self.date_title_loc)      # 等待
        self.element_input(self.date_title_loc, date_name)  # 日程输入日程名称
        self.element_click(self.new_date_submit_loc)    # 点击新建日程
        self.wait_element("//span[text()='%s']" % date_name)    # 等待

    def cancel_date(self, date_name):  # 取消日程
        log.info('取消日程:%s' % date_name)
        sleep(2)
        self.element_click(self.date_cancel_loc)  # 点击取消
        sleep(2)
        self.element_click(self.date_delete_sure_loc)  # 点击确认

    def delete_date(self, date_name):      # 删除日程
        log.info('删除日程:%s' % date_name)
        sleep(2)
        self.element_click(self.date_delete_loc)  # 点击删除
        sleep(2)
        self.element_click(self.date_delete_sure_loc)  # 点击确认

    def delete_all_date(self, date_name):   # 清空日程
        log.info('清空日程:%s' % date_name)
        sleep(2)
        self.element_click("//span[text()='%s']" % date_name)  # 点击该日程
        try:
            self.cancel_date(date_name)
        except:
            self.delete_date(date_name)


