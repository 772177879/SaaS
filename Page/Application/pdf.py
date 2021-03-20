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


class PDF(Action, Loc):

    def into_pdf_type(self, pdf_type):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.app_frame_loc)))
        self.element_click("//h1[text()='%s']" % pdf_type)

    def pdf_upload_file(self, filename):  # 20181012 重写上传方法，不需要第三方工具打包VBS
        log.info('pdf工具集上传文件:%s' % filename)
        # self.element_click(self.upload_loc)    # 点击上传
        # self.element_click(self.upload_file_loc)     # 点击上传
        self.element_click(self.pdf_select_file_loc)    # 选择本地文件
        path = get_project_path() + '\\Upload\\%s' % filename
        sleep(2)
        """路径一定要对，不然整个test cases晾在那里"""
        sleep(2)
        dialog = win32gui.FindWindow('#32770', u'打开')  # 找到windows对话框参数是（className，title）
        combo_box_ex32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        combo_box = win32gui.FindWindowEx(combo_box_ex32, 0, 'ComboBox', None)
        edit = win32gui.FindWindowEx(combo_box, 0, 'Edit', None)  # 上面3句依次找对象，直到找出输入框edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, path)  # 往输入框输入地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
        # self.wait_element("//span[contains(text(),'%s')]" % filename)   # 等待文件的出现
        self.wait_element(self.pdf_upload_success_loc)      # 等待上传完成
        sleep(2)
        self.element_click(self.pdf_start_loc)      # 点击开始转换
        self.wait_element(self.pdf_work_success_loc)    # 等待转换成功

