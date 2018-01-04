#coding=utf-8
from django.db import models


class Male(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("姓名", max_length=32)
    fname = models.CharField("法名", max_length=32)
    gender = models.CharField("性别", max_length=10)
    race = models.CharField("民族", max_length=20)
    degree = models.CharField("学历", max_length=32)
    guiyi_year = models.CharField("皈依年份", max_length=32)
    guiyi_date = models.CharField("皈依日期", max_length=32)
    fahui_name = models.CharField("法会名称", max_length=32)
    guiyi_code = models.CharField("法会名称", max_length=32)
    receipt = models.CharField("收据号", max_length=32)
    personnel_id = models.CharField("身份证号", max_length=32)
    job = models.CharField("职业", max_length=32)
    hobby = models.CharField("爱好", max_length=64)
    birthday = models.CharField("生日", max_length=32)
    phone = models.CharField("手机号", max_length=20)
    telephone = models.CharField("固定电话", max_length=20)
    workplace = models.CharField("工作单位", max_length=64)
    province = models.CharField("现居地址（省)", max_length=64)
    city = models.CharField("现居地址（市)", max_length=64)
    district = models.CharField("现居地址（县)", max_length=64)
    address = models.CharField("现居地址（乡镇/小区/街道)", max_length=64)
    graduate_school = models.CharField('毕业学校', max_length=64)

    def __unicode__(self):
        return self.name

class Female(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("姓名", max_length=32)
    fname = models.CharField("法名", max_length=32)
    gender = models.CharField("性别", max_length=10)
    race = models.CharField("民族", max_length=20)
    degree = models.CharField("学历", max_length=32)
    guiyi_year = models.CharField("皈依年份", max_length=32)
    guiyi_date = models.CharField("皈依日期", max_length=32)
    fahui_name = models.CharField("法会名称", max_length=32)
    guiyi_code = models.CharField("法会名称", max_length=32)
    receipt = models.CharField("收据号", max_length=32)
    personnel_id = models.CharField("身份证号", max_length=32)
    job = models.CharField("职业", max_length=32)
    hobby = models.CharField("爱好", max_length=64)
    birthday = models.CharField("生日", max_length=32)
    phone = models.CharField("手机号", max_length=20)
    telephone = models.CharField("固定电话", max_length=20)
    workplace = models.CharField("工作单位", max_length=64)
    province = models.CharField("现居地址（省)", max_length=64)
    city = models.CharField("现居地址（市)", max_length=64)
    district = models.CharField("现居地址（县)", max_length=64)
    address = models.CharField("现居地址（乡镇/小区/街道)", max_length=64)
    graduate_school = models.CharField('毕业学校', max_length=64)

    def __unicode__(self):
        return self.name



class Xiaozu(models.Model):
    name = models.CharField("姓名", max_length=32)
    gender = models.CharField("性别", max_length=10)
    phone_num = models.CharField("手机号", max_length=32)
    birthday = models.CharField("生日", max_length=32)
    address = models.CharField("现居地址（乡镇/小区/街道)", max_length=128)
    xiaozu_type = models.CharField("小组类型", max_length=32)
    xiaozu_lang = models.CharField("小组语言种类", max_length=32)
    xiaozu_dizhi = models.CharField("学佛小组地址", max_length=128)
    xiaozu_fou = models.CharField("是否参加学佛小组", max_length=128)


    def __unicode__(self):
        return self.name
