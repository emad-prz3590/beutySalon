from django.urls import path
from . import views

app_name = 'portfolio'



urlpatterns = [
    path('gallery/',views.portfolio,name='portfolio'),
    path('portfolio/', views.portfolio, name='portfolio'),
]