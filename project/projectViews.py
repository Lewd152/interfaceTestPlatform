from django.http import JsonResponse
from User.models import User
from django.shortcuts import redirect
from util import appLog
from project.models import Project
import time


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
def createProject(request):
    if request.method == 'POST':
        projectName = request.POST.get("projectName", "")
        projectDescribe = request.POST.get("projectDescribe", "")
        projectStatus = request.POST.get("projectStatus", "")
        username = request.session.get('username', "")
        userLevel = User.objects.get(username=username)
        if userLevel.level == 'visitors':
            return JsonResponse({"code": 0, "massage": "权限不足"})
        if userLevel.level == 'admin':
            project1 = Project()
            project1.p_name = projectName
            project1.p_describe = projectDescribe
            project1.p_status = projectStatus
            now = int(time.time())
            timeArray = time.localtime(now)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            project1.p_createtime = otherStyleTime
            project1.p_updatetime = otherStyleTime
            project1.p_exists = "True"
            print(userLevel.level)
            project1.save()
            appLog.info("log/projectOperation.log",
                        username + "创建了一个项目：" + projectName + "，项目描述：" + projectDescribe + "项目状态：" + projectStatus)
            return JsonResponse({"code": 200, "massage": "成功"})
        else:
            return JsonResponse({"code": 0, "massage": "权限不足"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})


def projectAll(request):
    if request.method == 'POST':
        try:
            res = list(Project.objects.all().filter(p_exists="True").values())
            return JsonResponse({"code": 200, "massage":"成功","res": res})
        except BaseException:
            return JsonResponse({"code": 0, "massage":"数据库异常"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})


@check_login
def queryProjectToName(request):
    if request.method == 'POST':
        p_name = request.POST.get('p_name', "")
        try:
            res = list(Project.objects.all().filter(p_name__contains=p_name,p_exists="True").values())
            return JsonResponse({"code": 200, "massage": "成功", "res": res})
        except BaseException:
            return JsonResponse({"code": 0, "massage": "数据异常"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})


@check_login
def deleteProject(request):
    # 前端需传递
    if request.method == 'POST':
        p_id = request.POST.get('p_id', "")
        username = request.session.get('username', "")
        userLevel = User.objects.get(username=username)
        if userLevel.level == 'visitors':
            return JsonResponse({"code": 0, "massage": "权限不足"})
        if p_id != "":
            try:
                res = Project.objects.get(p_id=p_id)
                res.p_exists = "False"
                res.save()
                appLog.info("log/projectOperation.log",username+"删除了"+p_id)
                return JsonResponse({"code": 200, "massage": "成功"})
            except BaseException:
                return JsonResponse({"code": 0, "massage": "数据库错误"})
        else:
            return JsonResponse({"code": 0, "massage": "参数错误"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})


def projectById(request):
    if request.method == 'POST':
        p_id = request.POST.get('p_id', "")
        try:
            res = list(Project.objects.all().filter(p_id=p_id, p_exists="True").values())
            return JsonResponse({"code": 200, "massage": "成功", "res": res})
        except BaseException:
            return JsonResponse({"code": 0, "massage": "数据异常"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})


def updateProject(request):
    if request.method == 'POST':
        projectName = request.POST.get("projectName", "")
        projectDescribe = request.POST.get("projectDescribe", "")
        projectStatus = request.POST.get("projectStatus", "")
        username = request.session.get('username', "")
        print(projectName,projectDescribe,projectStatus)
        userLevel = User.objects.get(username=username)
        if userLevel.level == 'visitors':
            return JsonResponse({"code": 0, "massage": "权限不足"})
        if userLevel.level == 'admin':
            Project.objects.filter(p_name=projectName).update(p_name=projectName,p_describe=projectDescribe,p_status=projectStatus)

            return JsonResponse({"code": 200, "massage": "成功"})
        else:
            return JsonResponse({"code": 0, "massage": "权限不足"})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})