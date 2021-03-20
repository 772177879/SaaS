from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Cooperate(Action, Loc):
    def open_cooperate(self, filename, cooperate_name, limit, forbid_download=0, forbid_modify=0):
        log.info('开启协作，并且选择权限:%s,%s, %s' % (filename, cooperate_name, limit))
        # 开启协作，选择权限
        self.right_click_filename(filename)  # 右击文件
        self.element_click(self.cooperate_loc)      # 点击协作
        self.element_input(self.cooperate_search_loc, cooperate_name)   # 搜索
        time.sleep(2)
        # self.element_click("//div[@class='input-view']//div[@class='name']/span[text()='%s']/../.."
        #                    "/div[@class='add-view']" % cooperate_name)      # 选择后选中人
        # self.element_click("//div[@class='input-view']//div[@class='name']/../../div[@class='add-view']")   # 选择后选中人
        self.element_click("//div[@class='add-view']")      # 搜索后选中人
        time.sleep(2)
        self.element_click(self.limit_choose_loc)       # 点击权限选择
        time.sleep(2)
        if limit == '查看':
            self.element_click(self.read_only_limit_loc)  # 查看权限
        elif limit == '编辑':
            self.element_click(self.edit_limit_loc)  # 编辑权限
        if forbid_download == 0:
            pass
        elif forbid_download == 1:
            self.element_click(self.download_save_print_switch_loc)     # 禁止查看权限下载
        if forbid_modify == 0:
            pass
        elif forbid_modify == 1:
            self.element_click(self.forbid_add_new_person_loc)      # 允许添加协作人按钮


