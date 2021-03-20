from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from Object import static
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Object.location import Loc
from Object.Logconfig import log
import traceback


class Action(Loc):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ，FindElement等
    """

    def __init__(self, selenium_driver):
        # 初始化driver、url、title等
        self.driver = selenium_driver

    def open_url(self, url):  # 打开网站
        try:
            self.driver.get(url)  # 使用get打开访问链接地址
            self.driver.maximize_window()  # 窗口最大化
        except:
            log.exception(traceback.format_exc())
            raise

    def find_element(self, loc):  # 改变定位器方法，少写点儿字
        try:
            return self.driver.find_element_by_xpath(loc)
        except:
            log.exception(traceback.format_exc())
            raise

    def element_input(self, loc, value, clear=0):   # 改变输入方法，少写点儿字
        try:
            if clear == 1:      # 如果需要清空再输入，clear设置为1
                self.element_click(loc)
                self.find_element(loc).clear()  # 清空
            sleep(1)
            self.find_element(loc).send_keys(value)    # 再输入
        except:
            log.exception(traceback.format_exc())
            raise

    def element_click(self, loc):       # 改变点击方法，少写点儿字
        try:
            self.find_element(loc).click()
        except:
            log.exception(traceback.format_exc())
            raise

    def change_page(self, switch_window=1):
        # 切换页面，switch_window为切换到
        # sleep(2)
        handles = self.driver.window_handles
        # sleep(2)
        self.driver.switch_to.window(handles[switch_window])

    def close_page(self, back_window=0):
        # 关闭当前界面，顺带返回到第一个界面里
        # sleep(2)
        handles = self.driver.window_handles
        self.driver.close()
        # sleep(2)
        self.driver.switch_to.window(handles[back_window])

    def right_click_loc(self, loc):  # 右击
        sleep(2)
        try:
            return ActionChains(self.driver).context_click(self.find_element(loc)).perform()
        except:
            log.exception(traceback.format_exc())
            raise

    def right_click_filename(self, filename):   # 右击文件名
        try:
            return ActionChains(self.driver).context_click(
                self.find_element("//span[contains(text(),'%s')]" % filename)).perform()
        except:
            log.exception(traceback.format_exc())
            raise

    def click_file(self, filename):     # 点击文件名
        try:
            self.find_element("//span[contains(text(),'%s')]" % filename).click()
        except:
            log.exception(traceback.format_exc())
            raise
        sleep(2)

    def verify_element_exist(self, loc):  # 验证元素是否存在
        sleep(1)
        try:
            self.find_element(loc)
        except:
            log.exception(traceback.format_exc())
            raise

    def verify_element_none_exist(self, loc):  # 验证元素不存在
        try:
            try:
                sleep(1)
                self.find_element(loc)
                raise BaseException  # 元素存在抛异常
            except TimeoutException and NoSuchElementException:
                pass
        except:
            log.exception(traceback.format_exc())
            raise

    def verify_file_exist(self, filename, file_type=0):
        try:
            if file_type == 0:
                self.verify_element_exist('//span[contains(text(),"%s")]' % filename)
            elif file_type == 1:
                self.verify_element_exist('//span[text()="%s"]' % filename)
        except:
            log.exception(traceback.format_exc())
            raise

    def verify_file_none_exist(self, filename):
        try:
            self.verify_element_none_exist('//span[contains(text(),"%s")]' % filename)
        except:
            log.exception(traceback.format_exc())
            raise

    def save_screenshots(self, screen):  # 截图
        self.driver.get_screenshot_as_file(static.get_project_path() + '\\ResultReport\\images\\%s.png' % screen)
        name = '%s.png' % screen
        return name

    def get_file_limit(self, filename):      # 获取文件权限列表
        try:
            self.right_click_filename(filename)     # 右击文件名
            sleep(2)
            all_xpath = self.driver.find_elements_by_xpath("//div[@class='menu MDHomeFileMenuView']/div[@class='menu-item']"
                                                           "/div/div")
            limit_list = []     # 权限列表
            for xpath in all_xpath:
                limit_list.append(xpath.text)
            return limit_list
        except:
            log.exception(traceback.format_exc())
            raise

    def get_group_list(self):
        # 获取群组列表和类型（我加入的，我创建的）
        try:
            group_list = []
            type_list = []
            all_list = []
            try:
                group_paths = self.driver.find_elements_by_xpath("//div[@class='view-scroll-b']/li//span")  # 群组列表
                type_paths = self.driver.find_elements_by_xpath("//div[@class='view-scroll-b']/li//em")  # 状态列表
                for group_path in group_paths:
                    group_list.append(group_path.text)
                for type_path in type_paths:
                    if 'tip tip-a l-ioc' in type_path.get_attribute('class'):
                        type_list.append('我创建的')
                    elif 'tip tip-b l-ioc' in type_path.get_attribute('class'):
                        type_list.append('我加入的')
            except:
                pass
            for i in range(len(group_list)):
                one_list = [group_list[i], type_list[i]]
                all_list.append(one_list)
            print(group_list)
            print(type_list)
            print(all_list)
            return all_list
        except:
            log.exception(traceback.format_exc())
            raise

    def into_console(self):     # 进入企业控制台
        log.info('以下为进入企业控制台')
        self.element_click(self.setting_loc)    # 点击设置
        self.element_click(self.console_loc)    # 点击企业控制台
        sleep(2)
        self.change_page()  # 切换到企业控制台
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.console_board_loc)))
        self.wait_element(self.console_board_loc)
        # 等待数据看板出现出现

    def wait_element(self, loc):     # 等待元素出现
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, loc)), message='失败，没等到该元素')
        sleep(1)

    def into_partment(self, partment):  # 组织架构中进入部门
        log.info('进入部门:%s' % partment)
        self.element_click("//span[@class='ant-tree-title']//span[text()='%s']" % partment)

    def get_file_status(self, file_type, filename):     # 文档管理中获取文件状态
        log.info('获取文件的当前状态：%s' % filename)
        if file_type == 'folder':
            status = self.find_element("//a[contains(text(), '%s')]/../../..//span[@class='undefined']" % filename).text
        else:
            status = self.find_element("//span[contains(text(), '%s')]/../../..//span[@class='undefined']" % filename).text
        return status

    def delete_doc(self, file_type, file_name):       # 删除文件
        log.info('删除文件:%s' % file_name)
        if file_type == 'folder':
            self.element_click("//a[contains(text(),'%s')]/../../..//button/span[text()='删除']" % file_name)
        else:
            self.element_click("//span[contains(text(),'%s')]/../../..//button/span[text()='删除']" % file_name)
        sleep(2)
        self.element_click(self.delete_doc_sure_loc)  # 点击确认

    def download_doc(self, file_type, file_name):      # 下载文件
        log.info('下载文件:%s' % file_name)
        if file_type == 'folder':
            self.element_click("//a[contains(text(),'%s')]/../../..//button/span[text()='下载']" % file_name)
        else:
            self.element_click("//span[contains(text(),'%s')]/../../..//button/span[text()='下载']" % file_name)
        sleep(5)

    def click_doc(self, file_type, file_name):    # 文档管理中点击文件
        log.info('点击文件:%s' % file_name)
        if file_type == 'folder':
            self.element_click("//a[contains(text(),'%s')]" % file_name)
        else:
            self.element_click("//span[contains(text(),'%s')]" % file_name)
















