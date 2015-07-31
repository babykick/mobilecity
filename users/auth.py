from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token



class TokenedURLAuthentication(authentication.BaseAuthentication):
    """
       Customed Authentication for url token authentification, example:
           http://127.0.0.1:8000/api/rcmdlist/?token=fdsfdsafdsf
    """
    def authenticate(self, request):
        token = request.GET.get('token')
        if not token:
            return None
        try:
            token = Token.objects.get(key=token)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such token')

        return (token.user, None)