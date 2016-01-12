from django.test import TestCase
import sys

# Create your tests here.
from downloader import read_page
from myapp.parser import get_pic_link, get_next_link
from myapp.filemanager import download_picture


class CrawlerExample(object):
    url = "http://bbs.fudan.edu.cn/bbs/tcon?new=1&bid=120&f=3044979147674748061"

    def test_read_page(self):
        res = read_page(self.url)
        print res
        return res

    def test_get_pic_link(self):
        rawdata = read_page(self.url)
        res = get_pic_link(rawdata)
        print res
        return res

    def test_get_next_link(self):
        rawdata = read_page(self.url)
        res = get_next_link(rawdata)
        print res
        return res

    def test_download_picture(self):
        url = "http://bbs.fudan.edu.cn/upload/Single/1451959150-0446.jpg"
        res = download_picture(url)
        print res
        return res


def main():
    C = CrawlerExample()
    C.test_read_page()
    C.test_get_pic_link()
    C.test_get_next_link()
    C.test_download_picture()

if __name__ == "__main__":
    sys.exit(main())