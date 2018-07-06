from django import forms
from movieapp.models import MovieModel,UpdateSeat


class AddMovieForm(forms.ModelForm):
	class Meta:
		model = MovieModel
		exclude=('created_on',)

class AddSeatForm(forms.ModelForm):
	class Meta:
		model=UpdateSeat
		exclude=('',)



class EditForm(forms.ModelForm):
	class Meta:
		model=MovieModel
		exclude=('created_on',)


class EditMovieForm(forms.Form):
	movie_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your first name', 'class': 'form-control'}),required=True)
	movie_language= forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type your last name', 'class': 'form-control'}),required=True)
	release_date =  forms.CharField(label='Release Date',widget=forms.TextInput(attrs={'class': 'form-control datepicker','id':'dob','required':'required','placeholder':'YYYY-MM-DD','readonly':'true'}))