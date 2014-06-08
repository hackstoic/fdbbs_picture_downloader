#!/usr/bin/env python
# -*- coding:utf-8 -*-
#-*- coding : gb10830 -*-
#---------------------------------------
#   程序：日月光华论坛图片爬虫
#   版本：0.1
#   作者：hackme
#   日期：2014-05-11
#   语言：Python 2.7
#   操作：输入带分页的地址，去掉最后面的数字，设置一下起始页数和终点页数。
#   功能：下载对应页码内的所有页面并存储为html文件。
#   更新：解决了命令提示行下乱码的问题
#---------------------------------------

import urllib2
import re
import xml.etree.cElementTree as ET
import bs4

class  HTML_Tool:
    pass

def read_page(url):
    headers = {
        'User-Agent':'fake-client'
    }

    req = urllib2.Request(
        url=url,
        headers=headers
    )
    # req.add_header('User-Agent','fake-client')
    try:
        response  = urllib2.urlopen(req)
    except urllib2.URLError,e:
        if hasattr(e,"reason"):
            print e.reason
            return 0
        elif hasattr(e,"code"):
            print e.code
            return 0
    else:
        print 'No exception raise.\n'

    print "The code :"
    print response.getcode()
    rawdata = response.read()
#     soup = bs4.BeautifulStoneSoup(rawdata)
#     print soup.prettify()
#     content = bs4.BeautifulSoup(rawdata,from_encoding='GB18030') 
    return rawdata

def get_pic_link(rawdata): ##using Beautifulsoup to parse rawdata and get the picture link
    #-----extract the picture link from the web source code-----#
#     print data
#     pattern = re.compile('http://bbs.fudan.edu.cn/upload/Single/.*(?i)jpg')
#     picture_link_list = pattern.findall(data)
    content = bs4.BeautifulSoup(rawdata,from_encoding='GB18030') 
    picture_link_list = []    
    hyperlinks = content.findAll(href=re.compile(r'http://bbs.fudan.edu.cn/[/a-zA-Z0-9-.]{1,}(jpg|JPG)'))
    for link in hyperlinks:
        picture_link_list.append(link['href'])
        
    return picture_link_list
  
def get_next_link(rawdata): #using the xml.elementtree to parse the rawdata and get the next link
   content = unicode(rawdata,"cp936").encode("utf-8")
   content = content.replace('''<?xml version="1.0" encoding="gb18030"?>''','''<?xml version="1.0" encoding="utf-8"?>''')
   root = ET.fromstring(content)
   frame = root.attrib['gid']
   next_link = 'http://bbs.fudan.edu.cn/bbs/tcon?new=1&bid=120&f'+str(frame)+'&a=b'
   return next_link

def download(url,file_path):
    #----------open the picture link and download the picture then save it to disk-----------# 
    try:
        m = re.match(r'[0-9.-]{1,}(jpg|JPG|gif)',url)
    except Exception :
        return
    filename = str(m)
    data = read_page(url)
    full_path = file_path + filename
    f = file(full_path,"wb")
    f.write(data)
    f.close()
    print url
    print "Download picture ok !!!"


if __name__ == "__main__":
    url_start = "http://bbs.fudan.edu.cn/bbs/tcon?new=1&bid=120&f=1004778&a=b"
    file_path = "/tmp/pic/"
    data = read_page(url_start)
    print get_next_link(data)
#     soup = bs4.BeautifulStoneSoup(data)
#     print soup.prettify()
#     print get_next_link(data)
#     pic_link_list = get_pic_link(data)  
#     print pic_link_list      
#     for picurl in pic_link_list:   
#           
#         download(picurl,file_path)
#         
    
    # print data
#     match = re.compile(r'(?<=href=["]).*?(?=["])')
#     print re.findall(match, data)

#     # print content
#     root = ET.fromstring(content)
#     print root.tag ,root.attrib['gid']
#     for child in root:
#         print child.tag ,child.attrib
# 
#     for link in root.findall('a'):
#         print link
    # data =  data.decode('gb18030','replace')
    # print data

    # picture_link_list = get_link(data)
    # print picture_link_list
    #ga
    # for pic_link in picture_link_list:
    #     download(pic_link,file_path)

    # from xml.dom.minidom import parseString
    # xmldoc = parseString(data)

