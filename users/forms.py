from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Author


class UserForm(ModelForm):
    class Meta:
        model = User  


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ['user']