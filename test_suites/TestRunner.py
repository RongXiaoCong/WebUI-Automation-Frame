#_*_ coding:utf-8 _*_

import unittest
from framework import HTMLTestReportCN
from framework.ReadConfig import ReadConfig
from framework.case_strategy import CaseStrategy
from test_suites.test_baidu import to_init

class RunAllTests(object):

    def __init__(self):
        cs = CaseStrategy()
        self.test_suite = cs.collect_cases()
        self.tester = ReadConfig().get_test_account()['name']

    def run(self):
        to_init().clean_test_data()

        # 启动测试时创建文件夹并获取报告的名字
        daf = HTMLTestReportCN.DirAndFiles()
        daf.create_dir(title='百度自动化测试报告')
        report_path = HTMLTestReportCN.GlobalMsg.get_value("report_path")

        with open(report_path, "wb") as fp:
            runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title='百度自动化测试报告', description='用例执行情况：', tester=self.tester)
            runner.run(self.test_suite)

        to_init().clean_test_data()

if __name__ == "__main__":
    RunAllTests().run()

