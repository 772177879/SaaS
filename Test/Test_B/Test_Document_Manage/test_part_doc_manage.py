from Object.myunit import MyTest
from Page.DocumentManage.part_doc_manage import PartDocumentManage
from Page.login import Login
from Object.static import get_config
from Page.File.new_file import New
import time
from Page.File.delete_file import Delete
account_admin = get_config('zsy')   # 读取账号
account_ynzf = get_config('cdd')   # 读取账号
part_name = get_config('part')['part_name']
part_doc = get_config('part_doc')
part_folder_name = get_config('part_folder')['part_folder_name']


class TestPartDocManage(MyTest, Login, PartDocumentManage, New):
    def test_TestPartDocManage_01(self):
        """后端直接删除所有文件后，验证前端新建的文件在这里是正常状态显示"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)   # 点击文档管理
        self.element_click(self.part_doc_manage_loc)    # 点击部门文档管理
        time.sleep(2)
        self.into_partment(part_name)   # 进入对应部门中
        time.sleep(2)
        self.search_doc(part_doc['part_doc_name'])  # 搜索文件
        try:
            self.delete_all()   # 删除所有文件
        except:
            pass
        self.element_click(self.reset_button_loc)   # 点击重置
        self.search_doc(part_folder_name)  # 搜索文件夹后
        try:
            self.delete_all()   # 删除所有文件
        except:
            pass
        self.close_page()  # 关闭后台，进入前端
        self.logout()  # 退出登录
        """前端开始新建文件"""
        self.login(account_ynzf['username'], account_ynzf['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)   # 点击部门
        time.sleep(2)
        self.click_file(part_name)      # 进入部门中
        try:
            Delete(self.driver).delete_all(delete_type=1)  # 删除所有文件
        except:
            pass
        self.new_folder(part_folder_name)   # 新建配置的文件夹
        self.new_file('ss', part_doc['part_doc_name'], part_doc['part_doc_content'])    # 新建配置的文件
        self.logout()   # 退出登录
        """后端再进入查看是否有文件，且是否是正常状态"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.part_doc_manage_loc)  # 点击部门文档管理
        time.sleep(2)
        self.into_partment(part_name)  # 进入对应部门中
        time.sleep(2)
        """搜索查看文件"""
        self.search_doc(part_doc['part_doc_name'], need_filter=1)   # 搜索文件
        time.sleep(1)
        doc_status = self.get_file_status('ss', part_doc['part_doc_name'])   # 获取文件状态
        self.assertEqual('正常', doc_status)      # 验证是文件是正常
        time.sleep(1)
        self.element_click(self.reset_button_loc)
        self.search_doc(part_folder_name, need_filter=1)   # 搜索文件夹后
        time.sleep(1)
        folder_status = self.get_file_status('folder', part_folder_name)    # 获取文件状态
        self.assertEqual('正常', folder_status)  # 验证是文件是正常

    def test_TestPartDocManage_02(self):
        """后端直接删除所有文件后，验证前端新建的文件在这里是正常状态显示, 前端删除后显示已删除"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.part_doc_manage_loc)  # 点击部门文档管理
        time.sleep(2)
        self.into_partment(part_name)  # 进入对应部门中
        time.sleep(2)
        self.search_doc(part_doc['part_doc_name'])  # 搜索文件
        try:
            self.delete_all()  # 删除所有文件
        except:
            pass
        self.element_click(self.reset_button_loc)   # 点击重置
        self.search_doc(part_folder_name)  # 搜索文件夹后
        try:
            self.delete_all()  # 删除所有文件
        except:
            pass
        self.close_page()  # 关闭后台，进入前端
        self.logout()  # 退出登录
        """前端开始新建文件"""
        self.login(account_ynzf['username'], account_ynzf['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)  # 点击部门
        time.sleep(2)
        self.click_file(part_name)  # 进入部门中
        try:
            Delete(self.driver).delete_all(delete_type=1)  # 删除所有文件
        except:
            pass
        self.new_folder(part_folder_name)  # 新建配置的文件夹
        self.new_file('ss', part_doc['part_doc_name'], part_doc['part_doc_content'])  # 新建配置的文件
        Delete(self.driver).delete_all(delete_type=1)        # 删除所有文件
        self.logout()  # 退出登录
        """后端再进入查看是否有文件，且是否是正常状态"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.part_doc_manage_loc)  # 点击部门文档管理
        time.sleep(2)
        self.into_partment(part_name)  # 进入对应部门中
        time.sleep(2)
        """搜索查看文件"""
        self.search_doc(part_doc['part_doc_name'], need_filter=1)  # 搜索文件
        time.sleep(1)
        doc_status = self.get_file_status('ss', part_doc['part_doc_name'])  # 获取文件状态
        self.assertEqual('已删除', doc_status)  # 验证是文件是已删除
        time.sleep(1)
        self.element_click(self.reset_button_loc)
        self.search_doc(part_folder_name, need_filter=1)  # 搜索文件夹后
        time.sleep(1)
        folder_status = self.get_file_status('folder', part_folder_name)  # 获取文件状态
        self.assertEqual('已删除', folder_status)  # 验证是文件是已删除

    def test_TestPartDocManage_03(self):
        """后端直接删除所有文件后，验证前端新建的文件在这里是正常状态显示, 前端删除后清空显示已彻底删除"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.part_doc_manage_loc)  # 点击部门文档管理
        time.sleep(2)
        self.into_partment(part_name)  # 进入对应部门中
        time.sleep(2)
        self.search_doc(part_doc['part_doc_name'])  # 搜索文件
        try:
            self.delete_all()  # 删除所有文件
        except:
            pass
        self.element_click(self.reset_button_loc)  # 点击重置
        self.search_doc(part_folder_name)  # 搜索文件夹后
        try:
            self.delete_all()  # 删除所有文件
        except:
            pass
        self.close_page()  # 关闭后台，进入前端
        self.logout()  # 退出登录
        """前端开始新建文件"""
        self.login(account_ynzf['username'], account_ynzf['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.element_click(self.part_loc)  # 点击部门
        time.sleep(2)
        self.click_file(part_name)  # 进入部门中
        try:
            Delete(self.driver).delete_all(delete_type=1)  # 删除所有文件
        except:
            pass
        self.new_folder(part_folder_name)  # 新建配置的文件夹
        self.new_file('ss', part_doc['part_doc_name'], part_doc['part_doc_content'])  # 新建配置的文件
        Delete(self.driver).delete_all(delete_type=1)  # 删除所有文件
        self.element_click(self.recycle_loc)  # 点击回收站
        self.element_click(self.part_recycle_loc)   # 点击部门回收站
        time.sleep(2)
        Delete(self.driver).clean_recycle()     # 清空回收站
        self.logout()  # 退出登录
        """后端再进入查看是否有文件，且是否是正常状态"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.part_doc_manage_loc)  # 点击部门文档管理
        time.sleep(2)
        self.into_partment(part_name)  # 进入对应部门中
        time.sleep(2)
        """搜索查看文件"""
        self.search_doc(part_doc['part_doc_name'], need_filter=1)  # 搜索文件
        time.sleep(1)
        doc_status = self.get_file_status('ss', part_doc['part_doc_name'])  # 获取文件状态
        self.assertEqual('彻底删除', doc_status)  # 验证是文件是彻底删除
        time.sleep(1)
        self.element_click(self.reset_button_loc)
        self.search_doc(part_folder_name, need_filter=1)  # 搜索文件夹后
        time.sleep(1)
        folder_status = self.get_file_status('folder', part_folder_name)  # 获取文件状态
        self.assertEqual('彻底删除', folder_status)  # 验证是文件是彻底删除
