from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Rename(Action, Loc):
    # 重命名
    def rename(self, file_type, old_name, new_name):
        log.info('重命名文件:%s,%s,%s' % (file_type, old_name, new_name))
        self.right_click_filename(old_name)    # 右击文件
        self.element_click(self.rename_loc)     # 点击重命名
        if file_type == 'folder':
            self.element_input(self.rename_input_loc, new_name, clear=1)     # 输入文件名的新名称
        else:
            self.element_input(self.rename_input_loc, new_name, clear=1)       # 输入文件夹新名称
        self.element_click(self.next_sure_loc)      # 点击确认

