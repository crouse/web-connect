# -*- coding:utf-8 -*-
from django.db.models import Q

from django.shortcuts import render
from django.http import HttpResponse
from zen.models import Male
from zen.models import Female
from zen.models import Xiaozu
from django.db import connection

import logging
logger = logging.getLogger('django')

def xiaozu(request):
    return render(request, 'xiaozu.html')

def xiaozued(request):
    dic = request.GET.dict()
    ret = Xiaozu.objects.filter(name=dic['name'], phone_num=dic['phone_num'])
    if not ret:
        person = Xiaozu(**dic)
        person.save()
        return render(request, 'xiaozu_bye.html')

    ret = Xiaozu.objects.filter(name=dic['name'], phone_num=dic['phone_num']).update(**dic)

    return render(request, 'xiaozu_bye.html')


def zen(request):
    return render(request, 'zen.html')

def zened(request):
    table = ""
    obj = ""
    dic = request.GET.dict()
    dic['comes'] = 1 # comes from mobile phone

    if dic['gender'] == u'男':
        obj = Male
        table = "zen_male"
    else:
        obj = Female
        table = "zen_female"

    ret = obj.objects.filter(name=dic['name'], phone_num=dic['phone_num'])
    if not ret:
        logger.info("{0} 没有交费".format(dic['name'].encode('utf8')))
        return render(request, 'error.html')

    rt = obj.objects.filter(name=dic['name'], phone_num=dic['phone_num']).update(**dic)
    if not rt:
        logger.error("{0} 错误".format(dic['name'].encode('utf8')))
        return HttpResponse("error")

    return render(request, 'bye.html')
