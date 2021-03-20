from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Attention(Action, Loc):

    def attention_file(self, filename):
        log.info('以下为关注文件:%s' % filename)
        # 关注文件
        self.right_click_filename(filename)  # 右击文件
        self.element_click(self.attention_loc)      # 关注文件

    def attention_cancel_file(self, filename):
        log.info('以下为取消关注:%s' % filename)
        # 取消关注
        self.right_click_filename(filename)     # 右击文件
        self.element_click(self.attention_cancel_loc)   # 取消关注

    def attention_file_list(self):
        log.info('以下为获取关注文件的列表')
        # 获取关注文件的列表
        file_names = []
        try:  # 尝试获取关注文件列表，为空的话文件列表为空
            all_xpath = self.driver.find_elements_by_xpath("//ul[@class='follow-file-view']//span")
            for xpath in all_xpath:
                file_names.append(xpath.text)
        except:
            pass
        return file_names


