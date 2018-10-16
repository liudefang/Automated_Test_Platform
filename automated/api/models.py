from django.db import models
from test_platform.models import Modules
# Create your models here.


class Api_test(models.Model):
    """
    业务场景接口表
    """
    # 关联模块id
    Modules = models.ForeignKey(to="test_platform.Modules", to_field='mid', on_delete=models.CASCADE, null=True)
    api_test_name = models.CharField('流程接口名称', max_length=64)     # 流程接口测试场景
    api_test_desc = models.CharField('描述', max_length=64, null=True)      # 流程接口描述
    api_tester = models.CharField('测试负责人', max_length=64)    # 执行人
    api_test_result = models.BooleanField('测试结果')     # 流程接口测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)       # 创建时间，自动读取当前时间

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name = '流程场景接口'

    def __str__(self):
        return self.api_test_name


class Api_step(models.Model):
    """
    接口步骤表
    """
    api_test = models.ForeignKey(to='Api_test', to_field='id', on_delete=models.CASCADE, null=True)   # 关联接口id
    api_test_name = models.CharField('接口名称', max_length=128)  # 接口标题
    api_url = models.CharField('URL地址', max_length=256)      # 接口URL地址
    api_param_value = models.CharField('请求参数和值', max_length=1024)     # 请求参数和值
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    # 请求方法
    api_method = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD,default='get', max_length=64, null=True)
    api_result = models.CharField('预期结果', max_length=256)    # 预期结果
    api_status = models.BooleanField('是否通过')     # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)   # 创建时间，自动读取当前时间

    def __str__(self):
        return self.api_test_name


class Apis(models.Model):
    """
    单一接口表
    """

    # 关联模块id
    Modules = models.ForeignKey(to='test_platform.Modules', to_field='mid', on_delete=models.CASCADE, null=True)
    api_name = models.CharField('接口名称', max_length=128)      # 接口标题
    api_url = models.CharField('URL地址', max_length=256)  # 接口URL地址
    api_param_value = models.CharField('请求参数和值', max_length=1024)  # 请求参数和值
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    # 请求方法
    api_method = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='get', max_length=64, null=True)
    api_result = models.CharField('预期结果', max_length=256)  # 预期结果
    api_status = models.BooleanField('是否通过')  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动读取当前时间

    def __str__(self):
        return self.api_name
