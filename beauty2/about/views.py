from django.shortcuts import render ,HttpResponse
from .models import *



def about(request):
    about_us = AboutUs.objects.first()
    
    return render(request,'about/about.html',{'about_us': about_us})

