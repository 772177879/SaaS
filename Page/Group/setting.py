from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class SettingGroup(Action, Loc):
    def group_setting(self, name_edit, introduce_edit):
        log.info('修改群组名称和介绍：%s,%s' % (name_edit, introduce_edit))
        # 群组设置
        self.element_click(self.group_setting_loc)  # 点击群组设置
        time.sleep(3)
        self.element_click(self.groupName_input_setting_loc)  # 修改群组名
        time.sleep(3)
        self.element_input(self.groupName_input_setting_loc, name_edit, clear=1)
        time.sleep(3)
        self.element_click(self.introduce_input_setting_loc)  # 修改群组描述
        time.sleep(3)
        self.element_input(self.introduce_input_setting_loc, introduce_edit, clear=1)
        time.sleep(3)
        self.element_click(self.group_icon_loc)  # 点击其他区域保存
        time.sleep(5)