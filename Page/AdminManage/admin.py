from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
from Object.static import get_config
from time import sleep


class Admin(Action, Loc):

    def new_admin(self, admin_type, name):  # 新建管理员
        log.info("新增管理员:%s,%s" % (admin_type, name))
        self.element_click(self.add_admin_loc)      # 点击添加管理员
        sleep(1)
        self.element_click(self.admin_select_loc)   # 点击管理员类型
        sleep(1)
        self.element_click("//div[@title='%s']" % admin_type)   # 选择某种管理员类型
        sleep(1)
        self.element_input(self.admin_search_loc, admin_type)   # 搜索
        self.element_click("//span[contains(text(),'%s') and contains(@class, 'siteTreeSearchValue')]/../../../..//span[@class='ant-tree-checkbox-inner']" % name)  # 选择
        self.element_click(self.admin_sure_loc)
        sleep(2)

    def manage_check(self, admin_type):   # 权限控制
        self.verify_element_exist(self.console_board_loc)   # 企业概况是存在的
        manage_list = get_config(admin_type)['list']    # 其他的直接循环扫出来
        actual_manage_list = []
        expect_manage_list = list(manage_list.keys())     # 大的列表状态
        elements = self.driver.find_elements_by_xpath("//li[contains(@class,'ant-menu-submenu ant-menu-submenu-inline') and @role='menuitem']")
        for element in elements:
            actual_manage_list.append(element.get_attribute('innerText'))    # 获取到实际情况下的大列表
        print(actual_manage_list)
        print(expect_manage_list)
        assert actual_manage_list == expect_manage_list
        for key, value in manage_list.items():  # 遍历情况表，点击每个表项，获取里面的具体的列表项
            sleep(2)
            self.element_click("//li[contains(@class,'ant-menu-submenu ant-menu-submenu-inline') and @role='menuitem']/div/span/span[text()='%s']" % key)
            sleep(1)
            actual_menu_list = []
            expect_menu_list = value
            elements = self.driver.find_elements_by_xpath("//li[contains(@class,'ant-menu-submenu ant-menu-submenu-inline') and @role='menuitem']/div/span/span[text()='%s']/../../..//li" % key)
            for element in elements:
                actual_menu_list.append(element.get_attribute('innerText'))    # 获取各个位置的菜单列表
            print(actual_menu_list)
            print(expect_menu_list)
            assert actual_menu_list == expect_menu_list

    def delete_admin(self, admin_name):
        self.element_click("//td[text()='%s']/..//span[text()='删除']" % admin_name)  # 删除某个管理员
        sleep(2)
        self.element_click(self.admin_sure_loc)     # 点击确认
        sleep(2)












