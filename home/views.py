from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    # return HttpResponse("SAP...")
    return render(request, 'home/index.html',)

def edu(request):

    return render(request, 'article/list.html',)

def user(request):

    return render(request, 'userprofile/login.html', )
