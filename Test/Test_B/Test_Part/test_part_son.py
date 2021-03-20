from Object.myunit import MyTest
from Page.login import Login
from Object.static import get_config
account_cdd = get_config('cdd')
account_sld = get_config('sld')
part = get_config('part')['part_name']
part_son = get_config('part_son')['part_son_name']


class TestPartSon(MyTest, Login):
    def test_TestPartSon_01(self):
        """验证部门经理和个人进入部门里，经理可以看到下属部门，成员看不到下属部门"""
        self.login(account_cdd['username'], account_cdd['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)   # 点击部门
        self.click_file(part)   # 进入自动化部门中
        self.verify_file_exist(part_son)    # 验证能看到子部门

    def test_TestPartSon_02(self):
        """验证部门经理和个人进入部门里，经理可以看到下属部门，成员看不到下属部门"""
        self.login(account_sld['username'], account_sld['password'])  # 登录账号
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)  # 点击部门
        self.click_file(part)  # 进入自动化部门中
        self.verify_file_none_exist(part_son)  # 验证能看到子部门


