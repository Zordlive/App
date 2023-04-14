from django.db import models
from .models import client

# Create your models here.
class produit(models.Model):
    id=models.fields.AutoField(primary_key=True),
    nom=models.fields.CharField(max_length=100),
    descrip=models.fields.TextField(),
    posologie=models.fields.TextField(),

class livraison(models.Model):
    id=models.fields.AutoField(primary_key=True),
    client_id=models.ForeignKey(client, null=True, on_delete=models.SET_NULL),
    N_adresse=models.fields.IntegerField(max_length=10),
    commune=models.fields.CharField(max_length=50),
    ville=models.fields.CharField(max_length=50),
class depot(models.Model):
    
    


