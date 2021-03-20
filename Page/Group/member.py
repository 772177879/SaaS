from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Member(Action, Loc):

    def add_group_member(self, add_name):
        # 添加成员
        log.info('添加成员:%s' % add_name)
        self.element_click(self.group_addUser_loc)  # 点击添加成员
        time.sleep(1)
        self.element_input(self.group_userInput_loc, add_name)  # 添加成员
        time.sleep(2)
        self.element_click("//div[@class='search-view']//div[@class='name']/span[text()='%s']/../.."
                           "//div[@class='add-view']" % add_name)  # 点击添加
        time.sleep(2)
        self.element_click(self.group_userInput_submit_loc)  # 点击确定
        time.sleep(1)

    def def_member_options(self, member_name, limit_select):
        log.info('对成员设置权限:%s,%s' % (member_name, limit_select))
        # 对成员以及成员的操作
        self.element_click("//div[@class='info']/span[text()='%s']/../..//div[@class='m-hd br-2']" % member_name)
        time.sleep(1)
        # 点击权限选择
        if limit_select == '查看':
            self.element_click(self.member_read_loc)    # 分配查看权限
        elif limit_select == '编辑':
            self.element_click(self.member_edit_loc)    # 分配编辑权限
        elif limit_select == '移除':
            self.element_click(self.member_remove_loc)  # 移除成员


