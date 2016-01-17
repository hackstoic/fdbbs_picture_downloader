# encoding=utf8
import os
import sys
import re

# set django env
paths = [
    "/root/project/fdbbs_picture_downloader",
    "/opt/proj/django/fdbbs_picture_downloader",
]   # Fixme, change hard code
for path in paths:
    if path not in sys.path:
        sys.path.append(path)
os.environ["DJANGO_SETTINGS_MODULE"] = 'mysite.settings'

from myapp import downloader, parser, urlmanager, filemanager


class Crawler(object):
    def __init__(self, start_url):
        self.start_url = start_url
        self.PicMgrObj = filemanager.PicMgr()

    def crawl(self):
        """
            使用递归，需要解决最大递归深度的问题
            RuntimeError: maximum recursion depth exceeded while calling a Python object
        """
        print "start crawling url: %s" % self.start_url
        raw_html_data = downloader.read_page(url=self.start_url)
        if not raw_html_data:
            return 1
        urlmanager.update_url(url=self.start_url, status=1)
        pic_links = parser.get_pic_link(raw_html_data)
        next_link = parser.get_next_link(raw_html_data)
        for pic_link in pic_links:
            print "get picture link: %s" % pic_link
            self.PicMgrObj.download_picture(pic_link)
            file_name, postfix = self.PicMgrObj.extract_pic_name(pic_link)
            desc = "查看描述请前往：%s" % self.start_url
            self.PicMgrObj.save_desc(file_name=file_name, desc=desc)
        urlmanager.update_url(url=next_link)
        non_visited_urls = urlmanager.get_non_visited_urls()
        while non_visited_urls:  # 只要有没被访问过的url， 就一直递归爬取下去
            for url in non_visited_urls:
                self.start_url = url
                self.crawl()
        return 0


def crawl_task(start_url):
    CL = Crawler(start_url)
    CL.crawl()




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "please input a start url of bbs to crawl"
    else:
        crawl_task(sys.argv[1])