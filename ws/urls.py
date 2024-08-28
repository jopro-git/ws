from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop-home'),
    path('about', views.about, name ='shop-about')
]
