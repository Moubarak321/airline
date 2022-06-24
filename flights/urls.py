from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight") , #int comme str indique le type de variable à inserer dans l'url
    path("<int:flight_id>/book",views.book, name="book")
]