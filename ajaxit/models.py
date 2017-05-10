from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Employees(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_email = models.CharField(max_length=100)
    emp_dob = models.DateField()
    emp_pass = models.CharField(max_length=100)
