from django.db import models




class PayAccountDetails(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    region_id = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=20, blank=True, null=True)
    account_balance = models.DecimalField(max_digits=10, decimal_places=3)
    recharge_total = models.DecimalField(max_digits=10, decimal_places=3)
    spend_total = models.DecimalField(max_digits=10, decimal_places=3)
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=20, blank=True, null=True)
    is_del = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pay_account_details'





# Create your models here.
