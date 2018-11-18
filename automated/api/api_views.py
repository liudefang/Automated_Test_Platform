from django.shortcuts import render

# Create your views here.


def index(request):
    """
    系统首页
    :param request:
    :return:
    """

    return render(request, "login.html")


def apitest_manage(request):


    return render(request, "apitest_manage.html")


def apistep_manage(request):

    return render(request, "apistep_manage.html")
