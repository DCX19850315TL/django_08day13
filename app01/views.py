# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from app01 import models
from app01 import common
from django.utils.safestring import mark_safe
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
    start = (page-1)*per_item
    end = page*per_item
    #count = models.Host.objects.all().count()
    #result = models.Host.objects.all()
    count = models.Host.objects.all().count()
    result = models.Host.objects.all()[start:end]

    temp = divmod(count,per_item)
    if temp[1] == 0:
        all_page_count = temp[0]
    else:
        all_page_count = temp[0] + 1

    page_html = []

    for i in range(all_page_count):
        a_html = "<a href='/index/%d'>%d</a>" %(i+1,i+1)
        page_html.append(a_html)

    page = mark_safe(''.join(page_html))

    ret = {'data':result,'count':count,'page':page}
    return render_to_response('index.html',ret)

