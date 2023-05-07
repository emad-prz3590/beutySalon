from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace='home')),
    path('blog/',include('blog.urls',namespace='blog')),
    path('portfolio/',include('portfolio.urls',namespace='portfolio')),
    path('reservation/',include('reservation.urls',namespace='reservation')),
    path('about-us/',include('about.urls',namespace='about')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)