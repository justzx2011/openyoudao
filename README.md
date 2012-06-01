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
        
        $git clone git@github.com:justzx2011/youdao.git
         
        $cd youdao
        
        $python youdao.py
        
TODO
--------------
        1 增强与其它程序的兼容性
        2 重新规划目录、打包
        3 重新格式化网页界面 ----- 使用beautiful soup 
        4 创建配置页面 
DONE
-----  
        1 Fixed   -------   解决了字符串问题，实现了特殊字符的正确提取 2012-05-30 
        2 Fixed   -------   解决了权限问题，可以用普通用户运行程序 2012-05-29
        3 功能模块划分完成   -------   成功的将界面和程序高度分离
        4 主程序结构设计完成   ------  一般情况下结构不会变更
        5 完成了程序退出机制  ------  全局统一退出标志，为差错控制模块预留了接口
UPDATES
--------------
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
