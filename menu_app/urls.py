from django.urls import path

from . import views

urlpatterns = [
    path('', views.MenuPageView.as_view(), name='menu'),    
]
