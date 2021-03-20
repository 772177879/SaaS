from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class GroupNotice(Action, Loc):
    def publish_group_notice(self, notice_title, notice_introduce):
        log.info('发布群组公告:%s,%s' % (notice_title, notice_introduce))
        # 发布群组公告
        self.element_click(self.group_addNotice_loc)  # 点击发布公告
        time.sleep(3)
        self.element_input(self.group_noticeTitle_input_loc, notice_title)  # 填写群组公告标题
        time.sleep(3)
        self.element_input(self.group_noticeIntroduce_input_loc, notice_introduce)  # 填写群组公告内容
        time.sleep(3)
        self.element_click(self.group_input_submit_loc)  # 点击确定
        time.sleep(3)

    def check_notice_content(self):
        log.info('查看群组公告')
        # 查看群组公告
        title = self.find_element(self.group_notice_title_loc).text
        content = self.find_element(self.group_notice_content_loc).text
        time.sleep(3)
        return title, content
