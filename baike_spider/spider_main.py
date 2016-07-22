#coding:utf8
import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.HtmlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        craw_conut = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s'%(craw_conut, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_url(new_urls)
                self.outputer.collect_data(new_data)
                if craw_conut == 10:
                    break
                craw_conut = craw_conut + 1
            except:
                print 'craw fail'

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)


