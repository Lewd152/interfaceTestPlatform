import time

from django.http import JsonResponse
from User.models import User
from django.shortcuts import redirect, render
from project.models import Project,Module
from util import appLog


def check_login(func):
    def warpper(request, *args, **kwargs):
        is_login = request.session.get('is_login', False)
        print(is_login)
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return JsonResponse({"code": -1, "massage": "未登录"})

    return warpper


@check_login
def modulehtml(request):
    name = request.session.get('username', "")
    res = {"username": name}
    return render(request, 'moduleManagement.html', res)


# 一些基础信息，用于交互使用
def basicInformation(request):
    resProject = list(Project.objects.all().filter(p_exists="True").values())
    resUser = list(User.objects.all().values())
    res = {
        'userAll' : resUser,
        'projectAll' : resProject
    }
    return JsonResponse({"code": 200,"massage":"成功", "res": res})

@check_login
def createModule(request):
    if request.method == 'POST':
        subordinateToProject = request.POST.get("subordinateToProject","")
        moduleName = request.POST.get("moduleName","")
        moduleDescribe = request.POST.get("moduleDescribe","")
        moduleTester = request.POST.get("moduleTester","")
        moduleStatus = request.POST.get("moduleStatus","")
        now = int(time.time())
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        module = Module()
        module.m_p_name = subordinateToProject
        module.m_name = moduleName
        module.m_tester = moduleTester
        module.m_describe = moduleDescribe
        module.m_status = moduleStatus
        module.m_createtime = otherStyleTime
        module.m_updatetime = otherStyleTime
        module.m_exists = "True"
        try:
            module.save()
        except BaseException:
            return JsonResponse({"code": 0, "massage": "创建失败"})
        return JsonResponse({"code": 200, "massage": "成功"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})




def moduleAll(request):
    if request.method == 'POST':
        try:
            res = list(Module.objects.all().filter(m_exists="True").values())

            return JsonResponse({"code": 200, "massage":"成功","res": res})
        except BaseException:
            return JsonResponse({"code": 0, "res": "异常"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})


@check_login
def queryModuleToName(request):
    if request.method == 'POST':
        m_name = request.POST.get('m_name', "")
        try:
            res = list(Module.objects.all().filter(m_name__contains=m_name,m_exists="True").values())
            return JsonResponse({"code": 200, "massage": "成功", "res": res})
        except BaseException:
            return JsonResponse({"code": 0, "massage": "数据异常"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})

@check_login
def deleteModule(request):
    # 前端需传递
    if request.method == 'POST':
        m_id = request.POST.get('m_id', "")
        username = request.session.get('username', "")
        userLevel = User.objects.get(username=username)
        if userLevel.level == 'visitors':
            return JsonResponse({"code": 0, "massage": "权限不足"})
        if m_id != "":
            try:
                res = Module.objects.get(m_id=m_id)
                res.m_exists = "False"
                res.save()
                appLog.info("log/projectOperation.log",username+"删除了"+m_id)
                return JsonResponse({"code": 200, "massage": "成功"})
            except BaseException:
                return JsonResponse({"code": 0, "massage": "数据库错误"})
        else:
            return JsonResponse({"code": 0, "massage": "参数错误"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})


