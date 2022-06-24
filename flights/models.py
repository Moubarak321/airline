from django.db import models
from django.forms import CharField

# Create your models here.

#chaque modele est une class python et correspond à une table de base de données

class Airport(models.Model):
    code= models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):   #aficher chaque ville avec le code de son aéroport 
        return f"{self.city} ({self.code})"


class Flight(models.Model):      # 1 chaque vol a une origine, une destination et une durée. fonctionne comme la poo mais ici, elle est stockée dasn une base de données
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")  #2  Ce que models.cascade signifie, c'est que si je supprime un jour un aéroport de la table des aéroports, cela va également supprimer tous les vols correspondants
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals") # 3 Et un nom lié, comme nous allons le voir dans un instant, va me permettre d'accéder à une relation dans l'ordre inverse. Ainsi, à partir d'un vol, je peux prendre un vol et dire .origin pour obtenir
    duration = models.IntegerField()                                                            #l'origine du vol dans l'aéroport.
                                                                                                #Mais l'autre question que je pourrais vouloir poser est dans l'ordre inverse.
                                                                                                #Si j'ai un aéroport, comment puis-je obtenir tous les vols qui
                                                                                                #qui ont cet aéroport comme origine ?
                                                                                                #Et donc ici, si je donne un nom apparenté à cette clé étrangère,
                                                                                                #Django va automatiquement mettre en place la relation
                                                                                                #dans la direction opposée.
                                                                                                #Et donc ici, si nous avons un aéroport,
                                                                                                #et que je veux connaître tous les vols qui ont cet aéroport comme origine,
                                                                                                #le nom raisonnable pour un nom de relation ici est quelque chose comme "départs".
                                                                                                #Donc si j'ai un aéroport, je peux accéder à tous les
                                                                                                #des départs, ce qui me donne tous les vols qui
                                                                                                #qui partent de cet aéroport
    def __str__(self):   # afficher la base de donnée sous forme de phrase 
        return f"{self.id}:{self.origin} to {self.destination}"


class Passenger(models.Model):   #nouvelle base de donnée pour enregistrer les passagers
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    flights= models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"