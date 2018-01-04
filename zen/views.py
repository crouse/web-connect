# -*- coding:utf-8 -*-
from django.db.models import Q

from django.shortcuts import render
from django.http import HttpResponse
from zen.models import Male
from zen.models import Female
from zen.models import Xiaozu
from django.db import connection
import django.utils.timezone as timezone
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

    if dic['gender'] == u'男':
        obj = Male
        table = "zen_male"
    else:
        obj = Female
        table = "zen_female"

    dic['guiyi_year'] = str(timezone.now().year)
    dic['guiyi_date'] = timezone.now().strftime('%Y/%m/%d')

    ret = obj.objects.filter(name=dic['name'], phone=dic['phone'])

    rt = None

    if not ret:
        rt = obj.objects.create(**dic)
        return HttpResponse(request, 'bye.html')

    else:
        rt = obj.objects.filter(name=dic['name'], phone=dic['phone']).update(**dic)

    return render(request, 'bye.html')
