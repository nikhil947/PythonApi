# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class employees(models.Model):

    firstName= models.CharField(max_length=10)
    lastName=models.CharField(max_length=10)
    empId=models.IntegerField()

    def __str__(self):
        return self.firstName