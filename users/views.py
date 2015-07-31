from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def loginView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            raise NotImplementError # Do something
        
    else:
        raise NotImplementError

def logoutView(request):
    logout(request)
