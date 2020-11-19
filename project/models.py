from django.db import models

class Project(models.Model):
    p_id = models.AutoField(null=False,primary_key=True)
    p_name = models.CharField(max_length=20,null=False)
    p_describe = models.CharField(max_length=110,null=False)
    p_status = models.CharField(max_length=11,null=False)
    p_createtime = models.CharField(max_length=110,null=False)
    p_updatetime = models.CharField(max_length=110,null=False)
    p_exists = models.BooleanField(null=False,default=True)


class Module(models.Model):
    m_id = models.AutoField(null=False, primary_key=True)
    m_p_name = models.CharField(max_length=15, null=False)
    m_name = models.CharField(max_length=20, null=False)
    m_tester = models.CharField(max_length=11, null=False)
    m_describe = models.CharField(max_length=110, null=False)
    m_status = models.CharField(max_length=11, null=False)
    m_createtime = models.CharField(max_length=110, null=False)
    m_updatetime = models.CharField(max_length=110, null=False)
    m_exists = models.CharField(max_length=11, null=False)


class Case(models.Model):
    c_id = models.AutoField(null=False, primary_key=True)
    c_m_name = models.CharField(max_length=15, null=False)
    c_name = models.CharField(max_length=20, null=False)
    c_url = models.CharField(max_length=100, null=False)
    c_method = models.CharField(max_length=10, null=False)
    c_header = models.CharField(max_length=500, null=False)
    c_param = models.CharField(max_length=500, null=False)
    c_checktype = models.CharField(max_length=20, null=False)
    c_checkvalue = models.CharField(max_length=20, null=False)
    c_expectresult = models.CharField(max_length=20, null=False)
    c_actualresult = models.CharField(max_length=20, null=False)
    c_describe = models.CharField(max_length=110, null=False)
    c_creator = models.CharField(max_length=11, null=False)
    c_status = models.CharField(max_length=11, null=False)
    c_createtime = models.CharField(max_length=110, null=False)
    c_updatetime = models.CharField(max_length=110, null=False)
    c_exists = models.CharField(max_length=11, null=False)
