# encoding=utf8

# standard libs
import re
import os
import time
from myapp.downloader import read_page


def download_picture(url):
    """
        ----------open the picture link and download the picture then save it to disk-----------
    """
    file_path = os.path.split(os.path.realpath(__file__))[0]
    try:
        match = re.search(r'[0-9.-]{1,}(jpg|JPG|gif)', url, re.I)
    except Exception :
        return
    if match:
        filename = match.group()
    else:
        filename = str(time.time()) + ".jpg"
    data = read_page(url)  # Fixme 此处有紧耦合的地方
    full_path = os.path.join(file_path, filename)
    print full_path
    f = file(full_path, "wb")
    f.write(data)
    f.close()
    print url
    print "Download picture ok !!!"
