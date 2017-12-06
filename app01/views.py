# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from app01 import models
from app01 import common
from django.utils.safestring import mark_safe
from app01 import page_helper
# Create your views here.
#操作数据库,进行分页
def index(request,page):
    '''
    try:
        page = int(page)
    except Exception,e:
        page = 1
    page = int(page)
    '''
    page = common.try_int(page,1)
    per_item = 5
    '''
    start = (page-1)*per_item
    end = page*per_item

    temp = divmod(count, per_item)
    if temp[1] == 0:
        all_page_count = temp[0]
    else:
        all_page_count = temp[0] + 1
    '''
    '''
    page_html = []

    #显示首页
    first_html = "<a href='/index/%d'>首页</a>" %(1,)
    page_html.append(first_html)

    #显示上一页
    if page <= 1:
        prv_html = "<a href='#'>上一页</a>"
    else:
        prv_html = "<a href='/index/%d'>上一页</a>" %(page-1,)
    page_html.append(prv_html)

    #显示每一个分页的页数
    for i in range(all_page_count):
        if page == i+1:
            a_html = "<a class='selected' href='/index/%d'>%d</a>" % (i + 1, i + 1)
        else:
            a_html = "<a href='/index/%d'>%d</a>" % (i + 1, i + 1)
        page_html.append(a_html)

    #显示下一页
    next_html = "<a href='/index/%d'>下一页</a>" %(page+1,)
    page_html.append(next_html)

    #显示尾页
    end_html = "<a href='/index/%d'>尾页</a>" %(all_page_count)
    page_html.append(end_html)

    page = mark_safe(''.join(page_html))
    '''
    count = models.Host.objects.all().count()
    # count = models.Host.objects.all().count()
    # result = models.Host.objects.all()
    pageobj = page_helper.PageInfo(page,count,20)

    result = models.Host.objects.all()[pageobj.start:pageobj.end]

    page_string = page_helper.page(page,pageobj.all_page_count)
    ret = {'data':result,'count':count,'page':page_string}
    return render_to_response('index.html',ret)

