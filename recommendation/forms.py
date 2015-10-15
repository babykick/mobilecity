from .models import RecommendItem
from django.forms import ModelForm



class RecommendItemForm(ModelForm):
    class Meta:
       model = RecommendItem
       #fields = []
       
       