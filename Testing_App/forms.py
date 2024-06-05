from django import forms
from .models import  Posts,User
from  django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class Registration(UserCreationForm):
    class Meta:
        model=User
        fields = ["username","email","password1","password2"]

class Login (forms.Form):
        username = forms.CharField(label="Введіть ваше ім'я",max_length=150)
        password = forms.CharField(label="Введіть ваш пароль",max_length=128)

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["text"]

class Comments(forms.Form):
    text = forms.CharField(label="Коментар",max_length=750)

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","bio"]