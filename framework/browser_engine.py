# -*- coding:utf-8 -*-

import os.path
from framework.ReadConfig import ReadConfig
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    def __init__(self, driver):
        self.driver = driver
        self.dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # 注意相对路径获取方法
        # windows的驱动程序后缀有exe
        # self.chrome_driver_path = self.dir + '/tools/chromedriver.exe'
        # mac的驱动程序后缀无exe
        self.chrome_driver_path = self.dir + '/tools/chromedriver'

    def open_browser(self, driver):
        # 读取配置
        config = ReadConfig()
        browser = config.get_browser_type()
        url = config.get_test_server()
        implicitly_wait = config.get_browser_attribute()

        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        # driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(implicitly_wait)
        logger.info("Set implicitly wait %s seconds."%str(implicitly_wait))
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()