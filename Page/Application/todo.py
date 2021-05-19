from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback


class Todo(Action, Loc):

    def into_todo(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.app_frame_loc)))
        # self.element_click("//h1[text()='%s']" % pdf_type)

    def new_todo(self, date_name):  # 新建待办
        log.info('新建待办:%s' % date_name)
        self.element_click(self.new_todo_loc)   # 点击新建
        self.wait_element(self.new_todo_title_loc)      # 等待
        self.element_input(self.new_todo_item_loc, date_name)  # 日程输入日程名称
        self.element_click(self.new_todo_submit_loc)    # 点击完成
        self.wait_element("//div[text()='%s']" % date_name)    # 等待

    def submit_date(self, date_name):      # 删除待办
        log.info('删除待办:%s' % date_name)
        sleep(2)
        self.element_click(self.todo_submit_loc)  # 点击完成待办
        sleep(2)
        self.element_click(self.todo_double_loc)  # 点击确认

    def delete_all_date(self, date_name):   # 清空未完成待办
        log.info('清空日程:%s' % date_name)
        sleep(2)
        self.element_click("//div[text()='%s']" % date_name)  # 点击该待办
        try:
            self.submit_date(date_name)
        except:
            pass

    def verify_todo_none_exist(self, date_name):
        try:
            self.verify_element_none_exist('//div[contains(text(),"%s")]' % date_name)
        except:
            log.exception(traceback.format_exc())
            raise