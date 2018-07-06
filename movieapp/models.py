# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MovieModel(models.Model):
	movie_name=models.CharField(max_length=50)
	movie_language=models.CharField(max_length=10)
	release_date=models.DateField(auto_now=False)
	pic=models.ImageField(upload_to='media/Images/')
	created_on=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.movie_name
 
class UpdateSeat(models.Model):
	select_movie=models.ForeignKey(MovieModel)
	total_seat=models.IntegerField()
	ticket_price=models.IntegerField()



class BookingOrder(models.Model):
	cust=models.CharField(max_length=50)
	movie=models.CharField(max_length=50)
	count=models.IntegerField()
	price=models.IntegerField()

	def __str__(self):
		return self.cust
