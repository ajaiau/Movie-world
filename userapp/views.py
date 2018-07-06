# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View,FormView,DetailView

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render,HttpResponse,render_to_response, redirect
from django.contrib import auth
from django.http import HttpResponseRedirect

from userapp.forms import RegForm,UserForm,EditForm
from userapp.models import Customer
from movieapp.models import MovieModel,BookingOrder
# Create your views here.


class HomeView(View):
    template_name='home.html'
    def get(self,request):
        mveobj=MovieModel.objects.all()
        context={
        'form':mveobj
        }
        return render(request,self.template_name,context)

class HomeMovieDetail(DetailView):
    template_name='home_movie_details.html'
    model= MovieModel


class CreateCustomerView(FormView):
    template_name="signup.html"
    form_class= UserForm
    model = User

    def get(self,request,*args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        reg_form = RegForm()
        return self.render_to_response(
            self.get_context_data(form1=user_form, form2=reg_form))

    def post(self,request,*args,**kwargs):
    	print("in posttttttttttttt")
        self.object = None
        form_class = self.get_form_class()
        user_form = self.get_form(form_class)
        reg_form = RegForm(self.request.POST)
        if (user_form.is_valid() and reg_form.is_valid()):
            return self.form_valid(user_form, reg_form)
        else:
            return self.form_invalid(user_form, reg_form)


    def get_success_url(self, **kwargs):
        return reverse_lazy('lgn')

    def form_valid(self, user_form, reg_form):
    	print("in form valid..................")
        self.object = user_form.save()
        self.object.is_staff=True
        self.object.save()
        p = reg_form.save(commit=False)
        p.user = self.object
        p.save()
        return super(CreateCustomerView, self).form_valid(user_form)


    def form_invalid(self, user_form, reg_form):
    	print("not form valid............................ss")
    	print(user_form.errors)
        return self.render_to_response(self.get_context_data(form1=user_form,
       form2=reg_form))




def login(request):
    form =AuthenticationForm()
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return redirect("/adminhome/")
        if request.user.is_staff:
            return redirect("/user/movies/")


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if request.user.is_superuser:
                return redirect("/adminhome/")
            if request.user.is_staff:
                return redirect("/user/movies/")

        else:
            return redirect('/login/',{'login_message' : 'Fill in all fields',})
            messages.error(request, 'Error wrong username/password')
    context = {}
    context['form']=form

    return render(request, 'registration/login.html', context)




@user_passes_test(lambda u: u.is_staff)
def StaffHome(request):
    context = {}
    return render(request, 'edit_user.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AdminHome(request):
    context = {}
    return render(request, 'admin_home.html', context)



class UserProfile(View):
    template_name ='user_profile.html'
    model=Customer
    def get(self,request):
        if request.user.is_staff:
            print(request.user)
            user_obj=User.objects.get(username=request.user)
            cust_obj=Customer.objects.get(user=user_obj)
            print(cust_obj.mobile_no)
            context={
                'form':cust_obj,
                 'user':user_obj
            }
            return render(request,self.template_name,context)
        else:
            print('not valid')
            return HttpResponseRedirect(reverse_lazy('eror'))
        




class EditUserView(View):
    template_name='edit_user.html'
    form_class1=EditForm
    form_class2=RegForm
    model=User
   
    def get(self,request,id):
        if request.user.is_staff:
            print('in get',request.user)
            user_obj = User.objects.get(username=request.user)
            print(user_obj)
            edt_obj=Customer.objects.get(user=user_obj)
            print(edt_obj)
            edt_obj2=User.objects.get(pk=id)
            # print(edt_obj)
            # print(edt_obj2)
            print(edt_obj2.email)
            form = self.form_class1(
                initial={
                'first_name':edt_obj2.first_name,
                'last_name':edt_obj2.last_name,
                'email':edt_obj2.email,
                
                
            
                }
            )
            form2 = self.form_class2(
                initial={
                'mobile_no':edt_obj.mobile_no,
                'place':edt_obj.place,
                
            
                }
            )
            context = {
                'form': form,
                'form2':form2

            }
            return render(request,self.template_name,context)
        else:
            return HttpResponseRedirect(reverse_lazy('eror'))
        
    def post(self,request,id):
        test_id = id
        edt_obj=Customer.objects.get(pk=test_id)
        edt_obj2=User.objects.get(pk=test_id)
        form = self.form_class1(self.request.POST)
        form2 =self.form_class2(self.request.POST)
        # print "FORNM",request.POST
        
        
        if form.is_valid():
            edt_obj2.first_name=request.POST.get('first_name')
            edt_obj2.last_name=request.POST.get('last_name')
            edt_obj2.email=request.POST.get('email')
            edt_obj2.save()

        if form2.is_valid():
            edt_obj.mobile_no=request.POST.get('mobile_no')
            edt_obj.place=request.POST.get('place')
            edt_obj.save()


            # context = {
            # 'form': form
            # }
            return HttpResponseRedirect(reverse_lazy('usrp'))
        



class AdminHomeView(View):
    template_name='admin_home.html'
    template_name2='error_page.html'
    def get(self,request):
        if request.user.is_superuser:
            ordr=BookingOrder.objects.all()
            context={
            'form':ordr
            }
            return render(request,self.template_name,context)
        else:
            return HttpResponseRedirect(reverse_lazy('eror'))


class BookedshowView(View):
    template_name='bookedshows.html'
    models=BookingOrder
    def get(self,request):
        if request.user.is_staff:
            user_obj=User.objects.get(username=request.user)
            print(user_obj)
            book=BookingOrder.objects.filter(cust=user_obj)
            print(book)
            context={
                'form':book
            }
            print()
            return render(request,self.template_name,context)
        else:
            return HttpResponseRedirect(reverse_lazy('eror'))





class ErrorPageView(View):
    template_name='error_page.html'
    def get(self,request):
        return render(request,self.template_name)







class AllMovies(View):
    template_name='all_movies.html'
    def get(self,request):
        if request.user.is_staff:
            mveobj=MovieModel.objects.all()
            context={
            'form':mveobj
            }
            return render(request,self.template_name,context)
        else:
            return HttpResponseRedirect(reverse_lazy('eror'))


class MovieDetail(DetailView):
    template_name='movie_details.html'
    model= MovieModel
    # def get(self,request):
    #     if request.user.is_superuser:
    #         return render(request,self.template_name)
           

class Contact(View):
    template_name='contact.html'
    def get(self,request):
        return render(request,self.template_name)

class Test(View):
    template_name='test_page.html'
    def get(self,request):
        return render(request,self.template_name)


class TicketBookView(View):
    def post(self,request):
        print("in post")
        tkt_id =request.POST.get('movie_id')
        cnt = request.POST.get('count')
        prc = request.POST.get('price')
        print(prc)
        us = request.user
        user = User.objects.get(username = us)
        move = MovieModel.objects.get(id = tkt_id)
        usr = Customer.objects.get(user=user)
        tktbook = BookingOrder.objects.create(cust = usr.user ,movie = move ,count = cnt,price=prc)
        tktbook.save()
        
        # return redirect('prolist')

        response = 'Success'
        return HttpResponse(json.dumps(response),content_type='json')   


