from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import JsonResponse
from .forms import AuthorForm, UserForm



class RegisterView(View):
    """ 注册用户
    """
    def post(self, request):
        uf = UserForm(request.POST, prefix='user')
        upf = AuthorForm(request.POST, prefix='userprofile')
        if uf.is_valid() and upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return JsonResponse({'sucess':1, 'name':username})
        

class LoginView(View):
    """ 登录用户
    """
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                raise NotImplemented # Do something
            
        else:
            raise NotImplemented


class logoutView(View):
    """ 登出用户
    """
    def get(self,request):
        logout(request)
