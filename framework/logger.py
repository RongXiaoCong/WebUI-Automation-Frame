# _*_ coding: utf-8 _*_
import logging
import os
import time


class Logger(object):
    def __init__(self, logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'logs')

        now_2d = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        now_2s = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        dir_path = os.path.join(self.path , now_2d)
        # 判断文件夹是否存在，不存在则创建
        if os.path.isdir(dir_path):
            pass
        else:
            os.makedirs(dir_path)

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 由于需要多次创建logger对象，所以有较低概率会产生1个以上的日志文件，此处进行一次修正
        try:
            last_log_name = os.listdir(dir_path)[-1]
            last_log_timestamp = time.mktime(time.strptime(last_log_name[:last_log_name.find('.')], "%Y-%m-%d_%H_%M_%S"))
            now_log_timestamp = time.mktime(time.strptime(now_2s, "%Y-%m-%d_%H_%M_%S"))
            if now_log_timestamp - last_log_timestamp < 2:
                # 创建一个handler，用于写入日志文件
                log_name = dir_path + '/' + last_log_name
            else:
                log_name = dir_path + '/' + now_2s + '.log'
        except IndexError:
            log_name = dir_path + '/' + now_2s + '.log'

        fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

