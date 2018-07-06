# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from movieapp.models import MovieModel,BookingOrder,UpdateSeat
# Register your models here.
admin.site.register(MovieModel)
admin.site.register(UpdateSeat)
admin.site.register(BookingOrder)


