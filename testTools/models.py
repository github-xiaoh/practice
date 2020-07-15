from django.db import models


class ClientUser(models.Model):
    u_mobile = models.CharField(max_length=11, blank=True, null=True)
    u_email = models.CharField(max_length=60, blank=True, null=True)
    u_password = models.CharField(max_length=40, blank=True, null=True)
    u_nickname = models.CharField(max_length=60)
    u_image = models.CharField(max_length=512, blank=True, null=True)
    u_mbtype = models.PositiveIntegerField()
    u_bind = models.PositiveIntegerField()
    u_dvcid = models.CharField(max_length=40, blank=True, null=True)
    u_uuid = models.CharField(max_length=32, blank=True, null=True)
    u_cid = models.CharField(max_length=40, blank=True, null=True)
    u_status = models.PositiveIntegerField()
    u_online = models.PositiveIntegerField()
    u_lgtype = models.PositiveIntegerField()
    u_sex = models.PositiveIntegerField()
    expand = models.CharField(max_length=300)
    u_area_code = models.CharField(max_length=10, blank=True, null=True)
    u_certified = models.IntegerField(blank=True, null=True)
    account_types = models.IntegerField()
    u_origin = models.IntegerField()
    region_name = models.CharField(max_length=60, blank=True, null=True)
    region_code = models.CharField(max_length=10, blank=True, null=True)
    region_id = models.IntegerField()
    u_lang = models.CharField(max_length=32)
    u_studio = models.IntegerField()
    u_last_login_time = models.IntegerField(blank=True, null=True)
    u_create_time = models.IntegerField()
    u_update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client_user'




# Create your models here.
