from django.contrib import admin

from .models import Flight, Airport, Passenger
# Register your models here.

class FlightAdmin(admin.ModelAdmin):  #spécifier comment afficher la liste des vols dans le panneau admin
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin (admin.ModelAdmin):
    filter_horizontal = ("flights",)  # pour chaque passager, afficher dans un cadran aside la liste des vols choisis par ce dernier
                                        #permet ainasi à l'administrateur  d'ajouter et de retirer les passagers des vols choisis en amont 


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)  #ajout de la fonction flightAdmin
admin.site.register(Passenger, PassengerAdmin)