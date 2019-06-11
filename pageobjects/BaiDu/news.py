from framework.base_page import BasePage
import unittest
from selenium.webdriver.common.by import By

class NewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        '''
        **********************************************百度新闻首页**************************************
        '''

        self.i_search = (By.ID, 'ww')  # 搜索框
        self.b_search = (By.ID, 's_btn_wr')  # 搜索按钮
        self.b_scroll_news = (By.ID, 'imgView')  # 首页的滚动新闻
        self.b_scroll_news_title = (By.ID, 'imgTitle')  # 首页的滚动新闻的标题
        # self.b_news_all_tab = (By.XPATH, '//*[@id="channel-all"]//*[@class="lavalamp-item"]/a')  # 新闻首页的导航条所有按钮


        # 其他页面元素
        self.b_news = (By.LINK_TEXT, '新闻')  # 新闻按钮