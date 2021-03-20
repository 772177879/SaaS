from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Search(Action, Loc):

    def search_filename(self, filename):        # 通过文件名搜索
        log.info('以下为通过文件名搜索：%s' % filename)
        self.element_input(self.search_area_loc, filename)      # 输入搜索的文件名
        # self.element_click(self.search_button_loc)      # 点击搜索
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()   # 点击搜索
        self.element_click(self.search_filename_loc)    # 文件名筛选结果
        time.sleep(1)
        all_xpath = self.driver.find_elements_by_xpath("//div[@class='m-window l-window search-window animated']"
                                                        "//span[@class='name']")
        file_names = []
        for xpath in all_xpath:
            file_names.append(xpath.get_attribute('title'))
        return file_names   # 获取所有的文件名

    def search_file_content(self, content):         # 通过文件内容搜索
        log.info('以下为通过文件内容搜索:%s' % content)
        self.element_input(self.search_area_loc, content)  # 输入搜索的内容
        # self.element_click(self.search_button_loc)  # 点击搜索
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()   # 点击搜索
        self.element_click(self.search_content_loc)  # 文件内容筛选结果
        time.sleep(1)
        all_xpath = self.driver.find_elements_by_xpath("//div[@class='m-window l-window search-window animated']"
                                                       "//span[@class='name']")
        file_names = []
        for xpath in all_xpath:
            file_names.append(xpath.get_attribute('title'))
        return file_names  # 获取所有的文件名

    def search_filter_type(self, search_text, filter_type):       # 按照文件类型筛选
        log.info('以下为按照文件类型筛选:%s, %s' % (search_text, filter_type))
        self.element_input(self.search_area_loc, search_text, clear=1)  # 输入搜索的内容
        # self.element_click(self.search_button_loc)  # 点击搜索
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()   # 点击搜索
        self.element_click(self.search_filename_loc)  # 文件名筛选结果
        time.sleep(1)
        self.element_click(self.filter_loc)     # 点击筛选
        time.sleep(1)
        # 按照类型筛选，0全部，1wp，2ss,3pg,4其他
        self.element_click("//li[@dataindex='%s']" % filter_type)
        time.sleep(2)
        all_xpath = self.driver.find_elements_by_xpath("//div[@class='m-window l-window search-window animated']"
                                                       "//span[@class='name']")
        file_names = []
        for xpath in all_xpath:
            file_names.append(xpath.get_attribute('title'))
        return file_names  # 获取所有的文件名






