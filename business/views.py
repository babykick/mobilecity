#coding=utf-8
from .models import POI
from django.shortcuts import render
from rest_framework import generics
from .serializers import POISerializer
from rest_framework.response import Response
from django.views.generic import View
from django.http import JsonResponse



class POIAround(View):
    def get(self, request):
        q = request.GET['q']
        loc = request.GET['loc'].split(',')
        radius = request.GET.get('radius',1000)
        return JsonResponse(POI.arounds.search(q=q, loc=loc, radius=radius))

 
    