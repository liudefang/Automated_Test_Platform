from django.contrib.auth.decorators import login_required
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

@login_required
def add_api_case(request):
    """
    新增项目
    :param request:
    :return:
    """
    if request.method == "POST":

        project_name = request.POST.get("project_name")
        project_desc = request.POST.get("project_desc")
        testers = request.POST.get("testers")

        print("project_name:", project_name)

        if len(project_name) != 0 and project_name != str(Project.objects.filter(project_name=project_name).first()):

            Project.objects.create(project_name=project_name, project_desc=project_desc, testers=testers)

            response = {"status": 0, "msg": "添加成功!"}

            # return redirect("/project")
        elif len(project_name) == 0:
            response = {"status": 1, "msg": "项目名称不能为空!"}
        else:
            response = {"status": 2, "msg": "项目名称已存在!"}

        return JsonResponse(response)

    return render(request, "project.html")
