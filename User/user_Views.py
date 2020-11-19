from django.http import JsonResponse
from django.shortcuts import render, redirect

from User.models import User

def check_login(func):
    def warpper(request, *args, **kwargs):
        is_login = request.session.get('is_login', False)
        print(is_login)
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect("/login")

    return warpper


def CreateUser(request):
    username = request.POST.get('username', "")
    password = request.POST.get('password', "")
    iphone = request.POST.get('iphone', "")
    repeat_password = request.POST.get('repeat_password', "")
    res = User.objects.get(username=username)
    vals = ['username', 'password', 'iphone', 'repeat_password']
    dict = {'username': '用户名', 'password': '密码', 'iphone': '手机号', 'repeat_password': '确认密码'}
    for i in vals:
        if locals()[i] == '':
            return JsonResponse({"code": 0, "massage": "{}不能为空".format(dict[i])})

    if username == res.username:
        try:
            res = User.objects.get(username=username)
            return JsonResponse({"code": 0, "massage": "用户名已存在"})
        except:
            if len(password) < 6:
                return JsonResponse({"code": 0, "massage": "密码太短，请输入6位以上"})
            elif len(iphone) != 11:
                return JsonResponse({"code": 0, "massage": "手机号不合法，重新输入"})
            elif repeat_password != password:
                return JsonResponse({"code": 0, "massage": "两次密码不一致"})
            else:
                try:
                    user = User()
                    user.username = username
                    user.passworld = password
                    user.iphone = iphone
                    user.save()
                    return JsonResponse({"code": 200, "massage": "成功", "username": username})
                except:
                    return JsonResponse({"code": 0, "massage": "数据库异常"})


def Login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    username = request.POST.get('username', "")
    password = request.POST.get('password', "")
    print(username, password)
    if username == "" or password == "":
        massage = {"code": 0, "massage": "账号密码为空"}
        return JsonResponse(massage)

    # 先判断是否存在用户名
    try:
        res = User.objects.get(username=username)
        if res.passworld == password:
            # 检查是否其他设备正在登陆
            request.session['is_login'] = True
            request.session['username'] = username
            massage = {"code": 200, "massage": "登录成功"}
            return JsonResponse(massage)
        else:
            massage = {"code": 0, "massage": "密码错误"}
            return JsonResponse(massage)
    except:
        massage = {"code": 0, "massage": "用户名不存在"}
        return JsonResponse(massage)


@check_login
def logout(request):
    # del request.session['is_login']
    # del request.session['username']
    request.session.flush()
    return redirect('/login/')


# 重置密码
def resetPwd(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        new_password = request.POST.get("new_password", "")
        print(username, password, new_password)
        if username == "" or password == "" or new_password == "":
            massage = {"code": 0, "massage": "账号密码为空"}
            return JsonResponse(massage)
        try:
            res = User.objects.get(username=username)
            if res.passworld == new_password:
                massage = {"code": 0, "massage": "新密码与最近密码类似"}
                return JsonResponse(massage)
            if res.username == username and res.passworld == password:
                res.passworld = new_password
                res.save()
                del request.session['is_login']
                del request.session['username']
                return redirect('/login/')
            else:
                massage = {"code": 0, "massage": "账号信息有误"}
                return JsonResponse(massage)
        except:
            massage = {"code": 0, "massage": "用户名不存在"}
            return JsonResponse(massage)


# 根据手机号找回密码
def retrievePassword(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        iphone = request.POST.get("iphone", "")
        new_password = request.POST.get("new_password", "")
        if username == "" or iphone == "" or new_password == "":
            massage = {"code": 0, "massage": "账号密码为空"}
            return JsonResponse(massage)
        try:
            res = User.objects.get(username=username)
            User.objects.filter()
            if res.username == username and res.iphone == iphone:
                if res.passworld == new_password:
                    massage = {"code": 0, "massage": "新密码与最近密码类似"}
                    return JsonResponse(massage)
                else:
                    try:
                        res.passworld = new_password
                        res.save()
                        return JsonResponse({"code": 200, "massage": "成功", "username": username})
                    except:
                        massage = {"code": 0, "massage": "数据库异常"}
                        return JsonResponse(massage)
            else:
                massage = {"code": 0, "massage": "信息验证失败"}
                return JsonResponse(massage)
        except:
            massage = {"code": 0, "massage": "用户名不存在"}
            return JsonResponse(massage)

    else:
        massage = {"code": 0, "massage": "请求异常"}
        return JsonResponse(massage)


@check_login
def Index(request):
    name = request.session.get('username', "")
    res ={"username":name}
    return render(request, "index.html", res)


def registerHtml(request):
    return render(request,'register.html')