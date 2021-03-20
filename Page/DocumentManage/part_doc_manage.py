from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
from time import sleep
import time


class PartDocumentManage(Action, Loc):
    def delete_all(self):
        log.info('删除后端所有文件')
        self.element_click(self.all_select_checkbox_loc)    # 点击选择框
        sleep(1)
        self.element_click(self.delete_all_button_loc)  # 点击总删除
        sleep(2)
        self.element_click(self.delete_sure_loc)    # 点击删除

    def search_doc(self, search_txt, need_filter=0):   # 搜索出文件
        log.info('搜索：%s' % search_txt)
        date = time.strftime("%Y-%m-%d")
        self.element_input(self.search_doc_loc, search_txt, clear=1)
        if need_filter == 1:    # 如果需要筛选的话，选1
            self.element_click(self.begin_time_loc)  # 点击开始时间
            time.sleep(1)
            self.element_click("//td[@title='%s']/div" % date)  # 选择本天
            time.sleep(1)
            self.element_click("//td[@title='%s']/div" % date)  # 选择本天
            time.sleep(1)
        self.element_click(self.search_doc_button_loc)      # 点击搜索
        sleep(2)






