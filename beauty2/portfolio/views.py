from django.shortcuts import render,HttpResponse
from .models import * 
from django.shortcuts import get_object_or_404



def portfolio(request,slug=None,id=None):
    photos = Photo.objects.all()
    category = Category.objects.all()
    if slug and id :
        data = get_object_or_404(Category,slug=slug,id=id)
        photos = photos.filter(category=data)
    
    return render(request,'portfolio/portfolio.html',{'photos':photos,'category':category})