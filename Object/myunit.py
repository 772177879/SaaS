# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
from Object import base
from Object.static import get_download_path, get_config, get_screen_size, get_video_path
import time
from PIL import ImageGrab
import numpy as np
import cv2
import os
from selenium.webdriver.chrome.options import Options
import threading
from Object.Logconfig import log
download_path = get_download_path()
video_path = get_video_path()
url = get_config('url')['url']


class MyTest(unittest.TestCase):

    def setUp(self):
        # option = webdriver.ChromeOptions()
        # option._arguments = ['disable-infobars']
        # warnings.simplefilter('ignore', ResourceWarning)
        # prefs = {'download.default_directory': download_path}
        # option.add_experimental_option('prefs', prefs)
        log.info('--------------------------'+self._testMethodName + '测试开始----------------------------------------')
        self.flag = False
        x, y = get_screen_size()
        prefs = {'download.default_directory': download_path}
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', prefs)
        # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--window-size=%s,%s" % (x, y))  # 专门应对无头浏览器中不能最大化屏幕的方案
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(20)
        self.driver.get(url)
        self.driver.maximize_window()
        #  启动录制程序
        name = video_path + '\\' + self._testMethodName     # 录制的文件名
        self.t = threading.Thread(target=self.video_record, args=(name,))
        self.t.start()

    def tearDown(self):
        """断言截图"""
        # 脚本结束后录制结束
        self.flag = True
        result = self.defaultTestResult()
        self._feedErrorsToResult(result, self._outcome.errors)
        error = self.list2reason(result.errors)
        failure = self.list2reason(result.failures)
        ok = not error and not failure
        if not ok:
            png = time.strftime("%H_%M_%S")
            name = base.Action(self.driver).save_screenshots(png)
            print('screenshot:%s' % name)
            self.driver.quit()
        else:
            self.driver.quit()
            os.remove(video_path + '\\' + self._testMethodName + '.avi')    # 如果是成功的，运行完后删除防止占空间
        log.info('-----------------------------------'+self._testMethodName + '测试结束-------------------------------')

    def list2reason(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    def video_record(self, name):     # 录屏
        p = ImageGrab.grab()
        a, b = p.size  #
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video = cv2.VideoWriter('%s.avi' % name, fourcc, 16, (a, b))
        log.info('start monitor!')
        while True:
            im = ImageGrab.grab()
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            video.write(imm)
            if self.flag:
                log.info("stop monitor")
                break
        video.release()
