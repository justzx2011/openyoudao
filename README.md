# YouDao

        It is a YouDao client for linux.

         Author: justzx2011@gmail.com  @justzx
                 lvzongting@gmail.com  @lvzongting
         Powered by xdlinux.info  西电开源社区 
        

#Dependencies:
        python-xlib python-webkit python-lxml  python-beautifulsoup xclip inotify-tools curl
#Installation:

#Archlinux：
        yaourt -S openyoudao
        
#Ubunte/debian:        
        Add mirrorlist:

        deb http://ppa.launchpad.net/justzx2011/openyoudao-v0.2/ubuntu trusty main 

        deb-src http://ppa.launchpad.net/justzx2011/openyoudao-v0.2/ubuntu trusty main

        sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys  14C9B91C3F9493B9

        sudo apt-get update 
         
        sudo apt-get install openyoudao
        
#其他发行版linux:
        #apt-get install python-xlib python-webkit python-lxml  python-beautifulsoup xclip inotify-tools curl
        
        $wget https://github.com/justzx2011/openyoudao/archive/beta0.2.tar.gz
        
         tar -xvf beta0.2.tar.gz && cd openyoudao-beta0.2
         
        安装bin文件，方便程序执行: 
        
        将bin文件：scripts/openyoudao安装到目录/usr/bin/openyoudao:
        
        #cp scripts/openyoudao /usr/bin/.
        
        设置权限：
        
        #chmod 755 /usr/bin/openyoudao
        
        安装libs文件: 
        
        #mkdir /usr/lib/openyoudao

        #cp ./*.py /usr/lib/openyoudao

        #chmod 644 /usr/lib/openyoudao/*.py
        
        安装cache文件:
        
        #mkdir /var/cache/openyoudao

        #cp -rf cache/* /usr/share/openyoudao/.
        
        安装desktop:
        
        #cp desktop/openyoudao.desktop /usr/share/applications/

        #chmod 644 /usr/share/applications/openyoudao.desktop

        哈哈～现在应该看到openyoudao的图标了吧～

        点击图标就能运行程序了
        
TODO
--------------
        01 重新设计软件界面
        02 增强与其它程序的兼容性
        03 重新规划目录、打包
        04 重新格式化网页界面 ----- 使用beautiful soup 
        05 创建配置页面
        06 去除滚动条，改用js
        07 编写config.html,作为配置页,用作主页,用js
        08 浏览器侧边加方形标签，用于切换
        09 推入软件源
        10 完善项目主页
        11 增加项目日志
        12 打包ppa
        13 打包rpm
        14 增加ocr取词功能
        15 编写QT版本
        16 添加离线取词功能
        17 修改取词模式添加快捷键辅助取词
        18 添加命令行查词功能
        19 编写mac版本
        20 优化项目主页，添加后台线程下载功能，加快访问速度
        21 编程多线程下载代理,提高取词速度
        22 实现程序的可脚本化 
        23 改用PyQT4Qt中Webkit
        24 捕捉程序异常，sqlite操作可能会抛出异常，特别是多线程
        25 减少global使用，太多的global 影响程序的健壮性
        26 对DOM操作，借鉴PhantomJS和CasperJS
        27 实现man手册的跳转
		28 以守护进程运行该程序
		29 脚本竞技场
		30 寻找轻量级的取词方案
		31 修复视频播放
DONE
-----  
        2014-4-16  -------   发布openyoudao v0.2版本
        2013-9-01  -------   发布openyoudao beta版本
        2012-8-23  -------   发布了ppa包
        2012-8-21  -------   修改了程序设计，将用户配置文件转移到了$HOME/.openyoudao目录下
        2012-8-17  -------   创建项目邮件列表，辅助项目测试
        2012-8-08  -------   修复了发音功能
        2012-8-07  -------   重新编写了使用教程，以兼容各个发行版linux
        2012-8-01  -------   修正了取词脚本
        2012-7-23  -------   添加程序运行过程中所需要的临时文件，以解决系统权限问题
        2012-7-22  -------   修正了desktop存在的bug
        2012-7-21  -------   考虑到python-requests存在过期依赖问题，改用curl进行网页下载
        2012-7-19  -------   将程序打包为aur
        2012-7-11  -------   编写了openyoudao.desktop
        2012-7-10  -------   kokdemo重新设计了项目主页
        2012-7-04  -------    增加了代理设置
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
        2012-6-09   -------   修复链接，解决了超长字符串替换问题，用js重写了滚动条
        2012-6-07   -------   增加了程序健壮性
        2012-6-06   -------   对网页进行了简单重构
        2012-6-01   -------   增加了滚动条
        2012-5-31  -------   解决了字符串问题，实现了特殊字符的正确提取 
        2012-5-30  -------   解决了权限问题，可以用普通用户运行程序 
        2012-5-28  -------   成功的将界面和程序高度分离
        2012-5-27  -------   主程序结构设计完成，一般情况下结构不会变更
        2012-5-26  -------   完成了程序退出机制，全局统一退出标志，为差错控制模块预留了接口
UPDATES
--------------
        2014-4-16  -------   解决了程序异常中断的bug
        2012-8-23  发布ppa
        2012-8-17  -------   创建项目邮件列表，辅助项目测试
        2012-8-08  修复了发音功能
        2012-7-19  发布aur包
        2012-7-01  发布Alpha
        2012-6-10  增加了侧边栏
        2012-6-9   增加了滚动条
        2012-6-6   重构了界面
        2012-6-4   对网页进行了重构,修改了css，网页交由bainizhao更新维护
        2012-6-1   增加了滚动条
        2012-5-31  给项目主页添加了域名,地址:http://openyoudao.org/    
        2012-5-30  修正了一些Bug,项目可以正常使用,正式命名为openyoudao
        2012-5-28  完善了项目主页,地址:http://74.117.59.126/,注册了推@openyoudao
        2012-5-27  整理代码并提交到github
        2012-5-26  实现了屏幕取词翻译，完善了程序的主框架
RULES
----
        1 界面上永远不许有按钮
        2 主程序中既是测试程序，不许有功能模块
        3 所有功能模块保持最大化的独立，尤其是界面和程序不许纠缠
        4 取词模块(xclip)、查词模块(curl)、显示模块(webkit)、聚合模块(beautiful soup)


Path & File
----
        .
        ├── cache                                 #存放页面相关的文件(html、js、图片、css)
        │   ├── config.html                       #程序启动时,默认的页面
        │   ├── construction
        │   │   ├── icb                           #icb字典重构需要的html元素
        │   │   │   ├── body-end.txt
        │   │   │   ├── body-start.txt
        │   │   │   └── head.html
        │   │   └── youdao                        #yoduao字典重构需要的html元素
        │   │       ├── body-end.txt
        │   │       ├── body-start.txt
        │   │       └── head.html
        │   ├── css                               #设计侧边栏使用的css
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
        │   ├── databases                          #用户数据库
        │   │   └── file__0.localstorage
        │   ├── images                             #页面用到的图片文件
        │   │   ├── bg_more2.png
        │   │   ├── blog_background.jpg
        │   │   ├── down_arrow.gif
        │   │   ├── icon
        │   │   │   └── icon.jpg
        │   │   ├── ok.png
        │   │   ├── scrollbar_handle.gif
        │   │   ├── scrollbar_track.gif
        │   │   └── up_arrow.gif
        │   └── js                                #页面用到的js文件
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
        ├── desktop                               #系统菜单配置文件
        │   └── openyoudao.desktop
        ├── fusionicb.py                          #icb界面重构脚本
        ├── fusionyoudao.py                       #youdao界面重构脚本
        ├── gl.py                                 #程序中用到的全局变量
        ├── README.md                             #程序的说明文档
        ├── record_xclip.py                       #屏幕取词脚本
        ├── ref                                   #供参考的源码
        │   ├── browser.py
        │   ├── inspector.py
        │   └── scrolledwin.py
        ├── scripts                               #打包aur时用到的可执行脚本
        │   └── openyoudao
        ├── web                                   #项目主页
        │   ├── css
        │   │   ├── bootstrap.css
        │   │   ├── bootstrap.min.css
        │   │   ├── loading.gif
        │   │   ├── themes
        │   │   │   ├── dark.css
        │   │   │   ├── font
        │   │   │   │   ├── AbrilFatface-Average.css
        │   │   │   │   ├── Arvo-PTSans.css
        │   │   │   │   ├── Bevan-PotanoSans.css
        │   │   │   │   ├── BreeSerif-OpenSans.css
        │   │   │   │   ├── DroidSerif-DroidSans.css
        │   │   │   │   ├── Lekton-Molengo.css
        │   │   │   │   ├── Lora-Istok.css
        │   │   │   │   ├── Merriweather-NewsCycle.css
        │   │   │   │   ├── NixieOne-Ledger.css
        │   │   │   │   ├── Pacifico-Arimo.css
        │   │   │   │   ├── PlayfairDisplay-Muli.css
        │   │   │   │   ├── PoiretOne-Molengo.css
        │   │   │   │   ├── PT.css
        │   │   │   │   ├── PTSerif-PTSans.css
        │   │   │   │   ├── Rancho-Gudea.css
        │   │   │   │   └── SansitaOne-Kameron.css
        │   │   │   ├── timeline-dark.png
        │   │   │   └── timeline-texture.png
        │   │   ├── timeline.css
        │   │   └── timeline.png
        │   ├── fork_me_on_github.png
        │   ├── img
        │   │   ├── glyphicons-halflings.png
        │   │   └── glyphicons-halflings-white.png
        │   ├── index.html
        │   ├── js
        │   │   ├── bootstrap.js
        │   │   ├── bootstrap.min.js
        │   │   ├── jquery-min.js
        │   │   ├── locale
        │   │   │   ├── cz.js
        │   │   │   ├── de.js
        │   │   │   ├── dk.js
        │   │   │   ├── en.js
        │   │   │   ├── es.js
        │   │   │   ├── fo.js
        │   │   │   ├── fr.js
        │   │   │   ├── id.js
        │   │   │   ├── is.js
        │   │   │   ├── it.js
        │   │   │   ├── ja.js
        │   │   │   ├── kr.js
        │   │   │   ├── nl.js
        │   │   │   ├── pl.js
        │   │   │   ├── pt-br.js
        │   │   │   ├── ru.js
        │   │   │   ├── zh-ch.js
        │   │   │   └── zh-tw.js
        │   │   ├── timeline-embed.js
        │   │   ├── timeline.js
        │   │   └── timeline-min.js
        │   ├── json
        │   │   |__ timeline.json
        │   ├── openyoudao.jpg
        │   └── tutorial.html
        ├── webshot.py                           #webkit组件
        └── youdao.py                            #主程序
        
        23 directories, 114 files

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
