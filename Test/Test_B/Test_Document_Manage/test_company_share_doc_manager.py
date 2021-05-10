from Object.myunit import MyTest
from Page.DocumentManage.part_doc_manage import PartDocumentManage
from Page.login import Login
from Object.static import get_config
from Page.File.new_file import New
import time
from Page.File.delete_file import Delete
account_admin = get_config('zsy')   # 读取账号
company_share_doc = get_config('company_share_doc')
company_share_folder = get_config('company_share_folder')['company_folder_name']
company_share_part = '企业共享文件夹'


class TestCompanyShareDocManage(MyTest, Login, PartDocumentManage, New):
    def test_TestCompanyShareDocManage_01(self):
        """后端直接删除所有文件后，验证前端新建的文件在这里是正常状态显示"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        # time.sleep(5)
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)   # 点击文档管理
        self.element_click(self.company_share_manage_loc)    # 点击企业共享文档管理
        time.sleep(2)
        self.search_doc(company_share_doc['share_doc_name'], need_filter=1)  # 搜索文件
        try:
            self.delete_all()   # 删除所有文件
        except:
            pass
        self.element_click(self.reset_button_loc)   # 点击重置
        self.search_doc(company_share_folder, need_filter=1)  # 搜索文件夹后
        try:
            self.delete_all()   # 删除所有文件
        except:
            pass
        self.close_page()  # 关闭后台，进入前端
        """前端开始新建文件"""
        self.element_click(self.part_loc)   # 点击部门
        time.sleep(2)
        self.click_file(company_share_part)      # 进入企业共享文件夹中
        try:
            Delete(self.driver).delete_all()  # 删除所有文件
        except:
            pass
        self.new_folder(company_share_folder)   # 新建配置的文件夹
        self.new_file('ss', company_share_doc['share_doc_name'], company_share_doc['share_doc_content'])    # 新建配置的文件
        """后端再进入查看是否有文件，且是否是正常状态"""
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.company_share_manage_loc)    # 点击企业共享文档管理
        time.sleep(2)
        """搜索查看文件"""
        self.search_doc(company_share_doc['share_doc_name'], need_filter=1)   # 搜索文件
        time.sleep(1)
        doc_status = self.get_file_status('ss', company_share_doc['share_doc_name'])   # 获取文件状态
        self.assertEqual('正常', doc_status)      # 验证是文件是正常
        time.sleep(1)
        self.element_click(self.reset_button_loc)
        self.search_doc(company_share_folder, need_filter=1)   # 搜索文件夹后
        time.sleep(1)
        folder_status = self.get_file_status('folder', company_share_folder)    # 获取文件状态
        self.assertEqual('正常', folder_status)  # 验证是文件是正常

    def test_TestCompanyShareDocManage_02(self):
        """后端直接删除所有文件后，验证前端新建的文件后删除，在这里是已删除状态显示"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        # time.sleep(5)
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.company_share_manage_loc)  # 点击企业共享文档管理
        time.sleep(2)
        self.search_doc(company_share_doc['share_doc_name'], need_filter=1)  # 搜索文件
        try:
            self.delete_all()  # 删除所有文件
        except:
            pass
        self.element_click(self.reset_button_loc)  # 点击重置
        self.search_doc(company_share_folder, need_filter=1)  # 搜索文件夹后
        try:
            self.delete_all()  # 删除所有文件
        except:
            pass
        self.close_page()  # 关闭后台，进入前端
        """前端开始新建文件"""
        self.element_click(self.part_loc)  # 点击部门
        time.sleep(2)
        self.click_file(company_share_part)  # 进入企业共享文件夹中
        try:
            Delete(self.driver).delete_all()  # 删除所有文件
        except:
            pass
        self.new_folder(company_share_folder)  # 新建配置的文件夹
        self.new_file('ss', company_share_doc['share_doc_name'], company_share_doc['share_doc_content'])  # 新建配置的文件
        time.sleep(2)
        Delete(self.driver).delete_all()  # 删除所有文件
        """后端再进入查看是否有文件，且是否是正常状态"""
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.company_share_manage_loc)  # 点击企业共享文档管理
        time.sleep(2)
        """搜索查看文件"""
        self.search_doc(company_share_doc['share_doc_name'], need_filter=1)  # 搜索文件
        time.sleep(1)
        doc_status = self.get_file_status('ss', company_share_doc['share_doc_name'])  # 获取文件状态
        self.assertEqual('已删除', doc_status)  # 验证是文件是已删除
        time.sleep(1)
        self.element_click(self.reset_button_loc)
        self.search_doc(company_share_folder, need_filter=1)  # 搜索文件夹后
        time.sleep(1)
        folder_status = self.get_file_status('folder', company_share_folder)  # 获取文件状态
        self.assertEqual('已删除', folder_status)  # 验证是文件是已删除

    def test_TestCompanyShareDocManage_03(self):
        """后端直接删除所有文件后，验证前端新建的文件后删除并且清空回收站，在这里是彻底删除状态显示"""
        self.login(account_admin['username'], account_admin['password'])  # 登录
        self.wait_element(self.my_file_loc)
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.company_share_manage_loc)  # 点击企业共享文档管理
        time.sleep(2)
        self.search_doc(company_share_doc['share_doc_name'])  # 搜索文件
        try:
            self.delete_all()  # 删除所有文件
        except:
            pass
        self.element_click(self.reset_button_loc)  # 点击重置
        self.search_doc(company_share_folder)  # 搜索文件夹后
        try:
            self.delete_all()  # 删除所有文件
        except:
            pass
        self.close_page()  # 关闭后台，进入前端
        """前端开始新建文件"""
        self.element_click(self.part_loc)  # 点击部门
        time.sleep(2)
        self.click_file(company_share_part)  # 进入企业共享文件夹中
        try:
            Delete(self.driver).delete_all()  # 删除所有文件
        except:
            pass
        self.new_folder(company_share_folder)  # 新建配置的文件夹
        self.new_file('ss', company_share_doc['share_doc_name'], company_share_doc['share_doc_content'])  # 新建配置的文件
        time.sleep(2)
        Delete(self.driver).delete_all()  # 删除所有文件
        self.element_click(self.recycle_loc)  # 点击回收站
        self.element_click(self.part_recycle_loc)   # 点击部门回收站
        time.sleep(2)
        Delete(self.driver).clean_recycle()     # 清空回收站
        """后端再进入查看是否有文件，且是否是正常状态"""
        self.into_console()  # 进入控制台
        self.element_click(self.console_document_loc)  # 点击文档管理
        self.element_click(self.company_share_manage_loc)  # 点击企业共享文档管理
        time.sleep(2)
        """搜索查看文件"""
        self.search_doc(company_share_doc['share_doc_name'], need_filter=1)  # 搜索文件
        time.sleep(1)
        doc_status = self.get_file_status('ss', company_share_doc['share_doc_name'])  # 获取文件状态
        self.assertEqual('彻底删除', doc_status)  # 验证是文件是已删除
        time.sleep(1)
        self.element_click(self.reset_button_loc)
        self.search_doc(company_share_folder, need_filter=1)  # 搜索文件夹后
        time.sleep(1)
        folder_status = self.get_file_status('folder', company_share_folder)  # 获取文件状态
        self.assertEqual('彻底删除', folder_status)  # 验证是文件是已删除
