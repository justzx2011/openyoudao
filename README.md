# YouDao

        It is a YouDao client for linux.

         Video:  http://v.youku.com/v_show/id_XNDAzMDUxNDk2.html
                 ftp://linux.xidian.edu.cn/xdlinux/youdao.mp4
         Author: justzx2011@gmail.com  @justzx
                 lvzongting@gmail.com  @lvzongting
         Powered by xdlinux.info  西电开源社区 
        

#Dependencies:
        python-xlib python-webkit python-requests python-lxml xclip inotify-tools
#Installation
        #apt-get install python-xlib python-webkit python-requests python-lxml xclip inotify-tools
        
        $git clone git://github.com/justzx2011/openyoudao.git
         
        $打开主菜单，新建项目：
         
         程序名称：openyoudao
         
         命令：python2.7 ~/workplace/openyoudao/youdao.py

         icon：~/workplace/openyoudao/cache/images/icon/icon.jpg

         注释：youdao client for linux
        
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
        9 推入软件源
        10 完善项目主页
        11 增加项目日志
DONE
-----  
        2012-7-11  -------   编写了openyoudao.desktop
        2012-7-10  -------   kokdemo重新设计了项目主页
        2012-7-01  -------   完善了README.md，更新了网页，发布Alpha
        2012-6-30  -------   增加了程序图标，调整了相对路径，清理了github分支
        2012-6-29  -------   改进了webshot
        2012-6-26  -------   修复了icb，解决了css冲突
        2012-6-25  -------   调整了线程的开启顺序,清空剪切板，清空管道
        2012-6-22  -------   通过inotify取词
        2012-6-20  -------   改用lxml加速下载，实现了字典的流畅切换，去除搜索框
        2012-6-18  -------   加速了页面重构
        2012-6-15  -------   从localStorage动态载入配置文件
        2012-6-11  -------   添加了侧边栏,通过localStorage.content存储配置信息
        2012-6-10  -------   调整了程序目录，添加了程序启动页面
        2012-6-9   -------   修复链接，解决了超长字符串替换问题，用js重写了滚动条
        2012-6-7   -------   增加了程序健壮性
        2012-6-6   -------   对网页进行了简单重构
        2012-6-1   -------   增加了滚动条
        2012-5-31  -------   解决了字符串问题，实现了特殊字符的正确提取 
        2012-5-30  -------   解决了权限问题，可以用普通用户运行程序 
        2012-5-28  -------   成功的将界面和程序高度分离
        2012-5-27  -------   主程序结构设计完成，一般情况下结构不会变更
        2012-5-26  -------   完成了程序退出机制，全局统一退出标志，为差错控制模块预留了接口
UPDATES
--------------
        2012-7-01  发布Alpha
        2012-6-10  增加了侧边栏
        2012-6-9  增加了滚动条
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
        .
        ├── cache
        │   ├── config.html
        │   ├── construction
        │   │   ├── icb
        │   │   │   ├── body-end.txt
        │   │   │   ├── body-start.txt
        │   │   │   └── head.html
        │   │   └── youdao
        │   │       ├── body-end.txt
        │   │       ├── body-start.txt
        │   │       └── head.html
        │   ├── css
        │   │   ├── blue-glass
        │   │   │   ├── inject-bottom.png
        │   │   │   ├── inject-left.png
        │   │   │   ├── inject-right.png
        │   │   │   ├── inject-top.png
        │   │   │   └── sidebar.css
        │   │   ├── dark-glass
        │   │   │   ├── inject-bottom.png
        │   │   │   ├── inject-left.png
        │   │   │   ├── inject-right.png
        │   │   │   ├── inject-top.png
        │   │   │   └── sidebar.css
        │   │   ├── red-glass
        │   │   │   ├── inject-bottom.png
        │   │   │   ├── inject-left.png
        │   │   │   ├── inject-right.png
        │   │   │   ├── inject-top.png
        │   │   │   └── sidebar.css
        │   │   ├── result-min.css
        │   │   └── style_result.css
        │   ├── images
        │   │   ├── bg_more2.png
        │   │   ├── blog_background.jpg
        │   │   ├── down_arrow.gif
        │   │   ├── icon
        │   │   │   └── icon.jpg
        │   │   ├── ok.png
        │   │   ├── scrollbar_handle.gif
        │   │   ├── scrollbar_track.gif
        │   │   └── up_arrow.gif
        │   └── js
        │       ├── autocomplete.r156903.js
        │       ├── extra.js
        │       ├── huaci.js
        │       ├── icibatop.js
        │       ├── jquery.min.js
        │       ├── jquery.sidebar.js
        │       ├── jquery-ui.min.js
        │       ├── jsScrollbar.js
        │       ├── jsScroller.js
        │       ├── jsScrollerTween.js
        │       └── result-min.js
        ├── fusionicb.py
        ├── fusionyoudao.py
        ├── gl.py
        ├── README.md
        ├── record_xclip.py
        ├── ref
        │   ├── browser.py
        │   ├── inspector.py
        │   └── scrolledwin.py
        ├── test
        ├── web
        │   ├── index.html
        │   └── style.css
        ├── webshot.py
        └── youdao.py
        
        13 directories, 56 files

Construction
----
        
                                               --------------
                                            |     主程序       |
                                            |    def main()    |
                                               ---------------
                      -------------       |    ---------------   |     --------------   |
                  |                       |                      |                      |
                  |                       |                      |                      |
             ---------------        ------------            -------------        ---------------
           |     取词        |    |     查字       |    |        显示         |       配置文件       |
           |  def gettext（）|    |  def lookup() |    |     def webshow()  |      loadconfig()     |
             ---------------        -------------           --------------       ----------------
