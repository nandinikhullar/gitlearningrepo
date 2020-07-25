from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def infomation(request):
    return render(request, 'information.html')