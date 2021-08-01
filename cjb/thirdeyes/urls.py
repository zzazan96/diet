from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login, name='login'),
    path('main/', views.main, name='main'),
    path('main/set/', views.set, name='set'),
    path('signup/', views.signup, name='signup'),
    path('main/set/user/', views.user, name='user'),
    path('main/morning/', views.morning, name='morning'),
    path('main/lunch/', views.lunch, name='lunch'),
    path('main/dinner/', views.dinner, name='dinner'),
    path('main/snack/', views.snack, name='snack'),
    path('main/set/alarm/', views.alarm, name='alarm'),
    path('main/diary/', views.diary, name='diary'),
    path('main/set/alarm/malarm/', views.malarm, name='malarm'),
    path('main/set/alarm/lalarm/', views.lalarm, name='lalarm'),
    path('main/set/alarm/dalarm/', views.dalarm, name='dalarm'),
    path('main/morning/msearch/', views.msearch, name='msearch'),
    path('main/lunch/lsearch/', views.lsearch, name='lsearch'),
    path('main/dinner/dsearch/', views.dsearch, name='dsearch'),
    path('main/snack/ssearch/', views.ssearch, name='ssearch'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
