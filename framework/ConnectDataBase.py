import pymysql
from framework.logger import Logger
import sys
from framework.ReadConfig import ReadConfig

# create a logger instance
logger = Logger(logger="DataBase").getlog()

class ConnectDataBase:
    # 构造函数
    def __init__(self):
        db_dict = ReadConfig().get_database()
        self.host = db_dict['host']
        self.user = db_dict['user']
        self.pwd = db_dict['password']
        self.db = db_dict['database']
        self.port = int(db_dict['port'])
        self.conn = None
        self.cur = None

    # 连接数据库
    def connect(self):
        try:
            self.conn = pymysql.connect(self.host, self.user,
                                        self.pwd, port=self.port, charset='utf8')
            logger.info("成功连接数据库！")
        except Exception as e:
            logger.error(e)
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
            logger.info("成功结束数据库连接！")
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None):
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql, params)
                self.conn.commit()
                logger.info("execute sql successed : >>>{}<<< \nparams : >>>{}<<<".format(sql,params))
        except Exception as e:
            logger.error("execute sql failed : >>>{}<<< \nparams : >>>{}<<<".format(sql,params))
            logger.error(e)
            return False
        return True

    # 用来查询多条数据
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.cur.fetchall()

    # 用来查询单条数据
    def fetchone(self, sql, params=None):
        self.execute(sql, params)
        return self.cur.fetchone()


