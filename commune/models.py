from django.db import models
from django.contrib import admin

# Create your models here.
class Reclamation(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    numTel = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    sujet = models.CharField(max_length=200, null=True, blank=True)
    adresseGoogle = models.URLField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    
    def __str__(self):
        return self.nom if self.nom else "Reclamation"    