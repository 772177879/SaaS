# -*- coding:utf-8 -*-
from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
import time


class GroupNoticeConsole(Action, Loc):
    def get_notice_status(self, notice):
        log.info("验证会出现该公告，且群组和发布人正确:%s" % notice)
        team = self.find_element("//span[text()='%s']/../../..//td[4]" % notice).text
        creator = self.find_element("//span[text()='%s']/../../..//td[5]" % notice).text
        return team, creator

    def get_notice_content(self, notice):
        log.info("获取公告的内容:%s" % notice)
        self.element_click("//span[text()='%s']" % notice)  # 点击公告
        time.sleep(2)
        content = self.find_element("//span[text()='公告内容：']/../span[2]").text    # 获取公告内容
        return content
