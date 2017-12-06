#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: page_helper.py
@time: 2017/12/6 11:19
'''
from django.utils.safestring import mark_safe

class PageInfo:

    def __init__(self,current_page,all_count,per_item=5):
        self.CurrentPage = current_page
        self.AllCount = all_count
        self.PerItem = per_item
    @property
    def start(self):
        #start = (page-1)*per_item
        return (self.CurrentPage - 1)*self.PerItem
    @property
    def end(self):
        #end = page*per_item
        return self.CurrentPage*self.PerItem
    @property
    def all_page_count(self):
        '''
        temp = divmod(count, per_item)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1
        '''
        temp = divmod(self.AllCount, self.PerItem)
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1
        return all_page_count

def page(page,all_page_count):

    page_html = []

    # 显示首页
    first_html = "<a href='/index/%d'>首页</a>" % (1,)
    page_html.append(first_html)

    # 显示上一页
    if page <= 1:
        prv_html = "<a href='#'>上一页</a>"
    else:
        prv_html = "<a href='/index/%d'>上一页</a>" % (page - 1,)
    page_html.append(prv_html)

    #11个页码
    if all_page_count < 11:
        begin = 0
        end = all_page_count
    #总页数大于11
    else:
        if page < 6:
            begin = 0
            end = 11
        else:
            if page + 5 > all_page_count:
                begin = page - 6
                end = all_page_count
            else:
                begin = page -6
                end = page + 5


    # 显示每一个分页的页数
    for i in range(begin,end):
        if page == i + 1:
            a_html = "<a class='selected' href='/index/%d'>%d</a>" % (i + 1, i + 1)
        else:
            a_html = "<a href='/index/%d'>%d</a>" % (i + 1, i + 1)
        page_html.append(a_html)

    # 显示下一页
    next_html = "<a href='/index/%d'>下一页</a>" % (page + 1,)
    page_html.append(next_html)

    # 显示尾页
    end_html = "<a href='/index/%d'>尾页</a>" % (all_page_count)
    page_html.append(end_html)

    page_string = mark_safe(''.join(page_html))

    return page_string