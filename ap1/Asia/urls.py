from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(r'^russia.html', views.russia, name='russia'),
    path(r'^turquia.html', views.turquia, name='turquia'),
    path(r'^cazaquistao.html', views.cazaquistao, name='cazaquistao')
]