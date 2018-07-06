from django.conf.urls import url,include
from django.contrib import admin

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


from movieapp.views import AddMovieView,MovieListView,ListAllUser,AllMovie,EditMovieView,DeleteUser,UpdateSeatView
from movieapp.views import DeleteMovie

urlpatterns = [

	url(r'^movieadd/',AddMovieView.as_view(),name='admve'),
	url(r'^allmovies/',MovieListView.as_view(),name='almve'),
	url(r'^listusers/',ListAllUser.as_view(),name='lstusr'),
	url(r'^listmovies/',AllMovie.as_view(),name='lstmve'),
	url(r'^editmovies/([a-zA-Z0-9_-]+)/$',EditMovieView.as_view(),name='edtmve'),
	url(r'^deluser/([a-zA-Z0-9_-]+)/$',DeleteUser.as_view(),name='dlusr'),
	url(r'^updateseat/',UpdateSeatView.as_view(),name='updteset'),
	url(r'^deletemve/([a-zA-Z0-9_-]+)/$',DeleteMovie.as_view(),name='delmve'),
	
	
	


	



    

]


urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)