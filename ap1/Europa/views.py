from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def europa(request):
    return render(request, "europa.html")

def georgia(request):
    return render(request, "georgia.html")

def chipre(request):
    return render(request, "chipre.html")

