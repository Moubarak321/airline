from django.http import HttpResponseRedirect 
from django.shortcuts import render 
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.

def index(request):
    return render(request, 'flights/index.html', {
        "flights": Flight.objects.all()
    })

def flight (request, flight_id):    #afficher les infos de chaque vol via leur id
    flight=Flight.objects.get(pk=flight_id)   #obtenir le vol dont l'id est stocké dans pk
    return render(request, "flights/flight.html", {
        "flight": flight,     #creation de la variable flight et la renvoyer au fichier  flight.html
        "passengers": flight.passengers.all(),  #prendre le vol et afficher tous les passagers du vol
        "non_passengers": Passenger.objects.exclude(flights=flight).all(), #passagers n'etant pas dans le vol mais enregistrés dans la base
    })


def book(request, flight_id):  # " add passenger by myself to the flight"
    if request.method == "POST":  # si le formulaire à été soumis, 
        flight = Flight.objects.get(pk=flight_id) # recuperer l'id du passager 
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"])) #passager dont l'id a été retiré
        passenger.flights.add(flight) #pointer vers le passager, accéder à sa liste de vols, et ajouter un vol
        return HttpResponseRedirect(reverse("flight",args=(flight.id,))) #rediriger l'user vers la page des vols apès soumission du formulaire