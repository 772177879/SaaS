from Object.base import Action
from Object.location import Loc
from Object.Logconfig import log
from Object.static import get_project_path
from time import sleep
import win32gui
import win32con


class Upload(Action, Loc):

    def upload_file(self, filename):  # 20181012 重写上传方法，不需要第三方工具打包VBS
        log.info('上传文件:%s' % filename)
        self.element_click(self.upload_loc)    # 点击上传
        self.element_click(self.upload_file_loc)     # 点击上传
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
        self.wait_element("//span[contains(text(),'%s')]" % filename)   # 等待文件的出现

    # def upload_folder(self, filename):  # 20181012 重写上传方法，不需要第三方工具打包VBS
    #     log.info('上传文件夹:%s' % filename)
    #     self.element_click(self.new_loc)    # 点击新建
    #     self.element_click(self.upload_folder_loc)     # 点击上传
    #     path = get_project_path() + '\\Upload\\%s' % filename
    #     sleep(2)
    #     """路径一定要对，不然整个test cases晾在那里"""
    #     sleep(2)
    #     dialog = win32gui.FindWindow('#32770', u'选择要上传的文件夹')  # 找到windows对话框参数是（className，title）
    #     # combo_box_ex32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    #     # combo_box = win32gui.FindWindowEx(combo_box_ex32, 0, 'ComboBox', None)
    #     edit = win32gui.FindWindowEx(dialog, 0, 'Edit', None)  # 上面3句依次找对象，直到找出输入框edit对象的句柄
    #     button = win32gui.FindWindowEx(dialog, 0, 'Button', u'上传')  # 确定按钮
    #     win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, path)  # 往输入框输入地址
    #     sleep(2)
    #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    #     sleep(2)
    #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    #     # self.wait_element("//span[contains(text(),'%s')]" % filename)   # 等待文件的出现
    #     # 对于弹出框进行处理
