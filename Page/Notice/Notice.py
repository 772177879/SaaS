from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Notice(Action, Loc):
    def into_notice(self):  # 进入通知
        log.info('进入通知')
        self.element_click(self.notice_loc)

    def into_person_notice(self):   # 进入消息
        log.info("进入个人版消息")
        self.element_click(self.person_notice_loc)

    def into_person_invite(self):   # 进入个人版邀请消息
        self.into_person_notice()   # 进入消息
        log.info("进入个人版邀请消息")
        self.element_click(self.person_notice_invite_loc)

    def into_notice_notice(self):   # 进入通知通知
        self.into_notice()  # 进入通知
        log.info('进入通知里的通知')
        self.element_click(self.notice_notice_loc)      # 进入通知的通知

    def into_notice_cooperation(self):  # 进入通知协作
        self.into_notice()  # 进入通知
        log.info('进入通知里的协作')
        self.element_click(self.notice_cooperation_loc)     # 进入通知的协作

    def invite_team_notice(self):    # 邀请加入群组的通知
        log.info('获取邀请加入群组的通知')
        text = self.find_element(self.notice_message_loc).get_attribute('innerText')
        return text

    def team_delete_notice(self):       # 群组解散通知
        log.info('获取群组被解散的通知')
        text = self.find_element(self.notice_message_loc).get_attribute('innerText')
        return text

    def close_notice(self):     # esc关闭
        log.info('关闭通知/公告界面')
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def invite_cooperate(self):     # 邀请协作
        log.info('获取邀请协作的通知')
        text1 = self.find_element(self.cooperate_message_name_loc).get_attribute('innerText')
        text2 = self.find_element(self.cooperate_message_txt_loc).get_attribute('innerText')
        text = text1 + text2
        return text

    def person_invite(self):    # 个人版里邀请消息里的内容
        log.info('个人版获取邀请消息里的内容')
        text = self.find_element(self.person_notice_invite_message_loc).get_attribute('innerText')
        return text





