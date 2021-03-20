from Object.base import Action
from Object.location import Loc
import time
from Object.Logconfig import log


class Tag(Action, Loc):
    def add_tag(self, filename, tag_name):
        log.info('为文件添加标签:%s,%s' % (filename, tag_name))
        # 为文件添加标签
        self.right_click_filename(filename)     # 右击
        self.element_click(self.tag_loc)    # 点击添加标签
        time.sleep(3)
        self.element_input(self.tag_input_loc, tag_name)     # 标签输入后会自动搜索
        time.sleep(1)
        try:
            self.element_click(self.create_tag_loc)    # 如果有创建，说明之前的被删了
        except:
            self.element_click(self.select_tag_loc)     # 如果没有创建，直接搜索结果里点一下
            self.element_click(self.add_tag_loc)        # 再点添加，为文件添加标签
        time.sleep(1)

    def tag_search(self, tag_name):
        log.info('通过标签筛选:%s' % tag_name)
        # 通过标签筛选
        self.element_click(self.into_tag_loc)   # 进入标签界面
        self.element_input(self.tag_search_input_loc, tag_name)   # 输入标签
        time.sleep(2)
        self.element_click(self.tag_search_button_loc)  # 点击立即搜索
        time.sleep(2)
        all_xpath = self.driver.find_elements_by_xpath("//div[@class='m-window l-window search-tag-window animated']"
                                                       "//span[@class='name']")
        file_names = []
        for xpath in all_xpath:
            file_names.append(xpath.text)
        return file_names  # 获取所有的文件名

