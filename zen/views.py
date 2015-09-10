# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from zen.models import Person

import logging
logger = logging.getLogger('django')

def zen(request):
    logger.debug("this is a debug info")
    return render(request, 'zen.html')

def zened(request):
    # name = request.GET['name']
    logger.info('Start here')
    dic = request.GET.dict()
    dic['comes'] = 1 # comes from mobile phone
    logger.info(dic.keys())
    person = Person(**dic)
    person.save()
    return render(request, 'bye.html')
