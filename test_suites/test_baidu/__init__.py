import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.ReadConfig import ReadConfig
from framework.HTMLTestReportCN import DirAndFiles
from framework.ConnectDataBase import ConnectDataBase
from pageobjects.BaiDu.Index import IndexPage
from pageobjects.BaiDu.news import NewsPage


class to_init():
    def __init__(self):
        self.user_info = {"userName":"hahaha", "password":"ahahah"}
        self.search_info = {"1":"python大法好", "2":"人生苦短，我用python"}

    def get_driver(self):
        """打开网页并获取driver"""
        browser = BrowserEngine(self)
        driver = browser.open_browser(self)
        return driver

    def clean_test_data(self):
        """清理测试数据"""
        pass

def get_daf():
    """
    获取测试报告对象
    :return:
    """
    return DirAndFiles()

def get_bd(driver):
    """
    获取百度首页
    :return:
    """
    return IndexPage(driver)

def get_news(driver):
    """
    获取百度新闻页面
    :return:
    """
    return NewsPage(driver)