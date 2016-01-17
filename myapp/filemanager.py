# encoding=utf8

# standard libs
import re
import os
import time
from downloader import read_page


class PicMgr(object):
    def __init__(self):
        proj_dir = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        static_dir = os.path.join(proj_dir, "static")
        self.media_dir = os.path.join(static_dir, "media")  # 如果直接join(path, "media/images")这种方式，路径会有一些问题， 因为windows用的是\, *nix 用的是/
        if not os.path.exists(self.media_dir):
            os.makedirs(self.media_dir)
        else:
            pass
        self.picname_pattern = r'([0-9.-]{1,})(jpg|JPG|gif)'

    def extract_pic_name(self, url):
        match = re.search(self.picname_pattern, url, re.I)
        if match:
            file_name_with_no_postfix = match.group(1)
            file_name_with_no_postfix = file_name_with_no_postfix.strip(".")
            postfix = match.group(2)
        else:
            file_name_with_no_postfix = None
            postfix = ".jpg"
        return file_name_with_no_postfix, postfix

    def download_picture(self, url):
        """
            ----------open the picture link and download the picture then save it to disk-----------
        """
        file_name, postfix = self.extract_pic_name(url)
        if file_name is None:
            file_name = str(time.time())
        filename = file_name + postfix
        data = read_page(url)  # Fixme 此处有紧耦合的地方
        if data:
            full_path = os.path.join(self.media_dir, filename)
            f = file(full_path, "wb")
            f.write(data)
            f.close()
            print "Download picture ok !!!"
        else:
            print "no data be loading"

    def save_desc(self, file_name, desc):
        """
            保存描述文件, 目前用于图片文件的内容描述
            文件名和文件保持一致，后缀为txt, 和图片放在同一目录
            每次写入内容前，都会清空内容， 如果没有文件，则创建文件
        """
        _file_name = file_name + ".txt"
        full_path = os.path.join(self.media_dir, _file_name)
        with open(full_path, "w") as f:
            f.write(desc)
        return True

    def traverse_pictures(self):
        """
            遍历下载的图片， 返回图片名和图片描述
        """
        pic_infos = []
        for rt, dirs, files in os.walk(self.media_dir):
            for fname in files:
                pic_name_with_no_postfix, postfix = self.extract_pic_name(fname)
                if pic_name_with_no_postfix:
                    try:
                        desc_file_path = os.path.join(self.media_dir, "%s.txt" % pic_name_with_no_postfix)
                        with open(desc_file_path, "r") as fdesc:
                            desc = fdesc.read()
                    except Exception as ex:
                        desc = "null"
                    pic_infos.append({"name": fname, "desc": desc})
                else:
                    pass
        return pic_infos