from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Object.static import get_screen_size


class New(Action, Loc):

    def new_folder(self, folder_name):
        log.info('新建文件夹:%s' % folder_name)
        # 新建文件夹
        self.element_click(self.new_loc)    # 点击新建
        self.element_click(self.new_folder_loc)     # 点击文件夹
        self.element_input(self.folder_input_loc, folder_name)  # 输入名称
        self.element_click(self.filename_input_submit_loc)  # 点击确认
        time.sleep(2)

    def new_file(self, file_type, file_name, value):
        log.info('新建文件:%s,%s,%s' % (file_type, file_name, value))
        # 新建文档-用户切换到WebOffice
        self.element_click(self.new_loc)    # 点击新建按钮
        if file_type == 'wp':
            self.element_click(self.new_wp_loc)      # 点击新建wp
        elif file_type == 'ss':
            self.element_click(self.new_ss_loc)    # 点击新建ss
        elif file_type == 'pg':
            self.element_click(self.new_pg_loc)    # 点击新建pg
        # self.element_input(self.filename_input_loc, file_name)      # 输入名称
        # self.element_click(self.filename_input_submit_loc)      # 点击确认
        self.change_page()  # 切换到模板页
        # try:
        #     self.find_element("//div[contains(@class, 'newFile')]").click()
        # except:
        #     self.find_element("/html/body/div/div/div/div[2]/div/div[1]/div/div/img").click()
        if file_type == 'wp' or file_type == 'ss':
            self.find_element("//div[contains(@class, 'newFile')]").click()
        elif file_type == 'pg':
            self.find_element("/html/body/div/div/div/div[2]/div/div[1]/div/div/img").click()
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, "bodyIframe")))  # 直接切换到该frame
        time.sleep(3)
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='文件']")))  # 等待文件出现
        self.wait_element("//span[text()='开始']")
        # self.driver.switch_to.default_content()
        self.find_element("//div[@class='fileName_wrap']").click()  # 点击默认名称
        self.find_element("//div[@class='input_wrap']/input").send_keys(Keys.CONTROL + 'a')
        self.find_element("//div[@class='input_wrap']/input").send_keys(Keys.BACKSPACE)
        self.find_element("//div[@class='input_wrap']/input").send_keys(file_name)  # 修改名称
        self.find_element("//div[@class='title']/div").click()  # 修改后点击别处，使其保存
        self.edit_file(file_type, value)
        self.wait_element("//span[contains(text(), '%s')]" % file_name)     # 等待出现该文件名称
        # self.check_status(file_name)

    def edit_file(self, file_type, value):
        log.info('编辑文件: %s, %s' % (file_type, value))
        # 编辑文档
        self.change_page()  # 切换到web office编辑界面
        # time.sleep(5)
        # self.driver.switch_to.frame(self.find_element(self.frame_loc))  # 切换到frame
        # time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.edit_frame_loc)))
        url = self.driver.current_url
        log.info("编辑地址：" + url)
        # 直接进入frame里
        if file_type == 'pg':
            x, y = get_screen_size()
            high = x//2
            width = y//2
            time.sleep(4)
            ActionChains(self.driver).move_by_offset(high, width).click().perform()       # 点击某个位置
        time.sleep(1)
        self.element_input(self.edit_area_loc, Keys.ENTER)      # 输入enter
        time.sleep(1)
        self.element_input(self.edit_area_loc, value)       # 输入值
        self.element_input(self.edit_area_loc, Keys.ENTER)      # 输入enter
        self.element_click(self.view_loc)       # 点击插入
        time.sleep(1)
        self.element_click(self.read_loc)       # 点击审阅
        self.close_page()       # 关闭当前界面
        time.sleep(2)

    # def check_status(self, file_name):
    #     log.info('验证文件出现多版本标识：%s' % file_name)
    #     self.wait_element("//span[contains(text(),'%s')]/../../../../..//i[@title='多版本']" % file_name)





