import json
import time

from django.http import JsonResponse
from django.shortcuts import redirect, render

from User.models import User
from project.models import Case
from util import findValuesInJson
from util.aSingleInterfaceAutomation import *
from util.reportHtml import *
from util.run_case import *


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
def casehtml(request):
    name = request.session.get('username', "")
    res = {"username": name}
    return render(request, 'case.html', res)

@check_login
def createCase(request):
    if request.method == 'POST':
        global result
        subordinateToModule = request.POST.get("subordinateToModule", "")
        caseName = request.POST.get("caseName", "")
        caseUrl = request.POST.get("caseUrl", "")
        caseMethod = request.POST.get("caseMethod", "")
        caseHeader = request.POST.get("caseHeader", "")
        caseParam = request.POST.get("caseParam", "")
        caseChecktype = request.POST.get("caseChecktype", "")
        caseCheckValue = request.POST.get("caseCheckValue", "")
        caseExpectresult = request.POST.get("caseExpectresult", "")
        caseDescribe = request.POST.get("caseDescribe", "")
        caseTester = request.POST.get("caseTester", "")
        now = int(time.time())
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        case = Case()
        case.c_m_name = subordinateToModule
        case.c_name = caseName
        case.c_url = caseUrl
        case.c_method = caseMethod
        case.c_header = caseHeader
        case.c_param = caseParam
        case.c_checktype = caseChecktype
        case.c_checkvalue = caseCheckValue
        case.c_expectresult = caseExpectresult

        case.c_creator = caseTester
        case.c_describe = caseDescribe
        case.c_createtime = otherStyleTime
        case.c_updatetime = otherStyleTime
        case.c_exists = "True"
        # 创建任务，执行用例
        try:
            #执行测试用例
            ress = runCaseReportHtml(TestMathMethod.test01(caseUrl=caseUrl,caseMethod=caseMethod,caseHeader=caseHeader,caseParam=caseParam,caseCheckValue=caseCheckValue,caseChecktype=caseChecktype))
            case.c_actualresult = ress
            case.c_status = "执行完毕"
        except BaseException:
            case.c_actualresult = 'False'
            case.c_status = "执行失败"
            result = {"code": 0, "massage": "用例执行失败"}
        try:
            case.save()
        except BaseException:
            result = {"code": 0, "massage": "创建失败"}
        result = {"code": 200, "massage": "成功"}

    else:
        result = {"code": 0, "massage": "请求异常"}
    return JsonResponse(result)


def caseAll(request):
    if request.method == 'POST':
            res = list(Case.objects.all().filter(c_exists="True").values())
            return JsonResponse({"code": 200, "massage": "成功","res": res})
    else:
        return JsonResponse({"code": 0, "massage": "请求异常"})


@check_login
def deleteCase(request):
    # 前端需传递
    global result
    if request.method == 'POST':
        c_id = request.POST.get('c_id', "")
        print(c_id)
        username = request.session.get('username', "")
        userLevel = User.objects.get(username=username)
        if userLevel.level == 'visitors':
            result = {"code": 0, "massage": "权限不足"}
        if c_id != "":
            try:
                res = Case.objects.get(c_id=c_id)
                res.c_exists = "False"
                res.save()
                result = {"code": 200, "massage": "成功"}
            except Exception:
                result = {"code": 0, "massage": "数据库错误"}
        else:
            result = {"code": 0, "massage": "参数错误"}
    else:
        result = {"code": 0, "massage": "请求异常"}
    return JsonResponse(result)