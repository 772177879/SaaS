from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class GroupDelete(Action, Loc):
    def delete_group(self):
        log.info('删除群组')
        # 删除群组
        self.element_click(self.group_delete_loc)  # 点击删除群组
        time.sleep(2)
        self.element_click(self.sure_loc)  # 点击确定
        time.sleep(2)

    def delete_all_group(self, member_name):
        log.info('清空创建的群组:%s' % member_name)
        # 清空创建的群组
        group_type_list = self.get_group_list()
        for group_type in group_type_list:
            if group_type[1] == '我创建的':
                self.click_file(group_type[0])   # 点击群组
                self.element_click(self.group_setting_loc)  # 点击设置
                self.delete_group()     # 删除
                time.sleep(1)
            elif group_type[1] == '我加入的':
                self.click_file(group_type[0])    # 点击群组
                self.element_click(self.group_user_loc)  # 点击成员管理
                self.member_quit(member_name)
                time.sleep(1)

    def member_quit(self, member_name):
        log.info('删除群组:%s' % member_name)
        # 成员退出群组
        self.element_click("//div[@class='info']/span[@title='%s']/../..//div[@class='m-hd br-2']" % member_name)
        time.sleep(1)
        self.element_click(self.member_quit_loc)  # 成员退出
        self.element_click(self.sure_loc)   # 点击确认
