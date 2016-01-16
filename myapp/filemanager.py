# encoding=utf8

# standard libs
import re
import os
import time
from downloader import read_page


def download_picture(url):
    """
        ----------open the picture link and download the picture then save it to disk-----------
    """
    _file_path = os.path.split(os.path.realpath(__file__))[0]
    file_path = os.path.join(_file_path, "media")
    file_path = os.path.join(file_path, "images")  # 如果直接join(path, "media/images")这种方式，路径会有一些问题， 因为windows用的是\, *nix 用的是/
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    else:
        pass
    try:
        match = re.search(r'[0-9.-]{1,}(jpg|JPG|gif)', url, re.I)
    except Exception :
        return
    if match:
        filename = match.group()
    else:
        filename = str(time.time()) + ".jpg"
    data = read_page(url)  # Fixme 此处有紧耦合的地方
    if data:
        full_path = os.path.join(file_path, filename)
        f = file(full_path, "wb")
        f.write(data)
        f.close()
        print "Download picture ok !!!"
    else:
        print "no data be loading"
