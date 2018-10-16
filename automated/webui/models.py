from test_platform.models import Modules
from django.db import models

# Create your models here.


class Web_case(models.Model):
    """
    webui测试用例表
    """
    # 关联模块id
    Modules = models.ForeignKey('test_platform.Modules', to_field='mid', on_delete=models.CASCADE, null=True)
    web_case_name = models.CharField('用例名称', max_length=256)      # web测试用例名称
    web_test_result = models.BooleanField('测试结果')     # web测试结果
    web_tester = models.CharField('测试负责人', max_length=64)    # 执行人
    create_time = models.DateTimeField('创建时间', auto_now=True)       # 创建时间，自动读取当前时间

    class Meta:
        verbose_name = 'web测试用例'
        verbose_name_plural = 'web测试用例'

    def __str__(self):
        return self.web_case_name


class Web_case_step(models.Model):
    """
    webui测试用例步骤
    """
    web_case = models.ForeignKey(to='Web_case', to_field='id', on_delete=models.CASCADE, null=True)
    web_case_name = models.CharField('测试用例标题', max_length=256)    # webui测试用例标题
    web_test_setp = models.CharField('测试步骤', max_length=256)      # webui 测试用例步骤
    web_testobj_name = models.CharField('测试对象名称描述', max_length=256)   # webui 测试对象名称描述(关键字）
    web_find_method = models.CharField('定位方式', max_length=256)    # 操作元素定位方式
    web_evelement = models.CharField('控件元素', max_length=512)     # 操作元素的定位表达式
    web_test_data = models.CharField('测试数据', max_length=512)      # 测试步骤中输入的数据
    web_assert_data = models.CharField('验证数据', max_length=128)    # 预期结果数据
    web_test_result = models.BooleanField('测试结果', max_length=32)  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)   # 创建时间，自动读取当前时间

    def __str__(self):
        return self.web_case_name

