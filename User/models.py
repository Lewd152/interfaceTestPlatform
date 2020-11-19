from django.db import models

class User(models.Model):
    # name
    username = models.CharField('用户名',max_length=15,null=False)
    # 机型  pc  mac
    passworld = models.CharField('密码',max_length=20,null=False)
    # 手机号，用于找回密码
    iphone = models.CharField('手机号',max_length=11,null=False)

    # 权限控制
    level = models.CharField('权限',max_length=11,default="visitors")
    # 指定表名 不指定默认APP名字——类名(app_demo_Student)
    class Meta:
        db_table = 'User'
