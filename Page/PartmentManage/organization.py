# -*- coding:utf-8 -*-
from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Organization(Action, Loc):

    def add_member(self, account, password, name, sex, telephone, email, position, comment):
        log.info('添加成员')
        self.element_input(self.add_account_loc, account)
        self.element_input(self.add_password_loc, password)
        self.element_input(self.add_name_loc, name)
        if sex == '男':
            self.element_click(self.add_sex_man_loc)
        elif sex == '女':
            self.element_click(self.add_sex_women_loc)
        self.element_input(self.add_tel_loc, telephone)
        self.element_input(self.add_email_loc, email)
        self.element_input(self.add_position_loc, position)
        # self.element_input(self.add_jobNo_loc, jobNo)
        self.element_input(self.add_comment_loc, comment)
        self.element_click(self.add_submit_loc)
        sleep(5)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()  # 去掉弹出的输入框

    def edit(self, member_name):     # 编辑成员按钮
        log.info('编辑成员:%s' % member_name)
        self.element_click("//td[text()='%s']/..//button/span[text()='编辑']" % member_name)

    def forbid(self, member_name):       # 禁用成员按钮
        log.info('禁用成员:%s' % member_name)
        # self.element_click("//td[text()='%s']/..//button/span[text()='禁用']" % member_name)
        self.element_click("//span[text()='%s']/../..//input[@type='checkbox']" % member_name)  # 先勾选
        self.element_click(self.forbid_member_loc)  # 点击禁用
        sleep(2)
        self.element_click(self.forbid_sure_loc)  # 点击确认

    def remove(self, member_name):       # 移除成员按钮
        log.info('移除成员:%s' % member_name)
        self.element_click("//td[text()='%s']/..//button/span[text()='移除']" % member_name)

    def delete(self, member_name):       # 删除成员按钮
        log.info('删除成员:%s' % member_name)
        self.element_click("//span[text()='%s']/../..//input[@type='checkbox']" % member_name)  # 先勾选
        # self.element_click("//td[text()='%s']/..//button/span[text()='删除']" % member_name)
        self.element_click(self.delete_member_loc)      # 点击删除
        sleep(2)
        self.element_click(self.delete_sure_loc)  # 点击确认

    def delete_part(self, part_name):  # 删除部门按钮
        log.info('删除部门:%s' % part_name)
        self.element_click("//td[text()='%s']/..//input[@type='checkbox']" % part_name)  # 先勾选
        self.element_click(self.delete_part_loc)  # 点击删除
        sleep(2)
        self.element_click(self.part_sure_loc)  # 点击确认

    def set_member_pwd(self):  # 设置随机密码
        log.info('设置随机密码')
        self.element_click(self.btn_member_pwd_loc)

    def get_member_pwd(self):  # 获取随机密码
        log.info('获取随机密码')
        casual = self.find_element(self.member_pwd_loc).get_attribute('value')
        return casual
