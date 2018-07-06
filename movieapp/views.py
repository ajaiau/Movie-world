# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy


from movieapp.models import MovieModel
from movieapp.forms import AddMovieForm,EditMovieForm,AddSeatForm
from userapp.models import Customer
# Create your views here.

class AddMovieView(View):
	template_name = 'add_movie.html'
	form_class = AddMovieForm
	def get(self,request):
		if request.user.is_superuser:

			print('in get')
			form = self.form_class()
			context={
				'form':form,
				
			}
			return render(request,self.template_name,context)
		else:
			return HttpResponseRedirect(reverse_lazy('eror'))


	def post(self,request):
		print('in post')
		form =self.form_class(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			context={
			'form':form,
			}

	 		return render(request,self.template_name,context)
		else:
			print('else post')
			context={
			'form':form

			}
			return render(request,self.template_name,context)
	
		
			




class MovieListView(View):
	template_name='movies.html'
	def get(self,request):
		if request.user.is_superuser:
			testobj=MovieModel.objects.all()
			context={
				'form':testobj
			}
			return render(request,self.template_name,context)
		else:
			return HttpResponseRedirect(reverse_lazy('eror'))



class ListAllUser(View):
	template_name='list_all_user.html'
	def get(self,request):
		if request.user.is_superuser:
			testobj=User.objects.all()
			# print(testobj)
			context={
				'form':testobj
			}
			return render(request,self.template_name,context)
		else:
			return HttpResponseRedirect(reverse_lazy('eror'))


class DeleteMovie(View):
	template_name='movies.html'
	def get(self,request,id):
		mve_id=id
		print(mve_id)
		delmve=MovieModel.objects.get(id=mve_id).delete()
		print(delmve)
		return HttpResponseRedirect(reverse_lazy('almve'))


class DeleteUser(View):
	template_name='list_all_user.html'
	def get(self,request,id):
		usr_id=id
		print(usr_id)
		delobj=User.objects.get(id=usr_id).delete()
		print(delobj)
		return HttpResponseRedirect(reverse_lazy('lstusr'))





class AllMovie(View):
	template_name='list_movies.html'
	def get(self,request):
		if request.user.is_superuser:
			testobj=MovieModel.objects.all()
			context={
				'form':testobj
			}
			return render(request,self.template_name,context)
		else:
			return HttpResponseRedirect(reverse_lazy('eror'))



class EditMovieView(View):
	template_name='edit_movie.html'
	form_class=EditMovieForm

	def get(self,request,id):
		if request.user.is_superuser:
			print('in get')
			edt_obj=MovieModel.objects.get(pk=id)
			print(edt_obj)
			form = self.form_class(
			initial={
			'movie_name':edt_obj.movie_name,
			'movie_language':edt_obj.movie_language,
			'release_date':edt_obj.release_date,
			
			
			}
			)
			context = {
				'form': form
			}

			return render(request,self.template_name,context)
		else:
			return HttpResponseRedirect(reverse_lazy('eror'))
			
	def post(self,request,id):

		print('in post')
		test_id = id
		print(test_id)
		edt_obj2=MovieModel.objects.get(pk=test_id)
		print(edt_obj2)
		form = self.form_class(self.request.POST,request.FILES)
		print(request.FILES)
		# print "FORNM",request.POST
		print('forum',request.POST)
				
				
		if form.is_valid():
			print('not valid')
			edt_obj2.movie_name=request.POST.get('movie_name')
			edt_obj2.movie_language=request.POST.get('movie_language')
			edt_obj2.release_date=request.POST.get('release_date')
				
			edt_obj2.save()
			return HttpResponseRedirect(reverse_lazy('lstmve'))


class UpdateSeatView(View):
	template_name = 'Update_seat.html'
	form_class = AddSeatForm
	def get(self,request):
		if request.user.is_superuser:
			print('in get')
			form = self.form_class()
			print(form)
			context={
				'form':form,
				
			}
			return render(request,self.template_name,context)
		else:
			return HttpResponseRedirect(reverse_lazy('eror'))


	def post(self,request):
		print('in post')
		form =self.form_class(request.POST)
		if form.is_valid():
			form.save()
			context={
			'form':form,
			}
			return render(request,self.template_name,context)
		else:
			print("not valid")
		
			





