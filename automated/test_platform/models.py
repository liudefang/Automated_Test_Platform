from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Project(models.Model):
    """
    项目管理表
    """
    pid = models.AutoField(primary_key=True)
    projectname = models.CharField('项目名称', max_length=64)   # 项目名称
    projectdesc = models.CharField('项目描述', max_length=256)  # 项目描述
    Testers = models.CharField('测试负责人', max_length=256)    # 项目负责人
    create_time = models.DateTimeField('创建时间', auto_now=True)   # 创建时间

    class Meta:
        verbose_name = '项目管理'
        verbose_name_plural = '项目管理'

    def __str__(self):
        return self.projectname


class Modules(models.Model):
    """
    模块表
    """
    mid = models.AutoField(primary_key=True)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Modules_name = models.CharField('模块名称', max_length=20)  # 模块名称
    Testers = models.CharField('测试人员', max_length=100)  # 测试执行人员
    Developer = models.CharField(max_length=100)    # 备用
    status = models.BooleanField()      # 备用
    Modules_desc = models.CharField('模块描述', max_length=200)     # 模块描述

    def __str__(self):
        return self.Modules_name


class Apitest(models.Model):
    """
    业务场景接口表
    """
    # 关联模块id
    Modules = models.ForeignKey(to='Modules', to_field='mid', on_delete=models.CASCADE, null=True)
    apitestname = models.CharField('流程接口名称', max_length=64)     # 流程接口测试场景
    apitestdesc = models.CharField('描述', max_length=64, null=True)      # 流程接口描述
    apitester = models.CharField('测试负责人', max_length=64)    # 执行人
    apitestresult = models.BooleanField('测试结果')     # 流程接口测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)       # 创建时间，自动读取当前时间

    class Meta:
        verbose_name = '流程场景接口'
        verbose_name = '流程场景接口'

    def __str__(self):
        return self.apitestname


class Apistep(models.Model):
    """
    接口步骤表
    """
    apitest = models.ForeignKey(to='Apitest', to_field='id', on_delete=models.CASCADE, null=True)   # 关联接口id
    apitestname = models.CharField('接口名称', max_length=128)  # 接口标题
    apiurl = models.CharField('URL地址', max_length=256)      # 接口URL地址
    apiparamvalue = models.CharField('请求参数和值', max_length=1024)     # 请求参数和值
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    # 请求方法
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD,default='get', max_length=64, null=True)
    apiresult = models.CharField('预期结果', max_length=256)    # 预期结果
    apistatus = models.BooleanField('是否通过')     # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)   # 创建时间，自动读取当前时间

    def __str__(self):
        return self.apitestname


class Apis(models.Model):
    """
    单一接口表
    """

    # 关联模块id
    Modules = models.ForeignKey(to='Modules', to_field='mid', on_delete=models.CASCADE, null=True)
    apiname = models.CharField('接口名称', max_length=128)      # 接口标题
    apiurl = models.CharField('URL地址', max_length=256)  # 接口URL地址
    apiparamvalue = models.CharField('请求参数和值', max_length=1024)  # 请求参数和值
    REQUEST_METHOD = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch'))
    # 请求方法
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='get', max_length=64, null=True)
    apiresult = models.CharField('预期结果', max_length=256)  # 预期结果
    apistatus = models.BooleanField('是否通过')  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动读取当前时间

    def __str__(self):
        return self.apiname


class Webcase(models.Model):
    """
    webui测试用例表
    """
    # 关联模块id
    Modules = models.ForeignKey(to='Modules', to_field='mid', on_delete=models.CASCADE, null=True)
    webcasename = models.CharField('用例名称', max_length=256)      # web测试用例名称
    webtestresult = models.BooleanField('测试结果')     # web测试结果
    webtester = models.CharField('测试负责人', max_length=64)    # 执行人
    create_time = models.DateTimeField('创建时间', auto_now=True)       # 创建时间，自动读取当前时间

    class Meta:
        verbose_name = 'web测试用例'
        verbose_name_plural = 'web测试用例'

    def __str__(self):
        return self.webcasename


class Webcasestep(models.Model):
    """
    webui测试用例步骤
    """
    webcase = models.ForeignKey(to='Webcase', to_field='id', on_delete=models.CASCADE, null=True)
    webcasename = models.CharField('测试用例标题', max_length=256)    # webui测试用例标题
    webtestsetp = models.CharField('测试步骤', max_length=256)      # webui 测试用例步骤
    webtestobjname = models.CharField('测试对象名称描述', max_length=256)   # webui 测试对象名称描述(关键字）
    webfindmethod = models.CharField('定位方式', max_length=256)    # 操作元素定位方式
    webevelement = models.CharField('控件元素', max_length=512)     # 操作元素的定位表达式
    webtestdata = models.CharField('测试数据', max_length=512)      # 测试步骤中输入的数据
    webassertdata = models.CharField('验证数据', max_length=128)    # 预期结果数据
    webtestresult = models.BooleanField('测试结果', max_length=32)  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)   # 创建时间，自动读取当前时间

    def __str__(self):
        return self.webcasename


class Appcase(models.Model):
    """
    webui测试用例表
    """
    # 关联模块id
    Modules = models.ForeignKey(to='Modules', to_field='mid', on_delete=models.CASCADE, null=True)
    appcasename = models.CharField('用例名称', max_length=256)  # web测试用例名称
    apptestresult = models.BooleanField('测试结果')  # web测试结果
    apptester = models.CharField('测试负责人', max_length=64)  # 执行人
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动读取当前时间

    class Meta:
        verbose_name = 'app测试用例'
        verbose_name_plural = 'app测试用例'

    def __str__(self):
        return self.appcasename


class Appcasestep(models.Model):
    """
    appui测试用例步骤
    """
    appcase = models.ForeignKey(to='appcase', to_field='id', on_delete=models.CASCADE, null=True)
    appcasename = models.CharField('测试用例标题', max_length=256)  # webui测试用例标题
    apptestsetp = models.CharField('测试步骤', max_length=256)  # webui 测试用例步骤
    apptestobjname = models.CharField('测试对象名称描述', max_length=256)  # webui 测试对象名称描述(关键字）
    appfindmethod = models.CharField('定位方式', max_length=256)  # 操作元素定位方式
    appevelement = models.CharField('控件元素', max_length=512)  # 操作元素的定位表达式
    apptestdata = models.CharField('测试数据', max_length=512)  # 测试步骤中输入的数据
    appassertdata = models.CharField('验证数据', max_length=128)  # 预期结果数据
    apptestresult = models.BooleanField('测试结果', max_length=32)  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动读取当前时间

    def __str__(self):
        return self.appcasename


class UserInfo(AbstractUser):
    """
    用户信息
    """
    nid = models.AutoField(primary_key=True)
    telephone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to='avatars/', default="/avatars/default.png")
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.username




