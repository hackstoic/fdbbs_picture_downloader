from django.test import TestCase
import sys
import datetime


# Create your tests here.
from downloader import read_page
from myapp.parser import get_pic_link, get_next_link
from myapp.filemanager import download_picture
from myapp.db_operation import ShelveOperation
from myapp.urlmanager import update_url, get_non_visited_urls


class CrawlerExample(object):
    url = "http://bbs.fudan.edu.cn/bbs/tcon?new=1&bid=120&f=3046325721854116981"

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
        url = "http://bbs.fudan.edu.cn/upload/Single/1452601277-2498.jpg"
        res = download_picture(url)
        print res
        return res

    def test_shelve_operation(self):
        with ShelveOperation() as S:
            res = S.update_db("y", {"url": "xxxx", "status": 1, "last_update": datetime.datetime.now()})
            res = S.get_value_by_key("y")
            res = S.get_all_values()
            res = S.reset_db()
            print res

    def test_update_url(self):
        url = "http://bbs.fudan.edu.cn/bbs/tcon?new=1&bid=120&f=3046325721854116981"
        status = 0
        res = update_url(url, status)
        print res

    def test_get_non_visited_urls(self):
        res = get_non_visited_urls()
        print res


def main():
    C = CrawlerExample()
    # C.test_read_page()
    # C.test_get_pic_link()
    # C.test_get_next_link()
    # C.test_download_picture()
    C.test_shelve_operation()
    # C.test_update_url()
    # C.test_get_non_visited_urls()
    return True

if __name__ == "__main__":
    sys.exit(main())