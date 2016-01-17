#encoding=utf8
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
from filemanager import PicMgr


def index(request):
    kwds = {
        "pictures": PicMgr().traverse_pictures()
    }
    # Fixme 下一步实现lazy_loading ， 否则每次刷新页面一次性下载几张图片非常耗时
    return render_to_response("myapp/index.html", kwds, context_instance=RequestContext(request))