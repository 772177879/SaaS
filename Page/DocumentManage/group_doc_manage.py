from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
import time


class GroupDocumentManage(Action, Loc):
    def select_group(self, group_name):
        log.info('选择群组:%s' % group_name)
        # self.element_click(self.group_select_loc)       # 点击群组筛选
        # time.sleep(5)
        self.element_input(self.group_select_loc, group_name)   # 直接搜索
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()  # 点击搜索
        # self.element_click("//div[text()='%s']" % group_name)   # 选择群组

