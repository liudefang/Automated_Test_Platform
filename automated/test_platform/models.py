from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Project(models.Model):
    """
    项目管理表
    """
    pid = models.AutoField(primary_key=True)
    project_name = models.CharField('项目名称', max_length=64)   # 项目名称
    project_desc = models.CharField('项目描述', max_length=256)  # 项目描述
    testers = models.CharField('测试负责人', max_length=256)    # 项目负责人
    create_time = models.DateTimeField('创建时间', auto_now=True)   # 创建时间

    class Meta:
        verbose_name = '项目管理'
        verbose_name_plural = '项目管理'

    def __str__(self):
        return self.project_name


class Modules(models.Model):
    """
    模块表
    """
    mid = models.AutoField(primary_key=True)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    modules_name = models.CharField('模块名称', max_length=20)  # 模块名称
    testers = models.CharField('测试人员', max_length=100)  # 测试执行人员
    developer = models.CharField(max_length=100)    # 备用
    # status = models.BooleanField()      # 备用
    modules_desc = models.CharField('模块描述', max_length=200)     # 模块描述
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间

    def __str__(self):
        return self.modules_name


class Set(models.Model):
    """
    设置表
    """
    set_name = models.CharField('设置名称', max_length=32)  # 系统设置名称
    set_value = models.CharField('设置值', max_length=128)     # 设置值
    platform_name = models.CharField('平台名称', max_length=64)     # 平台名称
    platform_version = models.CharField('平台版本', max_length=32)    # 操作系统的版本
    device_name = models.CharField('设备名称', max_length=64)       # 设备名称
    app = models.CharField('APP路径', max_length=256)     # app的路径
    no_reset = models.BooleanField('是否重启', max_length=16)   # 是否重启
    reset_key_board = models.BooleanField('重置键盘', max_length=16)    # 重置键盘
    unicode_key_board = models.BooleanField('unicode键盘', max_length=16)     # unicode键盘
    recreate_charome_driver_sessions = models.BooleanField('启动charomedriver', max_length=16)  # 切换webview的时候重新启动chromedriver

    def __str__(self):
        return self.set_name


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




