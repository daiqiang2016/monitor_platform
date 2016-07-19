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
from babyguard.chart.models import *
from babyguard.chart.forms import *
from babyguard.helper import JsonResponse
from babyguard.helper import pack_json_resp, objs2dict_list, update_all_fields
from babyguard.helper import get_md5
import util_log

# Create your views here.
@csrf_exempt
def show(request):
    form = []
    if request.method == 'POST':
        #print pyUsage.get_cur_info(), 'ret= ', ret
        return pack_json_resp(True, 'show error', -1)
    else:
        pass
    return render_to_response('main_chart.html')

@csrf_exempt
def show_video(request):
    form = []
    if request.method == 'POST':
        #print pyUsage.get_cur_info(), 'ret= ', ret
        return pack_json_resp(True, 'show error', -1)
    else:
        pass
    return render_to_response('video_chart.html')

@csrf_exempt
def show_crawl(request):
    form = []
    if request.method == 'POST':
        #print pyUsage.get_cur_info(), 'ret= ', ret
        return pack_json_resp(True, 'show error', -1)
    else:
        pass
    get_crawl_chart(None)    
    return render_to_response('crawl_chart.html')

def get_sorted_list(objs, desc, days):
    res_list = []
    dict_crawl = {}
    for day in days:
        dict_crawl[day] = 0

    sum_list = [(e.day, e.cnt) for e in objs if e.desc == desc]
    for day,cnt in sum_list:
        dict_crawl[day] += int(cnt)

    for d,c in dict_crawl.items():
        res_list.append((d,c))
    res_list.sort()
    return res_list

@csrf_exempt
def get_crawl_chart(request):
    objs = CrawlModel.objects.all()
    descs = [e.desc for e in objs]
    descs = [e[:16] for e in descs]
    descs = list(set(descs))

    days = [e.day for e in objs]
    days = list(set(days))
    days.sort()

    series = []
    for desc in descs:
        series.append({
            'name': desc,
            'data': [e[1] for e in get_sorted_list(objs, desc, days)],
        })
    util_log.info('days= ', days)
    util_log.info('series= ', series)

    categories = days
    chart = get_chart_info(title='crawl_cnt', sub_title='crawl',categories=categories,series=series)
    data = {'type':'type', 'chart':chart}
    encodedjson = json.dumps(data)
    #if len(web) > 0:
    #return HttpResponse(json.dumps(data))
    return HttpResponse('mycallback(%s)'%encodedjson)

@csrf_exempt
def test(request):
    form = []
    if request.method == 'POST':
        day  = request.POST.get('day','')
        desc = request.POST.get('desc','')
        cnt  = request.POST.get('cnt', '')
        if desc == 'delete':
            for e in CrawlModel.objects.all():
                e.delete()
        else:
            e = CrawlModel(day = day, desc = desc, cnt=cnt)
            ret = e.save()
            resp = pack_json_resp(ret, 'append_crawl err', -1)
            return resp
    else:
        pass
    form = CrawlForm()
    return render_to_response('test.html', {'form':form})

@csrf_exempt
def show_audio(request):
    form = []
    if request.method == 'POST':
        #print pyUsage.get_cur_info(), 'ret= ', ret
        return pack_json_resp(True, 'show error', -1)
    else:
        pass
    return render_to_response('audio_chart.html')
    
@csrf_exempt
def get_audio_chart(request):
    res_list = [
        ('test', 1),
        ('test1', 2),
        ('test2', 3),
        ('test3', 1),
    ]
    categories = [e[0] for e in res_list]
    series = [e[1] for e in res_list]
    chart = get_chart_info(title='audio_cnt', sub_title='ip',categories=categories, series=series)
    data = {'type':'type', 'chart':chart}
    encodedjson = json.dumps(data)
    #if len(web) > 0:
    #return HttpResponse(json.dumps(data))
    return HttpResponse('mycallback(%s)'%encodedjson)

@csrf_exempt
def get_video_chart(request):
    res_list = [
        ('test', 1),
        ('test1', 2),
        ('test2', 3),
        ('test3', 5),
        ('test3', 7),
    ]
    categories = [e[0] for e in res_list]
    series = [e[1] for e in res_list]
    chart = get_chart_info(title='video_cnt', sub_title='ip',categories=categories, series=series)
    data = {'type':'type', 'chart':chart}
    encodedjson = json.dumps(data)
    #if len(web) > 0:
    #return HttpResponse(json.dumps(data))
    return HttpResponse('mycallback(%s)'%encodedjson)
    
def get_chart_info(title='title', sub_title='sub_title', yAix_title='yAix', categories='cate', series='series', valueSuffix=''):
    chart_dict = {}
    chart_dict['title']={}
    chart_dict['title']['text'] = title
    chart_dict['title']['x'] = -20
    chart_dict['subtitle']={}
    chart_dict['subtitle']['text'] = sub_title
    chart_dict['subtitle']['x'] = -20
    chart_dict['xAxis']={}
    chart_dict['xAxis']['categories'] = categories
    chart_dict['xAxis']['gridLineColor'] = '#197F07'
    chart_dict['xAxis']['gridLineWidth'] = 1
    chart_dict['yAxis']={}
    chart_dict['yAxis']['title'] = {}
    chart_dict['yAxis']['title']['text'] = yAix_title
    chart_dict['yAxis']['title']['plotLines'] = [{'value':0, 'width':1, 'color':'#808080'}]
    chart_dict['tooltip']={}
    chart_dict['tooltip']['valueSuffix']=valueSuffix
    chart_dict['legend']={}
    chart_dict['legend']['layout']='vertical'
    chart_dict['legend']['align']='right'
    chart_dict['legend']['verticalAlign']='middle'
    chart_dict['legend']['borderWidth']=0
    chart_dict['series']= []
    cur_dict = {}
    cur_dict['name']=title
    cur_dict['data']=series
    chart_dict['series'].append(cur_dict)
    
    return chart_dict
