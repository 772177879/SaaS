from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
from Object.static import get_project_path
from time import sleep
import win32gui
import win32con
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Form(Action, Loc):

    def into_form(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.app_frame_loc)))
        # self.element_click("//h1[text()='%s']" % pdf_type)

    def new_form(self, form_question):  # 新建表单
        log.info('新建表单:问题是：%s' % form_question)
        self.element_click(self.new_form_loc)   # 点击新建
        self.wait_element(self.new_form_question_loc)    # 等待
        self.element_click(self.new_form_question_loc)  # 点击
        self.element_input(self.new_form_question_loc, form_question)   # 输入问题
        self.element_click(self.new_form_submit_loc)    # 点击发布

    def answer_form(self, form_answer):  # 填写表单
        log.info('填写表单：答案是：%s' % form_answer)
        self.element_input(self.answer_loc, form_answer)     # 填写答案
        self.element_click(self.answer_submit_loc)  # 点击提交
        self.wait_element(self.answer_submit_success_loc)   # 等待提交成功提示

    def check_answer(self, form_answer):    # 验证答案是收集到的
        log.info('填写表单：答案是：%s' % form_answer)
        self.element_click(self.first_form_loc)     # 点击第一个表单
        self.wait_element(self.collect_answer_loc)      # 定位在收集结果中
        self.verify_element_exist("//span[text()='%s']" % form_answer)      # 答案是收集到的

    def get_form_url(self): # 获取表单的url
        url = self.find_element(self.url_loc).get_attribute('value')
        return url

    def delete_all_forms(self):   # 删除所有的表单
        log.info('删除所有表单')
        sleep(2)
        all_xpath = self.driver.find_elements_by_xpath("//tr[@class='el-table__row']//pre")     # 找到所有的表单
        form_titles = []
        for xpath in all_xpath:
            form_titles.append(xpath.text)
        print(form_titles)
        for form_title in form_titles:
            element = self.driver.find_element_by_xpath("//pre[contains(text(),'%s')]" % form_title)
            ActionChains(self.driver).move_to_element(element).perform()  # 鼠标移动过来
            self.element_click(self.form_menu_loc)  # 点击菜单栏
            sleep(2)
            self.element_click(self.form_delete_loc)    # 点击删除
            sleep(2)
            self.element_click(self.form_delete_sure_loc)   # 点击确定
            sleep(2)



