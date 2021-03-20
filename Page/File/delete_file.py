from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Delete(Action, Loc):

    def delete_all(self, delete_type=0):
        log.info('删除所有文件')
        # 删除全部文件
        time.sleep(2)
        self.element_click(self.select_all_loc)     # 全选
        time.sleep(1)
        if delete_type == 1:
            self.element_click(self.select_first_loc)   # 去掉第一个
        self.element_click(self.all_delete_loc)     # 点击全选后的删除
        self.element_click(self.sure_loc)       # 点击后的确认删除
        time.sleep(5)

    def delete_file(self, filename):
        log.info('删除文件:%s' % filename)
        # 删除单个文件
        self.right_click_filename(filename)     # 右击文件
        self.element_click(self.delete_loc)     # 点击删除
        self.element_click(self.sure_loc)  # 点击后的确认删除
        time.sleep(2)

    def clean_recycle(self):
        log.info('清空回收站')
        # 清空回收站
        self.element_click(self.clean_recycle_loc)      # 点击清空回收站
        self.element_click(self.sure_loc)  # 点击后的确认删除
        time.sleep(5)










