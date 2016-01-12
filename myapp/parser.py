# encoding=utf8

import re
import xml.etree.cElementTree as ET
import bs4


def get_pic_link(rawdata):
    """
        using Beautifulsoup to parse rawdata and get the picture link
        -----extract the picture link from the web source code-----
    """
    content = bs4.BeautifulSoup(rawdata, from_encoding='GB18030')
    picture_link_list = []
    hyperlinks = content.findAll(href=re.compile(r'http://bbs.fudan.edu.cn/[/a-zA-Z0-9-.]{1,}(jpg|JPG)'))
    for link in hyperlinks:
        picture_link_list.append(link['href'])
    return picture_link_list


def get_next_link(rawdata):
    """
        using the xml.elementtree to parse the rawdata and get the next link
    """
    content = unicode(rawdata, "cp936").encode("utf-8")
    ori_xml_head = '''<?xml version="1.0" encoding="gb18030"?>'''
    new_xml_head = '''<?xml version="1.0" encoding="utf-8"?>'''
    content = content.replace(ori_xml_head, new_xml_head)
    root = ET.fromstring(content)
    frame = root.attrib['gid']
    next_link = 'http://bbs.fudan.edu.cn/bbs/tcon?new=1&bid=120&f=' + str(frame) + '&a=b'
    return next_link