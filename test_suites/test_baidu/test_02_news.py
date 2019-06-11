# coding=utf-8
import time
import unittest
from framework.logger import Logger
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from framework.ConnectDataBase import ConnectDataBase
from framework.ReadConfig import ReadConfig
from test_suites.test_baidu import *

logger = Logger(logger="Baidu > News").getlog()

class News(unittest.TestCase):
    """新闻页测试"""
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        ini = to_init()
        cls.driver = ini.get_driver()
        cls.daf = get_daf()
        cls.news = get_news(cls.driver)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def setUp(self):
        pass

    def test_01_check_scroll_news(self):
        """检查滚动新闻是否正常跳转"""
        self.news.wait_text(self.news.b_news, '新闻')
        self.news.click(self.news.b_news)
        self.news.wait_gone(self.news.b_news)
        self.news.wait((By.XPATH, '//*[text()="国内"]'), displayed=False)
        origin_handle = self.driver.current_window_handle
        title = self.news.title
        self.news.click(self.news.b_scroll_news)
        # 切换句柄，断言网页标题是否包含滚动新闻的标题
        for handle in self.driver.window_handles:
            if handle != origin_handle:
                self.driver.switch_to_window(handle)
                self.assertNotEqual(title, self.news.title)
        self.news.close()
        self.driver.switch_to.window(origin_handle)
