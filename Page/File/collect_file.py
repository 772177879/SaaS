from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Collect(Action, Loc):

    def collect_file(self, filename):
        log.info('以下为收藏文件:%s' % filename)
        # 收藏文件
        self.right_click_filename(filename)     # 右击文件
        self.element_click(self.collect_loc)    # 点击收藏
        time.sleep(2)

    def collect_cancel_file(self, filename):
        log.info('以下为取消收藏文件:%s' % filename)
        # 取消收藏
        self.right_click_filename(filename)     # 右击文件
        self.element_click(self.collect_cancel_loc)     # 取消收藏
        time.sleep(2)
