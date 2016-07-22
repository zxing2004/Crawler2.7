# Crawler2.7

* 最近学习了一下Python，其中的使用python爬虫，是我比较感兴趣的，所有就在网上查了一些资料来实现一个简单的爬虫。
* 这里的需求是：我们爬取百度百科关于Python的词条1000条，我们将提取词条的标题，简介等基本信息并写入到html文件中。

###大致我们需要四个步骤：

1. url管理器：对我们爬取的url进行统一管理，保障不重复爬取。 
2. html下载器：负责下载我们的对应url的html文件内容。 
3. html解析器：负责将我们下载的html进行解析，提取新的url，并提取该html的内容。 
4. html输出器：就是将我们收集的内容整体输出到一个html文件中，用于展示。

	我们这里使用的第三方库的beautifulsoup4来解析html，使用前请先安装（ pip install beautifulsoup4），详情参考：
	[beautifulsoup官网](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
		  


明白了大致的需求我们就来实现这给例子：
---- 
这里我们采用整体到局部的写代码方式，我们先创建我们需要的4个模块:

* url_manager.py, 
* html_downloader.py, 
* html_parser.py, 
* html_outputer.py
 
当然我们还需要一个入口模块:crawler.py