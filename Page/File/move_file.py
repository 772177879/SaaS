from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Move(Action, Loc):

    def move_file(self, filename, to_area, to_folder=None):
        log.info('移动文件：%s,%s,%s' % (filename, to_area, to_folder))
        # 移动文件
        self.right_click_filename(filename)     # 右击文件
        self.element_click(self.move_loc)       # 点击移动
        self.element_click("//section[@class='window-body']//span[text()='%s']" % to_area)      # 选择区域
        if to_folder is None:
            pass
        else:
            self.element_click("//section[@class='window-body']//span[text()='%s']" % to_folder)    # 选择文件夹
        self.element_click(self.next_sure_loc)   # 点击确认
