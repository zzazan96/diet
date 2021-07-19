from django.db import models

# Create your models here.
class UserTb(models.Model):
    user_no = models.AutoField(primary_key=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    pw = models.CharField(max_length=20, blank=True, null=True)
    nm = models.CharField(max_length=20, blank=True, null=True)
    tel = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tb'


class LoginTb(models.Model):
    user_id = models.CharField(max_length=20, blank=True, null=True)
    pw = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_tb'


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=20, blank=True, null=True)
    food_kcal = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'
