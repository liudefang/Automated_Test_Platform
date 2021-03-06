# Generated by Django 2.1.1 on 2018-10-16 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App_case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_case_name', models.CharField(max_length=256, verbose_name='用例名称')),
                ('app_test_result', models.BooleanField(verbose_name='测试结果')),
                ('app_tester', models.CharField(max_length=64, verbose_name='测试负责人')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'app测试用例',
                'verbose_name_plural': 'app测试用例',
            },
        ),
        migrations.CreateModel(
            name='App_case_step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_case_name', models.CharField(max_length=256, verbose_name='测试用例标题')),
                ('app_test_setp', models.CharField(max_length=256, verbose_name='测试步骤')),
                ('app_test_obj_name', models.CharField(max_length=256, verbose_name='测试对象名称描述')),
                ('app_find_method', models.CharField(max_length=256, verbose_name='定位方式')),
                ('app_evelement', models.CharField(max_length=512, verbose_name='控件元素')),
                ('app_test_data', models.CharField(max_length=512, verbose_name='测试数据')),
                ('app_assert_data', models.CharField(max_length=128, verbose_name='验证数据')),
                ('app_test_result', models.BooleanField(max_length=32, verbose_name='测试结果')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('app_case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appui.App_case')),
            ],
        ),
    ]
