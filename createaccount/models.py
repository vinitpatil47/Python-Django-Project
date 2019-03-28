from django.db import models
from datetime import datetime
from django.contrib import admin
import random

# Create your models here.

class Account(models.Model):
    account_holder_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    balance = models.IntegerField(default=500)
    mobile_number = models.IntegerField()
    account_type = models.CharField(max_length=10)
    email_id = models.EmailField()
    qualification = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    account_status = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    account_number = models.IntegerField(default=11000000000+random.randint(1,1000000000))
    j = models.IntegerField(default=1)

    def get_absolute_url(self):
        return u''

    def __str__(self):
        if self.j == 1:
            self.account_number = 11000000000 + random.randint(1,1000000000)
        self.j = 10
        self.save()
        return str(self.account_number)

class AccountAdmin(admin.ModelAdmin):
    exclude = ('account_holder_name',)

