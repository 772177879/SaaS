from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Share(Action, Loc):
    def open_share(self, filename, limit, forbid_download=0):
        log.info('开启共享:%s,%s' % (filename, limit))
        # 开启共享，选择权限
        self.right_click_filename(filename)     # 右击文件
        self.element_click(self.share_loc)      # 点击共享
        self.element_click(self.share_switch_loc)   # 开启共享开关
        time.sleep(2)
        self.element_click(self.limit_select_loc)       # 点击选择权限
        time.sleep(2)
        if limit == '仅上传':
            self.element_click(self.upload_only_limit_loc)      # 仅上传
        elif limit == '查看':
            self.element_click(self.read_only_limit_loc)        # 查看权限
        elif limit == '编辑':
            self.element_click(self.edit_limit_loc)     # 编辑权限
        if forbid_download == 0:
            pass
        elif forbid_download == 1:
            self.element_click(self.download_save_print_switch_loc)     # 禁止下载等操作

    def get_share_url(self):
        log.info('获取共享链接')
        # 获取共享的链接
        link = self.find_element(self.share_link_loc).get_attribute('value')
        return link

    def get_password(self):
        log.info('获取共享的密码')
        # 获取共享的密码
        password = self.find_element(self.share_password_loc).get_attribute('value')
        return password

    def get_share_file_list(self):
        log.info('获取链接共享界面的文件列表')
        # 获取链接共享界面的文件列表
        file_list = []  # 权限列表
        try:
            all_xpath = self.driver.find_elements_by_xpath("//div[@class='inner']/h2")
            for xpath in all_xpath:
                file_list.append(xpath.text)
        except:
            pass
        return file_list



