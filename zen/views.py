# -*- coding:utf-8 -*-
from django.db.models import Q

from django.shortcuts import render
from django.http import HttpResponse
from zen.models import Male
from zen.models import Female
from django.db import connection

import logging
logger = logging.getLogger('django')

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
    #person = obj(**dic)
    #person.save()
    cursor = connection.cursor()
    sql = "select id from {0} where name = '{1}' and phone_num = '{2}' ".format(table, dic['name'].encode("utf8"), dic['phone_num'])
    cursor.execute(sql)
    logger.info(sql)
    row = cursor.fetchone()
    if not row:
        return render(request, 'error.html')
    id = row[0]

    usql = """
                update {0} set race = '{1}', degree = '{2}', birthday = '{3}',
                    personnel_id = '{4}', province = '{5}', city = '{6}',
                    distinct = '{7}', address = '{8}' where id = '{9}'
           """.format(table, dic['race'].encode('utf8'),
                       dic['degree'].encode("utf8"),
                       dic['birthday'].encode("utf8"),
                       dic['personnel_id'].encode("utf8"),
                       dic['province'].encode("utf8"),
                       dic['city'].encode("utf8"),
                       dic['distinct'].encode("utf8"),
                       dic['address'].encode("utf8"),
                       str(id))

    cursor.execute(usql)
    logger.info(usql)

    return render(request, 'bye.html')
