from django.urls import path
from . import views

urlpatterns = [
    path("", views.europa, name="europa"),
    path(r'^georgia.html', views.georgia, name='georgia'),
    path(r'^chipre.html', views.chipre, name='chipre')
]