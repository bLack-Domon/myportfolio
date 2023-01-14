from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
  jeda = {
    'judul': 'My Portfolio',
  }
  return render(request, 'index.html', jeda)

def cv(request):
  jeda = {
    'judul': 'My CV',
  }
  return render(request, 'cv.html', jeda)