from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required,permission_required


from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from userapp import views
from userapp.views import HomeView,CreateCustomerView,UserProfile,EditUserView,AdminHomeView,ErrorPageView,AllMovies
from userapp.views import MovieDetail,HomeMovieDetail,Contact,Test,TicketBookView,BookedshowView
urlpatterns = [
	url(r'^$',HomeView.as_view(),name='hme'),
	url(r'^signup/',CreateCustomerView.as_view(),name='sgn'),
	url(r'^login/$', views.login, name='lgn'),
	url(r'^oauth/', include('social_django.urls', namespace='social')),
	url(r'^profile/',UserProfile.as_view(),name='usrp'),
	url(r'^edituser/([a-zA-Z0-9_-]+)/$',EditUserView.as_view(),name='edtusr'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'home.html'}, 
		name='lgut'),
	url(r'adminhome/',AdminHomeView.as_view(),name='admnhme'),
	url(r'error/',ErrorPageView.as_view(),name='eror'),
	url(r'^user/movies',AllMovies.as_view(),name='testsamp'),
	
	url(r'^moviedetails/(?P<pk>\d+)/$',MovieDetail.as_view(),name='mvedtail'),
	url(r'^homemoviedetails/(?P<pk>\d+)/$',HomeMovieDetail.as_view(),name='hmemvedtail'),
	url(r'^contact/',Contact.as_view(),name='ctct'),
	url(r'^test',Test.as_view(),name='tst'),

	url(r'^book/',TicketBookView.as_view(),name='tktbk'),
	url(r'^bookedshow',BookedshowView.as_view(),name='bked'),




    
]


urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)