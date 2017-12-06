#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse

# Create your views here.
def login(request):

    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        if user == 'tanglei' and pwd == '123':
            #设置session
            request.session['is_login'] = {'user':user}
            return redirect('/app02/index/')
        else:
            return render_to_response('app02/login.html',{'msg':'用户名和密码错误'})
    return render_to_response('app02/login.html')

def index(request):
    #获取session
    user_dict = request.session.get('is_login',None)
    if user_dict:
        return render_to_response('app02/index.html',{'username':user_dict['user']})
    else:
        return redirect('/app02/login/')

def logout(request):
    #销毁session
    del request.session['is_login']
    return redirect('/app02/login/')