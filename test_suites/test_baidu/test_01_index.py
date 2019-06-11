# coding=utf-8
import time
import unittest
from framework.logger import Logger
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from framework.ConnectDataBase import ConnectDataBase
from framework.ReadConfig import ReadConfig
from test_suites.test_baidu import *

logger = Logger(logger="Baidu > Index").getlog()

class Index(unittest.TestCase):
    """首页测试"""
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        ini = to_init()
        cls.driver = ini.get_driver()
        cls.daf = get_daf()
        cls.bd = get_bd(cls.driver)
        cls.user_info = ini.user_info
        cls.search_info = ini.search_info

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def setUp(self):
        pass

    def test_01_search(self):
        """搜索"""
        self.bd.send_keys(self.bd.i_search, self.search_info['1'])
        self.bd.click(self.bd.b_search)
        # 验证是否成功搜索到搜索结果的元素
        self.assertTrue(self.bd.wait(self.bd.t_search_result))

    def test_02_search_retry(self):
        """重新搜索"""
        title_1 = [element.text for element in self.bd.find_element(self.bd.b_result_title, None, displayed=False)]
        logger.info(title_1)
        self.bd.send_keys(self.bd.i_search, self.search_info['2'])
        self.bd.click(self.bd.b_search)
        self.bd.wait_text_gone(self.bd.b_result_title, title_1, None, displayed=False)
        title_2 = [element.text for element in self.bd.find_element(self.bd.b_result_title, None, displayed=False)]
        logger.info(title_2)


