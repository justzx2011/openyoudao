# YouDao

        It is a YouDao client for linux.

         Video:  http://v.youku.com/v_show/id_XNDAzMDUxNDk2.html
                 ftp://linux.xidian.edu.cn/xdlinux/youdao.mp4
         Author: justzx2011@gmail.com  @justzx
                 lvzongting@gmail.com  @lvzongting
         Powered by xdlinux.info  西电开源社区 
        

#Dependencies:
        python-xlib python-webkit xclip
#Installation
        #apt-get install python-xlib python-webkit xclip
        
        $git clone git://github.com/justzx2011/openyoudao.git
         
        $cd youdao
        
        $python youdao.py
        
TODO
--------------
        1 重新设计软件界面
        2 增强与其它程序的兼容性
        3 重新规划目录、打包
        4 重新格式化网页界面 ----- 使用beautiful soup 
        5 创建配置页面
        6 去除滚动条，改用js
        7 编写config.html,作为配置页,用作主页,用js
        8 浏览器侧边加方形标签，用于切换
DONE
-----  
        2012-6-6   -------   对网页进行了简单重构
        2012-6-1   -------   增加了滚动条
        2012-5-31  -------   解决了字符串问题，实现了特殊字符的正确提取 2012-05-30 
        2012-5-30  -------   解决了权限问题，可以用普通用户运行程序 2012-05-29
        2012-5-28  -------   成功的将界面和程序高度分离
        2012-5-27  -------   主程序结构设计完成，一般情况下结构不会变更
        2012-5-26  -------   完成了程序退出机制，全局统一退出标志，为差错控制模块预留了接口
UPDATES
--------------
        2012-6-6  重构了界面

        2012-6-4  对网页进行了重构,修改了css，网页交由bainizhao更新维护

        2012-6-1  增加了滚动条
        
        2012-5-31 给项目主页添加了域名,地址:http://openyoudao.org/    
    
        2012-5-30 修正了一些Bug,项目可以正常使用,正式命名为openyoudao

        2012-5-28 完善了项目主页,地址:http://74.117.59.126/,注册了推@openyoudao

        2012-5-27 整理代码并提交到github

        2012-5-26 实现了屏幕取词翻译，完善了程序的主框架
RULES
----
        1 界面上永远不许有按钮
        2 主程序中既是测试程序，不许有功能模块
        3 所有功能模块保持最大化的独立，尤其是界面和程序不许纠缠
        4 取词模块(xclip)、查词模块(curl)、显示模块(webkit)、聚合模块(beautiful soup)


Path & File
----
<p>├── cache

│   ├── construction

│   │   ├── body-end.txt

│   │   ├── body-start.txt

│   │   └── head.html

│   ├── css

│   │   └── result-min.css

│   ├── history.cache

│   ├── images

│   │   ├── down<em>arrow.gif

│   │   ├── scrollbar</em>handle.gif

│   │   ├── scrollbar<em>track.gif

│   │   └── up</em>arrow.gif

│   ├── js

│   │   ├── autocomplete.r156903.js

│   │   ├── extra.js

│   │   ├── jsScrollbar.js

│   │   ├── jsScroller.js

│   │   └── result-min.js

│   ├── result.html

│   └── youdao.html

├── fusion.py

├── fusion.pyc

├── README.md

├── record<em>xclip.py

├── record</em>xclip.pyc

├── ref

│   ├── browser.py

│   ├── inspector.py

│   ├── inspector.pyc

│   └── scrolledwin.py

├── web

│   ├── index.html

│   └── style.css

├── webshot.py

├── webshot.pyc

└── youdao.py</p>

Construction
----
        
                                     --------------
                                  |     主程序       |
                                  |    def main()    |
                                     --------------
                      -------------       |       ------------
                  |                       |                      |
                  |                       |                      |
             ---------------        ------------            -------------
           |     取词        |    |     查字      |    |        显示        |
           |  def gettext（）|    |  def lookup() |    |     def webshow()  |
             ---------------        -------------           --------------
