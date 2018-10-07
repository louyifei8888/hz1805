# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-28 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_num', models.IntegerField(default=1)),
                ('c_isselect', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=20)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=100)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=50)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.BooleanField(default=0)),
                ('pmdesc', models.IntegerField(default=0)),
                ('specifics', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('marketprice', models.FloatField(default=0)),
                ('categoryid', models.CharField(max_length=50)),
                ('childcid', models.CharField(max_length=50)),
                ('childcidname', models.CharField(max_length=100)),
                ('dealerid', models.CharField(max_length=50)),
                ('storenums', models.IntegerField(default=0)),
                ('productnum', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'axf_goods',
            },
        ),
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=50)),
                ('categoryid', models.CharField(max_length=50)),
                ('brandname', models.CharField(max_length=50)),
                ('img1', models.CharField(max_length=200)),
                ('childcid1', models.CharField(max_length=50)),
                ('productid1', models.CharField(max_length=50)),
                ('longname1', models.CharField(max_length=200)),
                ('price1', models.CharField(max_length=50)),
                ('marketprice1', models.CharField(max_length=50)),
                ('img2', models.CharField(max_length=200)),
                ('childcid2', models.CharField(max_length=50)),
                ('productid2', models.CharField(max_length=50)),
                ('longname2', models.CharField(max_length=200)),
                ('price2', models.CharField(max_length=50)),
                ('marketprice2', models.CharField(max_length=50)),
                ('img3', models.CharField(max_length=200)),
                ('childcid3', models.CharField(max_length=50)),
                ('productid3', models.CharField(max_length=50)),
                ('longname3', models.CharField(max_length=200)),
                ('price3', models.CharField(max_length=50)),
                ('marketprice3', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='MustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'axf_mustbuy',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('r_name', models.CharField(max_length=50)),
                ('r_call_phone', models.IntegerField(default=0)),
                ('r_address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'axf_receiver',
            },
        ),
        migrations.CreateModel(
            name='ShopModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=32, unique=True)),
                ('u_passwd', models.CharField(max_length=32)),
                ('u_mail', models.CharField(max_length=64, unique=True)),
                ('u_sex', models.BooleanField(default=1)),
                ('u_img', models.ImageField(upload_to='img')),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('trackid', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
        migrations.AddField(
            model_name='receiver',
            name='r_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserModel'),
        ),
        migrations.AddField(
            model_name='cart',
            name='c_goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Goods'),
        ),
        migrations.AddField(
            model_name='cart',
            name='c_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserModel'),
        ),
    ]
