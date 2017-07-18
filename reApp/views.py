# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from realestateSite import settings

from .models import *


def index(request):
    context = {
        'title':"Sell Your House Today!",
        }
    return render(request,'home.html',context)

# def home(request):
#     context = {
#         'title':'Home',
#     }
#     return render(request, 'home.html', context)
