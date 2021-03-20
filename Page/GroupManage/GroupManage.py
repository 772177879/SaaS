# -*- coding:utf-8 -*-
from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log


class GroupManage(Action, Loc):
    def get_group_status(self, group_name):
        log.info('获取群组的当前状态:%s' % group_name)
        status = self.find_element("//span[text()='%s']/../../..//td[5]/span" % group_name).text
        return status
