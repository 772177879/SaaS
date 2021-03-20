from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Copy(Action, Loc):

    def copy_file(self, filename, to_area, to_folder=None):
        log.info('复制文件:%s,%s,%s' % (filename, to_area, to_folder))
        # 复制文件
        self.right_click_filename(filename)     # 右击文件
        try:
            self.element_click(self.copy_loc)       # 点击复制
        except:
            self.element_click(self.person_copy_loc)    # 点击个人版复制
        self.element_click("//section[@class='window-body']//span[text()='%s']" % to_area)      # 选择区域
        if to_folder is None:
            pass
        else:
            self.element_click("//section[@class='window-body']//span[text()='%s']" % to_folder)    # 选择文件夹
        self.element_click(self.next_sure_loc)   # 点击确认
        time.sleep(3)
