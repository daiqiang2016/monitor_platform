from django.shortcuts import render
# -*- coding: utf-8 -*-
import os
import sys
import time
import datetime
import pyUsage
import pyIO
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.core.cache import cache
from django.shortcuts import render,render_to_response
#from babyguard.request_check import *
from urllib.parse import unquote
import json
#import tencentyun
from babyguard.food.forms import *
from babyguard.food.models import *
from babyguard.helper import JsonResponse
from babyguard.helper import pack_json_resp, objs2dict_list, update_all_fields
from babyguard.helper import get_md5

g_comment_fields=[e.name for e in CommentModel().fields]
g_eating_fields=[e.name for e in EatingModel().fields]
g_food_fields = [e.name for e in FoodModel().fields]
    
def append_food(food_id, day, breakfast, lunch, dinner):
    e = FoodModel(
          food_id = food_id,
          day = day,
          breakfast = breakfast,
          lunch = lunch, 
          dinner = dinner)
    ret = e.save()
    #print pyUsage.get_cur_info(), 'ret= ', ret
    resp = pack_json_resp(ret, 'append_food err', -1)
    return resp

@csrf_exempt
def reset_all_food(request):
    e_list = FoodModel.objects.all()
    for e in e_list:
        e.delete()

    #f = '/data/babyguard/babyguard/babyguard/food/all_food.txt'
    f = os.path.split(os.path.realpath(__file__))[0] + '/all_food.txt'
    t_list = pyIO.read_file_content(f, 'utf-8')
    for t in t_list:
        #print pyUsage.get_cur_info(), 't= ', t
        t = t.strip()
        if t.find('http://') == -1:
            continue

        arr = t.split('\t')
        if len(arr) < 4:
            continue
        
        arr = t.split('\t')
        food_id = arr[0]
        title = arr[1]
        type = arr[2]
        url = arr[3]
        day = ''
        ret = append_food(food_id, day, url, title, type)       
        #print pyUsage.get_cur_info(), 'add ret= ', ret

    objs = FoodModel.objects.all()
    #print pyUsage.get_cur_info(), 'cnt= ', len(objs)
    food_list = objs2dict_list(objs, g_food_fields)
    #print pyUsage.get_cur_info(), 'cnt= ', len(food_list)

    return JsonResponse(
            {
                'status': 'reset food',
                'status_code':0,
                'cnt':len(food_list),
                'food_list':food_list,
             })
    #print pyUsage.get_cur_info(), 'add ret= ', ret

@csrf_exempt
def add_food(request):
    form = FoodForm()
    food_list = []
    if request.method == 'POST':
        food_id = request.POST.get('food_id','')
        day = request.POST.get('day','')
        breakfast = request.POST.get('breakfast','')
        lunch = request.POST.get('lunch','')
        dinner = request.POST.get('dinner','')

        return append_food(food_id, day, breakfast, lunch, dinner)
    else:
        form = FoodForm(
            initial={
                    'food_id':1,
                    'day':'20160515',
                    'breakfast':'稀饭',
                    'lunch':'西红柿鸡蛋',
                    'dinner':"白菜炒肉",
                  }
              )

    objs = FoodModel.objects.all()
    food_list = objs2dict_list(objs, g_food_fields)
    #print pyUsage.get_cur_info(), 'food_list= ', food_list
    return render_to_response('add_food.html', {'form': form, 'food_list':food_list})      

@csrf_exempt
def get_food(request):
    objs = FoodModel.objects.all()
    food_list = objs2dict_list(objs, g_food_fields)
    ###append comment
    for i,v in enumerate(food_list):
        vid = v['food_id']
        comments = CommentModel.objects.filter(food_id=vid)
        if len(comments) > 0:
            #print pyUsage.get_cur_info(), 'g_comment_fields= ', g_comment_fields
            c_dict = objs2dict_list(comments, g_comment_fields)
            food_list[i]['comment'] = c_dict

    return JsonResponse(
            {
                'status': 'success',
                'status_code':0,
                'cnt': len(food_list),
                'food_list':food_list,
            })

@csrf_exempt
def del_food(request):
    food_id = request.POST.get('food_id','')
    if len(food_id) == 0:
        food_id = request.GET.get('food_id','')
    if len(food_id) == 0:
        return HttpResponse('empty food_id')
    
    e_list = FoodModel.objects.filter(food_id = food_id)
    if len(e_list) == 0:
        return HttpResponse('food_id:%s not exists'%food_id)

    assert(len(e_list) == 1)    
    e_list[0].delete()
    e_list = FoodModel.objects.filter(food_id = food_id)
    flag = True if len(e_list) == 0 else False
    return pack_json_resp(flag, 'del_food error', -1)

@csrf_exempt
def add_comment(request):
    form = []
    if request.method == 'POST':
        food_id = request.POST.get('food_id','')
        comment = request.POST.get('comment', '')
        username = request.POST.get('username')
        if len(username) == 0:
            return pack_json_resp(False, '[%s]not exists'%username, -1)
        if len(comment) == 0:
            return pack_json_resp(False, 'comment is empty', -1)
        objs = FoodModel.objects.filter(food_id=food_id)
        if len(objs) != 1:
            return pack_json_resp(False, '[%s]food id not exits'%food_id, -1)

        c = CommentModel(
                food_id = food_id, 
                comment = comment, 
                username = username)
        ret = c.save()
        #print pyUsage.get_cur_info(), 'ret= ', ret
        return pack_json_resp(ret, 'add_comment error', -1)
    else:
        pass
    form = CommentForm(
            initial={
                'username':'18684016495',
                'food_id':'14651978969257216923',
                'comment':'good film',
            }
    )
    return render_to_response('comment_food.html', {'form':form})

@csrf_exempt
def update_food(request):
    form = []
    if request.method == 'POST':
        food_id = request.POST.get('food_id','')
        if len(food_id) == 0:
            food_id = request.GET.get('food_id','')
        if len(food_id) == 0:
            return pack_json_resp(False, 'empty food_id', -1)
        
        e_list = FoodModel.objects.filter(food_id = food_id)
        if len(e_list) == 0:
            return HttpResponse('food_id:%s not exists'%food_id)
        e_list = FoodModel.objects.filter(food_id = food_id)    
        #print pyUsage.get_cur_info(), 'len= ', len(e_list)
        assert(len(e_list) == 1)    

        e = e_list[0]
        ret = update_all_fields(e, g_food_fields, request.POST)
        e_list = FoodModel.objects.filter(food_id = food_id)
        assert(len(e_list) == 1)

        return pack_json_resp(ret, 'update_food error', -1)
    else:
        pass
    form = FoodForm(
        initial={
                'breakfast':1,
                'lunch':1,
                'dinner':"title",
              }
          )
    return render_to_response('add_food.html', {'form': form})
