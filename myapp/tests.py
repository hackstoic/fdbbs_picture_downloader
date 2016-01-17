from django.test import TestCase
import sys
import datetime
import os

try:
    from ipdb import set_trace
except:
    from pdb import set_trace

# set django env
paths = [
    "/root/project/fdbbs_picture_downloader",
    "/opt/proj/django/fdbbs_picture_downloader",
    ]   # Fixme, change hard code
for path in paths:
    if path not in sys.path:
        sys.path.append(path)
os.environ["DJANGO_SETTINGS_MODULE"] = 'mysite.settings'

# Create your tests here.
from myapp.downloader import read_page
from myapp.parser import get_pic_link, get_next_link
from myapp.filemanager import PicMgr
from myapp.db_operation import ShelveOperation
from myapp.urlmanager import update_url, get_non_visited_urls
from myapp.tasks import Crawler


class CrawlerExample(object):
    url = "http://bbs.fudan.edu.cn/bbs/tcon?new=1&bid=120&f=3046325721854116981"
    # url = "http://bbs.fudan.edu.cn/upload/PIC/1258019944-1631.JPG"  # page not found case

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
        res = PicMgr().download_picture(url)
        print res
        return res

    def test_shelve_operation(self):
        with ShelveOperation() as S:
            # res = S.update_db("y", {"url": "xxxx", "status": 1, "last_update": datetime.datetime.now()})
            # res = S.get_value_by_key("y")
            # res = S.get_all_values()
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

    def test_crawler_task(self):
        CL = Crawler(self.url)
        CL.crawl()
        return True

    def test_traverse_pictures(self):
        res = PicMgr().traverse_pictures()
        print res
        return res

    def test_save_desc(self):
        name = "1452601277-2498"
        desc = self.url
        res = PicMgr().save_desc(name, desc)
        return res


def main():
    print "start"
    # set_trace()
    C = CrawlerExample()
    # C.test_read_page()
    # C.test_get_pic_link()
    # C.test_get_next_link()
    # C.test_download_picture()
    # C.test_shelve_operation()
    # C.test_update_url()
    # C.test_get_non_visited_urls()
    C.test_crawler_task()
    # C.test_traverse_pictures()
    # C.test_save_desc()
    return True

if __name__ == "__main__":
    sys.exit(main())