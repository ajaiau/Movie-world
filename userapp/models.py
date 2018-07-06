# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	user=models.OneToOneField(User)
	mobile_no=models.CharField(max_length=12)
	place=models.CharField(max_length=50)

	