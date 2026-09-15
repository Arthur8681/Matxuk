from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from models import *
from django.views import View
# Create your views here.




def get_users(request):
    users = User.objects.all()
