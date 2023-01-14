from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='beranda'),
    path('my-cv', views.cv, name='cve'),
]
