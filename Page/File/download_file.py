from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Download(Action, Loc):
    def download_file(self, filename):
        log.info('下载文件%s' % filename)
        # 下载单个文件
        self.right_click_filename(filename)     # 右击文件
        self.element_click(self.download_loc)   # 点击下载
        

