from Object.myunit import MyTest
from Page.login import Login
from Object.static import get_config
from Page.Approval.approval import Approval
from Page.File.new_file import New
from Page.File.delete_file import Delete
import time
account = get_config('zsy')  # 读取账号
account2 = get_config('sld')  # 读取账号
account3 = get_config('cdd')  # 读取账号


class TestCopy(MyTest, Login, Approval, New, Delete, ):

    def test_TestApproval_00(self):
        """发起文档审阅前，先清空未审阅记录"""
        self.login(account['username'], account['password'])  # 登录
        self.element_click(self.file_loc)  # 点击文件模块
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        # self.element_click(self.approval_todo_loc)  # 进入待处理
        self.delete_approval('通过', '清空审阅中的待处理')
        time.sleep(2)
        self.back_home()  # 切出frame
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件

    def test_TestApproval_01(self):
        """发起文档审阅，审阅通过"""
        self.login(account2['username'], account['password'])  # 登录发起人
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_file('wp', '审阅通过的文件', '审阅通过')      # 新建文件
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.element_click(self.approval_open_loc)  # 发起审批
        self.create_approval('发起审阅通过的标题', '发起审阅通过的备注')
        self.select_approval_file('审阅通过的文件')
        self.select_option('自定义审阅流程', reviewer=account['name'], cc=account3['name'])
        self.element_click(self.approval_open_button_loc)  # 下一步
        self.into_approval_submit()  # 切换至审批提交的frame
        self.element_click(self.approval_add_submit_loc)  # 提交
        self.wait_element(self.approval_add_success_loc)  # 等待
        self.back_home()  # 切出frame
        self.element_click(self.approval_add_submit_close_loc)  # 关闭弹窗
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account['username'], account['password'])  # 登录审阅人
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_todo_loc)  # 进入待处理
        time.sleep(1)
        self.search_approval_notes('发起审阅通过的标题', need_filter=1)
        self.element_click(self.approval_reviewer_check_loc)  # 查看详情
        time.sleep(2)
        self.wait_element("//span[@title='详情']")  # 等待
        self.check_approval_file('通过', '这是通过的审阅')  # 同意审阅
        time.sleep(2)
        self.element_click(self.approval_done_loc)  # 进入已处理
        time.sleep(2)
        self.search_approval_notes('发起审阅通过的标题', need_filter=1)
        self.verify_approval_file_exist('发起审阅通过的标题')
        self.back_home()  # 切出frame
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account3['username'], account['password'])  # 登录抄送人
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_my_check_loc)  # 进入抄送给我的
        time.sleep(1)
        self.search_approval_notes('发起审阅通过的标题', need_filter=1)
        self.verify_approval_file_exist('发起审阅通过的标题')

    def test_TestApproval_02(self):
        """发起文档审阅前，先清空未审阅记录"""
        self.login(account['username'], account['password'])  # 登录
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_todo_loc)  # 进入待处理
        self.delete_approval('通过', '清空审阅中的待处理')
        time.sleep(2)
        self.back_home()  # 切出frame
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件

    def test_TestApproval_03(self):
        """发起文档审阅，审阅驳回"""
        self.login(account2['username'], account['password'])  # 登录发起人
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_file('wp', '审阅驳回的文件', '审阅驳回')      # 新建文件
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.element_click(self.approval_open_loc)  # 发起审批
        self.create_approval('发起审阅驳回的标题', '发起审阅驳回的备注')
        self.select_approval_file('审阅驳回的文件')
        self.select_option('自定义审阅流程', reviewer=account['name'], cc=account3['name'])
        self.element_click(self.approval_open_button_loc)  # 下一步
        self.into_approval_submit()  # 切换至审批提交的frame
        self.element_click(self.approval_add_submit_loc)  # 提交
        self.wait_element(self.approval_add_success_loc)  # 等待
        self.back_home()  # 切出frame
        self.element_click(self.approval_add_submit_close_loc)  # 关闭弹窗
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account['username'], account['password'])  # 登录
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_todo_loc)  # 进入待处理
        time.sleep(1)
        self.search_approval_notes('发起审阅驳回的标题', need_filter=1)
        self.element_click(self.approval_reviewer_check_loc)  # 查看详情
        time.sleep(2)
        self.wait_element("//span[@title='详情']")  # 等待
        self.check_approval_file('驳回', '这是驳回的审阅')  # 驳回审阅
        time.sleep(2)
        self.element_click(self.approval_done_loc)  # 进入已处理
        time.sleep(2)
        self.search_approval_notes('发起审阅驳回的标题', need_filter=1)
        self.verify_approval_file_exist('发起审阅驳回的标题')
        self.back_home()  # 切出frame
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account3['username'], account['password'])  # 登录抄送人
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_my_check_loc)  # 进入抄送给我的
        time.sleep(1)
        self.search_approval_notes('发起审阅驳回的标题', need_filter=1)
        self.verify_approval_file_none_exist('发起审阅驳回的标题')

    def test_TestApproval_04(self):
        """发起文档审阅，审阅中文件权限校验"""
        self.login(account['username'], account['password'])  # 登录
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_todo_loc)  # 进入待处理
        self.delete_approval('通过', '清空审阅中的待处理')
        time.sleep(2)
        self.back_home()  # 切出frame
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', '审阅中的文件权限', '审阅中')  # 新建文件
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.element_click(self.approval_open_loc)  # 发起审批
        self.create_approval('审阅中的文件权限的标题', '审阅中的文件权限的备注')
        self.select_approval_file('审阅中的文件权限')
        self.select_option('自定义审阅流程', reviewer=account['name'], cc=account3['name'])
        self.element_click(self.approval_open_button_loc)  # 下一步
        self.into_approval_submit()  # 切换至审批提交的frame
        self.element_click(self.approval_add_submit_loc)  # 提交
        self.wait_element(self.approval_add_success_loc)  # 等待
        self.back_home()  # 切出frame
        self.element_click(self.approval_add_submit_close_loc)  # 关闭弹窗
        time.sleep(2)
        self.element_click(self.file_loc)  # 点击文件
        time.sleep(5)
        self.element_click(self.my_file_loc)  # 点击我的文件
        approval_file_status = self.get_approval_file_status('审阅中的文件权限')
        self.assertIn('审阅中', approval_file_status)
        limit_list = self.get_file_limit('审阅中的文件')  # 获取右击菜单的不可用权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertIn('重命名', limit_list)
        self.assertIn('放入回收站', limit_list)

    def test_TestApproval_05(self):
        """发起文档审阅通过，审阅通过文件权限校验"""
        self.login(account['username'], account['password'])  # 登录
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_todo_loc)  # 进入待处理
        self.delete_approval('通过', '清空审阅中的待处理')
        time.sleep(2)
        self.back_home()  # 切出frame
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', '审阅通过的文件权限', '审阅通过')  # 新建文件
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.element_click(self.approval_open_loc)  # 发起审批
        self.create_approval('审阅通过的文件权限的标题', '审阅通过的文件权限的备注')
        self.select_approval_file('审阅通过的文件权限')
        self.select_option('自定义审阅流程', reviewer=account['name'], cc=account3['name'])
        self.element_click(self.approval_open_button_loc)  # 下一步
        self.into_approval_submit()  # 切换至审批提交的frame
        self.element_click(self.approval_add_submit_loc)  # 提交
        self.wait_element(self.approval_add_success_loc)  # 等待
        self.back_home()  # 切出frame
        self.element_click(self.approval_add_submit_close_loc)  # 关闭弹窗
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account['username'], account['password'])  # 登录
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_todo_loc)  # 进入待处理
        time.sleep(1)
        self.search_approval_notes('审阅通过的文件权限的标题', need_filter=1)
        self.element_click(self.approval_reviewer_check_loc)  # 查看详情
        time.sleep(2)
        self.wait_element("//span[@title='详情']")  # 等待
        self.check_approval_file('通过', '这是通过的审阅')  # 同意审阅
        time.sleep(2)
        self.back_home()  # 切出frame
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account['password'])  # 登录
        time.sleep(2)
        self.element_click(self.my_file_loc)  # 点击我的文件
        approval_file_status = self.get_approval_file_status('审阅通过的文件权限')
        self.assertIn('通过', approval_file_status)
        limit_list = self.get_approval_file_limit('审阅通过的文件权限')  # 获取右击菜单的不可用权限
        self.assertNotIn('共享', limit_list)
        self.assertNotIn('协作', limit_list)
        self.assertNotIn('重命名', limit_list)
        self.assertNotIn('放入回收站', limit_list)

    def test_TestApproval_06(self):
        """发起文档审阅驳回，审阅驳回文件权限校验"""
        self.login(account['username'], account['password'])  # 登录
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_todo_loc)  # 进入待处理
        self.delete_approval('通过', '清空审阅中的待处理')
        time.sleep(2)
        self.back_home()  # 切出frame
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.my_file_loc)  # 点击我的文件
        self.new_folder('清空专用')
        self.new_folder('清空专用')
        self.delete_all()  # 清空文件
        self.new_file('wp', '审阅驳回的文件权限', '审阅驳回')  # 新建文件
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.element_click(self.approval_open_loc)  # 发起审批
        self.create_approval('审阅驳回的文件权限的标题', '审阅驳回的文件权限的备注')
        self.select_approval_file('审阅驳回的文件权限')
        self.select_option('自定义审阅流程', reviewer=account['name'], cc=account3['name'])
        self.element_click(self.approval_open_button_loc)  # 下一步
        self.into_approval_submit()  # 切换至审批提交的frame
        self.element_click(self.approval_add_submit_loc)  # 提交
        self.wait_element(self.approval_add_success_loc)  # 等待
        self.back_home()  # 切出frame
        self.element_click(self.approval_add_submit_close_loc)  # 关闭弹窗
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account['username'], account['password'])  # 登录
        self.element_click(self.approval_loc)  # 进入审阅模块
        self.into_approval()  # 进入审阅frame
        self.element_click(self.approval_todo_loc)  # 进入待处理
        time.sleep(1)
        self.search_approval_notes('审阅驳回的文件权限的标题', need_filter=1)
        self.element_click(self.approval_reviewer_check_loc)  # 查看详情
        time.sleep(2)
        self.wait_element("//span[@title='详情']")  # 等待
        self.check_approval_file('驳回', '这是驳回的审阅')  # 同意审阅
        time.sleep(2)
        self.back_home()  # 切出frame
        time.sleep(2)
        self.logout()  # 退出登录
        self.login(account2['username'], account['password'])  # 登录
        time.sleep(2)
        self.element_click(self.my_file_loc)  # 点击我的文件
        approval_file_status = self.get_approval_file_status('审阅驳回的文件权限')
        self.assertIn('驳回', approval_file_status)
        limit_list = self.get_approval_file_limit('审阅驳回的文件权限')  # 获取右击菜单的不可用权限
        self.assertIn('共享', limit_list)
        self.assertIn('协作', limit_list)
        self.assertNotIn('重命名', limit_list)
        self.assertNotIn('放入回收站', limit_list)
