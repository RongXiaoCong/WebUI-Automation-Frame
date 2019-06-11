from framework.base_page import BasePage
import unittest
from selenium.webdriver.common.by import By

class IndexPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        '''
        **********************************************百度首页**************************************
        '''

        self.i_search = (By.ID, 'kw')  # 搜索框
        self.b_search = (By.ID, 'su')  # 搜索按钮
        self.b_news = (By.NAME, 'tj_trnews')  # 新闻按钮
        self.b_hao123 = (By.NAME, 'tj_trhao123')  # hao123按钮
        self.b_map = (By.NAME, 'tj_trmap')  # 地图按钮
        self.b_video = (By.NAME, 'tj_trvideo')  # 视频按钮
        self.b_tieba = (By.NAME, 'tj_trtieba')  # 贴吧按钮
        self.b_xueshu = (By.LINK_TEXT, '学术')  # 学术按钮
        self.b_login = (By.LINK_TEXT, '登录')  # 登录按钮
        self.b_setting = (By.LINK_TEXT, '设置')  # 设置按钮
        self.b_more_prod = (By.LINK_TEXT, '更多产品')  # 更多产品

        self.b_login_user_name = (By.XPATH, '//*[text()="用户名登录"]')  # 用户名登录按钮
        self.i_login_user_name = (By.CLASS_NAME, 'pass-text-input-userName')  # 用户名输入框
        self.i_login_password = (By.CLASS_NAME, 'pass-text-input-password')  # 密码输入框
        self.b_login_submit = (By.ID, 'TANGRAM__PSP_10__submit')  # 用户名密码登录页的登录按钮

        self.b_result_title = (By.XPATH, '//*[@id = "content_left"]//*[@class = "t"]') #搜索结果标题
        # 其他页面内容
        self.t_search_result = (By.CLASS_NAME, 'nums_text')  # 搜索结果
        self.t_hot_news = (By.XPATH, '//*[text()="热点要闻"]')  # 新闻页面醒目的“热点要闻”四个字
