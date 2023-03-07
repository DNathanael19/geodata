from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def russia(request):
    return render(request, "russia.html")

def turquia(request):
    return render(request, "turquia.html")

def cazaquistao(request):
    return render(request, "cazaquistao.html")