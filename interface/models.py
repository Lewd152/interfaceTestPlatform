from django.db import models

class interface(models.Model):
    i_id = models.AutoField(null=False, primary_key=True)
    i_name = models.CharField(max_length=15, null=False)
    i_url = models.CharField(max_length=500, null=False)
    i_createtime = models.CharField(max_length=110, null=False)
    i_updatetime = models.CharField(max_length=110, null=False)
    i_exists = models.CharField(max_length=11, null=False)