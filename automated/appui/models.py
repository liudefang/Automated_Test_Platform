from django.db import models

# Create your models here.


class App_case(models.Model):
    """
    appui测试用例表
    """
    # 关联模块id
    Modules = models.ForeignKey(to='Modules', to_field='mid', on_delete=models.CASCADE, null=True)
    app_case_name = models.CharField('用例名称', max_length=256)  # web测试用例名称
    app_test_result = models.BooleanField('测试结果')  # web测试结果
    app_tester = models.CharField('测试负责人', max_length=64)  # 执行人
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动读取当前时间

    class Meta:
        verbose_name = 'app测试用例'
        verbose_name_plural = 'app测试用例'

    def __str__(self):
        return self.appcase_name


class App_case_step(models.Model):
    """
    appui测试用例步骤
    """
    app_case = models.ForeignKey(to='appcase', to_field='id', on_delete=models.CASCADE, null=True)
    app_case_name = models.CharField('测试用例标题', max_length=256)  # webui测试用例标题
    app_test_setp = models.CharField('测试步骤', max_length=256)  # webui 测试用例步骤
    app_testobj_name = models.CharField('测试对象名称描述', max_length=256)  # webui 测试对象名称描述(关键字）
    app_find_method = models.CharField('定位方式', max_length=256)  # 操作元素定位方式
    app_evelement = models.CharField('控件元素', max_length=512)  # 操作元素的定位表达式
    app_test_data = models.CharField('测试数据', max_length=512)  # 测试步骤中输入的数据
    app_assert_data = models.CharField('验证数据', max_length=128)  # 预期结果数据
    app_test_result = models.BooleanField('测试结果', max_length=32)  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动读取当前时间

    def __str__(self):
        return self.appcase_name