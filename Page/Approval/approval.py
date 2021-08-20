from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import traceback

class Approval(Action, Loc):

    def into_approval(self):  # 进入审阅tab
        WebDriverWait(self.driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.approval_frame_loc)))

    def into_approval_submit(self):  # 进入审批提交
        WebDriverWait(self.driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.approval_submit_loc)))

    def back_home(self):  # 返回主页面
        self.driver.switch_to.default_content()

    def search_approval_notes(self, search_txt, need_filter=0):   # 搜索出审批记录
        log.info('搜索：%s' % search_txt)
        date = time.strftime("%Y-%m-%d")
        self.element_input(self.approval_search_title_loc, search_txt, clear=1)
        if need_filter == 1:    # 如果需要筛选的话，选1
            self.element_click(self.approval_begin_time_loc)  # 点击开始时间
            time.sleep(1)
            self.element_input(self.approval_begin_time_loc, date)  # 选择本天
            time.sleep(2)
            self.element_input(self.approval_end_time_loc, date)  # 选择本天
            time.sleep(1)
        self.element_click(self.approval_search_btn_loc)      # 点击搜索
        time.sleep(2)

    def select_option(self, reviewer, cc):  # 流程选择及人员添加
        # option = self.find_element(self.approval_flow_loc)  # 定位下拉框
        # if select_type == '模板审批':
        #     Select(option).select_by_value("2")  # 选择下拉框 模板审阅流程
        # elif select_type == '自定义审阅流程':
        #     Select(option).select_by_value("1")  # 选择下拉框 自定义审阅流程
        #     # 添加审阅人
        #     time.sleep(1)
            self.element_click(self.approval_add_reviewer_loc)
            time.sleep(1)
            self.element_input(self.approval_search_reviewer_loc, reviewer)  # 添加审阅人
            time.sleep(2)
            self.element_click("//span[@title='%s']/../../div[@class='add-view']" % reviewer)  # 点击添加
            time.sleep(2)
            self.element_click(self.approval_reviewer_submit_loc)  # 点击确定
            time.sleep(1)
            # 添加抄送人
            self.element_click(self.approval_add_cc_loc)
            time.sleep(2)
            self.element_input(self.approval_search_cc_loc, cc)  # 添加抄送人
            time.sleep(2)
            self.element_click("//span[@title='%s']/../../div[@class='add-view']" % cc)  # 点击添加
            time.sleep(2)
            self.element_click(self.approval_cc_submit_loc)  # 点击确定
            time.sleep(1)

    def create_approval(self, title, comments):  # 输入标题及备注
        log.info('新建审阅输入标题,备注:%s,%s' % (title, comments))
        self.wait_element(self.approval_open_logo_loc)  # 等待
        self.element_input(self.approval_open_title_loc, title)  # 审阅输入审阅标题
        time.sleep(2)
        self.element_input(self.approval_open_area_loc, comments)  # 输入审阅备注

    def select_approval_file(self, filename):  # 选择审阅文件
        log.info('选择的审阅文件是：%s' % filename)
        self.element_click(self.approval_open_file_loc)  # 添加审阅文件
        time.sleep(2)
        self.element_input(self.approval_file_search_loc, filename)  # 搜索添加审阅文件添加
        time.sleep(2)
        self.element_click("//em[@class='bg-yellow']")
        self.element_click(self.approval_file_submit_loc)  # 确认选择
        time.sleep(2)

    def check_approval_file(self, status, comments):  # 审阅文件
        log.info('进行的审阅操作是：%s' % status)
        if status == "通过":
            self.element_click(self.approval_reviewer_agree_loc)  # 点击通过
            time.sleep(1)
            self.element_input(self.approval_reviewer_commit_loc, comments)  # 输入审批意见
            time.sleep(1)
            self.element_click(self.approval_reviewer_btn_loc)  # 点击确定
            time.sleep(2)
        elif status == "驳回":
            self.element_click(self.approval_reviewer_disagree_loc)  # 点击拒绝
            time.sleep(1)
            self.element_input(self.approval_reviewer_commit_loc, comments)  # 输入审批意见
            time.sleep(1)
            self.element_click(self.approval_reviewer_btn_loc)  # 点击确定

    def delete_approval(self, status, comments):  # 清空所有审阅中数据
        log.info('清空所有审阅中数据')
        time.sleep(2)
        try:
            all_xpath = self.driver.find_elements_by_xpath(self.approval_reviewer_check_loc)  # 找到所有审阅中数据的查看详情
            for i in range(len(all_xpath)):
                all_xpath[i].click()
                self.wait_element("//span[@title='详情']")  # 等待
                self.check_approval_file(status, comments)
                time.sleep(5)
        except:
            pass

    def get_approval_file_limit(self, filename):  # 获取审阅文件权限列表
        try:
            self.right_click_filename(filename)  # 右击文件名
            time.sleep(2)
            all_xpath = self.driver.find_elements_by_xpath(
                "//div[contains(@class,'disabled-color')]")  # 获取当前不可点击按钮
            limit_list = []  # 权限列表
            for xpath in all_xpath:
                limit_list.append(xpath.text)
            return limit_list
        except:
            log.exception(traceback.format_exc())
            raise

    def get_approval_file_status(self, filename):
        log.info('查看的审阅文件是：%s' % filename)
        approval_file = self.find_element("//span[text()='%s.docx']/../span/div" % filename).text
        return approval_file

    def verify_approval_file_exist(self, approval_title, file_type=0):
        try:
            if file_type == 0:
                self.verify_element_exist('//div[contains(text(),"%s")]' % approval_title)
            elif file_type == 1:
                self.verify_element_exist('//div[text()="%s"]' % approval_title)
        except:
            log.exception(traceback.format_exc())
            raise

    def verify_approval_file_none_exist(self, approval_title):
        try:
            self.verify_element_none_exist('//div[contains(text(),"%s")]' % approval_title)
        except:
            log.exception(traceback.format_exc())
            raise
