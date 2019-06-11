# web UI 自动化测试框架（基于selenium）
## 框架简介 ##
基于python语言对selnium做的二次封装，主要有以下特点：  
1.采用了主流的po模式  
2.实现了日志的记录与输出  
3.美观的测试报告输出  
4.灵活的测试用例获取  
5.数据库连接  
6.基础信息配置  
7.整合了大部分常用的方法进行了封装，尤其如find_element，click，send_keys等方法进行了高度封装，实现了智能等待  
8.代码不冗余，复用率高  

## 适合人群  ##
1.web自动化小白：帮助其迅速了解web自动化，并上手初步的自动化项目。  
2.测试老司机：节省自己编写框架的时间，直接可用，省时省力，老少皆宜。  

## 如何开始  ##
1.安装必要的环境，诸如python3+,selenium  
2.下载合适的浏览器驱动，并放置在/tools文件夹下  
[Chrome](http://chromedriver.storage.googleapis.com/index.html) [Firefox](https://github.com/mozilla/geckodriver/releases) [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  
3.使用终端进入项目根目录，运行以下命令  
python TestRunner.py  

## 框架目录构造： ##

- **[config](https://github.com/RongXiaoCong/WebUI-Automation-Frame/tree/master/config)：**
    - *[config.ini](https://github.com/RongXiaoCong/WebUI-Automation-Frame/blob/master/config/config.ini)*：浏览器,url的基础配置，及一些基本不需要更改的账号信息

- **[framwork](https://github.com/RongXiaoCong/WebUI-Automation-Frame/tree/master/framework)：**
	- *[logger.py](https://github.com/RongXiaoCong/WebUI-Automation-Frame/blob/master/framework/logger.py)*：封装了日志输入，包括文件输出和控制台的输出
	- *[base_page](https://github.com/RongXiaoCong/WebUI-Automation-Frame/blob/master/framework/base_page.py)*:封装了selenium库中常用的方法，包括定位，点击，输入，是否存在，等待等，是耗费了最多心力的类，本项目精华所在...
	- *[browser_engine](https://github.com/RongXiaoCong/WebUI-Automation-Frame/blob/master/framework/browser_engine.py)*:通过读取配置文件去选择浏览器和url，并返回浏览器对象实例
    - *[ConnectDataBase](https://github.com/RongXiaoCong/WebUI-Automation-Frame/blob/master/framework/ConnectDataBase.py)*:封装了数据库的简单操作
    - *[case_strategy](https://github.com/RongXiaoCong/WebUI-Automation-Frame/blob/master/framework/case_strategy.py)*:封装了数据库的简单操作

- **[logs](https://github.com/RongXiaoCong/WebUI-Automation-Frame/tree/master/logs)：**
接收日志文件的输出

- **[pageobjects](https://github.com/RongXiaoCong/WebUI-Automation-Frame/tree/master/pageobjects):**
用于封装页面对象

- **[test_report](https://github.com/RongXiaoCong/WebUI-Automation-Frame/tree/master/test_report)：**
测试报告的输出文件夹

- **[testsuites](https://github.com/RongXiaoCong/WebUI-Automation-Frame/tree/master/test_suites)：**
用于测试用例的存放和测试用例集合

- **[tools](https://github.com/RongXiaoCong/WebUI-Automation-Frame/tree/master/tools)：**
存放浏览器驱动

  
  
本项目最初参考了https://github.com/StrawberryFlavor/Selenium-Framework 的目录结构，有兴趣小伙伴的可以移步

有任何建议和疑问请提issue，佛系回复。
