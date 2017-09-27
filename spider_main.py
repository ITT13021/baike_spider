# coding=utf-8
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager


class SpriderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, count):
        i = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            if count != 0:
                try:
                    new_url = self.urls.get_new_url()
                    print 'we are collecting in %d : %s' % (i, new_url)
                    html_cont = self.downloader.download(new_url)
                    new_urls, new_data = self.parser.parse(new_url, html_cont)
                    self.urls.add_new_urls(new_urls)
                    self.outputer.collect_data(new_data)
                except:
                    print "collected failed in %d" % i
                i += 1
                count -= 1
            else:
                break

        self.outputer.output_html()


if __name__ == "__main__":
    obj_spider = SpriderMain()
    root_url = raw_input("请输入您要爬取首个百度百科词条的页面，我们会搜索与其相关的词条,例如：https://baike.baidu.com/item/Python：" + "\n")
    count = input("请输入您要爬取词条的个数（爬取越多消耗时间越长哦！）: ")
    obj_spider.craw(root_url, count)
