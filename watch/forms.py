from unicodedata import name
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile,Post,Neighborhood


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email','username','password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture','contact_info']

class NewPostForm(forms.ModelForm):
	picture = forms.ImageField(required=True)
	caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
	
	class Meta:
		model = Post
		fields = ('picture', 'caption')

class NewHoodForm(forms.ModelForm):
    name = forms.CharField(required=True)
    picture = forms.ImageField(required=True)
    location = forms.CharField(required=True)
    occupants_count = forms.IntegerField(required=True)
    
    class Meta:
        model = Neighborhood
        fields = ('name','picture','location','occupants_count')

class HoodUpdateForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['name','picture','occupants_count']
    