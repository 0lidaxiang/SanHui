# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('human_resources', '0002_auto_20171204_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='province',
            name='desc',
        ),
        migrations.AddField(
            model_name='personnelinformation',
            name='is_social_security',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=3, verbose_name='是否参加社保'),
        ),
        migrations.AddField(
            model_name='personnelinformation',
            name='remarks',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='personnelinformation',
            name='working_industry',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='务工行业'),
        ),
        migrations.AddField(
            model_name='personnelinformation',
            name='working_salary',
            field=models.CharField(blank=True, choices=[('5', '5万以下'), ('5to8', '5-8万'), ('8to12', '8-12万'), ('12', '12万以上')], max_length=5, null=True, verbose_name='务工年收入'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='health_status',
            field=models.CharField(choices=[('jk', '健康'), ('hyjb', '患有疾病'), ('cj', '残疾')], default='jk', max_length=9, verbose_name='身体状况'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='is_basic_living_allowances',
            field=models.CharField(choices=[('db', '低保'), ('wb', '五保'), ('w', '无')], default='w', max_length=3, verbose_name='最低保障'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='is_medical_insurance',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=3, verbose_name='是否参加医保'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='is_rural_social_endowment_insurance',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=3, verbose_name='是否农保'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='is_village_backup_cadres',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='no', max_length=3, verbose_name='是否为村后备干部'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='political_status',
            field=models.CharField(choices=[('qz', '群众'), ('ty', '团员'), ('rdjjfz', '入党积极分子'), ('ybdy', '预备党员'), ('zsdy', '正式党员')], max_length=6, verbose_name='政治面貌'),
        ),
        migrations.AlterField(
            model_name='personnelinformation',
            name='working_position',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='务工职位'),
        ),
    ]
