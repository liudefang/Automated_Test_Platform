from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from test_platform.forms import RegForm
from test_platform.models import *


# 注册
def register(request):
    if request.is_ajax():
        print(request.POST)
        form = RegForm(request.POST)

        response = {"username": None, "msg": None}
        if form.is_valid():
            response["username"] = form.cleaned_data.get("username")

            # 生成一条用户数据
            username = form.cleaned_data.get("username")
            print("username", username)
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")

            UserInfo.objects.create_user(username=username, password=password, email=email)


        else:
            print(form.cleaned_data)
            print(form.errors)
            response["msg"] = form.errors

        return JsonResponse(response)

    form = RegForm()
    return render(request, "register.html", {"form": form})


# 登录
def login(request):
    """
    登录视图函数：
        get请求相应页面
        post(Ajax)请求相应字典
    :param request:
    :return:
    """
    if request.method == "POST":

        response = {"username": None, "msg": None}
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            response["username"] = user.username

        else:
            response["msg"] = "用户名或者密码错误!"

        return JsonResponse(response)

    return render(request, "login.html")


def index(request):
    """
    系统首页
    :param request:
    :return:
    """

    return render(request, "login.html")


def logout(request):
    """
    退出系统
    :param request:
    :return:
    """
    auth.logout(request)

    return redirect("/login/")


@login_required
def home(request):
    """
    登录后的首页
    :param request:
    :return:
    """

    return render(request, "home.html")


@login_required
def project(request):
    """
    项目
    :param request:
    :return:
    """
    project_list = Project.objects.filter().all()

    return render(request, "project.html", {"project_list": project_list})


@login_required
def modules(request):
    """
    模块
    :param request:
    :return:
    """
    modules_list = Modules.objects.filter().all()
    project_list = Project.objects.all()

    return render(request, "modules.html", {"modules_list": modules_list, "project_list": project_list})


@login_required
def add_project(request):
    """
    新增项目
    :param request:
    :return:
    """
    if request.method == "POST":
        response = {"project_name": None, "msg": None}
        project_name = request.POST.get("project_name")
        project_desc = request.POST.get("project_desc")
        testers = request.POST.get("testers")

        print("project_name:", project_name)

        if len(project_name) != 0 and project_name != str(Project.objects.filter(project_name=project_name).first()):

            Project.objects.create(project_name=project_name, project_desc=project_desc, testers=testers)

            response["project_name"] = project_name

            return redirect("/project")
        elif len(project_name) == 0:
            response["msg"] = "项目名称不能为空!"
        else:
            response["msg"] = "项目名称已存在!"

        return JsonResponse(response)

    return render(request, "project.html")


@login_required
def add_modules(request):
    """
    新增模块
    :param request:
    :return:
    """

    # 搜索出所有的项目


    if request.method == "POST":

        response = {"modules_name": None, "msg": None}
        modules_name = request.POST.get("modules_name")
        modules_desc = request.POST.get("modules_desc")
        testers = request.POST.get("testers")
        project_id = request.POST.get("project_id")
        print("project_id:", project_id)

        if len(modules_name) != 0 and modules_name != str(Modules.objects.filter(modules_name=modules_name).first()):

            Modules.objects.create(modules_name=modules_name, modules_desc=modules_desc, testers=testers, Project_id=project_id)

            return redirect("/modules")
        elif len(modules_name) == 0:
            response["msg"] = "模块名称不能为空!"
        else:
            response["msg"] = "模块名称已存在!"

        return JsonResponse(response)

    return render(request, "modules.html")