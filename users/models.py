from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    """
       User field has:
            username
            password
            email
            first_name
            last_name
    """
    nickname = models.CharField(max_length=50)
    mobilephone = models.CharField(max_length=30)
    user = models.OneToOneField(User, null=True)
    avatar = models.CharField(max_length=100, null=True)
 
    def __unicode__(self):
        return self.user.username
    